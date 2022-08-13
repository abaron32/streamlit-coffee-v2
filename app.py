from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__) # hace referencia al nombre del archivo: app

@app.route('/')
def hello_flask():
    return 'This is an API to predict if a coffee is specialty or not. In order to see the prediction you have to add the value of each of the 8 features in the route separated by "/". For example: /Other/Other/7.1/7.4/7.2/7.6/8.0/0.1'


# API que recibe y retorna un json con el pronostico, mandamos los datos con una forma economica que tiene Flask
@app.route('/<string:country>/<string:variety>/<float:aroma>/<float:aftertaste>/<float:acidity>/<float:body>/<float:balance>/<float:moisture>')
def result(country, variety, aroma, aftertaste, acidity, body, balance, moisture):
    cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture'] 
    # contenido de objeto pandas
    data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]
    # df
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
    # Cargamos modelo entrenado
    loaded_model = pickle.load(open('coffee_model.pkl', 'rb')) # rb: read binary
    # Pasar los datos al modelo
    result = loaded_model.predict(posted) # devuelve archivo np, necesito llevarlo a texto
    text_result = result.tolist()[0]
    if text_result == 'Yes':
        return jsonify(message='It is a specialty coffee.'), 200
    else:
        return jsonify(message='It is not a specialty coffee.'), 200 
    




# le decimos a Flask que corra
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) # debug=True para poder hacer tracing del problema
