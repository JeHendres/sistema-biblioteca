# 📚 Sistema de Gerenciamento de Biblioteca

Projeto desenvolvido para a disciplina de **Lógica de Programação**, com foco em modularização, simulação de tempo e controle de empréstimos com regras específicas para alunos e professores.

## 🔧 Funcionalidades

- Cadastro de livros com controle de exemplares disponíveis
- Cadastro de usuários (aluno ou professor)
- Empréstimos com prazos diferenciados:
  - Alunos: 7 dias
  - Professores: 10 dias
- Devolução com cálculo de multa por atraso (R$1,00 por dia)
- Relatórios de empréstimos ativos e em atraso
- Simulação da passagem do tempo no sistema

## 🧱 Estrutura do Código

- `@dataclass` para representar `Livro`, `Usuario` e `Emprestimo`
- Variáveis globais para controle de tempo (`dia_atual`) e dados da biblioteca
- Funções modulares para cada funcionalidade
- Menu principal com navegação interativa

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/JeHendres/sistema-biblioteca.git
   cd sistema-biblioteca
   ```

2. Execute o programa:
   ```bash
   python Biblioteca_codigo.py
   ```

3. Siga o menu interativo para cadastrar, emprestar, devolver livros e simular o tempo.

## 📌 Exemplo de Fluxo de Uso

1. Cadastre um livro e um usuário.
2. Realize um empréstimo.
3. Avance o tempo (via menu “Gerenciar Tempo”).
4. Faça a devolução e veja a multa (se houver atraso).
5. Use os relatórios para verificar empréstimos ativos ou atrasados.

## 🗂️ Organização dos Arquivos

- `Biblioteca_codigo.py`: Código-fonte principal do sistema
- `README.md`: Este arquivo explicativo
- `Apresentacao_Sistema_Biblioteca.pdf`: Roteiro da apresentação oral (opcional)

## 📖 Apresentação Oral

Este projeto acompanha uma apresentação que explica:

- Estrutura geral do código
- Organização dos dados com dataclasses
- Principais funções e fluxo do sistema
- Demonstração prática com avanço de dias
- Tratamento de multas e relatórios

## 📎 Autor

Jeronimo Hendres — Projeto final da disciplina de **Lógica de Programação**
