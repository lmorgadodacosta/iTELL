#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from flask import Flask, current_app, g
from collections import defaultdict as dd

import delphin
from delphin.interfaces import ace
from delphin.derivation import UdfNode, UdfTerminal

def check_nodes(obj,errors):
    """
    Check each node for nodes marked for 'mal' or 'rbst';
    These would be problematic nodes identified by the grammar;
    """
    if isinstance(obj, UdfNode):
        error = ''
        if 'rbst' in obj.entity:
            error = obj.entity
        if  obj.type and 'mal_' in obj.type:
            error = obj.type
        if error:
            span = " ".join([t.form for t in obj.terminals()])
            errors.append((error, span))
            # print(error, span)
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

    def check_sents(sent_list):
        """
        Given a list of sentences, this function tries to parse each one with 
        the default ERG and, if it fails, it uses the ERG enhanced with mal-rules
        to parse the same input. It returns a list with the same list of
        sentences and a list of error codes found for each sentence.

        [(sent1, [error1.1, error1.2]), (sent2, [error2.1, error2.2])]
        """

        erg_results = [] 
        with ace.AceParser(path.join(ROOT, ERG),
                           executable=path.join(ROOT, ACE),
                           cmdargs=['-1', '--timeout=10']) as parser, \
             ace.AceParser(path.join(ROOT, MAL_ERG),
                           executable=path.join(ROOT, ACE),
                           cmdargs=['-1', '--timeout=10', '--udx']) as mal:

            for sent in sent_list:
                
                erg_parse = parser.interact(sent)

                if not erg_parse['results']: # if there were no parses

                    mal_result = mal.interact(sent) 

                    if mal_result['results']:  # If the mal-grammar got a parse

                        error_tags = check_nodes(mal_result.result(0).derivation(),[])

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
                
                else: # assumed error-free for now
                    erg_results.append((sent, []))  

        return erg_results
