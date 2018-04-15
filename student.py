class Student ():
    no_of_students = 0
    
    def __init__ (self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.emailaddress = firstname + '.' + lastname + '@school.ac.uk'

        Student.no_of_students += 1 #class variable that is fixed for the class
        
    def fullname (self):
        return '{} {}'.format(self.firstname, self.lastname)

    
print (Student.no_of_students)    
student_1 = Student('Don', 'Johnston', 'M')
student_2 = Student('Mary', 'Jones', 'F')
print (Student.no_of_students)

print (student_1.emailaddress)
print (student_2.fullname())

#instance variables vs class variables

#print (student_2.emailaddress
##student_1 = Student()
##student_2 = Student()
##
##print (student_1)
##print (student_2)
##
##student_1.firstname = 'Don'
##student_1.surname = 'Johnston'
##student_1.gender = 'M'
##student_1.emailaddress = 'don.johnston@school.ac.uk'
##
##student_2.firstname = 'Mary'
##student_2.surname = 'Jones'
##student_2.gender = 'F'
##student_2.emailaddress = 'mary.jones@school.ac.uk'
##
##print (student_2.emailaddress)
