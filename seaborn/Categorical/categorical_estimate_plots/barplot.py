import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")

sns.barplot(data=tips,x="sex",y="total_bill",hue="smoker")#axes_level
sns.catplot(data=tips,x="sex",kind="bar",y="total_bill",hue="smoker")#fig_level
plt.show()

"""
A bar plot is used to compare the average (or another statistical measure) of a numerical 
variable across categories.Unlike a normal bar chart, Seaborn's barplot() does not simply count values.
 By default, it calculates the mean of the numeric variable for each category.
"""