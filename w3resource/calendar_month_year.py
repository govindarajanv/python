import calendar

year = int(input("Input the year : "))
month = int(input("Input the month : "))
date = int(input("Input the day : "))
print(calendar.month(year, month))

print ("Is", year, "a leap year?",calendar.isleap(year))

print (calendar.weekday(year,month,date))

print ("Printing calendar in text format:")
# Here we say the display should begin with Sunday
print (calendar.TextCalendar(calendar.SUNDAY).formatmonth(year,month))

#Loop over the days displayed
for i in calendar.TextCalendar(calendar.SUNDAY).itermonthdays(year,month):
    print (i)

#Print month names
for month_name in calendar.month_name:
    print (month_name)

print ("\n\n")

#Print day names
for day_name in calendar.day_name:
    print (day_name)
