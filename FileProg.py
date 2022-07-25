

def fileOpen():
    fileData = open('abc.txt','r')
    #while fileData != '':
    for x in fileData:
        print(x)
    fileData.close()

import os
def cereateFile():
    if os.path.exists('newFile.txt'):
        file = open('newFile.txt', 'a')
    else:
        file = open('newFile.txt','x')

    file.write('Faisal is good boy')
    file.write('Faisal is good boy2')
    file = open('newFile.txt', 'r')
    print(file.read())
    file.close()
    os.remove("newFile.txt")

import numpy as np
import numpy.random as rd
def numPyTest():
    a = np.array([1,2,5,6,4,8])
    a1 = np.array([[1,2,5,6,4,8],[5,'d',7,9,8,8]])
    print(a)
    print(a1[1][0])
    print(a1[1,1])
    print('random')
    print(rd.randint(50,100, size=(5)))

numPyTest()
#cereateFile()
#fileOpen()