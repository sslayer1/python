

# for loop
for i in range (1, 15):
    print  ("for i = ", i)


# while loop
i = 15
while i > 0:
    print (" while i = ", i)
    i = i - 1


# if then
#i = 288
#j = 766

i = 766
j = 200

if i < j:
    #print ("i ", i, "is less than j ", j)
    print ("{} is less that {}".format (i,j))
else:
    #print ("i ", i, "is greater than j ", j)
    print ("{} is greater that {}".format (i,j))



#prime numbers
def isprime (num):
    if num == 1:
        return False
    elif (num == 2):
        return True
    else:
        for x in range (2, num):
            if (num % x == 0):
                return False
        return True

num = 99    
print ("Is {} a prime number true/false".format(num))
print (isprime(99))    
