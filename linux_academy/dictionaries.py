
#first way of creating a dictionary

ages = {"govind" : 35, "raghav" : 45, "seshu" : 41}
print (ages)
del ages['seshu']
print (ages)
ages.pop('raghav')
print (ages)
ages = {"govind" : 35, "raghav" : 45, "seshu" : 41}
print (ages)
print (ages.keys())
print (list(ages.keys()))
print (list(ages.values()))

#second way of creating a dictionary

weights = dict(govind=70,raghav=55,seshu=75)
print (weights)

#third way of creating a dictionary using tuples

colors = dict([('govind','blue'),('raghav','red'),('seshu','yellow')])
print (colors)

#fourth way, is creating an empty dictionary and then append values to it
teams = {}
print (teams)
