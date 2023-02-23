from flask import Flask
from views import get,post,get,put,delete


app = Flask(__name__)



#http://127.0.0.1:5000/ 
#http://127.0.0.1:5000/api/v1/movie
app.register_blueprint(get.get_movie)

#http://127.0.0.1:5000/api/v1/movie data={name,casts,genres}
app.register_blueprint(post.post_movie)

#http://127.0.0.1:5000/api/v1/movie/{index}
app.register_blueprint(put.updat_movie)

#http://127.0.0.1:5000/api/v1/movie{index}
app.register_blueprint(delete.del_movie)


if __name__ == "__main__":
    app.run(debug=True)
 
