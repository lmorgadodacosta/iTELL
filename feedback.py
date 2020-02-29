from collections import defaultdict as dd
eng_feedback = dd(lambda: dd())

eng_feedback['a_det_mass_rbst']['lcc'] = ("""<strong>⇒</strong> You may be using an indefinite article, 'a' or 'an', before an uncountable noun (such as 'research'): {}. Indefinite articles should only precede singular countable nouns. Please check your sentence for uncountable nouns and remove any indefinite articles that precede them.""", 1)
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





################################################################################
# LCC FEEDBACK 2.0
################################################################################


eng_feedback['a_det_mass_rbst']['lcc2'] = ('''<strong>ARTICLE (‘a’ + uncountable noun): '{}'</strong><br><ul> <li>You may be using ‘a’ (an indefinite article) before an uncountable noun (something that cannot be counted and does not have a plural form, e.g. ‘research’), including nouns which can also be adjectives (e.g. 'disabled'). <li>Please check your sentence for the use of ‘a’ before an uncountable noun, and remove 'a' OR replace 'a' with another determiner or quantifier (e.g. 'a piece of’, ‘a type of’, 'the', 'this') OR add a singular countable noun (e.g. 'person') after the noun which can also be an adjective (e.g. 'a disabled person').</ul>''',1) # 

eng_feedback['a_det_plur_rbst']['lcc2'] = ('''<strong>ARTICLE (‘a’ + plural noun): '{}'</strong><br><ul> <li>You may be using ‘a’ (an indefinite article) before a plural countable noun (more than one item of something that can be counted and has a plural form, e.g. ‘devices’).  <li>Please check your sentence for the use of ‘a’ before a plural countable noun, and remove 'a' OR replace 'a' with another determiner or quantifier (e.g. 'the', 'these',  'some') OR replace the plural countable noun with a singular one (e.g. ‘device’).</ul>''',1) #

eng_feedback['an_det_plur_rbst']['lcc2'] = ('''<strong>ARTICLE (‘an’ + plural nouns): '{}'</strong><br><ul> <li>You may be using ‘an’ (an indefinite article), before a plural countable noun (more than one of something that can be counted and has a plural form, e.g. 'errors').<li>Please check your sentence for the use of ‘an’ before a plural countable noun, and remove 'an' OR replace 'an' with another determiner or quantifier (e.g. 'the', 'these', 'some') OR replace the plural countable noun with a singular one (e.g. ‘error’).</ul>''',1) #

eng_feedback['a_prop_1_rbst']['lcc2'] = ('''<strong>ARTICLE (‘a’ + proper noun): '{}'</strong><br><ul> <li>You may have used ‘a’ (an indefinite article) before a proper noun (the name of a specific thing, usually beginning with a capital letter, e.g. ‘Singapore’).<li>Please check your sentence for the use of ‘a’ before a proper noun on its own (e.g. ‘a Singapore’), and remove ‘a’ if necessary.</ul>''',0.5) #

eng_feedback['after_pp_rbst']['lcc2'] = ('''<strong>PREPOSITION (‘after’ following by nothing): '{}'</strong><br><ul> <li>You may have used the preposition ‘after’ on its own, without specifying an event or object (e.g. ‘after this’, ‘after a minute’).<li>Please check your sentence for the use of ‘after’, and remove ‘after’ OR add an event or object behind ‘after’ (e.g. after this step’) OR change ‘after’ to ‘afterwards’.</ul>''',0.5) #

eng_feedback['an_det_mass_rbst']['lcc2'] = ('''<strong>ARTICLE (‘an’ + uncountable noun): '{}'</strong><br><ul> <li>You may be using ‘an’ (an indefinite article), before an uncountable noun (which does not have a plural form, e.g. 'information'), including nouns which can also be adjectives (e.g. 'elderly').<li>Please check your sentence for the use of ‘an’ before an uncountable noun, and remove the 'an' OR replace 'an' with another determiner or quantifier (e.g. 'the',  'a piece of’, ‘a type of', 'some') OR add a singular countable noun (e.g. 'person') after the noun which can also be an adjective (e.g. 'an elderly person').</ul>''',1) #

eng_feedback['an_prop_1_rbst']['lcc2'] = ('''<strong>ARTICLE (‘an’ + proper noun): '{}'</strong><br><ul> <li>You may have used ‘an’ (an indefinite article) before a proper noun (the name of a specific thing, usually beginning with a capital letter, e.g. ‘Asia’).<li>Please check your sentence for the use of ‘an’ before a proper noun on its own (e.g. ‘an Asia’), and remove ‘an’ if necessary.</ul>''',0.5) #

