import os
import mysql.connector
from datetime import datetime

# Configurações do banco de dados
DB_USER = "root"  # Substitua pelo seu usuário MySQL
DB_PASSWORD = "Phrh@5020"  # Substitua pela sua senha
DB_NAME = "bancoponto"  # Substitua pelo nome do banco de dados
HOST = "10.1.1.186"  # Ou o IP/host do servidor MySQL
BACKUP_DIR = "C:\\Users\\Dev\\Desktop\\backups"  # Diretório para salvar o backup

def execute_backup():
    try:
        # Verifica se o diretório de backups existe e cria se necessário
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        
        # Cria a conexão com o banco de dados
        connection = mysql.connector.connect(
            host=HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        
        # Arquivo de saída
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{timestamp}.sql")

        with open(backup_file, "w", encoding="utf-8") as f:
            # Backup da estrutura e dos dados
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()

            for table_info in tables:
                table_name = table_info[0]
                
                # Dump da estrutura da tabela
                cursor.execute(f"SHOW CREATE TABLE {table_name};")
                create_table_query = cursor.fetchone()[1]
                f.write(f"-- Estrutura da tabela `{table_name}`\n")
                f.write(f"{create_table_query};\n\n")

                # Dump dos dados da tabela
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                if rows:
                    f.write(f"-- Dados da tabela `{table_name}`\n")
                    for row in rows:
                        escaped_values = [
                            f"'{str(value).replace('\'', '\\\'')}'" if value is not None else "NULL"
                            for value in row
                        ]
                        insert_query = f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES ({', '.join(escaped_values)});"
                        f.write(insert_query + "\n")
                f.write("\n\n")
        
        print(f"Backup concluído com sucesso: {backup_file}")

    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao MySQL ou ao executar o backup: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    execute_backup()