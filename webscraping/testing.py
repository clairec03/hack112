from bs4 import BeautifulSoup
import requests

wordToSearch = input('word you want the definition of: ')

page = requests.get("https://www.dictionary.com/browse/" + wordToSearch).text
soup = BeautifulSoup(page, 'lxml')
allInfo = soup.find('div', class_='css-1avshm7 e16867sm0')
word = allInfo.find('h1', class_='css-1sprl0b e1wg9v5m5').text

allDefinitions = allInfo.find('div', class_='default-content').text
print(allDefinitions)