from nltk.corpus import words
from nltk.stem import PorterStemmer
from preProcessing import *
from classify import *
import requests 
from bs4 import BeautifulSoup 

#checks word wrt to nltk dictionary and also calls pos compare
def checkAll(s):
    posSlang = getStopWordsPOS(s)
    posSlang = retagPOS(posSlang)
    slang = set()
    for elem in posSlang:
        if (elem[0] in words.words()):
            if (not checkPOSChange(elem)) or notInSlangDict(elem[0]):
                continue
        slang.add(elem)
    return slang

#checks if pos between contextual word and actual word changed
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
    pos = set(pos)
    if wordPOS in pos or 'interjection' in pos:
        return False
    return True

#checks if word is in slang dictionary
def notInSlangDict(word):
    url = "https://slangit.com/meaning/" + word + ""
    file = requests.get(url).text
    soup = BeautifulSoup(file,'lxml')
    outer = soup.find(id = "main")
    slang = outer.find(class_ = "slang_meanings")
    if slang == None:
        return True
    return False

#stems word
def stem(w):
    stemmer = PorterStemmer()
    return stemmer.stem(w)

#scrapes pos from dictionary.com, returns list 
#minus noun if it is in the last few slots and also concrete
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
    halfway = max(len(poses)//2,2)
    if len(poses) > 1 and 'noun' in poses[halfway:]:
        if classifyWord(word) == 'concrete':
            poses.remove('noun')
    return poses
