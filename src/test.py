import pickle
import pandas as pd
import numpy as np

# Contenido ficticio para poner en el model
# Modelo recibe 8 variables

country='Other'
variety='Other'
aroma = 7.42
aftertaste = 7.33
acidity = 7.42
body=7.25
balance=7.33
moisture=8.0


# Usamos un pipeline entonces tenemos que ponerlo en un df

# cabecera de objeto pandas
cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture'] 

# contenido de objeto pandas
data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]

# df
posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
#print(posted)


# Cargamos modelo entrenado

loaded_model = pickle.load(open('../models/coffee_model.pkl', 'rb')) # rb: read binary


# Pasar los datos al modelo

result = loaded_model.predict(posted) # devuelve archivo np, necesito llevarlo a texto

text_result = result.tolist(result)[0]

print(text_result)
