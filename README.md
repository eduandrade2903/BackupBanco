# BackupBanco

## Descrição
O **BackupBanco** é um utilitário desenvolvido em Python para ajudar na criação de backups de bancos de dados MySQL. Ele exporta tanto a estrutura das tabelas quanto os dados em formato SQL, facilitando a recuperação em caso de incidentes ou necessidade de migração.

## Funcionalidades
- Conexão automática com o banco de dados MySQL.
- Exportação da estrutura das tabelas.
- Exportação dos dados de cada tabela.
- Criação de arquivos de backup com data e hora no nome para organização.

## Requisitos
- Python 3.x
- Bibliotecas necessárias:
  - `mysql-connector`
  - `os`
  - `datetime`

## Configuração
1. Clone este repositório:
    ```bash
    git clone https://github.com/eduandrade2903/BackupBanco.git
    cd BackupBanco
    ```

2. Instale as dependências:
    ```bash
    pip install mysql-connector-python
    ```

3. Configure o arquivo `backup.py`:
    - Preencha os seguintes valores com os dados do seu banco de dados MySQL:
      ```python
      DB_USER = "seu_usuario"          # Usuário do MySQL
      DB_PASSWORD = "sua_senha"       # Senha do MySQL
      DB_NAME = "nome_do_banco"       # Nome do banco de dados
      HOST = "localhost"              # Host do servidor MySQL
      BACKUP_DIR = "caminho/dos/backups"  # Caminho onde o backup será salvo
      ```

## Uso
Execute o script para criar o backup:
```bash
python backup.py
```
O backup gerado será salvo no diretório especificado na variável `BACKUP_DIR`, com o seguinte formato:
```
nome_do_banco_backup_YYYY-MM-DD_HH-MM-SS.sql
```

## Exemplo de Saída
Ao finalizar, o script exibe:
```
Backup concluído com sucesso: caminho/dos/backups/nome_do_banco_backup_YYYY-MM-DD_HH-MM-SS.sql
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um _pull request_ ou relatar um problema na aba de issues.

## Licença
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
