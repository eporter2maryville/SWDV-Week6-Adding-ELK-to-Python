#E Brent Porter
#SWDV 660 Week 6
#Adding ELK to a Python Application

#Placeholder for import
import socket
import logging
import logstash
import sys
import time


"""s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            # Create a socket object
host = '100.27.32.226'    
port = 5959
s.connect((host, port))"""

#Creating Logger
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('100.27.32.226' , 5959, version=1))
#test_logger.addHandler(logstash.TCPLogstashHandler('100.27.32.226' , 5010, version=1))

#Test Logger Info
"""
test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')


# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra)
"""

#Input class
class whoAreYou:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

#Get user input
firstName = raw_input("What is your first name? ")
lastName = raw_input("What is your last name? ")
age = raw_input("How old are you? ")

#Send inputs to log
userInputLog = {
    'firstNameLog_string': firstName,
    'lastNameLog_string': lastName,
    'ageLog_string': age,
}
test_logger.info('python-logstash: User input', extra=userInputLog)


user = whoAreYou(firstName, lastName, age)

#print greeting
print ('Hello {0} {1}! I hope {2} has been a good year!'.format(user.firstName, user.lastName, user.age))
