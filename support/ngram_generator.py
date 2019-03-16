import re


def generate_ngrams(sentence, n):
    sentence = sentence.lower()
    # Replace all none alphanumeric characters with spaces
    sentence = re.sub(r'[^a-zA-Z0-9\-\s]', ' ', sentence)
    print(sentence)
    # Tokenize
    tokens = [token for token in sentence.split(" ") if token != ""]

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


sent = input("Masukkan kalimat : ")
ngram = int(input("Masukkan (n)gram: "))
list_hasil = generate_ngrams(sent, ngram)
print('hasil: ', list_hasil,  list_hasil[0])
