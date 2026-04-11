from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "mensaje": "Microservicio funcionando"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0", "servicio": "mi-microservicio"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
