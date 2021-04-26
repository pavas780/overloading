class fact:                              #create a class fact
    def __init__(self):                 #define a init function
        print('in fact')
    def sq(self,n):                    #create a sq funcyion which return the square of the number
        return  (n*n)
class fact1(fact):               #create aclass fact1 which in herit the classs fact
    def __init__(self):
        print('in fact1')
    def sq(self,n):         # create a function sq same as in fact
        return (n*n)
m1=fact()                  #creating object of class fact
m2=fact1()                 #creating object of class fact1
print(m2.__init__())         #calling init fuction of class fact1
print(m1.sq(15))           #calling sq fuction of class fact
print(m2.sq(68))         #calling sq fuction of class fact1