eng_feedback['bad_adv1_rbst']['lcc2'] = ('''<strong>ADVERB (‘bad’ vs. ‘badly’): '{}'</strong><br><ul> <li>You may be using ‘bad’ (an adjective: used to describe things) instead of ‘badly’ or ‘poorly’ (adverbs: used to describe actions) to describe an action.<li>Please check your sentence for the use of ‘bad’, and change it to ‘badly’ or ‘poorly’ if necessary.</ul>''',0.5) #

eng_feedback['good_adv1_rbst']['lcc2'] = ('''<strong>ADVERB (‘good’ vs. ‘well’): '{}'</strong><br><ul> <li>You may be using ‘good’ (an adjective: used to describe things) instead of ‘well’ (adverbs: used to describe actions) to describe an action.<li>Please check your sentence for the use of ‘good’, and change it to ‘well’ if necessary.</ul>''',0.5) #

eng_feedback['be_are_have_rbst']['lcc2'] = ('''<strong>VERB FORM ('are' vs. 'have'): '{}'</strong><br><ul> <li>You may have used ‘are’ instead of ‘have’ at the beginning of a verb phrase (words describing an action, e.g. 'are solved', 'have solved').<li>Please check your sentence for the wrong use of ‘are’ at the beginning of a verb phrase, and change ‘are’ to ‘have’ if necessary.</ul>''',1) #

eng_feedback['be_is_has_rbst']['lcc2'] = ('''<strong>VERB FORM ('is' vs. 'has'):'{}'</strong><br><ul> <li>You may have used ‘is’ instead of ‘has’ at the beginning of a verb phrase (words describing an action, e.g. 'is done', 'has done').<li>Please check your sentence for the wrong use of ‘is’ at the beginning of a verb phrase, and change ‘is’ to ‘has’ if necessary.</ul>''',1) #

eng_feedback['be_c_are_rbst']['lcc2'] = ('''<strong>AGREEMENT ('are' vs. 'is'): '{}'</strong><br><ul> <li>This sentence may have the verb 'are', which does not agree with its subject, in person (e.g. 'she', 'it') and/or number (singular: just one item, e.g. 'device').<li>Please check the sentence, and change 'are' to 'is' so the verb agrees with its subject OR change the subject to a plural noun (more than one item, e.g. 'The devices are ...').</ul>''',1) # 

eng_feedback['be_c_been_rbst']['lcc2'] = ('''<strong>VERB FORM ('been'): '{}'</strong><br><ul> <li>You may have used the verb 'been' incorrectly, without 'has', 'have', 'having' or 'had' before it, in the sentence.<li>Please check your use of 'been' in the sentence, and change it to 'has been', 'have been', 'having been' or 'had been' OR change 'be' to another form of the verb 'be' (such as 'am', 'is', 'are', 'was', or 'were').</ul>''',1) #

eng_feedback['be_c_is_rbst']['lcc2'] = ('''<strong>AGREEMENT ('is' vs. 'are'): '{}'</strong><br><ul> <li>This sentence may have the verb 'is', which does not agree with its subject, in person  (e.g. 'I', 'you') and/or number (plural: more than one item, e.g. 'devices', 'they').<li>Please check the sentence for the use of ‘is’, and change 'is' to 'are' so the verb agrees with its subject OR change the subject to a singular noun (just one item, e.g. 'a device').</ul>''',1) #

eng_feedback['be_np_are_rbst']['lcc2'] = ('''<strong>AGREEMENT ('is' vs. 'are'): '{}'</strong><br><ul> <li>This sentence may have the verb 'is', which does not agree with its subject, in person  (e.g. 'I', 'you') and/or number (plural: more than one item, e.g. 'companies', 'they').<li>Please check the sentence for the use of ‘is’, and change 'is' to 'are' so the verb agrees with its subject OR change the subject to a singular noun (just one item, e.g. 'a company').</ul>''',0.5) #

eng_feedback['be_np_is_rbst']['lcc2'] = ('''<strong>AGREEMENT ('are' vs. 'is'): '{}'</strong><br><ul> <li>This sentence may have the verb 'are', which does not agree with its subject, in person  (e.g. 'I', 'he/she/it') and/or number (singular: just one item, e.g. 'company').<li>Please check the sentence for the use of ‘are’, and change 'are' to 'is' so the verb agrees with its subject OR change the subject to a plural noun (more than one item, e.g. 'companies').</ul>''',0.5) #

eng_feedback['be_th_cop_are_rbst']['lcc2'] = ('''<strong>AGREEMENT ('there are' vs. 'there is'): '{}'</strong><br><ul> <li>You may have used 'there are' followed by a singular noun (one item of something which can be counted, e.g. 'device') in this sentence.<li>Please check the sentence, and change 'there are' to 'there is' OR change the singular noun to a plural noun (e.g. 'there are devices ...').</ul>''',1) #

