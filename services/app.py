

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


from sqlalchemy.ext.automap import automap_base
import psycopg2


app = Flask(__name__)
app.config.from_pyfile('config.py')





db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

Base=automap_base()
Base.prepare(db.engine,reflect=True)


import routes


if __name__=="__main__":
    app.run(debug=True)