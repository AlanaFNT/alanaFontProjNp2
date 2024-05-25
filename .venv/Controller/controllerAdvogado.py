from flask import Blueprint, Flask, jsonify, request
from DTO.dtoAdvogado import AdvogadoDTO
from Service.serviceAdvogado import AdvogadoService
from flasgger import Swagger, swag_from


app = Flask(__name__)
swagger = Swagger(app)
advogado_service = AdvogadoService()
advogado_bp = Blueprint('advogado_bp', __name__)



@advogado_bp.route('/cadastrar_advogados', methods=['POST'])
@swag_from({
    'tags': ['Advogados'],
    'description': 'Endpoint para cadastrar um novo advogado.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'especialidade': {'type': 'string'},
                    'escritorio': {'type': 'string'},
                    'salario': {'type': 'number', 'format': 'float'}
                },
                'required': ['nome', 'especialidade', 'escritorio', 'salario']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Sucesso',
            'examples': {
                'application/json': {"msg": "Advogado cadastrado com sucesso"}
            }
        },
        '500': {
            'description': 'Error',
            'examples': {
                'application/json': {"msg": "Erro ao cadastrar advogado"}
            }
        }
    }
})
def cadastrar_advogado():
    return advogado_service.cadastrar_advogado_service()


#----------------------------------------//---------------------------------------------

@advogado_bp.route('/buscar_todos_advogados', methods=['GET'])
@swag_from({
    'tags': ['Advogados'],
    'responses': {
        '200': {
            'description': 'Lista de todos os advogados',
            'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Advogado'}}}}
        }
    }
})
def buscar_advogados():
    return advogado_service.buscar_advogados_service()


#----------------------------------------//---------------------------------------------


@advogado_bp.route('/buscar_advogado_por_id/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Advogados'],
    'description': 'Endpoint para buscar advogado pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do advogado a ser buscado'
        }
    ],
    'responses': {
        '200': {
            'description': 'Sucesso',
            'content': {'application/json': {'schema': {'$ref': '#/definitions/Advogado'}}}
        },
        '404': {
            'description': 'Advogado não encontrado',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def buscar_advogado_por_id(id):
    return advogado_service.buscar_advogado_por_id_service(id)


#----------------------------------------//---------------------------------------------


@advogado_bp.route('/editar_advogado/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Advogados'],
    'description': 'Endpoint para editar um advogado passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do advogado a ser editado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Informações do advogado a serem atualizadas',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'especialidade': {'type': 'string'},
                    'escritorio': {'type': 'string'},
                    'salario': {'type': 'float', 'format': 'float'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "advogado editado com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '500': {
            'description': '"msg": "Erro ao editar advogado"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def editar_advogado(id):
    return advogado_service.editar_advogado_service(id)


#----------------------------------------//---------------------------------------------



@advogado_bp.route('/deletar_advogado/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Advogados'],
    'description': 'Endpoint para deletar um advogado passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do advogado a ser excluído'
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Advogado excluído com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '404': {
            'description': '"msg": "Advogado não encontrado"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def excluir_advogado(id):
    return advogado_service.excluir_advogado_service(id)