eng_feedback['be_th_cop_is_rbst']['lcc2'] = ('''<strong>AGREEMENT ('there is' vs. 'there are'): '{}'</strong><br><ul> <li>You may have used 'there is' followed by a plural noun (more than one item of something which can be counted, e.g. 'devices') in this sentence.<li>Please check the sentence, and change 'there is' to 'there are' OR change the plural noun to a singular noun (e.g. 'there is a device ...').</ul>''',1) #

eng_feedback['cl-cl_runon-cma_c_rbst']['lcc2'] = ('''<strong>COMMA SPLICE: '{}'</strong><br><ul> <li>This sentence appears to have a comma separating two independent clauses (parts of a sentence that can stand on their own as sentences). <li>Please check the sentence, and consider using a period/full-stop (.), a semi-colon (;) or an appropriate conjunction (e.g. 'and', 'but', 'so') to separate the 2 clauses instead of a comma.</ul>''',0.5) #

eng_feedback['comm']['lcc2'] = ('''<strong>IMPERATIVES: '{}'</strong><br><ul> <li>The system has identified this sentence as an instruction/command (e.g. 'Collaborate with xxx'), which is discouraged in formal proposals. However, if you are confident that the ‘sentence’ is not meant to be a sentence in the first place, you can ignore the alert. For example, the ‘sentence’ may be part of a list of items and costs. <li>Read your sentence carefully, and change the instruction/command to a statement or description (e.g. 'Collaboration with xxx will ...') if it is actually a command/instruction.</ul>''',0.5) #

eng_feedback['Contraction']['lcc2'] = ('''<strong>CONTRACTION: '{}'</strong><br><ul> <li>This sentence may contain a contraction of a word or 2 words (e.g. 'it's', 'can't).<li>As contractions are not used in formal documents, please check the sentence for contractions, and spell out the word/s in full (e.g. 'it is …', 'cannot') if necessary.</ul>''',1) #

eng_feedback['d_-_poss-its-mal_le']['lcc2'] = ('''<strong>POSSESSIVE ('it's' vs. 'its'): '{}'</strong><br><ul> <li>This sentence appears to have a contraction, 'it's' (meaning: 'it is'), instead of 'its' (meaning: 'belonging to it') in it. <li>Please check the sentence, and remove the apostrophe (') if necessary, so 'it's' becomes 'its'.</ul>''',1) #

eng_feedback['d_-_sg-a-mal_le']['lcc2'] = ('''<strong>ARTICLE ('a' vs. 'an'): '{}'</strong><br><ul> <li>You may have used the wrong indefinite article 'a' instead of 'an' in your sentence (e.g. 'a hour'). If the word after the indefinite article begins with a vowel sound (sounds associated with 'a', 'e', 'i', 'o', and 'u', e.g. 'hour'), you should use 'an' before the word (e.g. 'an hour').<li>Please check the sentence, and change the indefinite article from 'a' to 'an' if necessary.</ul>''',1) #

eng_feedback['d_-_sg-an-mal_le']['lcc2'] = ('''<strong>ARTICLE ('an' vs. 'a'): '{}'</strong><br><ul> <li>You may have used the wrong indefinite article 'an' instead of 'a' in your sentence (e.g. 'an user', 'an one-time case'). If the word after the indefinite article does NOT begin with a vowel sound (sounds associated with 'a', 'e', 'i', 'o', and 'u'), you should use 'a' before the word (e.g. 'a user', 'a one-time case'). Please be careful about words that begin with vowels in their spelling but not in their pronunciation.  For example, 'user' begins with a 'u' in its spelling but with a sound similar to 'y' in its pronunciation. <li>Please check the sentence, and change the indefinite article from 'an' to 'a' if necessary.</ul>''',1) #

eng_feedback['do1_pos_sg_rbst']['lcc2'] = ('''<strong>AGREEMENT ('do' vs. 'does'): '{}'</strong><br><ul> <li>This sentence may have the verb 'do' at the beginning of a verb phrase (e.g. 'do make'), which does not agree with its subject, in person (e.g. 'it') and/or number (singular: one item, e.g. 'the device').<li>Please check the sentence for the use of 'do’ at the beginning of a verb phrase, and change it to 'does' (e.g. 'does make') so the verb agrees with its subject OR change the subject to a plural noun (more one item, e.g. 'The devices do make ...').</ul>''',1) #

