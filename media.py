import webbrowser
import json
import urllib

class Movie():
    # Used for getting information about a movie and storing it in an object, to be output by fresh_tomatoes
    def __init__(self, movie_title, youtube_url):
        
        # Use omdbapi.com to get movie information from a title
        # Search OMDb with movie title and parse the returned JSON object to a dict
        omdb_connect = urllib.urlopen('http://www.omdbapi.com/?plot=full&t='+movie_title)
        movie_data = json.loads(omdb_connect.read())

        # Set instance variables from OMDb data
        self.title = movie_data["Title"]
        self.storyline = movie_data["Plot"]
        self.year = movie_data["Released"][-4:] # get only the year
        self.poster_image_url = movie_data["Poster"]
        self.director = movie_data["Director"]
        self.starring = movie_data["Actors"]
        self.trailer_youtube_url = youtube_url
