
from dataclasses import dataclass
from typing import List

# ========= Estruturas de Dados =========

@dataclass
class Livro:
    codigo: str
    titulo: str
    autor: str
    ano: int
    genero: str
    quantidade_total: int
    quantidade_disponivel: int

@dataclass
class Usuario:
    id: int
    nome: str
    tipo: str

@dataclass
class Emprestimo:
    livro_id: str
    usuario_id: int
    data_emprestimo: int
    data_devolucao_prevista: int
    data_devolucao_real: int = None
    status: str = "ativo"

# ========= Variáveis Globais =========

livros: List[Livro] = []
usuarios: List[Usuario] = []
emprestimos: List[Emprestimo] = []
dia_atual = 1
valor_multa_por_dia = 1.0

# ========= Funções do Sistema =========

def menu_principal():
    global dia_atual
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Usuários")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Relatórios")
        print("6. Gerenciar Tempo")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerenciar_livros()
        elif opcao == "2":
            gerenciar_usuarios()
        elif opcao == "3":
            realizar_emprestimo()
        elif opcao == "4":
            realizar_devolucao()
        elif opcao == "5":
            exibir_relatorios()
        elif opcao == "6":
            dia_atual = menu_gerenciar_tempo(dia_atual)
        elif opcao == "7":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

def cadastrar_livro():
    codigo = input("Código do livro (único): ").strip()
    if any(livro.codigo == codigo for livro in livros):
        print("Código já cadastrado!")
        return
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    try:
        ano = int(input("Ano de Publicação: "))
        genero = input("Gênero: ").strip()
        quantidade_total = int(input("Quantidade Total de Exemplares: "))
    except ValueError:
        print("Entrada inválida.")
        return
    novo_livro = Livro(codigo, titulo, autor, ano, genero, quantidade_total, quantidade_total)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"\nCódigo: {livro.codigo}")
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Ano: {livro.ano}")
        print(f"Gênero: {livro.genero}")
        print(f"Total: {livro.quantidade_total}")
        print(f"Disponível: {livro.quantidade_disponivel}")

def buscar_livro():
    termo = input("Digite o código, título ou autor para buscar: ").lower().strip()
    encontrados = [l for l in livros if termo in l.codigo.lower() or termo in l.titulo.lower() or termo in l.autor.lower()]
    if not encontrados:
        print("Nenhum livro encontrado.")
        return
    for livro in encontrados:
        print(f"\nCódigo: {livro.codigo}")
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Ano: {livro.ano}")
        print(f"Gênero: {livro.genero}")
        print(f"Total: {livro.quantidade_total}")
        print(f"Disponível: {livro.quantidade_disponivel}")

def gerenciar_livros():
    while True:
        print("\n--- Gerenciar Livros ---")
        print("1. Cadastrar Novo Livro")
        print("2. Listar Todos os Livros")
        print("3. Buscar Livro")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cadastrar_livro()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            buscar_livro()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")

def cadastrar_usuario():
    try:
        id_usuario = int(input("ID do Usuário (único): "))
        if any(u.id == id_usuario for u in usuarios):
            print("ID já cadastrado!")
            return
    except ValueError:
        print("ID inválido.")
        return
    nome = input("Nome: ").strip()
    tipo = input("Tipo (aluno ou professor): ").strip().lower()
    if tipo not in ["aluno", "professor"]:
        print("Tipo inválido.")
        return
    usuarios.append(Usuario(id_usuario, nome, tipo))
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for u in usuarios:
        print(f"\nID: {u.id}")
        print(f"Nome: {u.nome}")
        print(f"Tipo: {u.tipo}")

def gerenciar_usuarios():
    while True:
        print("\n--- Gerenciar Usuários ---")
        print("1. Cadastrar Novo Usuário")
        print("2. Listar Todos os Usuários")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")

def realizar_emprestimo():
    """
    Realiza o empréstimo de um livro, definindo o prazo conforme tipo do usuário
    e registrando o dia de devolução prevista.
    """
    global dia_atual
    try:
        usuario_id = int(input("ID do Usuário: "))
    except ValueError:
        print("ID inválido.")
        return
    codigo_livro = input("Código do Livro: ").strip()

    usuario = next((u for u in usuarios if u.id == usuario_id), None)
    livro = next((l for l in livros if l.codigo == codigo_livro), None)

    if not usuario:
        print("Usuário não encontrado.")
        return
    if not livro:
        print("Livro não encontrado.")
        return
    if livro.quantidade_disponivel <= 0:
        print("Livro indisponível.")
        return

    ja_emprestado = any(
        e.livro_id == codigo_livro and e.usuario_id == usuario_id and e.status == "ativo"
        for e in emprestimos
    )
    if ja_emprestado:
        print("Este usuário já possui um empréstimo ativo deste livro.")
        return

    prazo = 7 if usuario.tipo == "aluno" else 10
    emprestimos.append(Emprestimo(
        livro_id=codigo_livro,
        usuario_id=usuario_id,
        data_emprestimo=dia_atual,
        data_devolucao_prevista=dia_atual + prazo
    ))
    livro.quantidade_disponivel -= 1
    print(f"Empréstimo realizado com sucesso! Devolução até o dia {dia_atual + prazo}.")

