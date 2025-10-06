# main.py

# 1. Importações Essenciais do Flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
from Core.sistema import SistemaLocker
from Models.cls_usuario import Administrador

# 2. Inicialização da Aplicação
app = Flask(__name__)
app.secret_key = 'chave-secreta'

# 3. Instância Única do Sistema
sistema = SistemaLocker() #cria uma instancia sistema locker, que gerencia toda logica do programa

# 4. Rota Principal: Página de Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_id = request.form['login']
        senha = request.form['senha']

        usuario_logado = sistema.fazer_login(usuario_id, senha)

        if usuario_logado:
            session['usuario_id'] = usuario_logado.id
            flash('Login realizado com sucesso!', 'success')

            if isinstance(usuario_logado, Administrador):
                return redirect(url_for('menu_adm'))
            else:
                return redirect(url_for('menu_usuario'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')

    return render_template('index.html')

# 5. Rota de Registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        usuario_id = request.form['login']
        senha = request.form['senha']

        if sistema.cadastrar_usuario(nome, usuario_id, senha):
            flash('Usuário cadastrado com sucesso! Faça o login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('ID de usuário já existe. Tente outro.', 'danger')
            return redirect(url_for('registro'))

    return render_template('registro.html')

# 6. Rota de Logout
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('login'))

# 7. Rota do Menu do Usuário
@app.route('/menu_usuario')
def menu_usuario():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    usuario_id = session['usuario_id']
    usuario = sistema.usuarios.get(usuario_id)

    return render_template('menu_usuario.html', usuario=usuario, lockers=sistema.lockers.values())

# 8. Rota para Reservar Locker
@app.route('/reservar_locker', methods=['POST'])
def reservar_locker():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    locker_id = request.form['id-reserva'].upper()
    usuario = sistema.usuarios.get(session['usuario_id'])

    if sistema.reservar_locker(usuario, locker_id):
        flash(f'Locker {locker_id} reservado com sucesso!', 'success')
    else:
        flash(f'Não foi possível reservar o locker {locker_id}. Verifique se ele está disponível ou se você já possui uma reserva.', 'danger')

    return redirect(url_for('menu_usuario'))


# 9. Rota para Liberar Locker
@app.route('/liberar_locker', methods=['POST'])
def liberar_locker():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    usuario = sistema.usuarios.get(session['usuario_id'])

    if sistema.liberar_locker(usuario):
        flash('Locker liberado com sucesso!', 'success')
    else:
        flash('Você não possui um locker para liberar.', 'danger')

    return redirect(url_for('menu_usuario'))


# 10. Rota do Menu do Administrador
@app.route('/menu_adm')
def menu_adm():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    usuario = sistema.usuarios.get(session['usuario_id'])
    if not isinstance(usuario, Administrador):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('menu_usuario'))

    return render_template('menu_adm.html', admin=usuario, lockers=sistema.lockers)

# 11. Rotas para Ações do Administrador
@app.route('/add_locker', methods=['POST'])
def add_locker():
    if 'usuario_id' not in session: return redirect(url_for('login'))

    locker_id = request.form['id'].upper()
    tamanho = request.form['tamanho'].upper()
    
    if sistema.adicionar_locker(locker_id, tamanho):
        flash(f'Locker {locker_id} adicionado com sucesso!', 'success')
    else:
        flash('Erro ao adicionar locker. Verifique os dados.', 'danger')
    return redirect(url_for('menu_adm'))

@app.route('/remove_locker', methods=['POST'])
def remove_locker():
    if 'usuario_id' not in session: return redirect(url_for('login'))

    locker_id = request.form['id-remove'].upper()
    
    if sistema.remover_locker(locker_id):
        flash(f'Locker {locker_id} removido com sucesso!', 'success')
    else:
        flash(f'Erro ao remover o locker {locker_id}. Verifique se ele não está ocupado.', 'danger')
    return redirect(url_for('menu_adm'))


@app.route('/manutencao_locker', methods=['POST'])
def manutencao_locker():
    if 'usuario_id' not in session: return redirect(url_for('login'))

    locker_id = request.form['id-manutencao'].upper()
    
    if sistema.colocar_em_manutencao(locker_id):
        flash(f'Locker {locker_id} colocado em manutenção.', 'info')
    else:
        flash(f'Erro ao colocar locker {locker_id} em manutenção.', 'danger')
    return redirect(url_for('menu_adm'))

@app.route('/tirar_de_manutencao', methods=['POST'])
def tirar_de_manutencao():
    if 'usuario_id' not in session: 
        return redirect(url_for('login'))

    locker_id = request.form['id-disponivel'].upper()
    
    if sistema.tirar_de_manutencao(locker_id):
        flash(f'Locker {locker_id} agora está disponível!', 'success')
    else:
        flash(f'Erro: Verifique se o ID do locker está correto e se ele está em manutenção.', 'danger')
    
    return redirect(url_for('menu_adm'))


# 12. Ponto de Entrada da Aplicação
if __name__ == "__main__":
    app.run(debug=True)