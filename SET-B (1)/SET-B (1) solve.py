def read_movie_data(filename):
    movies = []
    with open("D:\Assignment-02\SET-B (1)\MovieInfo.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 4:
                movie = {"title": parts[0], "year": parts[1], "director": parts[2], "genre": parts[3]}
                movies.append(movie)
    return movies
def search_by_year_genre(movies, year, genre, output_filename):
    with open(output_filename, "w") as file:
        for movie in movies:
            if movie["year"] == year and movie["genre"].lower() == genre.lower():
                file.write(f"{movie['title']}, {movie['year']}, {movie['director']}, {movie['genre']}\n")
                print(f"Results saved in {output_filename}")
                return
    print("No matching movies found.")
def search_by_director(movies, director):
    found = False
    for movie in movies:
        if movie["director"].lower() == director.lower():
            print(f"{movie['title']}, {movie['year']}, {movie['director']}, {movie['genre']}")
            found = True
    if not found:
        print("No movies found for this director.")
movies = read_movie_data("D:\Assignment-02\SET-B (1)\MovieInfo.txt")
year = input("Enter a release year: ")
genre = input("Enter a genre: ")
search_by_year_genre(movies, year, genre, "YearwiseGenreMovie.txt")
director = input("Enter director’s name: ")
search_by_director(movies, director)