import itertools
import time


# Check word from formal word from KBBI
def formalize1(original):
    with open(r'references/kata_baku.txt') as baku_row:
        for kata_baku in baku_row:
            if original == kata_baku.replace("\n", ""):
                return True


# Check word from 'alay' dictionary
def formalize2(original):
    # Check every row for same word, if exists then return correct word, if doesn't then return False
    for row in open(r'references/alay_dict.txt'):
        un_baku, baku = row.split(':')
        if original == un_baku:
            return baku.replace("\n", "")


# Main formalization function
def formalize(original):
    formalizing = original
    i = 0
    while i <= 2:
        if formalize2(formalizing) is not None:
            # print("masuk 2")
            return formalize2(formalizing)
        elif formalize1(formalizing) is True:
            # print("masuk 1")
            return formalizing
        elif i == 0:
            # Hilangkan angka
            # print("masuk 3")
            formalizing = ''.join([c for c in formalizing if not c.isdigit()])
        elif i == 1:
            # Hilangkan karakter duplikat
            # print("masuk 4")
            formalizing = ''.join(c[0] for c in itertools.groupby(formalizing))
        i += 1
    return formalizing


if __name__ == '__main__':
    t = time.time()

    word = input("Masukkan kata : ")
    print("Hasil :", formalize(word))

    print("Done in:", time.time() - t)
