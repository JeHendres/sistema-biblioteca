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

## 1. Estrutura Geral do Programa

Aqui explicamos como o sistema foi organizado para manter clareza e modularidade.

![Estrutura do código](https://github.com/user-attachments/assets/35cc60b2-a6dc-452d-8875-48ea41166fce)

## 2. Organização dos Dados com Dataclasses

Mostramos as dataclasses para Livro, Usuário e Empréstimo, explicando o porquê dessa escolha.

![Utilização de Dataclass](https://github.com/user-attachments/assets/c9493977-05a0-4ab2-a6d7-242dbe9504cf)

## 3. Principais Funções do Sistema

Explicação das funções-chave, como o menu principal, empréstimo, devolução, gerenciamento de tempo e relatórios.

### Exemplo: Função `realizar_emprestimo()`

![Exemplo da funcionalidade emp](https://github.com/user-attachments/assets/268a05c6-643b-40b7-89b3-f2ba962a4c65)

## 4. Lógica de Empréstimo

Detalhamento do funcionamento do empréstimo, incluindo prazos diferentes para alunos e professores.

![Lógica do Empréstimo](https://github.com/user-attachments/assets/724a861a-ac5d-42e3-a20f-2bf6b0fa995b)

## 5. Funcionalidade de Devolução e Cálculo de Multas

Explicação sobre o registro da devolução e como as multas são calculadas com base no sistema de tempo simulado.

![Lógica de Devolução](https://github.com/user-attachments/assets/7e764925-6882-4ddf-b357-9d8460485b32)

## 6. Menu de Gerenciamento de Tempo

Demonstração do menu que permite avançar dias para simular atrasos e testar multas.

![Gerenciamento de tempo](https://github.com/user-attachments/assets/4656fc39-b3a2-4714-b111-b501f272bcdd)

## 7. Demonstração do Sistema em Funcionamento:

Sugestão de fluxo para apresentar o sistema funcionando:

1. Cadastro de usuário e livro  
2. Empréstimo  
3. Avanço de dias  
4. Devolução e multa (se houver)  
5. Relatórios

---

## 8. Desafios Enfrentados e Soluções:

- Desafio: aplicar prazos e multas automaticamente. 
Solução: regras definidas por tipo de usuário e controle de datas. 
- Desafio: manter o código limpo e organizado. 
Solução: uso de dataclasses, modularização e listas bem gerenciadas

---

## 📎 Autor

Jeronimo Hendres — Projeto final da disciplina de **Lógica de Programação**
