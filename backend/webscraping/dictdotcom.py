# Source: 
# https://www.geeksforgeeks.org/beautifulsoup-find-all-li-in-ul/
from bs4 import BeautifulSoup
import requests

isSearch = True
while isSearch:
    word = input("Enter your word here: ").lower()
    url = f'https://www.vocabulary.com/dictionary/{word}'
    # page = requests.get(url).text
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    divList = soup.find('div', attrs={"class": "definition"})
    try: text = divList.get_text()
    except: 
        print("No words found.")
        continue
    result = ""
    for word in text.split():
        result += word 
        if (word == "noun" or word == "adjective" or word == "verb" or
            word == "adverb"):
            result += ": "
        elif word != "":
            result += " "
    print(result.strip())
    changeStatus = input("Do you want to keep searching? Press y or n. ")
    if changeStatus == "n":
        isSearch = False
print("Thank you for using the dictionary.")