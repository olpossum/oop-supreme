#Class is a blueprint for creating instances
#each unique employee is an instance of the class
class Employee:

    #create init method
    #method recieves the instance as the first arg automatically
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

#Instance is emp1/2
emp_1 = Employee('Andy', 'Welton', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

#print(emp_1.email)
#print(emp_2.email)

print(emp_1.fullname())
