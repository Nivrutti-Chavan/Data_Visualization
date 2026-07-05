import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.histplot(data=tips,x="total_bill",hue="sex")#axes level
sns.displot(data=tips,x="total_bill",hue="sex")#fig level

plt.show()