from flask import Flask, make_response, jsonify, request, g
import json

app = Flask(__name__)


@app.before_request
def load_data():
    with open("db.json") as f:
        g.data: dict = json.load(f)


@app.after_request
def save_data(response):
    with open('db.json', 'w') as f:
        json.dump(g.data, f, indent=4)
    return response

@app.route("/")
def root():
    return "<h1>Welcome to the simple json server<h1>"

#@app.route('/langs', methods=['GET'])
@app.get("/langs")
def get_langs():
    pass




@app.get("/langs/<int:id>")
def get_lang_by_id(id: int):
    pass




# TODO: write post route

# TODO: write delete route

# TODO: write patch route




if __name__ == "__main__":
    app.run(port=5555, debug=True)
