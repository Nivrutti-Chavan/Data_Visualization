import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")

sns.boxplot(data=tips,x="day",y="total_bill",hue="sex")#axes_level_function
sns.catplot(data=tips,x="day",y="total_bill",kind="box")#fig_level_function
plt.show()