#this reads the database file that contains the idf calculations

def readFile(fileName):
    #this function reads the database file into a map for the idf part
    f = open(fileName, 'r')
    s = f.read()
    lineList = s.split("\n")  #list of all the lines from the txt file

    idfMap = {}

    for i in range(len(lineList)-1):
        stringLine = lineList[i]  #stores a string of one line from the file
        wordValueList = stringLine.split(":")  #stores a list with the 1st element as the word, and the 2nd element as the idf value
        idfMap[wordValueList[0]] = wordValueList[1]


    f.close()
    return idfMap



#main program

print(readFile("database.txt"))