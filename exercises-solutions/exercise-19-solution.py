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

    dateForItem = input('Enter the item for which you look for the date:')
    date = options.index(dateForItem.lower())
    print ("Date corresponding to your item is:", dates[date])
