#python code

#aaahgdfsfcnchdfaafddssaaaalllaa   find out how many time repetation of char

#open a file

import re
def openNewFile():
    fileData = open(file="abc.txt", mode='r')
    print(fileData.read())
    countName = 0
    charTSearch = "faisal"
    for c in fileData:
        if charTSearch in c:
            countName = countName+1
    print(countName)
    fileData.close()

def chekCharCout():
    charData = "aaahgdfsfcnchdfaafddssaalaalllaa"
    subStr = "aa"
    print(charData)
    count = 0
    ls1 = re.findall(subStr,charData)

    print('pring ls ',ls1)

    for i in range(0,len(charData)-1):
        if charData[i] + charData[i+1] == subStr:
            print('Cont')
            count = count+1

    print(count)


#openNewFile()
chekCharCout()