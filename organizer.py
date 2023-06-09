import os
from tmdbv3api import TMDb
from tmdbv3api import Movie

# Create an instance of the TMDb class
tmdb = TMDb()

# Set your API key
tmdb.api_key = "9bc6dfc9ec25c1f5e9d67691503c8889"
movie = Movie()





# Define the TMDb ID of the movie or TV show you want to retrieve information about
tmdb_id = 550

# Retrieve information about the movie or TV show using its TMDb ID
movie = Movie().details(tmdb_id)
print(movie.title)



# # Determine whether the item is a movie or TV show
# if movie["media_type"] == "movie":
#     item_type = "movie"
# elif movie["media_type"] == "tv":
#     item_type = "tv_series"
# else:
#     raise ValueError("Item is not a movie or TV show")

# # Move the item to the appropriate folder based on its type
# source_path = "/home/shubham/Downloads/numpy/Jellyfin_Organizer"
# destination_path = f"/home/shubham/Downloads/{item_type}/folder"
# filename = f"{movie['title']} ({movie['release_date'][:4]})"
# os.rename(os.path.join(source_path, filename), os.path.join(destination_path, filename))
