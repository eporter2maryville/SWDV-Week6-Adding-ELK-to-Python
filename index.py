#E Brent Porter
#SWDV 660 Week 6
#Adding ELK to a Python Application

#Placeholder for import

#Input class
class whoAreYou:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

#Get user input
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
age = input("How old are you? ")
user = whoAreYou(firstName, lastName, age)

#print greeting
print ('Hello {0} {1}! I hope {2} has been a good year!'.format(user.firstName, user.lastName, user.age))
