import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[30,40,45,60,80,95]

plt.title("time per month for study")
plt.xlabel("months")
plt.ylabel("performance")
plt.xlim(1,6)
plt.ylim(35,95)
plt.xticks([1,2,3,4,5,6],["m1","m2","m3","m4","m5","m6"],color="pink")
plt.legend(loc="upper left",fontsize=1.5)
plt.grid(color="yellow",linestyle="--",linewidth=1)
plt.origin()
plt.plot(x,y,color="blue",linestyle="--",linewidth=2,marker="o")
plt.show()