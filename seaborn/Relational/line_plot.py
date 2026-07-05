import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = px.data.gapminder()
country=df[df["country"].isin(["India","Pakistan","China"])]

sns.relplot(data=country,x="year",y="pop",kind="line",hue="country")#fig level
sns.lineplot(data=country,x="year",y="pop",hue="country")#Axes level
plt.show()