<h1>Chance Murphy 507 Project 2</h1>
<p>
This project imports code from a python file called movie_tools.py into the SI507_project2.py and uses it to
create a flask app. This flask app will use the Class defined in movie_tools.py and the code within SI507_project2.py
to generate a random list of 5 movies from movies_clean.csv and display the name and IMDB rating of them. In addition,
another route will select one random movie from movies_clean.csv and display some general info on the movie
to the user such as the studio, release date, and IMDB rating.
<br><br>
This flask app can be ran downloading the required files and installing the requirments.txt file.
<br><br>
To run the flask app and install the requirments.txt file, you'll need to create
a virtual enviornment. In order to do this type in the following commands into
your command promot/terminal window.<br><br>
1: python3 -m venv project2-env
<br><br>
2: source project2-env/bin/activate for Mac/Linux OR source project2-env/Scripts/activate for Windows
<br><br>
3: pip install -r requirements.txt
<br><br>
4: Once you have installed the requirements you can then run your flask app by typing in...
<br><br>
5: python SI507_project_2.py runserver
<br><br>
From here you'll be prompted and given a local host address. Copy this into a web
and you can then freely run the flask app. Addresses you can enter into the local
host url are as follows.
<br>
<h3>Home Page:</h3> http://localhost:5000/
<br>
<h3>Movie Ratings List Page:</h3> http://localhost:5000/movies/ratings/<name>
<br>
<h3>Movie Info Page:</h3> http://localhost:5000/movie/info(pound/yuan/dollar)/<amount>
<br>
<h2>Overall Grade</h2>
1000/1000
<br>
This is because all of my routes work just as they are expected to work, and I also have an additional route that was not
required in the outlines of the project. Below is the image for my database table that I believe could be used in future projects
involving the movies_clean.csv file and a database.
</p>
