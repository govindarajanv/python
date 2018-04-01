from matplotlib import pyplot as plt

x = [5,6,7,8]
y = [7,3,8,3]
x1 = [5,6,7,8]
y1 = [1,3,5,7]

#length of both lists should be same else you get error
print (len(x))
print (len(y))

plt.grid(True, color='k')
plt.plot(x,y,'g',linewidth=5, label = 'Line One')
plt.plot(x1,y1,'c',linewidth=10, label = 'Line  Two')


plt.title('Sample chart')
plt.ylabel('Score')
plt.xlabel('Rounds')
plt.legend()
plt.show()
