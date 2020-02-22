#E Brent Porter
#SWDV 660 Week 6
#Adding ELK to a Python Application

#Placeholder for import
import logging
import logstash
import sys
import time

#creating logger
pythonELKLogger = logging.getLogger('python-logstash-logger')
pythonELKLogger.setLevel(logging.INFO)
pythonELKLogger.addHandler(logstash.LogstashHandler('34.201.47.23', 5959, version=1))

pythonELKLogger.error('python-logstash: test logstash error message.')
pythonELKLogger.info('python-logstash: test logstash info message.')
pythonELKLogger.warning('python-logstash: test logstash warning message.')

#Add extra field to logstash
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 126,
    'test_list': [1,2,3],
}
pythonELKLogger.info('python-logstash: test extra fields', extra=extra)

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
