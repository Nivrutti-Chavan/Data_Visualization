import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.pairplot(tips)
plt.show()




"""
A Pairplot automatically plots the relationship between every numerical column in a dataset.
Use when: You want to perform Exploratory Data Analysis (EDA) and quickly understand relationships.
"""