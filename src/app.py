from flask import Flask

app = Flask(__name__) # hace referencia al nombre del archivo: app

@app.route('/')
def hello_flask():
    return 'Hello Flask'

# le decimos a Flask que corra
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) #lo hacemos en modalidad debug
