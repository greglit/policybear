from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

import pandas as pd
import datetime as dt
import json

# complement time dims if not existent
def complement(df):
    for i in ['month','day','hour','minute','second']:
        if i not in list(df.columns):
            df[i] = 1
    return df

# load .csv into pd.Dataframe
def load_df(file):
    df = pd.read_csv(file+'.csv', sep=';')
    df = complement(df)
    df['time'] = [dt.datetime(Y,M,D,h,m,s)
                  for Y,M,D,h,m,s in zip(
                      df['year'],df['month'],df['day'],
                      df['hour'],df['minute'],df['second'])]
    df = df[['time','value']].set_index('time')
    return df

# load files into dictionary
data_vars = ['carbon_dioxide','methane']
data = {i: load_df(i) for i in data_vars}

var = 'methane'
df = data[var]




# # read data
# df = pd.read_csv('methane.csv', sep=';')
# df = complement(df)
# df['time'] = [dt.datetime(y,m,d) for y,m,d in zip(df['year'],df['month'],df['day'])]
# df = df[['time','value']].set_index('time')

def return_period(df, start_date,end_date):
    begin,end = pd.Timestamp(start_date),pd.Timestamp(end_date)
    mask = (df.index >= begin) & (df.index < end)
    return df.loc[mask]

def return_change(df):
    return df['value'].loc[df.index.max()] - df['value'].loc[df.index.min()]

app = Flask(__name__)
CORS(app)

@app.route('/datasets/')
def datasets()
    return jsonify(response)

@app.route('/datapoints/')
def datapoints():
    data = request.args.get('dataset')
    start_date = request.args.get('startdate')
    end_date = request.args.get('enddate')

    period = return_period(df,start_date,end_date)
    change = return_change(period)
    # return render_template('index.html')
    response = {'dataset': data,
                'begin_period': period.index.min().strftime("%Y-%m-%d"),
                'end_period': period.index.max().strftime("%Y-%m-%d"),
                'change': change}
    return jsonify(response)

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

#%%

