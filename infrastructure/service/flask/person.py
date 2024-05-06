from flask import Flask, jsonify, request

app = Flask()

@app.route("/")
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)
