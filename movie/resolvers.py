import json

def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie
def GetListMovies(_,info):
    print("GetListMovies", _, info)
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        return movies


def PostMovie(_,info,_id, _title,_director,_rating):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        movies.append({"title": _title, "rating": _rating, "director": _director, "id": _id})
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(movies, wfile)

    for movie in movies['movies']:
        if movie['id'] == _id:
            return movie

def DeleteByMovieId(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        newMovies = []
        for movie in movies['movies']:
            if movie['id'] == _id:
                movieDel = movie
            else:
                newMovies.append(movie)
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newMovies, wfile)
    return movieDel

def GetMovieByTitle(_,info,_title):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['title'] == _title:
                return movie

# def resolve_movies_in_movieData(movieData, info):
#     with open('{}/data/movies.json'.format("."), "r") as file:
#         movies = json.load(file)
#         print(movies['movies'])
#         return movies['movies']
def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile)
    return newmovie

def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def actor_with_id(_,info,_id):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        for actor in data['actors']:
            if actor["id"] == _id:
                return actor