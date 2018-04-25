# Error and Exception handling

import csv

with open('sample.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    #for row in readCSV:
        #print (row)
        #print (row[3])
        #print (row[2],row[3])

    #let us create a list for dates and options
    dates = []
    options = []
    for row in readCSV:
        date = row[0]
        option = row[3]

        dates.append(date)
        options.append(option)
    print (dates)
    print (options)

    try:
        dateForItem = input('Enter the item for which you look for the date:')
        if dateForItem in options:
            date = options.index(dateForItem.lower())
            print ("Date corresponding to your item is:", dates[date])
        else:
            print ("Item is not in the list")
    except NameError as e:
        print (e)
    except Exception as e:
        print (e)
