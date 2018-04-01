from matplotlib import pyplot as plt

x = [5,6,7,8]
y = [7,3,8,3]

#length of both lists should be same else you get error
print (len(x))
print (len(y))

plt.plot(x,y)
plt.title('Sample chart')
plt.ylabel('Score')
plt.xlabel('Rounds')
plt.show()
