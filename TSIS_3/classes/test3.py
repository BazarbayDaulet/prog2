movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    # ... (rest of your movie data)
]


name_input = input("Enter the name of the movie: ")

# Search for the movie in the list
found_movie = None
for movie in movies:    
    if movie["name"] == name_input:
        found_movie = movie
        break

# Check if the movie was found
if found_movie:
    print("Movie found:")
    print("Name:", found_movie["name"])
    print("IMDb:", found_movie["imdb"])
    print("Category:", found_movie["category"])
else:
    print("Movie not found.")
