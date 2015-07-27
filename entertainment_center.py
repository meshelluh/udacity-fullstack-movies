import media
import fresh_tomatoes

# Create the movie objects, requires first a title and then a youtube link
# We will fetch the rest of the information from omdbapi.com

big_lebowski = media.Movie("The Big Lebowski", "www.youtube.com/watch?v=cd-go0oBF4Y")
shawshank_redemption = media.Movie("The Shawshank Redemption", "www.youtube.com/watch?v=6hB3S9bIaco")
holy_mountain = media.Movie("The Holy Mountain", "www.youtube.com/watch?v=V_k8oaeHsnc")
forrest_gump = media.Movie("Forrest Gump", "www.youtube.com/watch?v=uPIEn0M8su0") 
pulp_fiction = media.Movie("Pulp Fiction", "www.youtube.com/watch?v=wZBfmBvvotE")
kill_bill_vol2 = media.Movie("Kill Bill Vol. 2", "www.youtube.com/watch?v=NSR7xRGBnOE")
dark_knight_rises = media.Movie("The Dark Knight Rises", "www.youtube.com/watch?v=g8evyE9TuYk")
fear_and_loathing = media.Movie("Fear and Loathing in Las Vegas", "www.youtube.com/watch?v=_d0hEzXrWT4&")
high_fidelity = media.Movie("High Fidelity", "www.youtube.com/watch?v=q8DIm_47xPU")
ex_machina = media.Movie("Ex Machina", "www.youtube.com/watch?v=XYGzRB4Pnq8")

# What movies to display, in order
movies = [big_lebowski, shawshank_redemption, holy_mountain, forrest_gump, pulp_fiction, kill_bill_vol2, dark_knight_rises, fear_and_loathing, high_fidelity, ex_machina]

# Generate an html page from the supplied movies and open it
fresh_tomatoes.open_movies_page(movies)
