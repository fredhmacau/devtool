from json_file import movies
from flask import jsonify
from . import get_movie


#views movies
#http://127.0.0.1:5000/
#http://127.0.0.1:5000/movies
@get_movie.route('/', methods=['GET'])
@get_movie.route('/api/v1/movies',methods=['GET'])
def index():
    return jsonify(movies)
