'''
Split the string into list of strings

Input : Geeks for Geeks
Output : ['Geeks', 'for', 'Geeks']
'''

def str2List():
    str1 = "Geeks for Geeks"
    listNew = str1.split(' ')
    print(listNew)

def list2str():
    listNew = ['Geeks', 'for', 'Geeks']
    strnew = "-".join(listNew)
    print(strnew)

str2List()
list2str()