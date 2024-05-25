from Model.modelAdvogado import Advogado
from DTO.dtoAdvogado import AdvogadoDTO
from Repository.repositoryAdvogado import AdvogadoRepository
from flask import Flask, jsonify, request


class AdvogadoService:
    def __init__(self):
        self.repository = AdvogadoRepository()

    def cadastrar_advogado_service(self):
        data = request.get_json()
        if True:
            advogado_dto = AdvogadoDTO(
                id=None,  # id eh atribuido automaticamente pelo BD
                nome=data['nome'],
                especialidade=data['especialidade'],
                escritorio=data['escritorio'],
                salario=data['salario']
            )
            if self.repository.cadastrar_advogado(advogado_dto):
                return jsonify({"msg": "Advogado cadastrado com sucesso"}), 201
        else:
            return jsonify({"msg": "Erro ao cadastrar advogado"}), 500


# ----------------------------------------//---------------------------------------------

    def buscar_advogados_service(self):
        advogados = self.repository.buscar_advogados()
        todos_advogados = [AdvogadoDTO(advogado[0], advogado[1], advogado[2], advogado[3], advogado[4]) for advogado in advogados]
        advogados_dict = [advogado.__dict__ for advogado in todos_advogados]
        return jsonify(advogados_dict), 200


# ----------------------------------------//---------------------------------------------


    def buscar_advogado_por_id_service(self, id):
        advogado = self.repository.buscar_advogado_por_id(id)
        if advogado:
            advogado = AdvogadoDTO(advogado[0], advogado[1], advogado[2], advogado[3], advogado[4])
            return jsonify(advogado.__dict__), 200
        else:
            return jsonify({"error": "Advogado não encontrado"}), 404


# ----------------------------------------//---------------------------------------------


    def editar_advogado_service(self, id):
        data = request.get_json()
        advogado_dto = AdvogadoDTO(None, data['nome'], data['especialidade'], data['escritorio'], data['salario'])

        if self.repository.editar_advogado(id, advogado_dto):
            return jsonify({"msg": "Advogado editado com sucesso"}), 200
        else:
            return jsonify({"msg": "Erro ao editar advogado"}), 500


# ----------------------------------------//---------------------------------------------


    def excluir_advogado_service(self, id):
        if self.repository.excluir_advogado(id):
            return jsonify({"msg": "Advogado excluído com sucesso"}), 200
        else:
            return jsonify({"msg": "Advogado não encontrado"}), 404
