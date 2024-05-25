from flask import Blueprint, Flask, jsonify, request
from DTO.dtoProcesso import ProcessoDTO
from Service.serviceProcesso import ProcessoService
from flasgger import Swagger, swag_from


app = Flask(__name__)
swagger = Swagger(app)
processo_service = ProcessoService()
processo_bp = Blueprint('processo_bp', __name__)



@processo_bp.route('/cadastrar_processos', methods=['POST'])
@swag_from({
    'tags': ['Processos'],
    'description': 'Endpoint para cadastrar um novo processo.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'numero': {'type': 'number'},
                    'prazo': {'type': 'string'},
                    'acusado': {'type': 'string'},
                    'acusador': {'type': 'string'}
                },
                'required': ['numero', 'prazo', 'acusado', 'acusador']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Sucesso',
            'examples': {
                'application/json': {"msg": "Processo cadastrado com sucesso"}
            }
        },
        '500': {
            'description': 'Error',
            'examples': {
                'application/json': {"msg": "Erro ao cadastrar processo"}
            }
        }
    }
})
def cadastrar_processo():
    return processo_service.cadastrar_processo_service()


#----------------------------------------//---------------------------------------------

@processo_bp.route('/buscar_todos_processos', methods=['GET'])
@swag_from({
    'tags': ['Processos'],
    'responses': {
        '200': {
            'description': 'Lista de todos os processos',
            'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Processo'}}}}
        }
    }
})
def buscar_processos():
    return processo_service.buscar_processos_service()


#----------------------------------------//---------------------------------------------


@processo_bp.route('/buscar_processo_por_id/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Processos'],
    'description': 'Endpoint para buscar processo pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do processo a ser buscado'
        }
    ],
    'responses': {
        '200': {
            'description': 'Sucesso',
            'content': {'application/json': {'schema': {'$ref': '#/definitions/Processo'}}}
        },
        '404': {
            'description': 'Processo não encontrado',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def buscar_processo_por_id(id):
    return processo_service.buscar_processo_por_id_service(id)


#----------------------------------------//---------------------------------------------


@processo_bp.route('/editar_processo/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Processos'],
    'description': 'Endpoint para editar um processo passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do processo a ser editado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Informações do processo a serem atualizadas',
            'schema': {
                'type': 'object',
                'properties': {
                    'numero': {'type': 'number'},
                    'prazo': {'type': 'string'},
                    'acusado': {'type': 'string'},
                    'acusador': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "processo editado com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '500': {
            'description': '"msg": "Erro ao editar processo"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def editar_processo(id):
    return processo_service.editar_processo_service(id)


#----------------------------------------//---------------------------------------------



@processo_bp.route('/deletar_processo/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Processos'],
    'description': 'Endpoint para deletar um processo passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do processo a ser excluído'
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Processo excluído com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '404': {
            'description': '"msg": "Processo não encontrado"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def excluir_processo(id):
    return processo_service.excluir_processo_service(id)






