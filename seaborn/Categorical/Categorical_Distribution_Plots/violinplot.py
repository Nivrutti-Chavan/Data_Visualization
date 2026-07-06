import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.violinplot(data=tips,y="total_bill",hue="sex")#axes_level
sns.catplot(data=tips,y="total_bill",hue="sex",kind="violin",split=True)#fig_level
plt.show()

"""
split=True is mainly used with violinplot() to display two categories (from hue) inside 
a single violin
"""