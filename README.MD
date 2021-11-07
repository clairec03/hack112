Description: Genzlator is a classification and webscraping based web app focused on bridging the generational cultural gap. The user can input any string into the genZlator and it will return the definition and example of all slang words within it. These definitions and examples are pulled from https://www.vocabulary.com/ for the traditional definitions, https://www.dictionary.com/e/slang/ for the slang definitions, and http://www.netlingo.com/acronyms.php for abbreviations (eg. gn, btw, omw) using web scraping. 

We split the project into a few sections:
Our frontend involves using a Flask API, Material UI, React modules, and HTML/CSS. The user can generate text input in the text editor field. Pressing the "genslate" button allows our Flask API to fetch the string and use the POST method to relay inputs to the backend python files. 

Word Tagging Algorithm:
	Using NLTK, we processed the input string by removing stopwords (i.e. common words that don't contribute to the meaning of a sentence like "the" "and" "is") and replacing contractions with expanded meanings. We also tagged the remaining words with their contextual part of speech.
	To determine whether or not a word counts as slang, we first checked if it existed within the NLTK words directory and added it to a set if not. To account for words that can be used as both slang and normal words, we compared the contextual part of speech to the 'common' parts of speech obtained by scraping dictionary.com, since changing part of speech tends to be an indicator of 'slangification'. (See https://aclanthology.org/K19-1082.pdf for more detail)
	Since dictionary.com included parts of speech for all the possible instances of a word, there were times when a word was tagged as 'matching' part of speech (specifically concrete nouns) but the meanings of the matching POS instances were clearly different (i.e. 'clutch (noun)' used in a slang context is clearly not the same as a 'clutch (noun)' bag). To account for this, we trained a model (obtained from our lord and savior StackOverflow) to recognize concrete and abstract nouns and then factored that into our POS function. 
	Lastly, because sometimes the NLTK POS tagging system hates us, we accounted for false positives from the POS checking function by cross checking with an existing slang dictionary. 


Modules (Highly recommended that you run everything on Python 3.7 or else you're going to have a really bad time :D)
 - NLTK
 - bs4
 - requests
 - pickle
 - spacy
 - sklearn
 - numpy
 - react with material ui library
 - node/npm

File to run to start your program: flaskapi.py, npm start
