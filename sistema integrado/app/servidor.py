from configuracoes import *
from modelos import Personagem

@app.route("/")
def index():
    return 'Sistema de cadastro de personagens. ' + '<a href="/listar_personagens">Operação Listar</a>'

@app.route("/listar_personagens")
def listar_personagens():
    personagens = db.session.query(Personagem).all()
    return render_template("listar_personagens.html", listagem=personagens)

@app.route("/incluir_personagem", methods=['post'])
def incluir_personagem():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        p = Personagem(**dados)
        db.session.add(p)
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes":str(e)})
        resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True, port=5000)