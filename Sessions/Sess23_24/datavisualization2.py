#third improvement: add a legend to name graph lines, with corresponding position of legend
#add different styles of lines

from matplotlib import pylab as plt

series1 = []
series2 = []
series3 = []

for i in range(0,30):
    series1.append(i)
    series2+=[i*i]
    series3+=[i**3]

plt.figure("first") #activate figure 1
plt.plot(list(range(0,30)), series1, "y+", label="Linear", linewidth=20, ms=10)
plt.plot(list(range(0,30)), series2, "g^:", label = "Quadric", linewidth=0.5, ms=4)
plt.legend(loc="upper left")
plt.figure("third")
plt.plot(list(range(0,30)), series3)

plt.figure("first")
plt.title("Linear")
plt.ylim(0, 1000)
plt.xlabel("Series")
plt.ylabel("Linear Progression")
plt.title("Quadratic")

plt.figure("third")
plt.title("Cubic")
plt.ylabel("Cubic Progression")
plt.show()