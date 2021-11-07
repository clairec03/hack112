# takes in a string and a set of lowercase slang words, and puts in markers
# around the specified slang words
def inputMarkers(string, setOfSlangWords):
    lowercaseString = string.lower()
    newString = string
    for word in setOfSlangWords:
        startIndex = 0
        num = lowercaseString.count(word)
        for numFound in range(num):
            index = lowercaseString.find(word[startIndex:])
            if (lowercaseString[index-1] == '<'):
                continue
            newString = (newString[:index] + '<mark>' +
                         newString[index:index+len(word)] + '</mark>' +
                         newString[index+len(word):])
            lowercaseString = (lowercaseString[:index] + '<mark>' +
                               lowercaseString[index:index+len(word)] + '</mark>' +
                               lowercaseString[index+len(word):])
            startIndex = index+len(word)
    return newString

string = 'hello my name is Mark'
setOfSlangWords = {'hello', 'name', 'mark'}
print(inputMarkers(string, setOfSlangWords))
