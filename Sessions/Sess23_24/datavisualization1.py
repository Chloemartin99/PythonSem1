from matplotlib import pylab as plt

#first step
series1 = []
series2 = []
series3 = []

for i in range(0,30):
    series1.append(i)
    series2+=[i*i]
    series3+=[i**3]

plt.plot(list(range(0,30)), series1)
plt.plot(list(range(0,30)), series2)
plt.plot(list(range(0,30)), series3)

#plt.show()

#first improvement: using the figure() function to display each graph in different windows,
# in order to be able to see each graph and axis more clearly
plt.figure("first") #activate figure 1
plt.plot(list(range(0,30)), series1)
plt.figure("second")
plt.plot(list(range(0,30)), series2)
plt.figure("third")
plt.plot(list(range(0,30)), series3)
#plt.show()

#second improvement: labels, titles, clear and ylim and xlim (having limits)
plt.figure("first")
plt.title("Linear")
plt.ylim(0, 1000)
plt.xlabel("Series")
plt.ylabel("Linear Progression")
plt.figure("second")
plt.title("Quadratic")
plt.figure("third")
plt.title("Cubic")
plt.ylabel("Cubic Progression")
plt.show()