eng_feedback['does1_pos_pl_rbst']['lcc2'] = ('''<strong>AGREEMENT ('does' vs. 'do'): '{}'</strong><br><ul> <li>This sentence may have the verb 'does' at the beginning of a verb phrase (e.g. 'does make'), which does not agree with its subject, in person (e.g. 'I', 'you') and/or number (plural: more than one item, e.g. 'the devices').<li>Please check the sentence for the use of 'does’ at the beginning of a verb phrase, and change it to 'do' (e.g. 'do make') so the verb agrees with its subject OR change the subject to a singular noun (one item, e.g. 'The device does make ...').</ul>''',1) #

eng_feedback['every_all_rbst']['lcc2'] = ('''<strong>DETERMINER ('every' + plural noun):'{}'</strong><br><ul> <li>You may have used 'every' (a determiner) before a plural countable noun (more than one item of something that can be counted and has a plural form, e.g. ‘devices’)  in this sentence.<li>Please check your use of ‘every’ in the sentence carefully, and change 'every' to 'all’/’all the’/’both’/’both the' OR change the plural countable noun (e.g. 'devices') to a singular one (e.g. 'device') if necessary.</ul>''',1) #

eng_feedback['everyday_adv_rbst']['lcc2'] = ('''<strong>ADVERB ('every day' vs. 'everyday'): '{}'</strong><br><ul> <li>You have used 'everyday' as an adverb (a word describing an action or event) in your sentence when it is an adjective (a word that describes a thing or entity).<li>Please check your sentence carefully, and add a space between 'every' and 'day' (e.g. 'The system is checked every day.') if necessary.</ul>''',1) #

eng_feedback['Formal']['lcc2'] = ('''<strong>TOO FORMAL: '{}'</strong><br><ul> <li>This sentence may contain overly formal/archaic words or expressions (such as 'aforementioned') that may make your writing seem stilted or pompous.<li>You may want to replace these words and expressions with more commonly used expressions, such as 'previously mentioned', that will make your writing more accessible.</ul>''',0.5) #

eng_feedback['hdn_bnp_c_rbst']['lcc2'] = ('''<strong>ARTICLE (missing): '{}'</strong><br><ul> <li>This sentence has a singular noun (one item of something which can be counted, e.g. 'device') without an article ('a', 'an', 'the'), determiner (e.g. 'each', 'this') or possessive (e.g. 'her', 'its') before it.<li>Please check your sentence carefully, and add an article, determiner or possessive before the singular noun (e.g. 'the device') OR change the subject to a plural noun (more than one item, e.g. 'devices').</ul>''',1) #

eng_feedback['Informal']['lcc2'] = ('''<strong>INFORMAL: '{}'</strong><br><ul> <li>This sentence may contain subjective or informal words or expressions.<li>You may want to replace these words and expressions with more formal and objective alternatives.</ul>''',0.5) #

eng_feedback['LongSentence']['lcc2'] = ('''<strong>LONG SENTENCE: '{}'</strong><br><ul> <li>This sentence is much longer than the average sentence. It may be difficult for readers to read the sentence and understand it after reading it once. There is also a higher risk of making grammar mistakes in such a long sentence. <li>You may want to consider breaking up the sentence to make it easier for the reader to follow the text, and to avoid making mistakes.</ul>''',0.5) #

eng_feedback['mal_va_has_le']['lcc2'] = ('''<strong>AGREEMENT ('have' vs. 'has'): '{}'</strong><br><ul> <li>This sentence may have the verb 'have', which does not agree with its subject, in person (e.g. 'she', 'it') and/or number (singular: just one item, e.g. 'device').<li>Please check the sentence, and change 'have' to 'has' so the verb agrees with its subject OR change the subject to a plural noun (more than one item, e.g. 'The devices have ...').</ul>''',1) #

eng_feedback['mal_va_have_fin_le']['lcc2'] = ('''<strong>AGREEMENT ('has' vs. 'have'): '{}'</strong><br><ul> <li>This sentence may have the verb 'has', which does not agree with its subject, in person (e.g. 'I', 'you') and/or number (plural: more than one item, e.g. 'devices').<li>Please check the sentence, and change 'have' to 'has' so the verb agrees with its subject OR change the subject to a singular noun (just one item, e.g. 'The device has ...').</ul>''',1) #

eng_feedback['mal_vc_prd_be_le']['lcc2'] = ('''<strong>VERB FORM ('be'): '{}'</strong><br><ul> <li>You may have used the verb 'be' incorrectly in the sentence.<li>Please check your sentence, and change 'be' to another form (e.g. 'is/are/am', 'was/were', 'being', 'been', 'will/shall be') OR remove the verb 'be' if necessary.</ul>''',1) #

