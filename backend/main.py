from bs4 import BeautifulSoup
import requests
import json
from tagSlang import *
# returns a dictionary containing the word, normal definition, and examples, or
# returns None if the word is not within the dictionary
def getDefinitionNormal(word,pos):
    partOfSpeech = ['noun', 'pronoun', 'verb', 'adjective', 'adverb', 'preposition',
                    'conjunction', 'interjection', 'auxiliary verb']
    url = f'https://www.vocabulary.com/dictionary/{word}'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    
    try:
        allDefinitions = soup.find_all('div', class_='definition')
    except:
        return None
    
    if (allDefinitions == []):
        return None
    
    try:
        firstDef = allDefinitions[0]
        textFirstDef = firstDef.get_text()
        splitByWord = textFirstDef.split()
        if (splitByWord[0] in partOfSpeech):
            oneDefinition = ''
            for wordInDef in splitByWord:
                oneDefinition += wordInDef + ' '
        return {'Word':word, 'Definition':oneDefinition, 'Example':'No examples','pos':pos}
    except:
        return None

# returns a dictionary containing the word, slang definition, and examples, or
# returns None if the word is not within the dictionary
def getDefinitionSlang(word,pos):
    url = f'https://www.dictionary.com/e/slang/{word}'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')

    try:
        wordTitle = soup.find('h1', class_='article-word__title').text.strip()
        allDefinitions = soup.find_all('div', class_='article-word__definition')
        allExamples = soup.find_all('div', class_='examples__item__content text')
    except:
        return None

    try:
        firstDefinition = allDefinitions[0]
        text = firstDefinition.get_text()
        lengthBeginning = len(f'\nWhat does {wordTitle} mean?\n\n')
        text = text[lengthBeginning:]
        textInList = text.split('\n')
        primaryDefinition = textInList[0]
    except:
        return None
    
    try:
        firstExample = allExamples[0]
        sentenceEx = firstExample.get_text()
        sentenceEx = sentenceEx.strip()
    except:
        sentenceEx = 'No examples'
    
    return {'Word':word, 'Definition':primaryDefinition, 'Example': sentenceEx,'pos':pos}

# Modified From: https://stackoverflow.com/questions/8502387/python-module-to-remove-internet-jargon-slang-acronym
# Creates a dictionary mapping slang words/abbreviations to their meanings
def createAbbreviationDict():
    resp = requests.get("http://www.netlingo.com/acronyms.php")
    soup = BeautifulSoup(resp.text, "html.parser")
    slangdict= {}
    key=""
    value=""
    for div in soup.findAll('div', attrs={'class':'list_box3'}):
        for li in div.findAll('li'):
            for a in li.findAll('a'):
                key =a.text
                allValues = li.text.split(key)[1].lower()
                splitValue = allValues.split('-or-')
                value = splitValue[0]
                key = key.lower()
                slangdict[key]=value
    return slangdict

abbreviationDict = createAbbreviationDict()

# returns a dictionary containing the word, abbreviation definition, and
# examples, or returns None if the word is not within the dictionary
def getDefinitionAbbreviation(word, abbreviationDict,pos):
    if word in abbreviationDict:
        definition = abbreviationDict[word]
        return {'Word':word, 'Definition':definition, 'Example':'No examples','pos':pos}
    else:
        return None

# takes in a set of the tagged slang words and returns a json converted
# dictionary of the output mapping to the result of the first occurence of the
# word in the slang, abbreviaiton, or normal dictionary. Returns json conversion
# of None if no slang words were tagged or if the word is not found in any
# dictionaries.
def getFirstElem(set):
    newset = set()
    for i in set:
        newset.add(i[0])
    return newset
def getDefinitionForWordsInSet(setOfWords, abbreviationDict):
    result = {'output':[]}
    if (setOfWords == set()):
        return json.dumps(None)
    for elem in setOfWords:
        word,pos = elem
        if (word not in result):
            normalDef = getDefinitionNormal(word,pos)
            slangDef = getDefinitionSlang(word,pos)
            abbreviationDef = getDefinitionAbbreviation(word, abbreviationDict,pos)
            if (slangDef != None):
                result['output'].append(slangDef)
            elif (abbreviationDef != None):
                result['output'].append(abbreviationDef)
            elif (normalDef != None):
                result['output'].append(normalDef)
            else:
                return json.dumps(None)
    return json.dumps(result)

#calls both checkAll and Get Definition
def mainFunct(s):
    set = checkAll(s)
    return getDefinitionForWordsInSet(set, abbreviationDict)

def auxFunct(s):
    return getDefinitionForWordsInSet(s, abbreviationDict)


# abbreviationDict = createAbbreviationDict()
# words = {'yeet', 'uwu', 'happy'}
# result = getDefinitionForWordsInSet(words, abbreviationDict)
# for key in result:
#     print(key)
#     for item in result:
#         print(result)
#         input()