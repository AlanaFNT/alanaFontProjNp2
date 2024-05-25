from flask import Flask
from flasgger import Swagger
from Controller.controllerAdvogado import advogado_bp
from Controller.controllerDefensor import defensor_bp
from Controller.controllerProcesso import processo_bp



app = Flask(__name__)
swagger = Swagger(app)

# Registra os blueprints
app.register_blueprint(advogado_bp, url_prefix='/advogado')
app.register_blueprint(defensor_bp, url_prefix='/defensor')
app.register_blueprint(processo_bp, url_prefix='/processo')




if __name__ == '__main__':
    app.run(debug=True)

