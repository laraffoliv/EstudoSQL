import sqlite3

def create_database(db_path, sql_file):
    """Cria um banco de dados SQLite e as tabelas a partir de um arquivo SQL."""
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # # Lê as instruções SQL do arquivo
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_commands = f.read()
        # Executa as instruções SQL
        cursor.executescript(sql_commands)

        # Commit para salvar as alterações
        conn.commit()
        print("Banco de dados e tabelas criados com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar banco de dados: {e}")
    finally:
        # Fecha a conexão
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    # Caminho para o arquivo do banco de dados e o arquivo SQL
    database_path = 'C:\\Users\\larao\\OneDrive - Universidade Federal de Minas Gerais\\ibd\\database.db'
    sql_file = 'C:\\Users\\larao\\OneDrive - Universidade Federal de Minas Gerais\\ibd\\database.sql'
    
    # Cria o banco de dados e as tabelas
    create_database(database_path, sql_file)
