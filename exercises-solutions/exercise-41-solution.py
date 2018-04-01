from matplotlib import pyplot as plt

x = [5,6,7,8]
y = [7,3,8,3]
x1 = [5,6,7,8]
y1 = [1,3,5,7]

#plt.scatter(x,y, color = 'g', label = 'Line One')
#plt.scatter(x1,y1, label = 'Line Two')
plt.bar(x,y, color = 'g', label = 'Line One')
plt.bar(x1,y1, label = 'Line Two')
plt.title('Sample chart')
plt.ylabel('Score')
plt.xlabel('Rounds')
plt.legend()
plt.show()
