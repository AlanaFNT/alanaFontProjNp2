from flask import Blueprint, Flask, jsonify, request
from DTO.dtoDefensor import DefensorDTO
from Service.serviceDefensor import DefensorService
from flasgger import Swagger, swag_from


app = Flask(__name__)
swagger = Swagger(app)
defensor_service = DefensorService()
defensor_bp = Blueprint('defensor_bp', __name__)



@defensor_bp.route('/cadastrar_defensores', methods=['POST'])
@swag_from({
    'tags': ['Defensores'],
    'description': 'Endpoint para cadastrar um novo defensor.',
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
                    'vara': {'type': 'string'},
                    'salario': {'type': 'number', 'format': 'float'}
                },
                'required': ['nome', 'especialidade', 'vara', 'salario']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Sucesso',
            'examples': {
                'application/json': {"msg": "Defensor cadastrado com sucesso"}
            }
        },
        '500': {
            'description': 'Error',
            'examples': {
                'application/json': {"msg": "Erro ao cadastrar defensor"}
            }
        }
    }
})
def cadastrar_defensor():
    return defensor_service.cadastrar_defensor_service()


#----------------------------------------//---------------------------------------------

@defensor_bp.route('/buscar_todos_defensores', methods=['GET'])
@swag_from({
    'tags': ['Defensores'],
    'responses': {
        '200': {
            'description': 'Lista de todos os defensores',
            'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Defensor'}}}}
        }
    }
})
def buscar_defensores():
    return defensor_service.buscar_defensores_service()


#----------------------------------------//---------------------------------------------


@defensor_bp.route('/buscar_defensor_por_id/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Defensores'],
    'description': 'Endpoint para buscar defensor pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do defensor a ser buscado'
        }
    ],
    'responses': {
        '200': {
            'description': 'Sucesso',
            'content': {'application/json': {'schema': {'$ref': '#/definitions/Defensor'}}}
        },
        '404': {
            'description': 'Defensor não encontrado',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def buscar_defensor_por_id(id):
    return defensor_service.buscar_defensor_por_id_service(id)


#----------------------------------------//---------------------------------------------


@defensor_bp.route('/editar_defensor/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Defensores'],
    'description': 'Endpoint para editar um defensor passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do defensor a ser editado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Informações do defensor a serem atualizadas',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'especialidade': {'type': 'string'},
                    'vara': {'type': 'string'},
                    'salario': {'type': 'float', 'format': 'float'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "defensor editado com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '500': {
            'description': '"msg": "Erro ao editar defensor"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def editar_defensor(id):
    return defensor_service.editar_defensor_service(id)


#----------------------------------------//---------------------------------------------



@defensor_bp.route('/deletar_defensor/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Defensores'],
    'description': 'Endpoint para deletar um defensor passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do defensor a ser excluído'
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Defensores excluído com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '404': {
            'description': '"msg": "Defensor não encontrado"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def excluir_defensor(id):
    return defensor_service.excluir_defensor_service(id)






