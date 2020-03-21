#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from flask import Flask, current_app, g
from collections import defaultdict as dd
import datetime

import subprocess
from subprocess import check_output
from subprocess import Popen, PIPE   # TESTING, remove if not in use

import json
import delphin.dmrs
import delphin.mrs
from delphin.codecs import mrsjson, dmrsjson, simplemrs
from delphin import ace
from delphin.derivation import UDFNode, UDFTerminal
from delphin import itsdb, tsql


def current_time():
    '''   YYYY-MM-DD  HH:MM    '''
    d = datetime.datetime.now()
    return d.strftime('%Y-%m-%d %H:%M:%S')


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

def sent_leaf_ids(deriv):
    """
    Not entirely sure if this is needed, 
    can't I just get the wids by splitting 
    the sentence on spaces? this will depend on 
    things like "don't as do n't" etc.
    """
    
    sent_struct = dd()
    for leaf in  [(t.form, t.parent.start, t.parent.end) for t in deriv.terminals()]:
        for i, wid in enumerate(range(leaf[1], leaf[2])):
            # print(wid, leaf[0].split()[i])
            sent_struct[wid] = leaf[0].split()[i]

    print(sent_struct)
    return sent_struct

def check_nodes(obj, errors, sent_struct):
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
        # print([t.to_dict(['start','end']) for t in obj.terminals()])
        # print([(t.form, t.parent.start, t.parent.end) for t in obj.terminals()])
        # for leaf in  [(t.form, t.parent.start, t.parent.end) for t in obj.terminals()]:
        #     for i, wid in enumerate(range(leaf[1], leaf[2])):
        #         print(wid, leaf[0].split()[i])
            # print(leaf[0], list(range(leaf[1], leaf[2])))
            
        # print(obj.entity)
        # print(obj.type if obj.type else "NO TYPE")
        if ('rbst' in obj.entity) or ('mal' in obj.entity) or ('stutter' in obj.entity):  
            error = obj.entity
 
            print("####################")
            print(error)
            print([(t.parent.start, t.parent.end) for t in obj.terminals()])
            # print([(t.parent.to_dict()) for t in obj.terminals()])
            # print(dir(obj.terminals()), obj.terminals())

            
            
            if int(obj.terminals()[0].parent.start)-1 in sent_struct.keys():
                left_periphery = sent_struct[int(obj.terminals()[0].parent.start)-1]
            else:
                left_periphery = None


            if int(obj.terminals()[-1].parent.end) in sent_struct.keys():
                right_periphery = sent_struct[int(obj.terminals()[-1].parent.end)]
            else:
                right_periphery = None
                
            print(left_periphery, right_periphery)
            span = " ".join([t.form for t in obj.terminals()])
            errors.append((error, span))
            
        # if  obj.type and (('mal_' in obj.type) or ('rbst' in obj.type) or ('stutter' in obj.type)):   
        #     span = " ".join([t.form for t in obj.terminals()])
        #     error = obj.type
        #     errors.append((error, span))
            
        for dtr in obj.daughters:
            dtrs = check_nodes(dtr, errors, sent_struct)
            

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
                        sent_struct = sent_leaf_ids(mal_result.result(0).derivation())
                        error_tags = check_nodes(mal_result.result(0).derivation(),[], sent_struct)

                        
                        # print(error_tags)
                        # WHY WAS THIS HERE?   ASK FCB
                        # for tag in rbst_tags:
                        # for tag, string in error_tags:
                        #     if type(tag) == list:
                        #         if len(tag) == 0:
                        #             tag = "empty_tag"
                        #         else:
                        #             tag = ":".join(tag)

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



    def full_parse(sent, selected_grammar, max_parses):
        """
        """

        results = dd(lambda: dd())
        
        # if grammar_mode == 'erg_strict':
        #     GRAMMAR = ERG
        # elif grammar_mode == 'erg_robust':
        #     GRAMMAR = MAL_ERG
        # elif grammar_mode == 'zhong_strict':
        #     GRAMMAR = ZHONG



        ########################################################################
        # ACE cmdargs (currently only for the number of parses)
        ########################################################################
        if max_parses == 'all':
            ace_cmdargs = ['--timeout=20',
                           '--rooted-derivations',
                           '--max-chart-megabytes=2000',
                           '--max-unpack-megabytes=2000']
        else:
            ace_cmdargs = ['-n',
                           max_parses,
                           '--timeout=20',
                           '--rooted-derivations',
                           '--max-chart-megabytes=2000',
                           '--max-unpack-megabytes=2000']

        ########################################################################
        # To silence ACE we need to give it a file to stream its own stderr.
        ########################################################################
        
        with ace.ACEParser(path.join(ROOT, 'delphin/'+selected_grammar),
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
                    
                sent_struct =  sent_leaf_ids(deriv)
                errors = check_nodes(deriv,[], sent_struct)

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
        The argument path_to_profile should be, for 
        example, '/delphin/erg2018/tsdb/mrs'.
        
        Both skeletons and filled/parsed profiles can be inspected.
        This is why tsql.select is done in multiple queries. 
        All profiles always have, minimally, the 'items' file.
        Anything else is should be checked. 

        This function returns a dictionary based on i-ids of that profile:
        data[1]['i-wf'] = 1
        data[1]['i-input'] = "This is an example sentence."
        data[1]['i-comment'] = "The comment left inside the items-file."

        Optionally it can include:
        data[1]['i-readings'] = 23 # number of derivation trees
        """
        ts = itsdb.TestSuite(path.join(ROOT, path_to_profile))

        data = dd(lambda: dd())
        
        for row in tsql.select('i-id i-wf i-input  i-comment i-length', ts):
            i_id = row[0]
            data[i_id]['i-wf'] = row[1]
            data[i_id]['i-input'] = row[2]
            data[i_id]['i-comment'] = row[3]
            data[i_id]['i-length'] = row[4]

        ########################################################################
        # If we don't check if the file 'parse' exists, then pydelphin creates
        # an empty 'parse' file. This is undesirable, especially for skeletons
        ########################################################################
        if path.isfile(path.join(ROOT, path_to_profile+'parse')):
            for row in tsql.select('i-id readings', ts):
                data[row[0]]['readings'] = row[1]
            
        return data


    def update_erg2018():
        cmd = path.join(ROOT, 'delphin/pull_update_erg2018.bash')
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def update_itell_erg2018():
        cmd = path.join(ROOT, 'delphin/pull_update_itell-erg2018.bash')
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()

        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def update_ergTRUNK():
        cmd = path.join(ROOT, 'delphin/pull_update_ergTRUNK.bash')
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()

        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def update_zhong():
        cmd = path.join(ROOT, 'delphin/pull_update_zhong.bash')
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()

        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def update_itell_zhong():
        cmd = path.join(ROOT, 'delphin/pull_update_itell-zhong.bash')
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()

        return stdout.decode('utf-8'), stderr.decode('utf-8')



    def new_regression(dir1, selected_grammar):

        date = current_time().replace(' ', '_')
        
        if '___' in dir1:
            newdir = dir1.split('___')[1]
        else:
            newdir = dir1

        newdir = date + '___' + newdir + '___' + selected_grammar 

        dir1_path = "delphin/regressions/" + dir1 + '/'
        newdir_path = "delphin/regressions/" + newdir + '/'
        grammar_path =  path.join(ROOT, 'delphin/'+selected_grammar)
        
        # example: art -a "ace -g ~/git/itell/delphin/zhong.dat" cmnedu-2020-03-17.03/
        
        # cmd = ['; '.join([
        #     "mkdir " + newdir_path,
        #     "cp " + dir1_path + "item " + newdir_path + 'item',
        #     "cp " + dir1_path + "relations " + newdir_path + 'relations',
        #     "touch " + newdir_path + 'analysis',
        #     "touch " + newdir_path + 'decision',
        #     "touch " + newdir_path + 'edge',
        #     "touch " + newdir_path + 'fold',
        #     "touch " + newdir_path + 'item-phenomenon',
        #     "touch " + newdir_path + 'item-set',
        #     "touch " + newdir_path + 'output',
        #     "touch " + newdir_path + 'parameter',
        #     "touch " + newdir_path + 'parse',
        #     "touch " + newdir_path + 'phenomenon',
        #     "touch " + newdir_path + 'preference',
        #     "touch " + newdir_path + 'result',
        #     "touch " + newdir_path + 'rule',
        #     "touch " + newdir_path + 'run',
        #     "touch " + newdir_path + 'score',
        #     "touch " + newdir_path + 'set',
        #     "touch " + newdir_path + 'tree',
        #     "touch " + newdir_path + 'update',
        #     'art -a "ace -g ' + grammar_path + '" ' + newdir_path
        # ])]
        
        # p = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
        # stdout, stderr = p.communicate()


        all_stdout = bytes()
        all_stderr = bytes()
        commands = [
            "mkdir " + newdir_path,
            "cp " + dir1_path + "item " + newdir_path + 'item',
            "cp " + dir1_path + "relations " + newdir_path + 'relations',
            "touch " + newdir_path + 'analysis',
            "touch " + newdir_path + 'decision',
            "touch " + newdir_path + 'edge',
            "touch " + newdir_path + 'fold',
            "touch " + newdir_path + 'item-phenomenon',
            "touch " + newdir_path + 'item-set',
            "touch " + newdir_path + 'output',
            "touch " + newdir_path + 'parameter',
            "touch " + newdir_path + 'parse',
            "touch " + newdir_path + 'phenomenon',
            "touch " + newdir_path + 'preference',
            "touch " + newdir_path + 'result',
            "touch " + newdir_path + 'rule',
            "touch " + newdir_path + 'run',
            "touch " + newdir_path + 'score',
            "touch " + newdir_path + 'set',
            "touch " + newdir_path + 'tree',
            "touch " + newdir_path + 'update',
            'art -a "ace -g ' + grammar_path + '" ' + newdir_path
        ]

        for c in commands:
            p = Popen(c, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
            stdout, stderr = p.communicate()
            all_stdout += stdout 
            all_stderr += stderr
            
        return all_stdout.decode('utf-8'), all_stderr.decode('utf-8'), newdir_path

