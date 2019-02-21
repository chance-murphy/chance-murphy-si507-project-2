from flask import Flask
from movie_tools import *

app = Flask(__name__)

#Opening the CSV to pull the data from it
f = open("movies_clean.csv", "r")
reader = csv.reader(f)
data = []
for movie in reader:
    data.append(movie)

@app.route('/')
def home():
    f = open("movies_clean.csv", "r")
    file_lines = f.readlines()
    num_lines = len(file_lines)
    return "<h1>There are {} movies in movies_clean.csv!</h1><h3>Options:</h3><p>/movies/ratings/<br>/movie/info/</p>".format(num_lines)
    #Using H1, H3, and br tags because the Flask app will display in HTML
@app.route('/movies/ratings/')
def rating():
    #Randomizing the first 50 results in the data
    movies = []
    for movie in data[:50]:
        movies.append(movie)

    random.shuffle(movies)
    #Displaying the ratings for the first 5 movies in the randomized list.
    string = ""
    for num in range(5):
        movie_rating = Movie(movies[num])
        string = string + movie_rating.__str__() + "<br>" #Including a br tag because the Flask app will display in HTML

    return string

@app.route('/movie/info/')
def info():
    #Randomizing the first 50 results in the data
    movies = []
    for movie in data[:50]:
        movies.append(movie)

    random.shuffle(movies)
    #Displaying the info on one random movie from the randomized list.
    for movie in movies[:1]:
        movie_info = Movie(movie)
        return movie_info.info()


if __name__ == "__main__":
    app.run()
