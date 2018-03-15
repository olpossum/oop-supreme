#Class is a blueprint for creating instances
#each unique employee is an instance of the class
class Employee:
#Class variables are variables that are shared among all instances of a class
#Class variables should be the same for each instance
    raise_amount = 1.04
    num_of_emps = 0

    #create init method
    #method recieves the instance as the first arg automatically
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

        #Should use Employee here instead of self. Keeps num_of_emps from being overridden
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
       self.pay = int(self.pay * self.raise_amount)

#Instance is emp1/2
emp_1 = Employee('Andy', 'Welton', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)

emp_1.apply_raise()

print(emp_1.pay)

#can set Class variable from outside class definition
#Changes for class and all instances
#Employee.raise_amount = 1.05

#What happens when you set the class variable with an instance?
#variable for emp_1 instance is the only variable changes
#Created the attribute in emp_1 can see this now when printing namespace of emp_1
emp_1.raise_amount = 1.05

#Both of these methods work
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#Print namespace of employee 1 instance
#note that it does not contain raise_amount attribute
print(emp_1.__dict__)

#Print namespace of Employee class
#note that it does contain raise_amount attribute
#print(Employee.__dict__)
