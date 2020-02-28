from collections import defaultdict as dd
eng_feedback = dd(lambda: dd())

eng_feedback['a_det_mass_rbst']['lcc'] = ("""<strong>⇒</strong> You may be using an indefinite article, 'a' or 'an', before an uncountable noun (such as 'research'): {}. Indefinite articles should only precede singular countable nouns. Please check your sentence for uncountable nouns and remove any indefinite articles that precede them.""", 1)
eng_feedback['a_det_mass_rbst']['lcc2'] = ("""<strong>⇒</strong> You may be using an indefinite article, 'a' before an uncountable noun (such as 'research'): {}. Indefinite articles should only precede singular countable nouns. Please check your sentence for uncountable nouns and remove any indefinite articles that precede them.""", 1)
eng_feedback['a_det_mass_rbst']['callig'] = """You may be using an indefinite article, 'a' or 'an', before an uncountable noun (such as 'research'). Indefinite articles should only precede singular countable nouns."""


eng_feedback['a_det_plur_rbst']['lcc'] = ("""<strong>⇒</strong> You may be using an indefinite article, 'a' or 'an', before a plural countable noun: {}. 
Indefinite articles should only precede singular countable nouns. Please check your sentence for plural countable nouns and either 
remove any indefinite articles that precede them, or change the plural noun to a singular one.""", 1)
eng_feedback['a_det_plur_rbst']['callig'] = """You may be using an indefinite article, 'a' or 'an', before a plural countable noun. 
Indefinite articles should only precede singular countable nouns."""


eng_feedback['after_pp_rbst']['lcc'] = ("""<strong>⇒</strong> You may be using an unnecessary preposition, such as ‘for’, ‘on’, and ‘about’, in this sentence: {}. 
Please check whether all the prepositions in the sentence are needed. """, 0.5)
eng_feedback['after_pp_rbst']['callig'] = """You may be using an unnecessary preposition, such as 'for', 'on', and 'about', in this sentence."""


eng_feedback['aj-hdn_c_rbst']['lcc'] = ("""<strong>⇒</strong>  You may be using an unnecessary comma between an adjective and a noun: {}. 
Please check whether the comma in the sentence is needed.""", 0.5)
eng_feedback['aj-hdn_c_rbst']['callig'] = """You may be using an unnecessary comma between an adjective and a noun."""


eng_feedback['an_det_mass_rbst']['lcc'] = ("""<strong>⇒</strong> You may be using an indefinite article, ‘a’ or ‘an’, before an uncountable noun (such as ‘research’):
 {}. Indefinite articles should only precede singular countable nouns. Please check your sentence for uncountable nouns and remove any
 indefinite articles that precede them. """, 1)
eng_feedback['an_det_mass_rbst']['callig'] = """You may be using an indefinite article, ‘a’ or ‘an’, before an uncountable noun (such as ‘research’). Indefinite articles should only precede singular countable nouns."""


eng_feedback['an_det_plur_rbst']['lcc'] = ("""<strong>⇒</strong>  You may be using an indefinite article, ‘a’ or ‘an’, before a plural countable noun: {}. 
Indefinite articles should only precede singular countable nouns. Please check your sentence for plural countable nouns and either 
remove any indefinite articles that precede them, or change the plural noun to a singular one.""", 1)
eng_feedback['an_det_plur_rbst']['callig'] = """You may be using an indefinite article, ‘a’ or ‘an’, before a plural countable noun. Indefinite articles should only precede singular countable nouns."""


eng_feedback['bad_adv1_rbst']['lcc'] = ("""<strong>⇒</strong> You may be using an adverb (e.g. 'too', 'only', 'rapidly') inappropriately or the adverb may be 
in the wrong position in the sentence: {}.  Please check your sentence and change either the adverb or its position if necessary.""", 0.5)
eng_feedback['bad_adv1_rbst']['callig'] = """You may be using an adverb (e.g. 'too', 'only', 'rapidly') inappropriately or the adverb may be in the wrong position in the sentence."""


