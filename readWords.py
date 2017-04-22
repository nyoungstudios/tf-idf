import os
#this is a program written by Nathaniel Young for tf-idf

def readIn(fileName):
    f = open(fileName, 'r')  #f is the file object
    s = f.read()  #s means string from the whole file
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    s = s.replace('\t', ' ')
    f.close()
    wordlist = s.split(' ')
    keywordlist = {}  #contains the map of all the words mapped to the number of times they appear
    numOfWords = 0  #number of words counter
    for i in range(len(wordlist)):
        word = wordlist[i]
        if word.__contains__(','):
            word = word.replace(',', '')
        if word.__contains__('.'):
            word = word.replace('.', '')
        if word.__contains__('?'):
            word = word.replace('?', '')
        if word.__contains__('!'):
            word = word.replace('!', '')
        if word.__contains__('"'):
            word = word.replace('"', '')
        if word.__contains__('('):
            word = word.replace('(', '')
        if word.__contains__(')'):
            word = word.replace(')', '')
        if word.__contains__('['):
            word = word.replace('[', '')
        if word.__contains__(']'):
            word = word.replace(']', '')
        if word.__contains__('{'):
            word = word.replace('{', '')
        if word.__contains__('}'):
            word = word.replace('}', '')
        if word.__contains__(':'):
            word = word.replace(':', '')
        if word.__contains__(';'):
            word = word.replace(';', '')

        word = word.lower()

        if len(keywordlist) == 0:
            keywordlist[word] = 1
        else:
            if keywordlist.__contains__(word):
                keywordlist[word] +=1
            else:
                keywordlist[word] = 1
        numOfWords = i+1



    #returns a list containing
    #index 0: a map of all the words in the document that is mapped to the number of times they appear,
    #index 1: and the total number of words in the document
    return [keywordlist, numOfWords]

def calcTotalTimes(total):
    totalAppearance = total[0][0]  #holds the total number of times a word appears across all documents
    for i in range(1,len(total)):
        tempMap = total[i][0]

        for word in tempMap.keys():  #iterates through all the keys in each list
            if totalAppearance.__contains__(word):
                totalAppearance[word] +=tempMap[word]
            else:
                totalAppearance[word] = tempMap[word]

    return totalAppearance



#main program - it reads in all of the files, and then

filelist = os.listdir("englishPaper")
total = []

for i in range(len(filelist)):
     total.append(readIn("englishPaper/" + filelist[i]))


#total.append(readIn("newfile.txt"))
#print(total[0][1])
print(calcTotalTimes(total))
"""
try:
    print(total[1]['1'])
except KeyError:
    print("Out of bounds error")
"""
