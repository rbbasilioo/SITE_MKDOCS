from flask import Flask, send_from_directory, redirect, url_for
import os

app = Flask(__name__, static_folder='site')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')
    #return redirect(url_for('serve_static', path='home/')) 
    ##caso do windowns por questoes de case-sensitive ou caminhos relativos podem dar conflitos.
    ## usar o redirect como na linha acima, lembrando de qual index.thml esta no caso deste projeto, está na /site/home/index.html
    ## Se sua home nao chamar home e qualquer outra coisa , por exemplo: index/index.html , informar o path='index/' que é o diretorio da primeira pagina onde está dentor do diretório site.

@app.route('/<path:path>.md')
def redirect_md(path):
    return redirect(url_for('serve_static', path=path + '/'))

@app.route('/<path:path>/')
@app.route('/<path:path>')
def serve_static(path):
    file_path = os.path.join(app.static_folder, path, 'index.html')
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, os.path.join(path, 'index.html'))
    else:
        # Tenta servir o arquivo diretamente se for um arquivo (ex: css, js)
        return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
    #debug=true -> se quiser ver problemas (colocar dentro o app.run)