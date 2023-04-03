from flask import Flask, render_template
app = Flask(__name__, static_folder='static')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('Projetos.html')

@app.route('/oficinas')
def oficinas():
    return render_template('oficinas.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/jogos')
def jogos():
    return render_template('jogos.html')

if __name__ == '__main__':
    app.run(debug=True)