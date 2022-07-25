class Parent:
    def __init__(self):
        print('Const')
    def __init__(self,a):
        print('Const',a)
    def show(self):
        print('Show fun Parent')
    def __del__(self):
        print('dist')

class Child(Parent):
    '''
    def __init__(self):
        #Parent.__init__(self)
        print('Child Cons')
    def __del__(self):
        print('child distc')
'''

#s = Parent()
s = Child('abc')
s.show()