def realizar_devolucao():
    global dia_atual
    try:
        usuario_id = int(input("ID do Usuário: "))
    except ValueError:
        print("ID inválido.")
        return
    codigo_livro = input("Código do Livro: ").strip()
    emprestimo = next(
        (e for e in emprestimos if e.usuario_id == usuario_id and e.livro_id == codigo_livro and e.status == "ativo"), None)
    if not emprestimo:
        print("Empréstimo não encontrado.")
        return
    emprestimo.data_devolucao_real = dia_atual
    emprestimo.status = "devolvido"
    livro = next((l for l in livros if l.codigo == codigo_livro), None)
    if livro:
        livro.quantidade_disponivel += 1
    atraso = dia_atual - emprestimo.data_devolucao_prevista
    if atraso > 0:
        multa = atraso * valor_multa_por_dia
        print(f"Multa por atraso: R${multa:.2f}")
    else:
        print("Devolução dentro do prazo.")
    print("Devolução registrada com sucesso.")

def exibir_relatorios():
    while True:
        print("\n--- Relatórios ---")
        print("1. Livros Emprestados Atualmente")
        print("2. Livros com Devolução em Atraso")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            relatorio_emprestimos_ativos()
        elif opcao == "2":
            relatorio_emprestimos_atrasados()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def relatorio_emprestimos_ativos():
    ativos = [e for e in emprestimos if e.status == "ativo"]
    if not ativos:
        print("Nenhum empréstimo ativo.")
        return
    for e in ativos:
        u = next((u for u in usuarios if u.id == e.usuario_id), None)
        l = next((l for l in livros if l.codigo == e.livro_id), None)
        if u and l:
            print(f"Livro: {l.titulo} | Usuário: {u.nome} | Devolução até: {e.data_devolucao_prevista}")

def relatorio_emprestimos_atrasados():
    atrasados = [e for e in emprestimos if e.status == "ativo" and e.data_devolucao_prevista < dia_atual]
    if not atrasados:
        print("Nenhum empréstimo em atraso.")
        return
    for e in atrasados:
        u = next((u for u in usuarios if u.id == e.usuario_id), None)
        l = next((l for l in livros if l.codigo == e.livro_id), None)
        if u and l:
            atraso = dia_atual - e.data_devolucao_prevista
            print(f"Livro: {l.titulo} | Usuário: {u.nome} | Atraso: {atraso} dia(s)")

def menu_gerenciar_tempo(dia_sistema_atual_param):
    while True:
        print("\n--- Gerenciar Tempo ---")
        print(f"Dia Atual do Sistema: {dia_sistema_atual_param}")
        print("1. Avançar 1 dia")
        print("2. Avançar 7 dias (1 semana)")
        print("3. Avançar N dias")
        print("4. Consultar dia atual")
        print("5. Voltar ao Menu Principal")
        opcao_tempo = input("Escolha uma opção: ")
        if opcao_tempo == '1':
            dia_sistema_atual_param += 1
            print(f"Sistema avançou para o dia: {dia_sistema_atual_param}")
        elif opcao_tempo == '2':
            dia_sistema_atual_param += 7
            print(f"Sistema avançou 7 dias. Novo dia: {dia_sistema_atual_param}")
        elif opcao_tempo == '3':
            try:
                n_dias = int(input("Quantos dias deseja avançar? "))
                if n_dias > 0:
                    dia_sistema_atual_param += n_dias
                    print(f"Sistema avançou {n_dias} dias. Novo dia: {dia_sistema_atual_param}")
                else:
                    print("Por favor, insira um número maior que zero.")
            except ValueError:
                print("Entrada inválida.")
        elif opcao_tempo == '4':
            print(f"O dia atual do sistema é: {dia_sistema_atual_param}")
        elif opcao_tempo == '5':
            print("Retornando ao Menu Principal...")
            break
        else:
            print("Opção inválida.")
        return dia_sistema_atual_param

# ========= Execução =========
if __name__ == "__main__":
    menu_principal()
