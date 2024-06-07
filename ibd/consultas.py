import sqlite3

# Caminho para o arquivo do banco de dados
database_path = 'database.db'

def connect_to_db(db_path):
    """Conecta ao banco de dados SQLite."""
    try:
        conn = sqlite3.connect(db_path)
        print(f"Conexão bem-sucedida ao banco de dados: {db_path}")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def fetch_results(conn, query):
    """Busca e retorna os resultados de uma consulta."""
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()  # Retorna apenas uma linha, já que estamos interessados apenas no total
        return result[0]  # Retorna o valor da primeira coluna (total)
    except sqlite3.Error as e:
        print(f"Erro ao buscar os resultados: {e}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    conn = connect_to_db(database_path)
    
    if conn:
        # Consulta SQL
        consulta_sql = """
       SELECT 
    SUM(
        CASE WHEN QTD_JAN IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN QTD_FEV IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN QTD_MAR IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN QTD_ABR IS NOT NULL THEN 1 ELSE 0 END
    ) AS total
FROM 
    DENGUE_MUNICIPIO;
        """

        # Executar a consulta
        total = fetch_results(conn, consulta_sql)
        if total is not None:
            print("Total Final:", total)
        else:
            print("Nenhum resultado encontrado.")

        # Fechar a conexão
        conn.close()
