import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.pointplot(data=tips,x="sex",y="total_bill",hue="smoker")
plt.show()

"""
A point plot is used to compare the average (or another statistic) of a numerical variable across categories,
 with the averages shown as points connected by lines.
"""