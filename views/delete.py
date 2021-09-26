from flask import jsonify
from json_file import movies
from . import del_movie

#delete movie view function
#http://127.0.0.1:5000/movie/{index}


@del_movie.route('/api/v1/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return "None", 200
