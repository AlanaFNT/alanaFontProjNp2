from Model.modelProcesso import Processo
from DTO.dtoProcesso import ProcessoDTO
from Repository.repositoryProcesso import ProcessoRepository
from flask import Flask, jsonify, request


class ProcessoService:
    def __init__(self):
        self.repository = ProcessoRepository()

    def cadastrar_processo_service(self):
        data = request.get_json()
        if True:
            processo_dto = ProcessoDTO(
                id=None,  # id eh atribuido automaticamente pelo BD
                numero=data['numero'],
                prazo=data['prazo'],
                acusado=data['acusado'],
                acusador=data['acusador']
            )
            if self.repository.cadastrar_processo(processo_dto):
                return jsonify({"msg": "Processo cadastrado com sucesso"}), 201
        else:
            return jsonify({"msg": "Erro ao cadastrar processo"}), 500


# ----------------------------------------//---------------------------------------------

    def buscar_processos_service(self):
        processos = self.repository.buscar_processos()
        todos_processos = [ProcessoDTO(processo[0], processo[1], processo[2], processo[3], processo[4]) for processo in processos]
        processos_dict = [processo.__dict__ for processo in todos_processos]
        return jsonify(processos_dict), 200


# ----------------------------------------//---------------------------------------------


    def buscar_processo_por_id_service(self, id):
        processo = self.repository.buscar_processo_por_id(id)
        if processo:
            processo = ProcessoDTO(processo[0], processo[1], processo[2], processo[3], processo[4])
            return jsonify(processo.__dict__), 200
        else:
            return jsonify({"error": "Processo não encontrado"}), 404


# ----------------------------------------//---------------------------------------------


    def editar_processo_service(self, id):
        data = request.get_json()
        processo_dto = ProcessoDTO(None, data['numero'], data['prazo'], data['acusado'], data['acusador'])

        if self.repository.editar_processo(id, processo_dto):
            return jsonify({"msg": "Processo editado com sucesso"}), 200
        else:
            return jsonify({"msg": "Erro ao editar processo"}), 500


# ----------------------------------------//---------------------------------------------


    def excluir_processo_service(self, id):
        if self.repository.excluir_processo(id):
            return jsonify({"msg": "Processo excluído com sucesso"}), 200
        else:
            return jsonify({"msg": "Processo não encontrado"}), 404
