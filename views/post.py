from flask import jsonify,request
from json_file import movies
from . import post_movie

#Add movie view function
#http://127.0.0.1:5000/movie data={name,casts,genres}


@post_movie.route('/api/v1/movie', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)

    return jsonify({'id': len(movies)}), 201
