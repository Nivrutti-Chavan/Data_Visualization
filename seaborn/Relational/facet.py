import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


df=px.data.gapminder()
country=df[df["country"].isin(["India","Pakistan","China"])]
sns.relplot(data=country,x="pop",y="gdpPercap",hue="country",col="year",col_wrap=3)
plt.show()
#will not work on scatterplot and lineplot