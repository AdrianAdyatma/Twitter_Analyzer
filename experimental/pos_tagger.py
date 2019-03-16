from nltk.tag import CRFTagger
import nltk

import credentials_var as cred

ct = CRFTagger()
ct.set_model_file('references/all_indo_man_tag_corpus_model.crf.tagger')


def pos_tagger(tokens):
    return ct.tag_sents([tokens])


for element in list(cred.find_all):
    text = element['extended_tweet']['full_text'] if element['truncated'] is True else element['text']
    print(pos_tagger(nltk.tokenize.word_tokenize(text)))
