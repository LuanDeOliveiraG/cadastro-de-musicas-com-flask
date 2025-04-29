from flask import render_template, request, redirect, url_for
from projetos import app

musicas = ['Bye bye bye']
cantor= ['Nsync']


@app.route('/')
def home():
    return render_template('cadastro.html')

@app.route('/adicionar', methods = ["POST", "GET"])
def adicionar():

    nome = request.form.get('txtMusica')
    cant = request.form.get('Cantor')
    musicas.append(nome)
    cantor.append(cant)

    return redirect('/nomes')

@app.route('/nomes')
def listar():
    
    lista= zip(musicas,cantor)
    return render_template('nomes.html',
    lista = lista)
