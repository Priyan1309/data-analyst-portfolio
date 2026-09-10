import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Clean data
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# -----------------------------
# 1. Movies vs TV Shows
# -----------------------------
print("\nMOVIES VS TV SHOWS")
print(df["type"].value_counts())

# -----------------------------
# 2. Top 10 Release Years
# -----------------------------
print("\nTOP 10 RELEASE YEARS")
print(df["release_year"].value_counts().head(10))

# -----------------------------
# 3. Top 10 Countries
# -----------------------------
print("\nTOP 10 COUNTRIES")
print(df["country"].value_counts().head(10))

# -----------------------------
# 4. Top 10 Ratings
# -----------------------------
print("\nTOP RATINGS")
print(df["rating"].value_counts().head(10))

# -----------------------------
# 5. Movies vs TV Shows by year
# -----------------------------
print("\nMOVIES VS TV SHOWS BY YEAR")
print(
    df.groupby(["release_year", "type"])
      .size()
      .tail(20)
)

# -----------------------------
# 6. Basic statistics
# -----------------------------
print("\nTOTAL TITLES")
print(len(df))

print("\nUNIQUE COUNTRIES")
print(df["country"].nunique())

print("\nUNIQUE RATINGS")
print(df["rating"].nunique())


import matplotlib.pyplot as plt

# 1. Movies vs TV Shows
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# 2. Top 10 Release Years
df["release_year"].value_counts().head(10).sort_index().plot(kind="bar")
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# 3. Top 10 Ratings
df["rating"].value_counts().head(10).plot(kind="bar")
plt.title("Top Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
# 4. Top 10 Directors

df["director"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Directors on Netflix")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
# 5. Top 10 Genres

df["listed_in"].str.split(", ").explode().value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
# 6. Top 10 Countries

df["country"].str.split(", ").explode().value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Countries by Netflix Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
# 7. Movies vs TV Shows

type_counts = df.groupby(["country", "type"]).size().unstack(fill_value=0)

top_countries = df["country"].str.split(", ").explode().value_counts().head(10).index

type_counts.loc[type_counts.index.intersection(top_countries)].plot(kind="bar")

plt.title("Movies vs TV Shows by Country")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
# 4. Movie Duration Distribution
movies = df[df["type"] == "Movie"].copy()

movies["duration_min"] = movies["duration"].str.extract(r"(\d+)").astype(float)

movies["duration_min"].dropna().plot(kind="hist", bins=20)

plt.title("Movie Duration Distribution on Netflix")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()


# 5. TV Shows by Number of Seasons
tv_shows = df[df["type"] == "TV Show"].copy()

tv_shows["seasons"] = tv_shows["duration"].str.extract(r"(\d+)").astype(float)

tv_shows["seasons"].value_counts().sort_index().plot(kind="bar")

plt.title("TV Shows by Number of Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of TV Shows")
plt.tight_layout()
plt.show()


# 6. Netflix Content Added Over Time
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

year_added = df["date_added"].dt.year.value_counts().sort_index()

year_added.plot(kind="bar")

plt.title("Netflix Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
