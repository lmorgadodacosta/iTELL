#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from flask import Flask, current_app, g
from collections import defaultdict as dd

import subprocess
from subprocess import check_output


import json
import delphin.dmrs
import delphin.mrs
from delphin.codecs import mrsjson, dmrsjson, simplemrs
from delphin import ace
from delphin.derivation import UDFNode, UDFTerminal
from delphin import itsdb, tsql

def list_lexids(deriv_tree):
    """
    ACE must called with udx mode otherwise the terminals
    are the types.
    This is printing the lexical instance ID e.g.
    i
    like_v1
    the_3_rbst
    apple_n1

    this can be used to check which lexical entries need 
    to be kept for a specific treebank/level.

    """

    lexids = []
    for t in deriv_tree.terminals():
        lexids.append(t._parent[1])
    # print("\n\n LEXIDS")
    # print(lexids)
    return lexids

def check_nodes(obj,errors):
    """
    Check each node for nodes marked for 'mal' or 'rbst';
    These would be problematic nodes identified by the grammar;

    FIXME: we are always keeping the "mal" error tag instead the 
    "rbst" if both occur. Both occur, for example, in "the the".
    Must make sure this is desirable.

    Some error tags now have no msgs... and the span is still shown 
    but no msgs.
    
    In principle, the ERG puts "rbst" on instance names/Ids
    and "mal_" is in the type hierarchy. This is not necessarity 
    true for Zhong later

    FIXME: there are special types, such as 'stutter' that do not 
    have 'mal' or 'rbst' in the name.

    'stutter'  must also be included in this search for some errors.

    """
    if isinstance(obj, UDFNode):
        error = ''
        if ('rbst' in obj.entity) or ('mal' in obj.entity) or ('stutter' in obj.entity):  
            error = obj.entity
            span = " ".join([t.form for t in obj.terminals()])
            errors.append((error, span))
            
        if  obj.type and (('mal_' in obj.type) or ('rbst' in obj.type) or ('stutter' in obj.type)):   
            span = " ".join([t.form for t in obj.terminals()])
            error = obj.type
            errors.append((error, span))
            
        for dtr in obj.daughters:
            dtrs = check_nodes(dtr,errors)

    return errors


error_msgs = dd(tuple)