eng_feedback['such_an_det_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence has a singular noun without an article ('a', 'an', 'the') or determiner 
(e.g. 'each', 'this', 'my'): {}. As singular nouns require an article or determiner in front of them, you may want to consider 
adding one in front of the noun.""", 1)
eng_feedback['such_an_det_rbst']['callig'] = """This sentence has a singular noun without an article ('a', 'an', 'the') or determiner 
(e.g. 'each', 'this', 'my'). As singular nouns require an article or determiner in front of them."""


eng_feedback['their_rbst']['lcc'] = ("""<strong>⇒</strong> You have used 'there' in this sentence: {}. Please check if it should be 'their' instead and 
make the change if necessary.""", 0.5)
eng_feedback['their_rbst']['callig'] = """You have used 'there' in this sentence. Please check if it should be 'their' instead."""


eng_feedback['too_deg_nc_rbst']['lcc'] = ("""<strong>⇒</strong> You have used 'to' in this sentence: {}. Please check if it should be 'too' instead 
and make the change if necessary.""", 0.5)
eng_feedback['too_deg_nc_rbst']['callig'] = """You have used 'to' in this sentence. It likely should have been 'too' instead."""


eng_feedback['too_deg_rbst']['lcc'] = ("""<strong>⇒</strong> You have used 'to' more than once in this sentence: {}. Please check if 'too' should have been 
used in any of these instances instead and make the change if necessary.""", 0.5)
eng_feedback['too_deg_rbst']['callig'] = """You have used 'to' in this sentence. It likely should have been 'too'."""


eng_feedback['v_np_its-mal_le']['lcc'] = ("""<strong>⇒</strong> This sentence contains a third person singular pronoun ('he', 'she', 'it') which may not be 
compatible with its reference noun: {}. Please check the sentence and change the pronoun if necessary.""", 0.5)
eng_feedback['v_np_its-mal_le']['callig'] = """This sentence contains a third person singular pronoun ('he', 'she', 'it') which may not be compatible with its reference noun."""


eng_feedback['v_pst_olr_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence contains a verb which has an irregular form in the past tense (e.g. 'ate', 
'shook'): {}. You may want to consider changing the verb form.""", 1)
eng_feedback['v_pst_olr_rbst']['callig'] = """This sentence contains a verb which has an irregular form in the past tense (e.g. 'ate', 'shook')."""


