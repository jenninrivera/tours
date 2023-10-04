from flask import make_response, jsonify, request, g
from flask import Flask
from models import db, Student, Course, Enrollment

from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def root():
    return "<h1>Registrar</h1>"




if __name__ == "__main__":
    app.run(port=5555, debug=True)
