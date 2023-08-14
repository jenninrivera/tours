from flask import Flask, make_response, jsonify, request, g
import json

app = Flask(__name__)


@app.before_request
def load_data():
    with open("db.json") as f:
        g.data: dict = json.load(f)


@app.route("/")
def root():
    return "<h1>Welcome to the simple json server<h1>"


@app.get("/langs")
def get_langs():
    return make_response(jsonify(g.data["langs"]), 200)




@app.get("/langs/<int:id>")
def get_lang_by_id(id: int):
    lang_list: list[dict] = [l for l in g.data["langs"] if l["id"] == id]
    if len(lang_list) == 0:
        return make_response(jsonify({"error": f"id {id} not found"}), 404)
    return make_response(jsonify(lang_list[0]), 200)




@app.post("/langs")
def post_lang():
    new_lang: dict = request.get_json()
    max_id: int = max([item["id"] for item in g.data["langs"]])
    new_lang["id"] = max_id + 1
    g.data["langs"].append(new_lang)
    print(g.data)
    with open("db.json", "w") as f:
        json.dump(g.data, f, indent=4)
    return make_response(jsonify(new_lang), 201)




@app.delete("/langs/<int:id>")
def delete_lang_by_id(id: int):
    updated_langs: list[dict] = [item for item in g.data["langs"] if item["id"] != id]
    if len(updated_langs) == len(g.data["langs"]):
        return make_response(jsonify({"error": f"id {id} not found"}), 404)
    g.data["langs"] = updated_langs
    with open("db.json", "w") as f:
        json.dump(g.data, f, indent=4)
    return make_response(jsonify({}), 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
