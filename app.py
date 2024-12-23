import webbrowser
from flask import Flask, render_template, request
import threading

app = Flask(__name__)

# Ruta principal de la pàgina
@app.route('/')
def index():
    return render_template('index.html')

# Ruta per verificar la resposta de la planta
@app.route('/verificar', methods=['POST'])
def verificar():
    resposta = request.form.get('planta').lower()  # Convertim la resposta a minúscules
    
    if resposta == 'potus':  # Canvia 'potus' per la resposta correcta
        return render_template('index.html', missatge="Correcte! La contrasenya del .rar es ABC123. ")
    else:
        return render_template('index.html', missatge="Incorrecte! Torna-ho a provar.")

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Obre el navegador en un fil separat per evitar bloquejar el servidor
    threading.Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)
