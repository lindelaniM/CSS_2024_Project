# -*- coding: utf-8 -*-
import pandas as pd

# Spacer
print("---Spacer")

df = pd.read_csv('movie_dataset.csv')
df.columns = df.columns.str.replace(" ","")
df.dropna(inplace = True)

print(df.describe())
print(df['Rating'].max())

print(" ")
print(" ")

# Question No. 1
print("---Question_1")

highest_rated_movie = df.loc[df['Rating'].idxmax()]
print(highest_rated_movie)

print(" ")
print(" ")

# Question No. 2
print("---Question_2")

avg_revenue = df['Revenue(Millions)'].mean()
print(avg_revenue)

print(" ")
print(" ")

# Question No. 3
print("---Question_3")

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
avg_revenue_2015_to_2017 = filtered_df['Revenue(Millions)'].mean()

print("Average Revenue of Movies from 2015 to 2017:", avg_revenue_2015_to_2017)

print(" ")
print(" ")

# Question No. 4
print("---Question_4")

movies_2016_count = df[df['Year'] == 2016].shape[0]
print("Number of movies released in 2016:", movies_2016_count)

print(" ")
print(" ")

# Question No. 5
print("---Question_5")

nolan_movies_count = df[df['Director'] == 'Christopher Nolan'].shape[0]
print("Number of movies directed by Christopher Nolan:", nolan_movies_count)

print(" ")
print(" ")

# Question No. 6
print("---Question_6")

high_rating_movies_count = df[df['Rating'] >= 8.0].shape[0]
print("Number of movies with a rating of at least 8.0:", high_rating_movies_count)

print(" ")
print(" ")

# Question No. 7
print("---Question_7")

nolan_movies_ratings = df[df['Director'] == 'Christopher Nolan']['Rating']
median_rating_nolan_movies = nolan_movies_ratings.median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan_movies)

print(" ")
print(" ")

# Question No. 8
print("---Question_8")

average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_avg_rating = average_rating_by_year.idxmax()
highest_avg_rating = average_rating_by_year.max()

print("Year with the highest average rating:", year_highest_avg_rating)
# print("Highest average rating:", highest_avg_rating)

print(" ")
print(" ")

# Question No. 9
print("---Question_9")

movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print("Percentage increase in the number of movies made between 2006 and 2016:", percentage_increase, "%")

print(" ")
print(" ")

# Question No. 10
print("---Question_10")

all_actors = df['Actors'].str.split(', ').explode()
most_common_actor = all_actors.mode().iloc[0]
print("Most common actor in all movies:", most_common_actor)

print(" ")
print(" ")

# Question No. 11
print("---Question_11")

unique_genres_count = df['Genre'].nunique()
print("Number of unique genres in the dataset:", unique_genres_count)

print(" ")
print(" ")

# Question No. 12
print("---Question_12")

numerical_features = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_features.corr()
print("Correlation Matrix:")
print(correlation_matrix)

#Correlation_plot
print("")
import seaborn as sns
import matplotlib.pyplot as plt

numerical_features = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_features.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