eng_feedback['many_div_mal_adj ']['lcc2'] = ('''<strong>DETERMINER ('many' + uncountable noun): '{}'</strong><br><ul> <li>You may have used 'many' before an uncountable noun (e.g. 'information') in this sentence.<li>Please check your sentence for the use of 'many' before an uncountable noun, and change 'many' to 'a lot of', 'some', 'the', 'this', or 'that' if necessary.</ul>''',1) #

eng_feedback['many_mal_adj']['lcc2'] = ('''<strong>DETERMINER ('many' + singular noun): '{}'</strong><br><ul> <li>You may have used 'many' before a singular countable noun (just one item of something which can be counted, e.g. 'device') in this sentence.<li>Please check your sentence for the use of 'many' before a singular countable noun, and change the noun to a plural noun (e.g. 'many devices') OR change 'many' to 'a', 'the', 'this', or 'that' if necessary.</ul>''',1) #

eng_feedback['much_a1_rbst']['lcc2'] = ('''<strong>DETERMINER ('much' + plural noun): '{}'</strong><br><ul> <li>You may have used 'much' before a plural countable noun (more than one item of something which can be counted, e.g. 'devices') in this sentence.<li>Please check your sentence for the use of 'much' before a plural countable noun, and change it to 'many' or 'some' if necessary (e.g. 'many devices').</ul>''',1) #

eng_feedback['n_pl_mass_olr_rbst']['lcc2'] = ('''<strong>NOUN (uncountable + plural marker): '{}'</strong><br><ul> <li>You may have added a plural marker (e.g. '-s') to an uncountable noun (something that cannot be counted and does not have a plural form, e.g. ‘research’).<li>Please check your sentence, and remove the plural marker (e.g. 'researches') from the uncountable noun.</ul>''',0.5) #

eng_feedback['n_pl-mass_olr_rbst']['lcc2'] = ('''<strong>PLURAL (uncountable): '{}'</strong><br><ul> <li>This sentence contains an uncountable noun (something that cannot be counted and does not have a plural form, e.g. ‘information’) with a plural marking (e.g. 'informations').<li>Please check the uncountable noun in the sentence, and remove its plural marking if necessary.</ul>''',0.5) #

eng_feedback['non_third_sg_fin_v_rbst']['lcc2'] = ('''<strong>AGREEMENT (plural noun): '{}'</strong><br><ul> <li>This sentence may have a verb that expects subject which is a singular noun (just one item of something which can be counted, e.g. 'device') , but its subject does not agree with the verb. <li>Please check the sentence, and change the verb so it agrees with its subject (e.g. 'The devices cost ...') OR make the subject a singular noun (e.g. 'The device costs ...').</ul>''',1) #

eng_feedback['NoParse']['lcc2'] = ('''<strong>UNKNOWN/TOO MANY ERRORS: '{}'</strong><br><ul> <li>The system indicates that this sentence may be problematic but cannot specify the error/s.  <li>Please read the sentence carefully to check whether there are any errors, and correct them.</ul>''',0.5) #

eng_feedback['num_det_2_rbst']['lcc2'] = ('''<strong>NUMBER (plural): '{}'</strong><br><ul> <li>You may have used a singular noun (one item of something which can be counted, e.g. 'device') with a number for plural  nouns (e.g. 'two device').<li>Please check the number and the noun, and change the singular noun to a plural noun (e.g. 'devices') OR change the number to one (e.g. 'One device', '1 device') if necessary.</ul>''',1) #

eng_feedback['num_det_1_rbst']['lcc2'] = ('''<strong>NUMBER (plural): '{}'</strong><br><ul> <li>You may have used a plural noun (more than one item of something which can be counted, e.g. 'devices') with a number for singular nouns (e.g. 'one devices').<li>Please check the number and the noun, and change the plural noun to a singular noun (e.g. 'device') OR change the number to (e.g. '2 devices', 'three devices') if necessary.</ul>''',1) #

eng_feedback['only_adv1_mal']['lcc2'] = ('''<strong>ADVERBIAL ('only'):'{}'</strong><br><ul> <li>Only' may be in the wrong position in your sentence.  <li>Please check the sentence and move 'only' to another position in the sentence if necessary.</ul>''',0.5) #

eng_feedback['other_rbst']['lcc2'] = ('''<strong>DETERMINER ('other'): '{}'</strong><br><ul> <li>You may have used 'other' before a singular noun (one item of something which can be counted, e.g. 'device') in this sentence.<li>Please check the sentence, and replace 'other' with 'another' (e.g. 'another device') OR change the noun to its plural form (e.g. 'other devices') if necessary.</ul>''',0.5)

