from flask import Flask
from views import get,post,get,put,delete
from flask_sqlalchemy import SQLAlchemy
from database.db import create_app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database/store.db"
create_app(app)



#http://127.0.0.1:5000/ 
#http://127.0.0.1:5000/api/v1/movies
app.register_blueprint(get.get_movie)

#http://127.0.0.1:5000/api/v1/movie data={name,casts,genres}
app.register_blueprint(post.post_movie)

#http://127.0.0.1:5000/api/v1/movie/{index}
app.register_blueprint(put.updat_movie)

#http://127.0.0.1:5000/api/v1/movie{index}
app.register_blueprint(delete.del_movie)


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
