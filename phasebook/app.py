from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    if data.get('department') is None:
        print("something")
    response = {
        'message': 'Data received!',
        'data': data
    }
    return jsonify(response)


@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True)


