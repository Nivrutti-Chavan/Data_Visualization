import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.show()




"""
The relationship between two numerical variables (center plot).
The distribution of each variable separately (top and right plots).

It combines a Scatter Plot + Histogram (or KDE) in one figure.
"""