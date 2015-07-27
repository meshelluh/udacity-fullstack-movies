# Fresh Tomatoes

This is a python project I created for the Udacity Full Stack Web Developer Nanodegree.  It is a dynamically generated website that displays a list of my favourite movies.

This utilizes the OMDb (Open Movie Database) API to get movie information based on a supplied movie title.  This allows me to write less code and expend less effort copying and pasting all the fields for my list of movies.  Unfortunately as of today the API doesn't include a link to a trailer so that must be provided seperately for each film.

To add a movie simply add a new movie object to `entertainment_center.py`, like this:
```
my_movie_object = media.Movie("Your Favourite Movie's Title","http://youtubeurl")
```
You must also add it to the movies list:
```
movies = [..., 'some_movie','my_movie_object', ...]
```

The order the movies are added to the list is the order they will be displayed on the website.  They are also given a "ranking" from starting at #1 going up to how many ever movies you supply.

I also wrote some custom CSS to style the page a little differently.

Enjoy!  Maybe you will find your new favourite movie in this list!


