#Problem Statement
#Develop your own module for reversing an int or you can develop a module for any other functionality.

class Reverse:
    #init initilise a new object of a class self is an instance and num is a parameter

    def __init__(self, num):  
        self.num = num    #assigns value of num to the instance variable num
    
    #it perform action for reversing the number
    def rev(self): 
        number = self.num
        convert = str(self.num)
        reversed = convert[::-1] #slice use to reverse string notation
        numb = int(reversed)
        return numb
num1 = Reverse(9876)
rev_num = num1.rev() #calling the method
print(rev_num)
