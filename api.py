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
    
    info = [registro for registro in dicionario if registro['Class'] == classes]

    return jsonify(info)

@app.route('/fight')
def fight():

    pontos1 = 0
    pontos2 = 0

    name1 = request.args.get('name1')
    name2 = request.args.get('name2')

    dados1 = [registro for registro in dicionario if registro['Name'] == name1]
    dados2 = [registro for registro in dicionario if registro['Name'] == name2]

    power1 = dados1[0]['Power']
    speed1 = dados1[0]['Speed']
    magic1 = dados1[0]['Magic']
    healing1 = dados1[0]['Healing Factor']
    weakness1 = dados1[0]['Weakness']

    power2 = dados2[0]['Power']
    speed2 = dados2[0]['Speed']
    magic2 = dados2[0]['Magic']
    healing2 = dados2[0]['Healing Factor']
    weakness2 = dados2[0]['Weakness']

    #Personagem 1
    if(power1 > power2): pontos1 += 1
    if(speed1 > speed2): pontos1 += 1
    if(magic1 > magic2): pontos1 += 1
    if(healing1 > healing2): pontos1 += 1

    if(power1 > power2 and weakness2 == 'Power'): pontos1 += 2
    if(speed1 > speed2 and weakness2 == 'Speed'): pontos1 += 2
    if(magic1 > magic2 and weakness2 == 'Magic'): pontos1 += 2
    if(healing1 > healing2 and weakness2 == 'Healing Factor'): pontos1 += 2
 
    #Personagem2
    if(power1 < power2): pontos2 += 1
    if(speed1 < speed2): pontos2 += 1
    if(magic1 < magic2): pontos2 += 1
    if(healing1 < healing2): pontos2 += 1

    if(power1 < power2 and weakness1 == 'Power'): pontos2 += 2
    if(speed1 < speed2 and weakness1 == 'Speed'): pontos2 += 2
    if(magic1 < magic2 and weakness1 == 'Magic'): pontos2 += 2
    if(healing1 < healing2 and weakness2 == 'Healing Factor'): pontos2 += 2

    if(pontos1 > pontos2):
        return jsonify(dados1)
    else:
        return jsonify(dados2)


if __name__ == '__main__':
    app.run('0.0.0.0')