from flask import Flask, request, make_response
# from flask_cors import CORS
import pymysql

app = Flask(__name__)
# CORS(app)

@app.route('/messages', methods=['POST'])
def add_message():
    nome = request.form['nome']
    mensagem = request.form['mensagem']
    
    conn = pymysql.connect(
        host='mysql-connection',
        user='root',
        password='Senha123',
        database='meubanco'
    )

    cursor = conn.cursor()

    cursor.execute("INSERT INTO mensagens(nome, mensagem) VALUES (%s, %s)", (nome, mensagem))
    conn.commit()

    cursor.close()
    conn.close()

    response = make_response("Mensagem adicionada com sucesso!")
    return response

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)