import pandas as pd
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt

st.header("Violin Plot")
st.subheader("A plot of GDP per capacity, population and LifeExpectancy")

dataframe = pd.read_csv("gapminder_with_codes.csv")

st.text("The data of the year 2007")
data = dataframe[dataframe['year'] == 2007]

#Plot
fig = plt.figure(figsize=(6, 6))
gs = fig.add_gridspec(1, 3)

ax = fig.add_subplot(gs[0, 0])

sb.violinplot(x = data['pop'])
ax.set_xlabel("Population")

ax = fig.add_subplot(gs[0, 1])
sb.violinplot(x = data['lifeExp'])
ax.set_xlabel("Life Exp.")

ax = fig.add_subplot(gs[0, 2])
sb.violinplot(x = data['gdpPercap'])
ax.set_xlabel("GDP Capacity")

fig.tight_layout()
st.pyplot(fig)