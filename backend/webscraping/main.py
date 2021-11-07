from bs4 import BeautifulSoup
import requests

# returns a list of definitions for word from the normal dictionary or none if a
# definition doesn't exist
def getDefinitionNormal(word):
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
   
   definitions = []
   for definition in allDefinitions:
      try:
         text = definition.get_text()
         splitByWord = text.split()
         if (splitByWord[0] in partOfSpeech):
            oneDefinition = ''
            for word in splitByWord:
                  oneDefinition += word + ' '
            definitions.append(oneDefinition)
      except:
         return None
   return definitions


def getDefinitionSlang(word):
    url = f'https://www.dictionary.com/e/slang/{word}'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')

    try:
        wordTitle = soup.find('h1', class_='article-word__title').text.strip()
        allDefinitions = soup.find_all('div', class_='article-word__definition')
        allExamples = soup.find_all('div', class_='examples__item__content text')
    except:
        return None

    for definition in allDefinitions:
        try:
            text = definition.get_text()
            lengthBeginning = len(f'\nWhat does {wordTitle} mean?\n\n')
            text = text[lengthBeginning:]
            textInList = text.split('\n')
            primaryDefinition = textInList[0]
            secondaryDefinition = ''
            for elem in textInList[1:]:
                secondaryDefinition += '\n' + elem
            definitions = [primaryDefinition, secondaryDefinition]
        except:
            return None
    
    examples = []
    for example in allExamples:
        try:
            sentence = example.get_text()
            sentence = sentence.strip()
            examples.append(sentence)
        except:
            examples.append('no examples')
    
    return (definitions, examples)

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
    
def getDefinitionAbbreviation(word, abbreviationDict):
    if word in abbreviationDict:
        return abbreviationDict[word]
    else:
        return None

def getDefinitionForWordsInSet(setOfWords, abbreviationDict):
    result = dict()
    for word in setOfWords:
        if (word not in result):
            normalDef = getDefinitionNormal(word)
            slangDef = getDefinitionSlang(word)
            abbreviationDef = getDefinitionAbbreviation(word, abbreviationDict)
            if (slangDef != None):
                result[word] = slangDef
            elif (abbreviationDef != None):
                result[word] = abbreviationDef
            elif (normalDef != None):
                result[word] = normalDef
            else:
                result[word] = 'sorry, word is not found'
    return result

abbreviationDict = createAbbreviationDict()
words = {'yeet', 'uwu', 'happy'}
result = getDefinitionForWordsInSet(words, abbreviationDict)
for key in result:
    print(key)
    for item in result:
        print(result)
        input()