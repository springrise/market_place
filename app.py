from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
app.secret_key = "SECRET_KEY"

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    #define admin


jwt = JWTManager(app)

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True, port=5000)