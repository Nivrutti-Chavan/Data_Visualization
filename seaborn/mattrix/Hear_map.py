import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = px.data.gapminder()

#data=df.pivot(index="country",columns="year",values="lifeExp")
new_data=df[df["continent"]=="Asia"].pivot(index="country",columns="year",values="lifeExp")
plt.figure(figsize=(20,20))
sns.heatmap(data=new_data,cmap="coolwarm",linewidths=0.5,annot=True)
plt.show()