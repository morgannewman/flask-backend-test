from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json

# spin up Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)

# POST /search endpoint
@app.route('/search', methods=['POST'])
def request_handler():
    if request.method == 'POST':
        data = (request.get_json())['content']
        print data
        # HERE WE HAVE CONTENT TO PARSE
        # INSERT MAGIC FUNCTION TO DO MAGIC THINGS HERE
        response = jsonify({'PLACEHOLDER': 'DATA'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 201
    else: 
        return jsonify({'Error': 'does not exist'}, 404)

# spin up server
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)