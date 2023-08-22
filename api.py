import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():

    dados = pd.read_csv('dados.csv',sep=';')

    dicionario = dados.to_dict(orient='records')

    return jsonify(dicionario)

app.run(host='0.0.0.0')