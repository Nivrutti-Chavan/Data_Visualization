import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.kdeplot(data=tips,x="total_bill")
sns.rugplot(data=tips,x="total_bill")
plt.show()