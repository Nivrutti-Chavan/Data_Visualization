import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

g=sns.FacetGrid(data=tips,col="time",row="sex")
g.map(sns.scatterplot,"tip","total_bill")

plt.show()
#read documentation

"""
FacetGrid creates multiple graphs based on one or more categorical variables.
Use when: You want to compare the same graph across categories.
"""