app = Flask(__name__)
with app.app_context():

    ROOT  = path.dirname(path.realpath(__file__))
    
    ACE = 'static/ace'

    ERG = 'static/erg.dat'
    MAL_ERG = 'static/erg-mal.dat'

    ZHONG = 'static/zhong.dat'


    ace_stderr = open(path.join(ROOT, 'delphin/ace_stderr.txt'), 'w+')

    
    def check_sents(sent_list):
        """
        Given a list of sentences, this function tries to parse each one with
        the default ERG and, if it fails, it uses the ERG enhanced with mal-rules
        to parse the same input. It returns a list with the same list of
        sentences and a list of error codes found for each sentence.

        [(sent1, [error1.1, error1.2]), (sent2, [error2.1, error2.2])]
        """

        erg_results = [] 
        with ace.ACEParser(path.join(ROOT, ERG),
                           executable=path.join(ROOT, ACE),
                           cmdargs=['-1', '--timeout=20', '--max-chart-megabytes=2000', '--max-unpack-megabytes=2000']) as parser, \
             ace.ACEParser(path.join(ROOT, MAL_ERG),
                           executable=path.join(ROOT, ACE),
                           cmdargs=['-1', '--timeout=20', '--udx', '--max-chart-megabytes=2000', '--max-unpack-megabytes=2000']) as mal:

            for sent in sent_list:

                
                erg_parse = parser.interact(sent)

                if not erg_parse['results']: # if there were no parses

                    mal_result = mal.interact(sent)

                    if mal_result['results']:  # If the mal-grammar got a parse
                        error_tags = check_nodes(mal_result.result(0).derivation(),[])

                        # print(error_tags)
                        
                        # WHY WAS THIS HERE?   ASK FCB
                        # for tag in rbst_tags:
                        for tag, string in error_tags:
                            if type(tag) == list:
                                if len(tag) == 0:
                                    tag = "empty_tag"
                                else:
                                    tag = ":".join(tag)

                        erg_results.append((sent, error_tags))
                        
                    else: # only a general NoParse tag can be given
                        erg_results.append((sent, [('NoParse', '')]))
                
                else:

                    # Check for Mood (Imperative and Interrogative)
                    try:
                        mrs = erg_parse.result(0).mrs()
                        sf = mrs.properties(mrs.index)['SF']
                    except:
                        print("MRS ERROR: "+sent , file=sys.stderr)
                        sf = []

                    
                    if sf != 'prop':
                        erg_results.append((sent, [(sf, '')]))
                                

                    else: # Propositions are good
                        erg_results.append((sent, []))
                    
        return erg_results



    def full_parse(sent, grammar_mode, max_parses):
        """
        """

        results = dd(lambda: dd())
        
        if grammar_mode == 'erg_strict':
            GRAMMAR = ERG
        elif grammar_mode == 'erg_robust':
            GRAMMAR = MAL_ERG
        elif grammar_mode == 'zhong_strict':
            GRAMMAR = ZHONG



        ########################################################################
        # ACE cmdargs (currently only for the number of parses)
        ########################################################################
        if max_parses == 'all':
            ace_cmdargs = ['--timeout=20', '--timeout=20', '--max-chart-megabytes=2000', '--max-unpack-megabytes=2000']
        else:
            ace_cmdargs = ['-n', max_parses, '--timeout=20', '--timeout=20', '--max-chart-megabytes=2000', '--max-unpack-megabytes=2000']

        ########################################################################
        # To silence ACE we need to give it a file to stream its own stderr.
        ########################################################################
        # ace_stderr = open(path.join(ROOT, 'static/ace_stderr.txt'), 'w+')
        
        with ace.ACEParser(path.join(ROOT, GRAMMAR),
                           executable=path.join(ROOT, ACE),
                           cmdargs=ace_cmdargs,
                           stderr=ace_stderr) as parser:

            erg_parse = parser.interact(sent)

        if erg_parse['results']:

            n_parses = len(erg_parse['results'])

            for n in list(range(n_parses)):
                
                deriv = erg_parse.result(n).derivation()
                deriv_json = json.dumps(deriv.to_dict())


                mrs = erg_parse.result(n).mrs()
                mrs_json = mrsjson.encode(mrs)
                mrs_simplemrs = simplemrs.encode(mrs)

                ################################################################
                # This was breaking too often, throwing keyErrors for handles.
                # We need to check if it's well formed before conversion.
                ################################################################
                if delphin.mrs.is_well_formed(mrs):
                    dmrs = delphin.dmrs.from_mrs(mrs)
                    dmrs_json = dmrsjson.encode(dmrs)
                else:
                    dmrs_json = False
                    
                errors = check_nodes(deriv,[])

                results[n]['deriv_json'] = deriv_json
                results[n]['mrs_json'] = mrs_json
                results[n]['mrs_simplemrs'] = mrs_simplemrs
                results[n]['dmrs_json'] = dmrs_json
                results[n]['errors'] = errors


            return results
        else:
            return results





    def tsdb_min(path_to_profile):
        """
        Profile should be the path to a GOLD/PARSED profile.
        for now this should look like 'static/mrs'
        """
        ts = itsdb.TestSuite(path.join(ROOT, path_to_profile))

        data = list()
        for row in tsql.select('i-id i-wf readings i-input  i-comment', ts):
            data.append(row)

        return data


    def update_erg2018():
        stdout = check_output([path.join(ROOT,
                 'delphin/pull_update_erg2018.bash')],
                 stderr=ace_stderr).decode('utf-8')
        return stdout

    def update_ergTRUNK():
        stdout = check_output([path.join(ROOT,
                 'delphin/pull_update_ergTRUNK.bash')],
                 stderr=ace_stderr).decode('utf-8')
        return stdout

    def update_zhong():
        stdout = check_output([path.join(ROOT,
                 'delphin/pull_update_zhong.bash')],
                 stderr=ace_stderr).decode('utf-8')
        return stdout


