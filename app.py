from flask import Flask, jsonify
import random

app = Flask(__name__)

counter = 0

@app.route('/random')
def rnd():
    global counter
    counter += 1

    return jsonify({
        "number": random.randint(0, 65535)
    })

@app.route("/metrics")
def metrics():
    return jsonify({
        "count": counter
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
