import csv

from collections import Counter


def cek_alay_kbbi():
    with open(r'references/alay_dict.txt') as alay:
        for row1 in alay:
            un_baku, baku = row1.split(':')
            reader = csv.DictReader(open(r'references/kata_kelas_makna.tsv', encoding="utf8"), dialect='excel-tab')
            for row2 in reader:
                if un_baku == row2.get("kata"):
                    with open('references/data.txt', 'a') as data:
                        data.write(str(un_baku + " = " + baku + " -- " + row2.get("kata") + "\n"))
                    print(un_baku, "=", baku, "--", row2.get("kata"))
                    break


def cek_kembar_per_file():
    with open(r'references/negative.txt') as f:
        c = Counter(c.strip().lower() for c in f if c.strip())
    for line in c:
        if c[line] > 1:
            print(line)


def cek_kembar_pos_neg():
    count = 0
    with open(r'references/positive.txt') as p:
        for pos in p:
            with open('references/negative.txt') as n:
                for neg in n:
                    if pos == neg:
                        count += 1
                        print(pos, neg)
    print(count)


def sort():
    with open(r'references/positive_old.txt') as r:
        for line in sorted(r):
            with open(r'references/positive_n.txt', 'a') as w:
                w.write(line)
                print(line, end='')
    with open(r'references/negative_old.txt') as r:
        for line in sorted(r):
            with open(r'references/negative_n.txt', 'a') as w:
                w.write(line)
                print(line, end='')


def sort_weight():
    with open(r'references/weighting_data.txt') as doc:
        for line in sorted(doc):
            with open(r'references/weighting_data_new.txt', 'a') as new_doc:
                new_doc.write(line)
                print(line, end='')


def give_value():
    with open('references/positive.txt') as pos1:
        for text in pos1:
            text = text.replace("\n", "")
            text = text + ":1\n"
            with open(r'references/pos_n.txt', 'a') as pos2:
                pos2.write(text)

    with open(r'references/negative.txt') as pos1:
        for text in pos1:
            text = text.replace("\n", "")
            text = text + ":-1\n"
            with open(r'references/neg_n.txt', 'a') as pos2:
                pos2.write(text)


def create_kbbi():
    kata_2 = ""
    reader = csv.DictReader(open(r'references/kata_kelas_makna.tsv', encoding="utf8"), dialect='excel-tab')
    for row in reader:
        kata_1 = str(row.get("kata").lower())
        if " " not in kata_1 and not kata_2 == kata_1:
            kata_2 = kata_1
            with open(r'references/kata_baku.txt', 'a') as new:
                print(kata_1)
                new.write(kata_1 + "\n")


if __name__ == '__main__':
    # cek_alay_kbbi()
    # cek_kembar_per_file()
    # cek_kembar_pos_neg()
    # sort()
    # sort_weight()
    # give_value()
    # create_kbbi()
    pass
