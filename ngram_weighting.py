import re
import nltk
import emoji

import time

import formalization


def give_emoji_free_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text


def generate_ngrams(sentence, n):
    # Tokenize
    tokens = [token for token in sentence.split(" ") if token != ""]
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


# def weighting(sentence):
#     n = 4
#     weight = 0
#     while n > 0:
#         for item_gram in generate_ngrams(sentence, n):
#             for row in open(r'references/weighting_data.txt'):
#                 kata, nilai = row.split(':')
#                 nilai = int(nilai)
#                 if item_gram == kata:
#                     if nilai == 1:
#                         weight += 1
#                     elif nilai == -1:
#                         weight -= 1
#                     # print("\nKata terbobot pada n", n, ":", item_gram)
#                     sentence = sentence.replace(item_gram, '', 1)
#                     break
#         n -= 1
#     return weight


def weighting(sentence):
    n = 4
    weight = 0
    while n > 0:
        for item_gram in generate_ngrams(sentence, n):
            for row in open(r'references/weighting_data.txt'):
                kata, nilai = row.split(':')
                nilai = int(nilai)
                if item_gram == kata:
                    if nilai == 1:
                        weight += 1
                    elif nilai == -1:
                        weight -= 1
                    # print("\nKata terbobot pada 1, n", n, ":", item_gram)
                    sentence = sentence.replace(item_gram, '', 1)
                    break
                elif item_gram == "tidak "+kata:
                    if nilai == 1:
                        weight -= 1
                    elif nilai == -1:
                        weight += 1
                    # print("\nKata terbobot pada 2, n", n, ":", item_gram)
                    sentence = sentence.replace(item_gram, '', 1)
                    break
        n -= 1
    return weight


# Main process of system
def sentence_processing(sentence):
    # Delete emoji
    sentence = give_emoji_free_text(sentence)
    # print(sentence)

    # Case folding kalimat awal
    sentence = re.sub(r'@\w+|#\w+|[!-\-/-~]+\.[!-\-/-~]+\.[!-\-/-~]+|[!-\-/-~]+\.[!-\-/-~]+|\\n', '', sentence)
    sentence = re.sub(r' +', ' ', sentence).strip()
    # print(sentence)

    # Formalisasi menjadi list token
    list_temp = [formalization.formalize(token) for token in nltk.tokenize.word_tokenize(sentence.lower())]

    # Hasil formalisasi disatukan kembali
    formed_sentence = (' '.join(list_temp))
    # print(formed_sentence)

    # N-gram weighting
    return weighting(formed_sentence)


if __name__ == '__main__':
    t = time.time()

    sentence = input("Masukkan kalimat : ")
    print("Hasil :", sentence_processing(sentence))

    print("Done in:", time.time() - t)
