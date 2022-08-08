from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__) # hace referencia al nombre del archivo: app

@app.route('/')
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio') #inicio nos lleva a la pag web
def show_home():
    return render_template('index.html') #le ponemos el nombre de nuestra pagina web

# API que recibe y retorna un json
@app.route('/<string:country>/<string:variety>/<float:aroma>/<float:aftertaste>/<float:acidity>/<float:body>/<float:balance>/<float:moisture>')
def result(country, variety, aroma, aftertaste, acidity, body, balance, moisture):
    cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture'] 
    # contenido de objeto pandas
    data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]
    # df
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
    # Cargamos modelo entrenado
    loaded_model = pickle.load(open('../models/coffee_model.pkl', 'rb')) # rb: read binary
    # Pasar los datos al modelo
    result = loaded_model.predict(posted) # devuelve archivo np, necesito llevarlo a texto
    text_result = result.tolist()[0]
    if text_result == 'Yes':
        return jsonify(message='Es un cafe de especialiad'), 200
    else:
        return jsonify(message='No es un cafe de especialidad'), 200 
    




# le decimos a Flask que corra
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) #lo hacemos en modalidad debug
