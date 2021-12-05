# Lesson 1 assignment.  Creating functions for my name and the current date
# and time and then outputs the results to the console with print statements

# Import datetime.datetime using the "as" keyword
from datetime import datetime as dt

# Create a function that returns my name as a string
def my_name():
        return "Geoff Ball"

# Create a function that returns the current date and time as a string
def date_and_time():
    # Gets the current date and time
    x = dt.now()
    # Returns the current date and time formatted as the month name, day, 
    # year, and the time in a 12 hour format 
    return x.strftime('%B %d, %Y at %I:%M %p')

# Calls the functions and assigns the function output to variables and them print them
#name = my_name()
#date = date_and_time()


#print ("My name is: ", name)
#print ("It is currently: ", date)

print ('My name is:', my_name())
print ('The date is', date_and_time())
