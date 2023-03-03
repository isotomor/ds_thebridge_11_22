from flask import Flask, request, jsonify
import os
import pickle
from sklearn.model_selection import cross_val_score
import pandas as pd
import sqlite3


os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"

@app.route('/v2/predict', methods=['GET'])
def predict():
    model = pickle.load(open('data/advertising_model','rb'))

    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    if tv is None or radio is None or newspaper is None:
        return "Missing args, the input values are needed to predict"
    else:
        prediction = model.predict([[tv,radio,newspaper]])
        return "The prediction of sales investing that amount of money in TV, radio and newspaper is: " + str(round(prediction[0],2)) + 'k €'

@app.route('/v2/ingest_data', methods=['POST'])
def new_data():
    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)
    sales = request.args.get('sales', None)

    connection = sqlite3.connect('data/advertising.db')
    cursor = connection.cursor()
    query = '''INSERT INTO campañas VALUES (?,?,?,?)'''
    result = cursor.execute(query, (tv, radio, newspaper, sales) ).fetchall()

    query = '''SELECT * FROM campañas'''
    result = cursor.execute(query).fetchall()
    connection.commit()
    connection.close()
    return jsonify(result)


@app.route('/v2/retrain', methods=['PUT'])
def retrain():
    connection = sqlite3.connect('data/advertising.db')
    cursor = connection.cursor()
    query = '''SELECT * FROM campañas'''
    result = cursor.execute(query).fetchall()
    names = [description[0] for description in cursor.description]
    df = pd.DataFrame(result, columns=names)

    X = df.drop(columns=['sales'])
    y = df['sales']
    
    model = pickle.load(open('data/advertising_model', 'rb'))
    model.fit(X,y)
    pickle.dump(model, open('data/advertising_model', 'wb'))

    scores = cross_val_score(model, X, y, cv=10, scoring='neg_mean_absolute_error')

    return "New model trained. The results of MAE with cv is " + str(round(scores.mean()*(-1),2))


# app.run()

