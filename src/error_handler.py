from flask import jsonify

def registrar_errores(app):
    @app.errorhandler(404)
    def no_encontrado(e):
        return jsonify({"error": "Ruta no encontrada", "codigo": 404}), 404

    @app.errorhandler(500)
    def error_servidor(e):
        return jsonify({"error": "Error interno del servidor", "codigo": 500}), 500
