class student:
    def __init__(self,a,b):
        self.a=a                      #CREATING A STUDENT CLASS
        self.b=b
    def __add__(self, other):
        a=self.a +other.a                 #TAKING __ADD__ A INBUILD FUNCTION
        b=self.b +other.b                 #TAKING SELF AS S1 ANF OTHER AS S2
        s3=student(a,b)                  #ADDING THE ELEMETS OF SELF WITH OTHER
        return s3   #CREATING A OBJECT OF STUDENT THAT IS S3 AND RETURN IT


s1=student(23,34)   #DEFNING S1
s2=student(76,290) #DEFNING S2
s3=s1+s2             #S3 ISSUM OF S1 AND S2
print(s3.a,s3.b)   # CALLING S3

