from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return jsonify(message="Welcome to the home of EPL stats.")


if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True, port=5001)