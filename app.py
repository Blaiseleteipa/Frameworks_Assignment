import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Exploration of COVID-19 research papers (metadata.csv)")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("metadata.csv", low_memory=False)

df = load_data()

# Data overview
st.subheader("Dataset Overview")
st.write(f"Total Rows: {df.shape[0]}")
st.write(f"Total Columns: {df.shape[1]}")
st.dataframe(df.head())

# Year filter
df["year"] = pd.to_datetime(df["publish_time"], errors="coerce").dt.year
year_range = st.slider("Select Year Range", int(df["year"].min()), int(df["year"].max()), (2019, 2021))

filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, color="lightblue")
ax.set_title("Publications per Year")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
st.bar_chart(top_journals)

# Word cloud
st.subheader("Word Cloud of Titles")
titles = " ".join(filtered["title"].dropna().tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots()
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
