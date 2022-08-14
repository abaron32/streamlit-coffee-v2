import streamlit as st
import pickle
import pandas as pd
import numpy as np



st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
st.title('Specialty coffee prediction')
st.sidebar.title('Select the parameters to analyze if you have a specialty coffee')


country = st.sidebar.selectbox(
    'Select a country',['Other', 'Colombia', 'Brazil', 'Guatemala', 'Mexico', 'Taiwan']
)

variety = st.sidebar.selectbox(
    'Select a variety',['Bourbon', 'Catuai', 'Caturra', 'Other', 'Typica']
)

aroma = st.sidebar.slider("Choose aroma: ", min_value=5.0,   
                       max_value=9.0, value=7.0, step=0.01)

aftertaste = st.sidebar.slider("Choose aftertaste: ", min_value=5.0,   
                       max_value=9.0, value=7.0, step=0.01)

acidity = st.sidebar.slider("Choose acidity: ", min_value=5.0,   
                       max_value=9.0, value=7.0, step=0.01)

body = st.sidebar.slider("Choose body: ", min_value=5.0,   
                       max_value=9.0, value=7.0, step=0.01)

balance = st.sidebar.slider("Choose balance: ", min_value=5.0,   
                       max_value=9.0, value=7.0, step=0.01)

moisture = st.sidebar.slider("Choose moisture: ", min_value=0.0,   
                       max_value=1.0, value=0.5, step=0.01)





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
    respuesta='You have a specialty coffee.'
else:
    respuesta='You do not have a specialty coffee.'


# Respuesta en la app
st.code(respuesta)