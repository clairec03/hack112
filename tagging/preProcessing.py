import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

stop_words = set(stopwords.words('english'))
#removes punctuation, apostrophes, and casts everything to lowercase
def removePunct(s):
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
#'hey, today is a really nice day isnt it? I would love to yeet myself out of a window'
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





