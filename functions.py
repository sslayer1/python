#--------------------------------------------------
# Name :    Python Coding - Functions
# Purpose : How to use functions.
#
#
# Date          Version     Author      Description
# 07 Mar 2017   1.0         S Salahudin Original
#
#
#---------------------------------------------------
#1. First write the code to print 7 times tables and 9 times tables
print ("******Task 1*************")
for x in range (13):
    print (x, "multiplied by 7 equals", 7*x)


for x in range (13):
    print (x, "multiplied by 9 equals", 9*x)

print ("******Task 1*************")

##2. Now lets create functions for each timestable
## and call the functions
print ("******Task 2*************")
def seventimestable ():
    for x in range (13):
        print (x, "multiplied by 7 equals", 7*x)


def ninetimestable ():
    for x in range (13):
        print (x, "multiplied by 7 equals", 7*x)


seventimestable()
ninetimestable()
print ("End of ******Task 2*************")
##3. Lets just have one function for the user to select the
## times tables they want.
# inside the function they are called parameters
def timestable (number):
    for x in range (13):
        print (x, "multiplied by", number , "equals >>", number*x)


#main program
number = int (input ("What times table do you want to see?"))
##when the function is called, it is called with argument that is stored in variable number
timestable(number) 

#4. Lets just have one function for the user to select the
# times tables they want.
# This is a procedure because it does not return anything. The
# output is printed inside the procedur
def timestable (number, rangesize):
    for x in range (rangesize):
        
        print (x, "multiplied by", number , "equals >>", number*x)


#main program
number = int (input ("What times table do you want to see?"))
howmany = int (input ("What range would you like to use?"))

timestable(number, howmany)

#5.Function returning a value. 
def multiplyby10 (number):
	y = number * 10
	return y

#main program
number = int (input ("What number  would you like to multiply?"))
answer = multiplyby10 (number)
print (number, " * 10 = ", answer)


#6 Function returnng multiple values
def multiplytwonumbers (x, y):
    z = x * y
    return  x, y, z

#main program

number1 = int (input ("What number  would you like to multiply? "))
number2 = int (input ("What number  would you like to multiply it by? "))

# Three pieces of data can be returned into the main program. 
# Of course many more could be returned in one go in this same manner.
# As these values are being returned to one variable ‘answer’, 
# the variable automatically becomes a tuple, which is a data type 
# that can hold a number of different values 
# (like a ‘list’, but tuples are not editable)

answer = multiplytwonumbers (number1, number2)
print ("The answer for ", answer [0], " * ", answer [1], " = ", answer [2])

