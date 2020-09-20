from flask_restful import Resource

lista_habilidades = ['Python','C++','Java','PHP','Dephi','C#','Flask']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
