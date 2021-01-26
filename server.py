import json
import sys
import flask
from flask import request

app = flask.Flask('jolha')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No \'valor\' or \'horas\' field provided. Please specify an them."

    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05

    liquido = bruto - ir - inss - sindicato

    info = {
        "salario_bruto": float(format(bruto, '.2f')),
        "ir": float(format(ir, '.2f')),
        "inss": float(format(inss, '.2f')),
        "sindicato": float(format(sindicato, '.2f')),
        "salario_liquido": float(format(liquido, '.2f'))
    }

    json_file = json.dumps(info)
    #return json_file
    data = "<h1>Salário Bruto: R$ " + str(info['salario_bruto']) + "</h1>" + "<p>- IR (11%) : R$ " + str(info["ir"]) + "</p>" + "<p>- INSS (8%) : R$ " + str(info["inss"]) + "</p>" + "<p>- Sindicato (5%) : R$ " + str(info["sindicato"]) + "</p>" + "<p>- Salário Líquido : R$ " + str(info["salario_liquido"]) + "</p>"

    return data 

@app.route('/bruto', methods=['GET'])
def bruto():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05

    liquido = bruto - ir - inss - sindicato

    info = {
        "salario_bruto": float(format(bruto, '.2f')),
        "ir": float(format(ir, '.2f')),
        "inss": float(format(inss, '.2f')),
        "sindicato": float(format(sindicato, '.2f')),
        "salario_liquido": float(format(liquido, '.2f'))
    }

    data = "<h1>Salário Bruto: R$ " + str(info['salario_bruto']) + "</h1>"

    return data

@app.route('/ir', methods=['GET'])
def ir():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05

    liquido = bruto - ir - inss - sindicato

    info = {
        "salario_bruto": float(format(bruto, '.2f')),
        "ir": float(format(ir, '.2f')),
        "inss": float(format(inss, '.2f')),
        "sindicato": float(format(sindicato, '.2f')),
        "salario_liquido": float(format(liquido, '.2f'))
    }

    data = "<h1>IR: R$ " + str(info['ir']) + "</h1>"

    return data

@app.route('/inss', methods=['GET'])
def inss():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05

    liquido = bruto - ir - inss - sindicato

    info = {
        "salario_bruto": float(format(bruto, '.2f')),
        "ir": float(format(ir, '.2f')),
        "inss": float(format(inss, '.2f')),
        "sindicato": float(format(sindicato, '.2f')),
        "salario_liquido": float(format(liquido, '.2f'))
    }

    data = "<h1>INSS: R$ " + str(info['inss']) + "</h1>"

    return data

@app.route('/sindicato', methods=['GET'])
def sindicato():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05

    liquido = bruto - ir - inss - sindicato

    info = {
        "salario_bruto": float(format(bruto, '.2f')),
        "ir": float(format(ir, '.2f')),
        "inss": float(format(inss, '.2f')),
        "sindicato": float(format(sindicato, '.2f')),
        "salario_liquido": float(format(liquido, '.2f'))
    }

    data = "<h1>Sindicato: R$ " + str(info['sindicato']) + "</h1>"

    return data

@app.route('/liquido', methods=['GET'])
def liquido():
    if 'valor' in request.args:
        valor = int(request.args['valor'])
    if 'horas' in request.args:
        horas = int(request.args['horas'])
    else:
        return "Error: No id field provided. Please specify an id."

    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05

    liquido = bruto - ir - inss - sindicato

    info = {
        "salario_bruto": float(format(bruto, '.2f')),
        "ir": float(format(ir, '.2f')),
        "inss": float(format(inss, '.2f')),
        "sindicato": float(format(sindicato, '.2f')),
        "salario_liquido": float(format(liquido, '.2f'))
    }

    data = "<h1>Salário Líquido: R$ " + str(info['salario_liquido']) + "</h1>"

    return data

app.run(host="0.0.0.0", port="3000", debug=True)