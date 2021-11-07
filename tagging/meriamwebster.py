import requests 
from bs4 import BeautifulSoup 

def getNouns():
    url = "https://onlymyenglish.com/concrete-nouns-list/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    parent = soup.find(class_="entry-content")
    parent = soup.find("ol")
    text = list(parent.descendants)
    for i in range(len(text)):
        text[i] = text[i].getText()
    return(text)

def help(s):
    l =[]
    for i in s.split():
        l.append(i.lower())
    return l
