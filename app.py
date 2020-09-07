from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Valdir', 'habilidades': ['Python','Flask']},
    {'nome':'Alves', 'habilidades': ['C++','Delphi']}
]
#
@app.route('/dev/<int:id>/', methods=['POST','GET','PUT','DELETE'])

def desenvolvedor(id):
    if request.method == 'GET':
        try:
            ator = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe' .format(id)
            ator = {'status':'erro','mensagem':mensagem}
            return jsonify(response)
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API'
            ator = {'status': 'erro', 'mensagem': mensagem}

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id]= dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'registro exluido'})

#
@app.route('/dev/',methods=['POST','GET'])

def lista_devensolvedores():
    if request.method =='POST':
        dados=json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'registro inserido'})


if __name__ == '__main__':
    app.run(debug=True)
