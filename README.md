# Sistema de Registro e Login de Usuários

Este é um projeto de sistema de contas desenvolvido em Python, utilizando um banco de dados local baseado em um arquivo JSON. O sistema permite o registro e login de usuários, garantindo a segurança dos dados e mantendo um backup das credenciais antes de cada alteração.

## Funcionalidades
- **Registro de Usuário**:
  - O usuário fornece seu e-mail e digita sua senha duas vezes para confirmação.
  - O sistema verifica se o e-mail já está cadastrado.
  - Caso o e-mail ainda não esteja registrado, ele é armazenado no banco de dados local (arquivo JSON).
  - Antes de salvar os novos dados, um backup do banco de dados é criado para evitar a perda de informações.

- **Login de Usuário**:
  - O sistema verifica as credenciais inseridas comparando-as com o banco de dados local.
  - Se os dados forem válidos, o login é realizado com sucesso.
  - Caso haja erro nas credenciais, o sistema solicita a correção e verifica novamente.

- **Carregar Credenciais**:
  - O sistema possui um algoritmo que abre o banco de dados JSON e exibe todas as credenciais registradas diretamente no terminal.

## Tecnologias Utilizadas
- Python
- Arquivo JSON para armazenamento de credenciais
