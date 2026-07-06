import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")

#cannot use hue function
sns.regplot(data=tips,x="total_bill",y="tip")#axes level

#use hue function
sns.lmplot(data=tips,x="total_bill",y="tip",hue="sex")
plt.show()

"""
A scatter plot with a regression (best-fit) line.

.regplot()
Axes-level function
Draws a scatter plot and a regression line.
Works on one Axes.
Used for a single plot.

.lmplot()
Figure-level function
Also creates a scatter plot with a regression line.
Supports faceting (row, col).
Returns a FacetGrid.

The regression line represents the best-fit linear relationship between two numerical variables.
It shows the overall trend in the data and can be used to understand the direction of the \n
relationship (positive, negative, or none) and to make predictions.
"""