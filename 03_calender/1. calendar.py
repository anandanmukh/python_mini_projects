#Program to print the calender for a particular month and year

import calendar

year=int(input("Enter the year: "))
month=int(input("Enter the number of month(1-12): "))
print(calendar.month(year,month,))