import spacy
import pickle

nlp = spacy.load("en_core_web_md")
classes = ['concrete', 'abstract']

def classifyWord(x):
    classifier = pickle.load(open('nounClassifier', 'rb'))
    for token in nlp(x):
        return(classes[classifier.predict([token.vector])[0]])