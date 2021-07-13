#
# Example file for working with date information
#
# we are telling the python interpreter here that from the datetime standard built in module that comes with the standard library - importing date, time, datetime classes. These are the predefined pieces of functionality in the Python library. To use it, you need to import it.

from datetime import date
from datetime import time
from datetime import datetime


def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("todays date is:", today)

  # print out the date's individual components
  print("Dates Components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's week day number is: ", today.weekday())
  days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
  print("Which is a : ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print(today)
  
  # Get the current time
  t = datetime.time(datetime.now())
  print(t)
  
  
 

  
if __name__ == "__main__":
  main()
  