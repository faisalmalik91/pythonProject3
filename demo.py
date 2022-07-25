import keyword
"""
print(keyword.kwlist)
i = (int)(input('Entre Num'))
print(type(i))
j = (int)(input('Entre Num2'))
s = (int)(i/j)
print(s)
print(type(s))
"""

dictdata = {1:'FM',3:'MG',7:'LS'}
for i, dictdatum in enumerate(dictdata):
    print("i",+i)
    print("tum",+dictdatum)
listKey = dictdata.values()
print(listKey)
print(type(listKey))
for i in listKey:
    print(i)

dictdata[6] = 'LKH'
print(dictdata)
dictdata[6] = 'eknkk'
print(dictdata)

ld = dictdata.items()
print(ld)
print(type(ld))
av = dictdata.pop(7)
print(av)
print(dictdata)

'''
import datetime as dt

print(dt.datetime.now())
x = dt.datetime.dst()
print(x)
'''

strN = "faisal malaik dsd"
str2 = strN.split(' ')
print(type(str2))

def devide(a,b):
    try:
        if b == 0:
            raise ValueError('b is zero')
        else:
            s = a / b
        return s
    except OSError:
        print('exception found {}'.format(OSError))
    except ValueError as v:
        print('Zero errror {}'.format(v.args))
    finally:
        print('end of the program')

print(devide(10,0))