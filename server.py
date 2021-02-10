import json
import sys
import flask
from flask import request

app = flask.Flask('jolha')
app.config["DEBUG"] = True

info = {
        "salario_bruto": "",
        "ir": "",
        "inss": "",
        "sindicato": "",
        "salario_liquido": ""
    }

def preenche(bruto, ir, inss, sindicato, liquido):
    info["salario_bruto"] = float(format(bruto, '.2f'))
    info["ir"] = float(format(ir, '.2f'))
    info["inss"] = float(format(inss, '.2f'))
    info["sindicato"] = float(format(sindicato, '.2f'))
    info["salario_liquido"] = float(format(liquido, '.2f'))

def calcula(horas, valor):
    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - ir - inss - sindicato
    return bruto, ir, inss, sindicato, liquido

@app.route('/', methods=['GET'])
def home():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No \'valor\' or \'horas\' field provided. Please specify an them."

    bruto, ir, inss, sindicato, liquido = calcula(horas, valor)
    preenche(bruto, ir, inss, sindicato, liquido)

    #data = "<h1>Salário Bruto: R$ " + str(info['salario_bruto']) + "</h1>" + "<p>- IR (11%) : R$ " + str(info["ir"]) + "</p>" + "<p>- INSS (8%) : R$ " + str(info["inss"]) + "</p>" + "<p>- Sindicato (5%) : R$ " + str(info["sindicato"]) + "</p>" + "<p>- Salário Líquido : R$ " + str(info["salario_liquido"]) + "</p>"
    return json.dumps(info)

@app.route('/bruto', methods=['GET'])
def bruto():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto, ir, inss, sindicato, liquido = calcula(horas, valor)
    preenche(bruto, ir, inss, sindicato, liquido)
    #data = "<h1>Salário Bruto: R$ " + str(info['salario_bruto']) + "</h1>"
    json_file = json.dumps({"salario_bruto": info["salario_bruto"]})
    return json_file

@app.route('/ir', methods=['GET'])
def ir():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto, ir, inss, sindicato, liquido = calcula(horas, valor)
    preenche(bruto, ir, inss, sindicato, liquido)
    #data = "<h1>IR: R$ " + str(info['ir']) + "</h1>"

    return json.dumps({"ir": info["ir"]})

@app.route('/inss', methods=['GET'])
def inss():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto, ir, inss, sindicato, liquido = calcula(horas, valor)
    preenche(bruto, ir, inss, sindicato, liquido)
    #data = "<h1>INSS: R$ " + str(info['inss']) + "</h1>"

    return json.dumps({"inss": info["inss"]})

@app.route('/sindicato', methods=['GET'])
def sindicato():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto, ir, inss, sindicato, liquido = calcula(horas, valor)
    preenche(bruto, ir, inss, sindicato, liquido)
    #data = "<h1>Sindicato: R$ " + str(info['sindicato']) + "</h1>"

    return json.dumps({"sindicato": info["sindicato"]})

@app.route('/liquido', methods=['GET'])
def liquido():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto, ir, inss, sindicato, liquido = calcula(horas, valor)
    preenche(bruto, ir, inss, sindicato, liquido)
    #data = "<h1>Salário Líquido: R$ " + str(info['salario_liquido']) + "</h1>"

    return json.dumps({"salario_liquido": info["salario_liquido"]})

app.run(host="0.0.0.0", port="3000", debug=True)