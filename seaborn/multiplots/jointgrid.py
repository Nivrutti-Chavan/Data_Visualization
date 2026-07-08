import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

g = sns.JointGrid(
    data=tips,
    x="total_bill",
    y="tip"
)

g.plot(
    sns.scatterplot,
    sns.histplot
)

plt.show()

"""
JointGrid() is the advanced version of jointplot().

jointplot() creates a predefined plot automatically.
JointGrid() lets you choose what plot appears in the center and on the margins.
"""