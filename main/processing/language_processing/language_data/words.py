import csv

LEXICON = '../processing/language_processing/language_data/lexicon.csv'
SWEAR_WORDS = "../processing/language_processing/language_data/swear_words.csv"

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
    return arr

def getBigotWords():
    with open("../processing/language_processing/language_data/bigot.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content