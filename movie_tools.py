import csv
from flask import Flask
import random
from itertools import product, permutations


class Movie:
    def __init__(self, movie):
        self.title = movie[0]
        self.release_date = movie[5]
        self.studio = movie[8]
        self.genre = movie[10]
        self.rating = movie[14]
        self.ratings = movie[15]

    def __str__(self):
        return "{} | {}".format(self.title,self.rating)

    def info(self):
        return "{} was a {} genre movie released on {} by {} studios. It has recieved {} ratings on IMDB and has an average rating of {}.<br>".format(self.title,self.genre,self.release_date,self.studio,self.ratings,self.rating)
####
#### Ends class definitions
####

if __name__ == "__main__":

    with open("movies_clean.csv", "r") as f:
        reader = csv.reader(f)
        data = []
        for x in reader:
            data.append(x)

    movies = []
    for movie in data[:25]:
        movies.append(movie)

    random.shuffle(movies)

    movies_info = ""
    for movie in movies[:5]:
        x = Movie(movie)
        movies_info += str(x) + "\n\n"

    print(movies_info)


    #movie_info = Movie(data[3])

    #print(movie_info)
