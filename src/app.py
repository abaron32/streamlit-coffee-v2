from flask import Flask, render_template, jsonify, request

app = Flask(__name__) # hace referencia al nombre del archivo: app

@app.route('/')
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio') #inicio nos lleva a la pag web
def show_home():
    return render_template('index.html') #le ponemos el nombre de nuestra pagina web

@app.route('/url_variables/<string:name>/<int:age>') #le pasamos parametros a la url
def url_variables(name, age):
    if age<18:
        return jsonify(message = 'Lo siento ' + name + ' no estas autorizado'), 401 # 401 es el error
    else:
        return jsonify(message = 'Bienvenida ' + name), 200 # por default ya viene 200, no es necesario ponerlo



# le decimos a Flask que corra
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) #lo hacemos en modalidad debug
