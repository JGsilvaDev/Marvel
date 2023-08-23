import pandas as pd
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
dados = pd.read_csv('dados.csv',sep=';')
dados = dados.dropna()
dicionario = dados.to_dict(orient='records')

@app.route('/')
def obter_dados_como_json():
    return jsonify(dicionario)

@app.route('/info')
def info():
    name = request.args.get('name')
    if name is None:
        return "O parâmetro 'nome' é obrigatório.", 400

    info = [registro for registro in dicionario if registro['Name'] == name]

    return jsonify(info)

@app.route('/info/classes')
def classes():
    classes = request.args.get('class')
    if classes is None:
        return "O parâmetro 'class' é obrigatório.", 400
    
    # info = [registro for registro in dicionario if registro['Class'] == classes]

    info = pd.read_json('dados.json')

    return jsonify(info)


if __name__ == '__main__':
    app.run('0.0.0.0')