eng_feedback['vmod_i_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence contains a missing, inappropriate or unnecessary modal ('can, 'will', 'shall', 
etc.): {}. Please check your sentence and reconsider your use of the modal if necessary.""", 0.5)
eng_feedback['vmod_i_rbst']['callig'] = """This sentence contains a missing, inappropriate or unnecessary modal ('can, 'will', 'shall', etc.)."""


eng_feedback['w_comma-sdwch_plr_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence has a comma separating two independent clauses. Please check the 
sentence and consider using a peroid/full-stop, a semi-colon or an appropriate conjunction instead.""", 0.5)
eng_feedback['w_comma-sdwch_plr_rbst']['callig'] = """This sentence has a comma separating two independent clauses. It should be using a peroid/full-stop, a semi-colon or an appropriate conjunction instead."""


eng_feedback['well_a1_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence may contain the wrong form of a verb: {}. Please check the sentence
 and consider changing the form of the verb if necessary.""", 0.5)
eng_feedback['well_a1_rbst']['callig'] = """This sentence may contain the wrong form of a verb."""


eng_feedback['every_all_rbst']['lcc'] = ("""<strong>⇒</strong> You may have used 'every' before a plural noun in this sentence: {}. Please check 
your sentence carefully and change it to 'all' if necessary. """, 1)
eng_feedback['every_all_rbst']['callig'] = """You may have used 'every' before a plural noun in this sentence. It might be better to use 'all'."""


eng_feedback['everyday_adv_rbst']['lcc'] = ("""<strong>⇒</strong> You have used 'everyday' as an adverb in your sentence: {}.  It should be spelled 
'every day', with a space in between when it does not modify a noun (e.g. 'an everyday affair'). Please check your sentence carefully and add 
a space between 'every' and 'day' if necessary.""", 1)
eng_feedback['everyday_adv_rbst']['callig'] = """You have used 'everyday' as an adverb in your sentence.  It should be spelled 
'every day', with a space in between when it does not modify a noun (e.g. 'an everyday affair')."""


eng_feedback['hdn_bnp_c_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence has a singular noun without an article ('a', 'an', 'the'), determiner 
(e.g. 'each', 'this') or possessive (e.g. 'my', 'her') before it: {}. Please check your sentence carefully and add an article, determiner 
or possessive before the singular noun if necessary.""", 1)
eng_feedback['hdn_bnp_c_rbst']['lcc2'] = ("""<strong>Missing Article: "{}"</strong><br><ul> <li>This sentence has a singular noun without an article ('a', 'an', 'the'), determiner (e.g. 'each', 'this') or possessive (e.g. 'my', 'her') before it. <li>Please check your sentence carefully and add an article, determiner or possessive before the singular noun if necessary.</ul>""", 1)
eng_feedback['hdn_bnp_c_rbst']['callig'] = """This sentence has a singular noun without an article ('a', 'an', 'the'), determiner 
(e.g. 'each', 'this') or possessive (e.g. 'my', 'her') before it."""


eng_feedback['mal_det_pl_le']['lcc'] = ("""<strong>⇒</strong> This sentence has a singular noun without an article ('a', 'an', 'the'),  determiner 
(e.g. 'each', 'this') or possessive (e.g. 'my', 'her') before it: {}. Please check your sentence carefully and add an article, determiner 
or possessive before the singular noun or make the singular noun plural if necessary.""", 0.5)
eng_feedback['mal_det_pl_le']['callig'] = """This sentence has a singular noun without an article ('a', 'an', 'the'),  determiner 
(e.g. 'each', 'this') or possessive (e.g. 'my', 'her') before it."""


eng_feedback['n_pl-mass_olr_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence contains the wrong form of the countable/uncountable noun:
 {}. Please check the noun and remove the plural marking from the uncountable noun if necessary.""", 1)
eng_feedback['n_pl-mass_olr_rbst']['callig'] = """This sentence contains the wrong form of the countable/uncountable noun. Remove the plural marking from the uncountable noun."""


eng_feedback['non_third_sg_fin_v_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb which does not agree in person 
(e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject: {}. Please check the sentence and ensure that the verb 
agrees with its subject.""", 1)
eng_feedback['non_third_sg_fin_v_rbst']['callig'] = """This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject."""


eng_feedback['num_det_2_rbst']['lcc'] = ("""<strong>⇒</strong> You may have used the singular form of a noun with a determiner for plural 
nouns: {}. Please check the determiner and the noun and ensure that they agree in number if necessary.""", 1)
eng_feedback['num_det_2_rbst']['callig'] = """You may have used the singular form of a noun with a determiner for plural 
nouns. The determiner and the noun must agree in number."""


eng_feedback['of_poss_stutter_rbst']['lcc'] = ("""<strong>⇒</strong> You may have repeated a preposition (e.g. 'of') in your sentence: {}. Please 
check the sentence and remove one of the prepositions if necessary.""", 1)
eng_feedback['of_poss_stutter_rbst']['callig'] = """You may have repeated a preposition (e.g. 'of') in your sentence."""


eng_feedback['only_adv1_rbst']['lcc'] = ("""<strong>⇒</strong> 'Only' may be in the wrong position in your sentence: {}. 
Please check the sentence and move 'only' to another position if necessary. """, 0.5)
eng_feedback['only_adv1_rbst']['callig'] = """'Only' may be in the wrong position in your sentence. """


eng_feedback['other_rbst']['lcc'] = ("""<strong>⇒</strong> You may have used 'other' wrongly in this sentence: {}. 
Please check the sentence and replace 'other' if necessary.""", 0.5)
eng_feedback['other_rbst']['callig'] = """You may have used 'other' wrongly in this sentence."""


eng_feedback['sb-hd_mc-cma_c_rbst']['lcc'] = ("""<strong>⇒</strong> You may not have used commas appropriately in this sentence: 
{}.  Please check the sentence and make changes to your use of commas if necessary. """, 0.5)
eng_feedback['sb-hd_mc-cma_c_rbst']['callig'] = """You may not have used commas appropriately in this sentence."""


eng_feedback['such_a_det_rbst']['lcc'] = ("""<strong>⇒</strong> You have used 'such' before a singular countable noun in this 
sentence: {} when there should be an article, 'a' or 'an' in between them.  Please read your sentence 
carefully and insert an article after 'such' if necessary.""", 1)
eng_feedback['such_a_det_rbst']['callig'] = """You have used 'such' before a singular countable noun in this sentence. There should be an article, 'a' or 'an' in between them."""


eng_feedback['be_are_have_rbst']['lcc'] = ("""<strong>⇒</strong> In this sentence, you have used the passive verb phrase 
'is/are + verb-ed': {}.  Please check whether you intended to use 'has/have + verb-ed' instead.""", 1)
eng_feedback['be_are_have_rbst']['callig'] = """In this sentence, you have used the passive verb phrase 'is/are + verb-ed'. It should be 'has/have + verb-ed' instead."""


eng_feedback['be_is_has_rbst']['lcc'] = ("""<strong>⇒</strong> In this sentence, you have used the passive verb phrase 
'is/are + verb-ed': {}.  Please check whether you intended to use 'has/have + verb-ed' instead.""", 1)
eng_feedback['be_is_has_rbst']['callig'] = """In this sentence, you have used the passive verb phrase 'is/are + verb-ed'. It should be 'has/have + verb-ed' instead."""


eng_feedback['third_sg_fin_v_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') 
and number (singular/plural) with its subject: {}. Please check the sentence and ensure that the verb agrees with its subject.""", 0.5)
eng_feedback['third_sg_fin_v_rbst']['callig'] = """This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject."""


eng_feedback['be_np_are_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb which does not agree in person 
(e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject: {}. Please check the sentence and ensure that 
the verb agrees with its subject.""", 0.5)
eng_feedback['be_np_are_rbst']['callig'] = """This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject."""


eng_feedback['be_np_is_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb which does not agree in person 
(e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject: {}. Please check the sentence and ensure that 
the verb agrees with its subject.""", 0.5)
eng_feedback['be_np_is_rbst']['callig'] = """This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject."""


eng_feedback['mal_va_does_le']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb which does not agree in person 
(e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject: {}. Please check the sentence and ensure that 
the verb agrees with its subject.""", 1)
eng_feedback['mal_va_does_le']['callig'] = """This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject."""


eng_feedback['mal_va_has_le']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb which does not agree in person 
(e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject: {}. Please check the sentence and ensure that 
the verb agrees with its subject.""", 1)
eng_feedback['mal_va_has_le']['callig'] = """This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject."""


eng_feedback['mal_va_have_fin_le']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb which does not agree in person 
(e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject: {}. Please check the sentence and ensure that 
the verb agrees with its subject.""", 1)
eng_feedback['mal_va_have_fin_le']['callig'] = """This sentence may have a verb which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with its subject."""


eng_feedback['mal_vc_prd_are_le']['lcc'] = ("""<strong>⇒</strong> You may have used the verb 'are' incorrectly in the sentence: {}.  
Please check your sentence and change the form of the verb if necessary.""", 1)
eng_feedback['mal_vc_prd_are_le']['callig'] = """You may have used the verb 'are' incorrectly in the sentence."""


eng_feedback['mal_vc_prd_be_le']['lcc'] = ("""<strong>⇒</strong> You may have used the verb 'be' incorrectly in the sentence: {}. 
 Please check your sentence and change the form of the verb if necessary.""", 1)
eng_feedback['mal_vc_prd_be_le']['callig'] = """You may have used the verb 'be' incorrectly in the sentence."""


eng_feedback['mal_vc_prd_been_le']['lcc'] = ("""<strong>⇒</strong> You may have used the verb 'been' incorrectly in the sentence: {}. 
Please check your sentence and change the form of the verb if necessary.""", 1)
eng_feedback['mal_vc_prd_been_le']['callig'] = """You may have used the verb 'been' incorrectly in the sentence."""


eng_feedback['mal_vc_prd_is_le']['lcc'] = ("""<strong>⇒</strong> You may have used the verb 'is' incorrectly in the sentence: {}.  
Please check your sentence and change the form of the verb if necessary.""", 1)
eng_feedback['mal_vc_prd_is_le']['callig'] = """You may have used the verb 'is' incorrectly in the sentence."""


eng_feedback['cl-cl_runon-cma_c_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence appears to have a comma separating two 
independent clauses. Please check the sentence and consider using a peroid/full-stop, a semi-colon or an appropriate 
conjunction instead.""", 0.5)
eng_feedback['cl-cl_runon-cma_c_rbst']['callig'] = """This sentence appears to have a comma separating two independent clauses. You should use a peroid/full-stop, a semi-colon or an appropriate conjunction instead."""


eng_feedback['d_-_poss-its-mal_le']['lcc'] = ("""<strong>⇒</strong> This sentence appears to have the wrong form of a possessive, such 
as 'its', 'her', 'his' and 'their': {}.  Please check the sentence and change the form of the possessive if necessary.""", 1)
eng_feedback['d_-_poss-its-mal_le']['callig'] = """This sentence appears to have the wrong form of a possessive, such as 'its', 'her', 'his' and 'their'."""


eng_feedback['d_-_sg-a-mal_le']['lcc'] = ("""<strong>⇒</strong> You have used the wrong form of the indefinite article “a/an”: {}. 
Please check the sentence and change the indefinite article if necessary.""", 1)
eng_feedback['d_-_sg-a-mal_le']['callig'] = """You have used the wrong form of the indefinite article “a/an”."""


eng_feedback['d_-_sg-an-mal_le']['lcc'] = ("""<strong>⇒</strong> You have used the wrong form of the indefinite article “a/an”: {}. 
Please check the sentence and change the indefinite article if necessary.""", 1)
eng_feedback['d_-_sg-an-mal_le']['callig'] = """You have used the wrong form of the indefinite article “a/an”."""


eng_feedback['d_-_the-mal_le']['lcc'] = ("""<strong>⇒</strong> There may be a problem with the use or omission of the definite 
article 'the' in this sentence. Please check your sentence and remove or insert a 'the' if necessary.""", 1)
eng_feedback['d_-_the-mal_le']['callig'] = """There may be a problem with the use or omission of the definite article 'the' in this sentence."""


eng_feedback['mal_vc_there_are_le']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb after 'there' which does not agree in 
person (e.g. 'I', 'you', 's/he') and number (singular/plural) with the noun that comes after it: {}. Please check the sentence 
and ensure that the verb agrees with noun after it.""", 1)
eng_feedback['mal_vc_there_are_le']['callig'] = """This sentence may have a verb after 'there' which does not agree in person (e.g. 'I', 'you', 's/he') and number (singular/plural) with the noun that comes after it."""


eng_feedback['mal_vc_there_is_le']['lcc'] = ("""<strong>⇒</strong> This sentence may have a verb after 'there' which does not agree in 
person (e.g. 'I', 'you', 's/he') and number (singular/plural) with the noun that comes after it: {}. Please check the sentence 
and ensure that the verb agrees with noun after it.""", 1)
eng_feedback['mal_vc_there_is_le']['callig'] = """This sentence may have a verb after 'there' which does not agree in  person (e.g. 'I', 'you', 's/he') and number (singular/plural) with the noun that comes after it."""


eng_feedback['much_a1_rbst']['lcc'] = ("""<strong>⇒</strong> This sentence may have a determiner, such as 'much' or 'many', that should 
not be used with the countable/uncountable after it: {}. Please check the sentence and change the determiner if necessary.""", 1)
eng_feedback['much_a1_rbst']['callig'] = """This sentence may have a determiner, such as 'much' or 'many', that should not be used with the countable/uncountable after it."""




################################################################################
# FEEDBACK ON STYLE
################################################################################

eng_feedback['Contraction']['lcc'] = ("""<strong>⇒</strong> This sentence contains a contraction (e.g. 'it's', 'he'll', 'can't): {}. Contractions are 
not used in formal documents. You may want to expand the contractions to spell out the verb or the word 'not' in full.""", 1)


eng_feedback['Formal']['lcc'] = ("""<strong>⇒</strong> This sentence may contain overly formal/archaic words or expressions that may make your writing seem stilted or pompous: {}. You may want to replace these words and expressions with more commonly used expressions, such as mentioned above, previously and according to, that will make your writing more accessible. """, 0.5)


eng_feedback['Informal']['lcc'] = ("""<strong>⇒</strong> This sentence may contain subjective or informal words or expressions: {}. You may want to replace these words and expressions with more formal and objective alternatives. """, 0.5)


eng_feedback['LongSentence']['lcc'] = ("""<strong>⇒</strong> This sentence is much longer than the average sentence. It may be difficult for readers to read the sentence and understand it after reading it once. There is also a higher risk of making grammar mistakes in such a long sentence. You may want to consider breaking up the sentence to make it easier for the reader to follow the text.""", 0.5)


eng_feedback['VeryLongSentence']['lcc'] = ("""<strong>⇒</strong> This sentence is much longer than the average sentence. It may be difficult for readers to read the sentence and understand it after reading it once. There is also a higher risk of making grammar mistakes in such a long sentence. You may want to consider breaking up the sentence to make it easier for the reader to follow the text.""", 1)


eng_feedback['PronounStyle']['lcc'] = ("""<strong>⇒</strong> This sentence contains a first person singular pronoun (e.g. 'I', 'mine') or a second person pronoun (e.g. 'you', 'yours'): {}. These pronouns are not used in formal technical writing. You may want to remove the pronouns listed above and use alternative sentence constructions that avoid the use of such pronouns.""", 1)


eng_feedback['ques']['lcc'] = ("""<strong>⇒</strong> The system has identified this sentence as a question (discouraged in formal writing). Read your sentence
 carefully, and decide whether you need to change it. You should change it if it is actually a question in the main part of your 
proposal. You can ignore the alert if the ‘question’ appears in your references list.""", 0.5)


eng_feedback['WordCase']['lcc'] = ("""<strong>⇒</strong> You may be using upper or lower case (capital and small letters) inappropriately in this 
sentence: {}. Please check your sentence and make changes to your use of upper or lower case only if you feel it is 
necessary.""", 0.5)


eng_feedback['sb-hd_mc-ques_c_rbst']['lcc'] = ("""<strong>⇒</strong> The system has identified this sentence as a question (discouraged 
in formal writing). Please read your sentence carefully, and decide whether you need to change it. You should 
change it if it is actually a question in the main part of your proposal. You can ignore the alert if the 
‘question’ appears in your references list. """, 0.5)


eng_feedback['comm']['lcc'] = ("""<strong>⇒</strong> The system has identified this sentence as an instruction/command (discouraged in formal proposals) 
rather than as a statement/description. However, if you are confident that the ‘sentence’ is not meant to be a sentence in the 
first place, you can ignore the alert. For example, the ‘sentence’ may be a heading, part of a list of items and costs, or an 
entry in your references list. Read your sentence carefully, and decide whether you need to change it. You should change it 
if it is actually a command/instruction.""", 0.5)


# FIXME: Maybe these should be distributed among other categories?
eng_feedback['WordChoice']['lcc'] = ("""<strong>⇒</strong> You may used a word or phrase that our lecturers would like you to avoid: {}. Please double check if it is necessary, and rephrase it if possible.""", 0.5)



################################################################################
# OTHER GENERIC FEEDBACK
################################################################################

eng_feedback['RepeatedWord']['lcc'] = ("""<strong>⇒</strong> You may have repeated a word in this sentence: {}. Please check the sentence and remove one instance of this word if necessary.""", 1)

eng_feedback['Spelling']['lcc'] = ("""<strong>⇒</strong> You may have mispelled a word: {}. Please double check the spelling of this word and change it if necessary.""", 0.5)


eng_feedback['NoParse']['lcc'] = ("""<strong>⇒</strong> The system indicates that this sentence may be problematic but cannot specify the error/s. 
Please read the sentence carefully to check whether there are any errors, and correct them.""", 0.5)

