from Model.modelDefensor import Defensor
from DTO.dtoDefensor import DefensorDTO
from Repository.repositoryDefensor import DefensorRepository
from flask import Flask, jsonify, request


class DefensorService:
    def __init__(self):
        self.repository = DefensorRepository()

    def cadastrar_defensor_service(self):
        data = request.get_json()
        if True:
            defensor_dto = DefensorDTO(
                id=None,  # id eh atribuido automaticamente pelo BD
                nome=data['nome'],
                especialidade=data['especialidade'],
                vara=data['vara'],
                salario=data['salario']
            )
            if self.repository.cadastrar_defensor(defensor_dto):
                return jsonify({"msg": "Defensor cadastrado com sucesso"}), 201
        else:
            return jsonify({"msg": "Erro ao cadastrar defensor"}), 500


# ----------------------------------------//---------------------------------------------

    def buscar_defensores_service(self):
        defensores = self.repository.buscar_defensores()
        todos_defensores = [DefensorDTO(defensor[0], defensor[1], defensor[2], defensor[3], defensor[4]) for defensor in defensores]
        defensores_dict = [defensor.__dict__ for defensor in todos_defensores]
        return jsonify(defensores_dict), 200


# ----------------------------------------//---------------------------------------------


    def buscar_defensor_por_id_service(self, id):
        defensor = self.repository.buscar_defensor_por_id(id)
        if defensor:
            defensor = DefensorDTO(defensor[0], defensor[1], defensor[2], defensor[3], defensor[4])
            return jsonify(defensor.__dict__), 200
        else:
            return jsonify({"error": "Defensor não encontrado"}), 404


# ----------------------------------------//---------------------------------------------


    def editar_defensor_service(self, id):
        data = request.get_json()
        defensor_dto = DefensorDTO(None, data['nome'], data['especialidade'], data['vara'], data['salario'])

        if self.repository.editar_defensor(id, defensor_dto):
            return jsonify({"msg": "Defensor editado com sucesso"}), 200
        else:
            return jsonify({"msg": "Erro ao editar defensor"}), 500


# ----------------------------------------//---------------------------------------------


    def excluir_defensor_service(self, id):
        if self.repository.excluir_defensor(id):
            return jsonify({"msg": "Defensor excluído com sucesso"}), 200
        else:
            return jsonify({"msg": "Defensor não encontrado"}), 404
