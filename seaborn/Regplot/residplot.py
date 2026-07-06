import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

sns.residplot(data=tips,x="total_bill",y="tip")
plt.show()

"""
A Residual Plot (residplot) is used to check how well a regression line fits the data.

Positive residual → Actual value is above the regression line.
Negative residual → Actual value is below the regression line.
Zero residual → The point lies exactly on the regression line.

residplot() is an Axes-level Seaborn function that plots the residuals (actual value − predicted value) 
of a regression model. It is used to evaluate how well a linear regression model fits the data. A good model
produces residuals that are randomly scattered around zero with no clear pattern.
"""