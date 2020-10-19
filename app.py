from flask import Flask


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return '<h1>Pagina Flask en Heroku</h1>'



if __name__ == '__main__':
    app.run(debug=True)