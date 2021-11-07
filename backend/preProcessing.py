import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

stop_words = set(stopwords.words('english'))

#sourced from https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)
    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

#removes punctuation, apostrophes, and casts everything to lowercase
def removePunct(s):
    s = decontracted(s)
    s = s.lower()
    result = ''
    for c in s:
        if c in string.punctuation:
            continue
        else:
            result +=c
    return result

#takes in string, returns set of words that aren't stopwords
def removeStopWords(s):
    tokens = word_tokenize(s)
    result = set()
    for word in tokens:
        if word not in stop_words:
            result.add(word)
    return result

#takes in string, returns list of tuples with words and possible 
def getPOS(s):
    try:
        tokens = word_tokenize(s)
        tagged = nltk.pos_tag(tokens)
        return set(tagged)
    except Exception as e:
        print(str(e))

#takes in string, returns set of non-stopwords and their parts of speech
def getStopWordsPOS(s):
    s = removePunct(s)
    setPOS = getPOS(s)
    setWords = removeStopWords(s)
    setWordsAndPOS = set()
    for elem in setPOS:
        if elem[0] in setWords:
            setWordsAndPOS.add(elem)
    return setWordsAndPOS

#takes set from defStopWordsPOS, retags to 'verb', 'noun' etc...
def retagPOS(s):
    result = set()
    for elem in s:
        if elem[1][0] == 'N':
            result.add((elem[0],'noun'))
        elif elem[1][0] == 'V':
            result.add((elem[0],'verb'))
        elif elem[1][0] == 'J':
            result.add((elem[0],'adjective'))
        elif elem[1][0] == 'R':
            result.add((elem[0],'adverb'))
        elif elem[1][0] == 'M':
            result.add((elem[0],'auxiliary verb'))
    return result





