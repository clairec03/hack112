from nltk.corpus import words
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from preProcessing import *
from classify import *
import requests 
from bs4 import BeautifulSoup 

def checkAll(s):
    posSlang = getStopWordsPOS(s)
    posSlang = retagPOS(posSlang)
    slang = set()
    for elem in posSlang:
        if (elem[0] in words.words()):
            if (not checkPOSChange(elem)) or notInSlangDict(elem[0]):
                continue
        slang.add(elem[0])
    return slang

def checkPOSChange(elem):
    word,wordPOS = elem
    stemmedWord = stem(word)
    pos = scrape(stemmedWord)
    if stemmedWord != word and len(pos) == 0:
        pos = scrape(word)
    for i in range(len(pos)):
        new = pos[i].split()[0]
        new = removePunct(new)
        pos[i] = new
    if wordPOS in set(pos):
        return False
    print(word,pos)
    return True

def notInSlangDict(word):
    url = "https://slangit.com/meaning/" + word + ""
    file = requests.get(url).text
    soup = BeautifulSoup(file,'lxml')
    outer = soup.find(id = "main")
    slang = outer.find(class_ = "slang_meanings")
    if slang == None:
        return True
    return False
    
def stem(w):
    stemmer = PorterStemmer()
    return stemmer.stem(w)

def scrape(word):
    url = "https://www.dictionary.com/browse/" + word + ""
    file = requests.get(url).text
    soup = BeautifulSoup(file,'lxml')
    poses = []
    outer = soup.find(class_="css-1avshm7 e16867sm0")
    if outer == None:
        return poses
    pos = outer.find_all(class_="luna-pos")
    for i in pos:
        poses.append(i.get_text())
    halfway = max(len(poses)//2,3)
    if len(poses) > 1 and 'noun' in poses[halfway:]:
        if classifyWord(word) == 'concrete':
            poses.remove('noun')
    return poses
