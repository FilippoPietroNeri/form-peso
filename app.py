from flask import Flask, request, render_template
app = Flask(__name__)

def imc(peso,altezza):
    return peso/(altezza**2)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def homeGet():
    return render_template('form.html')

@app.route('/data', methods=['GET'])
def data():
    altezza = float(request.args.get('altezza'))
    peso = float(request.args.get('peso'))
    calcImc = imc(peso,altezza)
    return render_template('riepilogo.html', altezza=altezza, peso=peso, imc=calcImc)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)