eng_feedback['PronounStyle']['lcc2'] = ('''<strong>PRONOUN (1st or 2nd person): '{}'</strong><br><ul> <li>This sentence contains a first person singular pronoun (e.g. 'I', 'mine') or a second person pronoun (e.g. 'you', 'yours'). These pronouns are not used in formal technical writing. <li>You may want to remove the first person singular or second person pronouns (e.g. 'You can use the product to …'), and use alternative sentence constructions, such as passive constructions (e.g. 'The product can be used to …'), that avoid the use of such pronouns.</ul>''',1) #

eng_feedback['ques']['lcc2'] = ('''<strong>INTERROGATIVE: '{}'</strong><br><ul> <li>The system has identified this sentence as a question, which is discouraged in formal writing.<li>Read your sentence carefully, and decide whether you need to change it. You should change it if it is actually a question in the main part of your proposal. </ul>''',0.5)

eng_feedback['RepeatedWord']['lcc2'] = ('''<strong>REPETITION: '{}'</strong><br><ul> <li>You may have repeated a word in this sentence.<li>Please check the sentence, and remove one instance of this word if necessary.</ul>''',1) #

eng_feedback['sb-hd_mc-cma_c_rbst']['lcc2'] = ('''<strong>COMMA: '{}'</strong><br><ul> <li>You may have used a comma just before a verb in the sentence (e.g. 'The device, is needed …').<li>Please check the sentence, and remove the comma if necessary.</ul>''',0.5) #

eng_feedback['sb-hd_mc-ques_c_rbst']['lcc2'] = ('''<strong>QUESTION MARK: '{}'</strong><br><ul> <li>You may have used a question mark at the end of a sentence that is not meant to be a question (e.g. 'How this device is used can be easily understood?').<li>Please check the sentence, and change the question mark to a period/full stop if necessary (e.g. 'How this device is used can be easily understood.').</ul>''',1) #

eng_feedback['such_a_det_rbst']['lcc2'] = ('''<strong>DETERMINER ('such a'): '{}'</strong><br><ul> <li>You have used 'such' immediately before a singular noun (one item of something which can be counted, e.g. 'device') in this sentence when there should be an article, 'a', between them (e.g. 'such a device').<li>Please read your sentence carefully, and insert 'a' after 'such' (e.g. 'such a device') OR change the singular noun to a plural noun (e.g. 'such devices') if necessary.</ul>''',1) #

eng_feedback['such_an_det_rbst']['lcc2'] = ('''<strong>DETERMINER ('such an'): '{}'</strong><br><ul> <li>You have used 'such' immediately before a singular noun (one item of something which can be counted, e.g. 'error') in this sentence when there should be an article, 'an', between them (e.g. 'such an error').<li>Please read your sentence carefully, and insert 'an' after 'such' (e.g. 'such an error') OR change the singular noun to a plural noun (e.g. 'such errors') if necessary.</ul>''',1) #

eng_feedback['that_det_rbst']['lcc2'] = ('''<strong>DETERMINER ('that' vs. 'those'): '{}'</strong><br><ul> <li>You may have used the determiner ‘that’ instead of ‘those’ before a plural countable noun (more than one item of something that can be counted and has a plural form, e.g. devices’) in your sentence.<li>Please check your sentence for the use of ‘that’ before a plural noun, and change it to ‘those’ OR change the plural noun to a singular noun (e.g. ‘that device’).</ul>''',1) #

eng_feedback['the_2_rbst']['lcc2'] = ('''<strong>ARTICLE ('the' + 'a'): '{}'</strong><br><ul> <li>You may have used ‘the’ (a definite article) before ‘a’ (an indefinite article) in front of a noun (a thing or entity).<li>Please check your sentence for the use of ‘the a’, and remove either ‘the’ or ‘a’.</ul>''',1) #

eng_feedback['the_3_rbst']['lcc2'] = ('''<strong>ARTICLE ('a' + 'the'): '{}'</strong><br><ul> <li>You may have used ‘a’ (an indefinite article) before ‘the’ (a definite article) in front of a noun (a thing or entity).<li>Please check your sentence for the use of ‘a the’, and remove either ‘a’ or ‘the’.</ul>''',1) #

eng_feedback['the_4_rbst']['lcc2'] = ('''<strong>ARTICLE/DETERMINER ('the' + 'both'): '{}'</strong><br><ul> <li>You may have used ‘the’ (a definite article) before ‘both’ (a determiner) in front of a noun (a thing or entity).<li>Please check your sentence for the use of ‘the both’, and remove either ‘the’ or ‘both’.</ul>''',1) #

