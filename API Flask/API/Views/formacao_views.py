from flask_restful import Resource
from API import api
from ..Schema import formacao_schema
from flask import request, make_response, jsonify
from ..Entidades import formacao
from ..Services import formacao_service

class FormacaoList(Resource):
    def get(self):
        formacoes = formacao_service.listar_formacoes()
        fs = formacao_schema.FormacaoSchema(many=True)
        return make_response(fs.jsonify(formacoes), 200)

    def post(self):
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            professores = request.json['professores']

            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)
            resultado = formacao_service.cadastrar_formacao(novo_formacao)
            x = fs.jsonify(resultado)
            return make_response(x, 201)

class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify('Formacao não encontrado'), 404)
        fs = formacao_schema.FormacaoSchema()
        return make_response(fs.jsonify(formacao), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify('Formacao não encontrado'), 404)
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            professores = request.json['professores']

            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)
            formacao_service.atualiza_formacao(formacao_bd, novo_formacao)
            formacao_atualizado = formacao_service.listar_formacao_id(id)
            return make_response(fs.jsonify(formacao_atualizado, 200))

    def delete(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify('Formacao não encontrado'), 404)
        formacao_service.remove_formacao(formacao_bd)
        return make_response("Formacao removida!", 204)

api.add_resource(FormacaoList, '/formacoes')
api.add_resource(FormacaoDetail, '/formacoes/<int:id>')
