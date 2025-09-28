import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("metadata.csv", low_memory=False)

# Clean data
df = df.dropna(subset=["title", "abstract", "publish_time"])
df["year"] = pd.to_datetime(df["publish_time"], errors="coerce").dt.year

# Publications by year
year_counts = df["year"].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.xticks(rotation=45)
plt.title("Publications by Year")
plt.savefig("static/publications_by_year.png")
plt.close()

# Word cloud of titles
titles = " ".join(df["title"].dropna().tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(titles)
wc.to_file("static/title_wordcloud.png")

print("Exploration complete. Plots saved in /static/")
