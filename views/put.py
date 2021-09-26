from flask import jsonify,request
from json_file import movies
from . import updat_movie

#Update movie view function
#http://127.0.0.1:5000/movie/{index}


@updat_movie.route('/api/v1/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200
