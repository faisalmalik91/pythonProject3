import string


def removeChar(str,i):
    str1 = str[:i]
    str2 = str[i+1:]
    print(str1)
    print(str2)
    print(str1+str2)

removeChar('faisal',3)