import json

def movie_with_id(_,info,_id):
    """ return le movie ou id == _id """
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie
def GetListMovies(_,info):
    """ return tous les movies sous forme de Movie """
    print("GetListMovies", _, info)
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        return movies


def PostMovie(_,info,_id, _title,_director,_rating):
    """ Ajoute un movie dans le json.
        Parametre : id,title,director,rating."""
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        movies.append({"title": _title, "rating": _rating, "director": _director, "id": _id})
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(movies, wfile)

    for movie in movies['movies']:
        if movie['id'] == _id:
            return movie

def DeleteByMovieId(_,info,_id):
    """ supprimme dans le json le film avec id == _id """
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
    """ return le movie ou title == _title """
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['title'] == _title:
                return movie

""" resolver prévu pour movies pour : GetListMovies 
    inutilisée car non utile """
# def resolve_movies_in_movieData(movieData, info):
#     with open('{}/data/movies.json'.format("."), "r") as file:
#         movies = json.load(file)
#         print(movies['movies'])
#         return movies['movies']
def update_movie_rate(_,info,_id,_rate):
    """ via l'id et une nouvelle note modifie la note d'un film """
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
    """ renvoie les acteurs du film via movie['id'] """
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def actor_with_id(_,info,_id):
    """ return un actor lorsque _id == id """
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        for actor in data['actors']:
            if actor["id"] == _id:
                return actor