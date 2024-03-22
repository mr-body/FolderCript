import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('database/cripeel.db')

def cadastrar(folder_path, description, senha):
    try:
        comando = conn.cursor()

        # Insere os dados na tabela
        comando.execute("INSERT INTO dados (folder_path, description, senha) VALUES (?, ?, ?)",
                  (folder_path, description, senha))

        # Confirma a transação e fecha a conexão com o banco de dados
        conn.commit()
        conn.close()
        return True  # Retorna True se o cadastro foi realizado com sucesso
    except:
        conn.rollback()  # Desfaz a transação em caso de erro
        conn.close()
        return False  # Retorna False se o cadastro falhou

def Historic():
    try:
        comando = conn.cursor()

        # Executa a consulta SQL para selecionar todos os dados da tabela
        comando.execute("SELECT * FROM dados")

        # Recupera os resultados da consulta
        dados = comando.fetchall()

        # Fecha a conexão com o banco de dados
        conn.close()

        return dados  # Retorna os dados selecionados como uma lista de tuplas
    except:
        conn.close()
        raise Exception("Falha ao selecionar dados do banco de dados")  # Levanta uma exceção em caso de erro