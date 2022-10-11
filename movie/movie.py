from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify, make_response

import resolvers as r

PORT = 3001
HOST = 'localhost'
app = Flask(__name__)

type_defs = load_schema_from_path('movie.graphql')

movie = ObjectType('Movie')
actor = ObjectType('Actor')
movieData = ObjectType('MovieData')


query = QueryType()
query.set_field('movie_with_id', r.movie_with_id)
query.set_field('actor_with_id', r.actor_with_id)
query.set_field('GetMovieByTitle', r.GetMovieByTitle)
query.set_field('GetListMovies', r.GetListMovies)

mutation = MutationType()
mutation.set_field('update_movie_rate', r.update_movie_rate)
mutation.set_field('DeleteByMovieId', r.DeleteByMovieId)
mutation.set_field('PostMovie', r.PostMovie)

movie.set_field('actors', r.resolve_actors_in_movie)
#movieData.set_field('movies', r.resolve_movies_in_movieData)


schema = make_executable_schema(type_defs, movie, query, mutation, actor, movieData)

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>", 200)


#####
# graphql entry points

@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=None, debug=app.debug)
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT, debug=True)
