
## 🗂️ Dataset
The dataset file `metadata.csv` (~1.2 GB) is **too large to be uploaded to GitHub**.  

➡️ You can download it from the official sources:  
- [CORD-19 on Kaggle](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge)  
- [Allen Institute for AI CORD-19 release](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/cord_19_embeddings.tar.gz)  

After downloading, extract the `metadata.csv` in the **project root folder**.

---

## 🚀 Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/Blaiseleteipa>/frameworks-assignment.git
   cd frameworks-assignment


# 📊 CORD-19 Frameworks Assignment


## 📌 Overview
This project explores the **CORD-19 Metadata dataset** using Python, pandas, and visualization libraries.  
It includes:
- Data loading, cleaning, and exploration  
- Basic analysis and visualizations  
- A simple **Streamlit app** for interactive exploration  

---

## 📂 Project Structure
Frameworks_Assignment/
│
├── explore.py # Data loading, cleaning, analysis, visualizations
├── app.py # Streamlit app for interactive exploration
├── requirements.txt # List of dependencies
├── README.md # Documentation and reflection
└── metadata.csv # Dataset 

---
## ⚙️ Requirements
Install the required Python libraries:

```bash
pip install -r requirements.txt

How to Run
1. Run the Data Exploration Script
python explore.py


This script:

Loads metadata.csv

Cleans missing data

Performs basic analysis

Generates visualizations

2. Run the Streamlit App

streamlit run app.py


The app includes:

Title and description

Interactive year range slider

Charts: publications over time, top journals

Word cloud of paper titles

Sample data display

📈 Example Analysis

Publications by Year – Bar chart of research papers over time

Top Journals – Bar chart of top publishing sources

Word Cloud – Most frequent words in paper titles

📝 Reflection

Challenges: Handling missing data in publish_time and abstract, installing external libraries (wordcloud, streamlit).

Learning: Practiced the full data science workflow – from raw CSV to interactive dashboard.

Next steps: Could expand analysis with NLP on abstracts or trend analysis across topics.

Author

Blaise Leteipa Partoip

Frameworks Assignment – PLP Academy
