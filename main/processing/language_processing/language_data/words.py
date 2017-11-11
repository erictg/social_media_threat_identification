import csv

LEXICON = 'lexicon.csv'
SWEAR_WORDS = "swear_words.csv"

def getLexicon():
    dict = {}
    with open(LEXICON, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            dict[row[0]] = row[1]
    return dict

def getSwearWords():
    arr = []
    with open(SWEAR_WORDS, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            arr.extend(row[1])
    return dict