eng_feedback['the_5_rbst']['lcc2'] = ('''<strong>ARTICLE/DETERMINER ('the' + 'this'): '{}'</strong><br><ul> <li>You may have used ‘the’ (a definite article) before ‘this’ (a determiner) in front of a noun (a thing or entity).<li>Please check your sentence for the use of ‘the this’, and remove either ‘the’ or ‘this’.</ul>''',1) #

eng_feedback['the_6_rbst']['lcc2'] = ('''<strong>ARTICLE/DETERMINER ('the' + 'these'): '{}'</strong><br><ul> <li>You may have used ‘the’ (a definite article) before ‘these’ (a determiner) in front of a noun (a thing or entity).<li>Please check your sentence for the use of ‘the these’, and remove either ‘the’ or ‘these’.</ul>''',1) #

eng_feedback['the_7_rbst']['lcc2'] = ('''<strong>ARTICLE/DETERMINER ('the' + 'each'): '{}'</strong><br><ul> <li>You may have used ‘the’ (a definite article) before ‘each’ (a determiner) in front of a noun (a thing or entity).<li>Please check your sentence for the use of ‘the each’, and remove either ‘the’ or ‘each’.</ul>''',1) #

eng_feedback['the_stutter_1']['lcc2'] = ('''<strong>ARTICLE (repeated, hyphen):'{}'</strong><br><ul> <li>You may have used 'the-the' (with a hyphen) in this sentence.<li>Please check your sentence carefully, and change 'the-the' to 'the'.</ul>''',1) #

eng_feedback['the_stutter_2']['lcc2'] = ('''<strong>ARTICLE (repeated, comma):'{}'</strong><br><ul> <li>You may have used 'the, the' (with a comma in between) in this sentence.<li>Please check your sentence carefully, and change 'the, the' to 'the'.</ul>''',1) #

eng_feedback['this_det_rbst']['lcc2'] = ('''<strong>DETERMINER ('this' vs. 'these'): '{}'</strong><br><ul> <li>You may have used the determiner ‘this’ instead of ‘these’ before a plural countable noun (more than one item of something that can be counted and has a plural form, e.g. devices’) in your sentence.<li>Please check your sentence for the use of ‘this’ before a plural noun, and change it to ‘these’ OR change the plural noun to a singular noun (e.g. ‘that device’).</ul>''',1) #

eng_feedback['afternoon_nospr_n1_rbst']['lcc2'] = ('''<strong>ARTICLE ('the afternoon'): '{}'</strong><br><ul> <li>You may be using 'afternoon' on its own instead of 'the afternoon' in the sentence.<li>Please check your sentence, and add 'the' before 'afternoon' if necessary.</ul>''',1) # 

eng_feedback['evening_nospr_n1_rbst']['lcc2'] = ('''<strong>ARTICLE ('the evening'): '{}'</strong><br><ul> <li>You may be using 'evening' on its own instead of 'the evening' in the sentence.<li>Please check your sentence, and add 'the' before 'evening' if necessary.</ul>''',1) #

eng_feedback['its_be_cop_rbst ']['lcc2'] = ('''<strong>APOSTROPHE ('its' vs. 'it's): '{}'</strong><br><ul> <li>You may have used 'its' (meaning: belonging to it) instead of 'it's' (meaning: 'it is') in this sentence (e.g. 'Its simple to use').<li>Please check the use of 'its' in the sentence, and change it to 'it is' if necessary (e.g. 'It is simple to use').  Contractions such as 'it's' are not used in formal writing.</ul>''',1) #

eng_feedback['its_be_np_rbst  ']['lcc2'] = ('''<strong>APOSTROPHE ('its' vs. 'it's): '{}'</strong><br><ul> <li>You may have used 'its' (meaning: belonging to it) instead of 'it's' (meaning: 'it is') in this sentence (e.g. 'Its a useful device').<li>Please check the use of 'its' in the sentence, and change it to 'it is' if necessary (e.g. 'It is a useful device').  Contractions such as 'it's' are not used in formal writing.</ul>''',1) #

eng_feedback['its_poss_2_rbst']['lcc2'] = ('''<strong>DETERMINER ('it's' vs. 'its'): '{}'</strong><br><ul> <li>You may have used 'it's' (meaning: 'it is') instead of 'its' (meaning: belonging to it) in this sentence (e.g. 'The device relies on it's sensors').<li>Please check the use of 'it's' in the sentence, and change it to 'its' if necessary (e.g. 'The device relies on its sensors'). </ul>''',1) #

