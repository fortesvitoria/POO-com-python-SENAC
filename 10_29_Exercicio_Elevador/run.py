from componentes.elevador import *
from flask import Flask, render_template, request

# def main():
#         elevador = Elevador() #cria uma instancia 
#         print(elevador.get_andar())
#         print(elevador.locomover(4))
#         print(elevador.get_andar())
#         print(elevador.locomover(15))

# # Programa principal
# if __name__ == "__main__":
#     main()

# 1 Inicia flask
app = Flask(__name__, static_folder='static')
# 1.2 Chave secreta necessária para inicar sessao
app.secret_key = 'secret-key-guesss'

# 2 Cria instancia do elevador
elevador = Elevador()

# 3. Rota para elevador
@app.route('/', methods=['GET', 'POST'])
def index():
    #incia com mensagem informando que está no térreo
    mensagem = ''

    # 3.1 Se houver envio de formulario (clique no botao)
    if request.method == 'POST':
        # 3.1.1 Pega o andar do destino value=""
        destino = request.form['destino']
        # 3.1.2 Chama a logica da classe Elevador
        mensagem = elevador.locomover(destino)
    # 3.2 Pega o andar atual
    andar_atual = elevador.get_andar()
    # 3.3 Renderiza(atualiza) a página com a mensagem e o andar atual
    return render_template('interface_elevador.html', mensagem=mensagem, andar_atual=andar_atual)

# 4. Inicia aplicação
# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)


