import re
import nltk

import formalization

import ngram_weighting

sentence_example = "Jokowi... github.com/adrianadyatma @telah berhasil kesuksesan thn, masa-masa mant.ap/$#==~!@#$%^&*() https://asu.com keluarga. #JokowiAja https://t.co/WAOAW9sja"

sentence_example = "Baju Pak Bangun bagus sekali, sepertinya mahal..."


def format_word(sentence):
    # Remove all alphanumeric character and word that starts with @, #, and http
    # Also lower the case of sentence
    sentence = re.sub(r'@\w+|#\w+|[!-\-/-~]+\.[!-\-/-~]+', '', sentence).lower()
    sentence = re.sub(' +', ' ', sentence).strip()
    return sentence


def tokenize(sentence):
    tokens = nltk.tokenize.word_tokenize(sentence)
    # tokens = [token for token in sentence.split(" ") if token != ""]
    return tokens


def main():
    # Read tweet text data from SQL
    # For every tweet, main_process() get called
    # Return weighting data to be written to SQL
    pass


# Main process of system
def main_process(sentence):
    # Kalimat awal
    print(sentence, "\n")

    # Kalimat sudah melewati format awal
    formatted = format_word(sentence)
    print(formatted, "\n")

    # # Tokenisasi kalimat menjadi list
    # tokens = tokenize(formatted)
    # print(tokens, "\n")
    #
    # # Formalisasi tiap token
    # list_temp = []
    # for token in tokens:
    #     # Perbandingan tiap token sebelum dan sesudah formalisasi
    #     formed_word = formalization.formalize(token)
    #     print("--------", token, "=", formed_word)
    #     list_temp.append(formed_word)

    # Formalisasi
    list_temp = [formalization.formalize(t) for t in tokenize(formatted)]

    # Hasil formalisasi
    formed_sentence = (' '.join(list_temp))
    print("\nSudah di format :", formed_sentence)

    # N-gram weighting
    weight = ngram_weighting.weighting(formed_sentence)
    print("\nBobot :", weight)


if __name__ == '__main__':
    # main()
    main_process(sentence_example)
