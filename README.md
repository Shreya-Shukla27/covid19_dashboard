# 🦠 COVID-19 Data Analysis — Complete Project

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-1.x-green?logo=scikit-learn)
![Colab](https://img.shields.io/badge/Google%20Colab-Ready-yellow?logo=google-colab)


> This repository contains two parts:
> 1. 📊 An interactive Streamlit dashboard for COVID-19 analysis
> 2. 🤖 An end-to-end ML/DL data science notebook covering Labs 1–10


## 📊 Part 1 — Interactive Dashboard (Streamlit)

An interactive data analysis dashboard built with Python and Streamlit.

### 🌐 Live Demo
👉 [Click here to view the dashboard](https://covid19dashboard-n2imdzfaqzfxu6dwfdcd4x.streamlit.app/)

### Features
- KPI summary — total cases, deaths, recovered, CFR
- Global trend over time
- Top 10 most affected countries
- Interactive world map
- Country-wise comparison (select any country)
- Case Fatality Rate analysis
- Correlation heatmap
- India deep dive analysis

### Dataset
- Source: Kaggle — Corona Virus Report
- Files: `country_wise_latest.csv`, `covid_19_clean_complete.csv`, `day_wise.csv`

### 🛠️ Tech Stack
- Python
- Pandas
- Plotly
- Streamlit

### 🚀 Run Locally
```bash
pip install -r requirements.txt
streamlit run covid_dashboard.py

## 🤖 Part 2 — End-to-End Data Science Notebook (Labs 1–10)

A complete data science pipeline built on COVID-19 data covering
data collection, cleaning, EDA, visualization, machine learning, and deep learning.

### 📋 Course Details

| Field        | Details                      |
|--------------|------------------------------|
| Subject Code | DSE3231                      |
| Dataset      | Our World in Data — COVID-19 |
| Platform     | Google Colab                 |
| Language     | Python 3.10                  |

### 📚 Labs Covered

| Lab | Topic                              | Course Outcome |
|-----|------------------------------------|----------------|
| 1   | Data Collection & Import           | DSE3231.1      |
| 2   | Data Cleaning Techniques           | DSE3231.1      |
| 3   | Feature Engineering & Scaling      | DSE3231.1      |
| 4   | Exploratory Data Analysis (EDA)    | DSE3231.2      |
| 5   | Static Visualization               | DSE3231.2      |
| 6   | Interactive Visualization (Plotly) | DSE3231.2      |
| 7   | Regression Models                  | DSE3231.3      |
| 8   | Classification Models              | DSE3231.3      |
| 9   | Clustering Techniques              | DSE3231.4      |
| 10  | Deep Learning (LSTM, BiGRU, CNN)   | DSE3231.5      |

### 🤖 Models Implemented

**Machine Learning**
| Model                   | Task           |
|-------------------------|----------------|
| Linear Regression       | Regression     |
| Ridge Regression        | Regression     |
| Logistic Regression     | Classification |
| Decision Tree           | Classification |
| Random Forest           | Classification |
| Support Vector Machine  | Classification |
| Gradient Boosting       | Classification |
| K-Means Clustering      | Clustering     |
| Hierarchical Clustering | Clustering     |

**Deep Learning**
| Model             | Task                    |
|-------------------|-------------------------|
| LSTM              | Time-Series Forecasting |
| Bidirectional GRU | Time-Series Forecasting |
| CNN-LSTM Hybrid   | Time-Series Forecasting |

### 🚀 Open in Colab
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. **File → Open notebook → GitHub tab**
3. Paste this repo URL
4. Open `COVID19_DataScience_Complete.ipynb`
5. **Runtime → Change runtime type → GPU**
6. **Runtime → Run All**

---

## 📁 Repository Structure

```
covid19_dashboard/
│
├── 📓 COVID19_DataScience_Complete.ipynb  ← ML/DL Notebook (Labs 1-10)
├── 🐍 covid_dashboard.py                  ← Streamlit Dashboard
├── 📄 country_wise_latest.csv             ← Dashboard Dataset
├── 📄 covid_19_clean_complete.csv         ← Dashboard Dataset
├── 📄 day_wise.csv                        ← Dashboard Dataset
├── 📄 requirements.txt                    ← Dependencies
└── 📄 README.md                           ← This file


