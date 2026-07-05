import matplotlib.pyplot as plt

jiostar_Month=["jan","Feb","March","Apr","May"]
jiostar_user=[15,24,25,25,18]

Netflix_Month=["jan","Feb","March","Apr","May"]
Netflix_user=[20,15,14,25,26]


plt.scatter(jiostar_Month,jiostar_user,color="Blue",marker="^",label="Jiostat")
plt.scatter(Netflix_Month,Netflix_user,color="Red",marker="*",label="Netflix")

plt.grid(True)
plt.legend()


plt.savefig("plot.png",dpi=300,bbox_inches="tight")
plt.show()