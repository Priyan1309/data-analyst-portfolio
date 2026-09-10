# 🎬 Netflix Data Analysis & Visualization

## 📌 Project Overview

This project explores the Netflix titles dataset to identify patterns and trends across movies and TV shows.

The analysis focuses on content distribution, countries, ratings, and other important characteristics of Netflix's content library.

## 🎯 Objectives

- Analyze the distribution of Movies and TV Shows
- Explore Netflix content by country
- Analyze content ratings
- Clean and preprocess the dataset
- Identify useful patterns and trends
- Create visualizations to communicate insights

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Data Cleaning
- Exploratory Data Analysis (EDA)

## 📂 Dataset

The project uses the `netflix_titles.csv` dataset containing information about Netflix movies and TV shows.

Key columns include:

- Title
- Type
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Listed In

## 🧹 Data Cleaning

The dataset was cleaned using Python and Pandas.

The following steps were performed:

- Handled missing values
- Replaced missing values in important columns with `Unknown`
- Converted the `date_added` column into a date format
- Prepared the dataset for analysis

## 📊 Analysis Performed

### 1. Movies vs TV Shows
Analyzed the number of Movies and TV Shows available in the dataset.

### 2. Countries
Analyzed the countries represented in the Netflix dataset.

### 3. Ratings
Explored the different content ratings available on Netflix.

### 4. Content Trends
Used data analysis and visualizations to identify patterns in Netflix's content library.

## 📈 Key Results

- Total titles analyzed: **8,807**
- Unique countries represented: **749**
- Unique ratings identified: **18**

## 📁 Project Structure

```text
Netflix-Data-Analysis/
│
├── chart/
│   ├── chart1
│   ├── chart2
│   └── chart3
│
├── netflix_analysis.py
├── netflix_titles.csv
└── README.md