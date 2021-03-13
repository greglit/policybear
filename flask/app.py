from flask import Flask, request, jsonify, redirect
# from flask_cors import CORS

import pandas as pd
import json

app = Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    # return render_template('index.html')
    return 'hellowfadsfa'

# @app.route('/study')
# def study():
#     return render_template('study.html')
#
# @app.route('/sample', methods=['POST'])
# def sample():
#     df = pd.DataFrame(request.get_json(), index=[0])
#     data = expl.get_json_data_for_sample(df)
#     print('POST /sample data:')
#     print(data)
#     response = app.response_class(
#         response=json.dumps(data),
#         status=200,
#         mimetype='application/json'
#     )
#     return response
#
# @app.route('/counter', methods=['POST'])
# def counter():
#     df = pd.DataFrame(request.get_json(), index=[0])
#     data = expl.get_json_data_for_sample(df)
#     response = app.response_class(
#         response=json.dumps(data),
#         status=200,
#         mimetype='application/json'
#     )
#     return response
#
# @app.route('/results', methods=['POST'])
# def results():
#     data = request.get_json()
#     print(data)
#     new_subject = Subject(**data)
#     try:
#         db.session.add(new_subject)
#         db.session.commit()
#         return 'success'
#     except:
#         return 'fail'
#
# @app.route('/finish')
# def finish():
#     return render_template('finish.html')

if __name__ == "__main__":
    app.run(debug=True)
