from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/')
def display_results():
    with open('results.json', 'r') as json_file:
        results = json.load(json_file)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
