from flask import Flask
import request
import json

app = Flask(__name__)


# @app.route('/json-example', methods=['POST'])  # GET requests will be blocked
# def json_example():
#     req_data = request.get_json()
#
#     language = req_data['language']
#     language = None
#     if 'language' in req_data:
#         language = req_data['language']
#     framework = req_data['framework']
#     python_version = req_data['version_info']['python']  # two keys are needed because of the nested object
#     example = req_data['examples'][0]  # an index is needed because of the array
#     boolean_test = req_data['boolean_test']
#
#     return '''
#            The language value is: {}
#            The framework value is: {}
#            The Python version is: {}
#            The item at index 0 in the example list is: {}
#            The boolean value is: {}'''




@app.route('/home', methods=('GET', 'POST'))
def request_handler():
    if request.method == 'POST':
        data = json.loads(request.body['content'])
        print data
        return json.dumps({'Hello': 'World'})

    #return render_template(<template name e.g. xyz.html>, posts=data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


