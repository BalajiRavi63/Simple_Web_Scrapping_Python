###########################################################
############### Author - Balaji Ravi ######################
###########################################################
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#Getting Datas From URL
URL = 'https://www.imdb.com/chart/top/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
# print(response.content)
#Variable for stroing data
titles = []
years = []
imdb_ratings = []
#Get specific data from the content
movie_name = soup.find_all('td', class_='titleColumn')
movie_rating = soup.find_all('td', class_='ratingColumn imdbRating')
#Get data alone not the html scripts
for container in movie_name:
    name = container.a.text
    titles.append(name)
    date = container.span.text
    years.append(date)
    # print(name + " " + date)

for container1 in movie_rating:
    rating = container1.strong.text
    imdb_ratings.append(rating)
    # print(rating)

movies = pd.DataFrame({
    'Name Of Movie':titles,
    'Year Released':years,
    'Ratings': imdb_ratings,
})

# print(movies)
movies.to_csv('movies_list.csv')