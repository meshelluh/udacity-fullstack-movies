import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<html>
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link href='http://fonts.googleapis.com/css?family=Lobster|Roboto+Slab:400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            padding-top: 20px;
            padding-bottom: 20px;
        }

        body {
            font-family: 'Roboto Slab', serif;
            color: #000;
        }
        .info {
            text-align: left;
        }

        .data {
            margin-top: -20px;
        }
        .right {
            text-align: right;
        }
        .right h1 {
            font-size: 5em;
            font-weight: 700;
            font-family: 'Lobster', cursive;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .navbar-brand {
            font-family: 'Lobster', cursive;
        }
        @media screen and (max-width: 768px) {
            .movie-tile {
                text-align: center;
            }
            .right {
                text-align: center;
            }
            .data {
                margin-top: 0px;
            }
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Top 10 Movies Nate Usher Would Watch Right Now</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''

<div class="movie-tile row" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class = "col-sm-1 right">
        <h1>#{movie_number}</h1>
    </div>
    <div class="col-sm-3 col-sm-offset-1">    
        <img src="{poster_image_url}" width="220" height="342">
    </div>
    <div class="col-sm-6 data">
        <h2>{movie_title}</h2>
        <h4>{year}</h4>
        <div class = "info">
            <p><b>Director: </b>{director}</p>
            <p><b>Starring: </b>{starring}</p>
            <p><b>Synopsis: </b>{movie_storyline}</p>
        </div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    # Use an integer to count the movies in the list from 1 to whatever and display it
    movie_number = 1;
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        # Encode neccesary strings in utf-8 to avoid UnicodeEncode error
        content += movie_tile_content.format(
            movie_number=movie_number,
            movie_title=movie.title.encode('utf-8'),
            movie_storyline=movie.storyline.encode('utf-8'),
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            year=movie.year,
            director=movie.director.encode('utf-8'),
            starring=movie.starring.encode('utf-8')
        )
        # Iterate displayed movie number
        movie_number += 1
    return content
def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    unencoded_file = main_page_head + rendered_content
    output_file.write(unencoded_file)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open(url) # open in a new tab, if possible