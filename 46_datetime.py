

''' This file contains examples of working with datetime in Python '''


import datetime
from datetime import date

''' Get today's date and print its components '''

today = date.today()
print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("weekday : " , today.weekday()) # Monday is 0 and Sunday is 6


print("formeted date" , today.strftime("%B %d, %Y")) # Format the date as "Month Day, Year"
print("formeted date" , today.strftime("%d/%m/%Y")) # Format the date as "Day/Month/Year"
print("formeted date" , today.strftime("%A, %B %d, %Y")) # Format the date as "Weekday, Month Day, Year"


''' Create a specific date and print it '''
specific_date = date(2022, 1, 1)
print("Specific date:", specific_date)

''' Calculate the difference between two dates '''
date1 = date(2022, 1, 1)
date2 = date(2022, 12, 31)
date_difference = date2 - date1
print("Difference between", date2, "and", date1, "is", date_difference.days, "days")