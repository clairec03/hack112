import spacy
from sklearn.linear_model import LogisticRegression
import numpy as np
import requests 
from bs4 import BeautifulSoup 
import pickle
#Scrapes list of concrete nouns
def getNouns():
    url = "https://onlymyenglish.com/concrete-nouns-list/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    parent = soup.find(class_="entry-content")
    parent = soup.find("ol")
    text = list(parent.descendants)
    for i in range(len(text)):
        new = text[i].getText()
        new = new.lower()
        text[i] = new
    return(list(set(text)))

def help(s):
    l =[]
    for i in s.split():
        l.append(i.lower())
    return l

#https://examples.yourdictionary.com/examples-of-abstract-nouns.html
def getAbstract(s):
    return help(s)
#['ability', 'adventure', 'artistry', 'awe', 'belief', 'chaos', 'comfort', 'communication', 'consideration', 'crime', 'culture', 'customer', 'service', 'death', 'deceit', 'defeat', 'democracy', 'dexterity', 'dictatorship', 'disquiet', 'disturbance', 'dreams', 'energy', 'enhancement', 'failure', 'faith', 'faithfulness', 'faithlessness', 'favoritism', 'forgiveness', 'fragility', 'frailty', 'freedom', 'gossip', 'grace', 'hearsay', 'homelessness', 'hurt', 'idea', 'idiosyncrasy', 'imagination', 'impression', 'improvement', 'inflation', 'information', 'justice', 'knowledge', 'laughter', 'law', 'liberty', 'life', 'loss', 'luck', 'luxury', 'memory', 'mercy', 'motivation', 'movement', 'move', 'need', 'omen', 'opinion', 'opportunism', 'opportunity', 'parenthood', 'patriotism', 'peace', 'peculiarity', 'poverty', 'principle', 'reality', 'redemption', 'refreshment', 'riches', 'rumor', 'service', 'shock', 'skill', 'slavery', 'sleep', 'sparkle', 'speculation', 'speed', 'strictness', 'submission', 'success', 'thought', 'thrill', 'truth', 'unemployment', 'unreality', 'victory', 'wealth']

#MODEL FROM: https://stackoverflow.com/questions/28575082/classify-a-noun-into-abstract-or-concrete-using-nltk-or-similar
nlp = spacy.load("en_core_web_md")
classes = ['concrete', 'abstract']
train_set = [
    getNouns(),
    getAbstract(),
]
X = np.stack([list(nlp(w))[0].vector for part in train_set for w in part])
y = [label for label, part in enumerate(train_set) for _ in part]
classifier = LogisticRegression(C=0.1, class_weight='balanced').fit(X, y)
filename = 'nounClassifier'
pickle.dump(classifier,open(filename,'wb'))

def test(x):
    classifier = pickle.load(open('nounClassifier', 'rb'))
    for token in nlp(x):
        print(token, classes[classifier.predict([token.vector])[0]])


