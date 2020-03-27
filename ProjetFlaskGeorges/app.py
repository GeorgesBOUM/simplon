from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulaire():
    return render_template("formulaire.html")

@app.route('/', methods=['POST'])
def affichage():
    phrase ='Bonjour ' + request.form['civilite'] + ' ' + request.form['nom'] + ' ' + request.form['prenom']
    
    return render_template("page_cible.html", message=phrase)

if __name__ == '__main__':
    app.run()