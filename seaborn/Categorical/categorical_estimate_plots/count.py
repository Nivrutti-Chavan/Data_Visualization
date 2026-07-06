import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.countplot(data=tips,x="smoker",hue="sex")
plt.show()



#also use facet 
"""
A count plot is used to count the number of occurrences (frequency) of each category in a categorical variable.
Unlike barplot(), it does not calculate averages. It simply counts how many times each category appears.
"""