eng_feedback['its_poss_2_u_rbst']['lcc2'] = ('''<strong>DETERMINER ('it's' vs. 'its'): '{}'</strong><br><ul> <li>You may have used 'it's' (meaning: 'it is') instead of 'its' (meaning: belonging to it) in this sentence (e.g. 'The device relies on it's sensors').<li>Please check the use of 'it's' in the sentence, and change it to 'its' if necessary (e.g. 'The device relies on its sensors'). </ul>''',1) #

eng_feedback['its_poss_rbst']['lcc2'] = ('''<strong>DETERMINER ('it's' vs. 'its'): '{}'</strong><br><ul> <li>You may have used 'it's' (meaning: 'it is') instead of 'its' (meaning: belonging to it) in this sentence (e.g. 'The device relies on it's sensors').<li>Please check the use of 'it's' in the sentence, and change it to 'its' if necessary (e.g. 'The device relies on its sensors'). </ul>''',1) #

eng_feedback['morning_nospr_n1_rbst']['lcc2'] = ('''<strong>ARTICLE ('the morning'): '{}'</strong><br><ul> <li>You may be using 'morning' on its own instead of 'the morning' in the sentence.<li>Please check your sentence, and add 'the' before 'morning' if necessary.</ul>''',1) #

eng_feedback['their_rbst']['lcc2'] = ('''<strong>DETERMINER ('there' vs. 'their'): '{}'</strong><br><ul> <li>You may have used 'there' instead of 'their' in this sentence.<li>Please check the sentence and change 'there' to 'their' if necessary.</ul>''',1) #

eng_feedback['third_sg_fin_v_rbst']['lcc2'] = ('''<strong>AGREEMENT (singular noun): '{}'</strong><br><ul> <li>This sentence may have a subject which is a singular noun (just one item of something which can be counted, e.g. 'device') with a verb for a plural subject (e.g. 'The device cost ...').<li>Please check the sentence, and change the verb so it agrees with its subject (e.g. 'The device costs ...') OR make the subject a plural noun (e.g. 'The devices cost ...').</ul>''',1) #

eng_feedback['too_deg_nc_rbst']['lcc2'] = ('''<strong>ADVERB ('too' vs. 'to'): '{}'</strong><br><ul> <li>You may have used 'to' instead of 'too' in this sentence.<li>Please check your use of 'to' in the sentence, and change it to 'too' if necessary.</ul>''',0.5) #

eng_feedback['too_deg_rbst']['lcc2'] = ('''<strong>ADVERB ('too' vs. 'to'): '{}'</strong><br><ul> <li>You have used 'to' more than once in this sentence (e.g. 'the device is to hot to handle') instead of using 'too' in one of these instances (e.g. 'the device is too hot to handle').<li>Please check the sentence to see if 'too' should replace 'to' anywhere in the sentence.</ul>''',0.5) #

eng_feedback['v_pst_olr_rbst']['lcc2'] = ('''<strong>VERB FORM (participle): '{}'</strong><br><ul> <li>You may have used the wrong form of a verb on its own (e.g. 'shown', 'done') in this sentence (e.g. 'This shown that ...', 'This done by ...')<li>Please check the sentence, and change the verb form (e.g. 'This showed that ...', 'This is done by ...'), if necessary.</ul>''',1) #

eng_feedback['VeryLongSentence']['lcc2'] = ('''<strong>V LONG SENTENCE: '{}'</strong><br><ul> <li>This sentence is much longer than the average sentence. It may be difficult for readers to read the sentence and understand it after reading it once. There is also a higher risk of making grammar mistakes in such a long sentence. <li>You may want to consider breaking up the sentence to make it easier for the reader to follow the text.</ul>''',1) #

eng_feedback['w_comma-sdwch_plr_rbst']['lcc2'] = ('''<strong>COMMA (missing space): '{}'</strong><br><ul> <li>This sentence has a comma without any space after it (e.g. 'The device is cheap,portable and user-friendly.'). <li>Please check the sentence, and add a space after the comma (e.g. 'The device is cheap, portable and user-friendly.') if necessary.</ul>''',0.5) #

eng_feedback['w_hasinitcap_dlr']['lcc2'] = ('''<strong>ARTICLE ('the evening'): '{}'</strong><br><ul> <li>You may be starting your sentence without a capital letter (e.g. 'the problem is …').<li>Please check your sentence, and start the first word with a capital letter if necessary (e.g. 'The problem is …').</ul>''',0.5) 

eng_feedback['WordCase']['lcc2'] = ('''<strong>WORD CASE (capitals): '{}'</strong><br><ul> <li>You may be using lower case (small letters) instead of capital letters (upper case) for a word or words (e.g. 'singapore') in this sentence.<li>Please check your sentence, and lower case to upper case only if you feel it is necessary (e.g. 'Singapore').</ul>''',0.5)
