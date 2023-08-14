from flask import Flask, make_response, jsonify, request, g
import json

app = Flask(__name__)



@app.before_request
def load_data():
    with open('db.json') as f:
        g.data = json.load(f)

@app.route('/')
def root():
    return "<h1>Welcome to the simple json server<h1>"

@app.get('/langs')
def get_langs():
    return make_response(jsonify(g.data['langs']), 200)

'''
TODO: Add error handling if the id is not found
'''
@app.get('/langs/<int:id>')
def get_lang_by_id(id:int):
    lang = [l for l in g.data['langs'] if l['id'] == id][0]
    return make_response(jsonify(lang), 200)

'''
TODO: Implement a POST request
Note that in order to persist the change you will have 
to write it to db.json. The route and function have been
provided. You'll also have to take care of keeping track
of giving the new item an id.
'''
@app.post('/langs')
def post_lang():
    return ''

'''
TODO: Implement a DELETE request
Note that in order to persist the change you will have 
to write it to db.json. You'll have to write the 
route and function.
'''

if __name__ == '__main__':
    app.run(port=5555, debug=True)

