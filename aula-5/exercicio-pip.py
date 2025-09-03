'''
CRUD -Create, Read, Update e Delete
    - conjunto de operações básicas de manipulção de dados

Módulo (biblioteca) python-orecledb (sucessor do cx_oracle)
    - permite que a aplicação de python se conecte ao banco de dados oracle
    e execute as instruções SQL

Pré Requisitos
    -instalar a biblioteca oracledb
        - pip install <biblioteca>
        Exemplo: pip install oracledb
        atualização: python -m pip install --upgrade pip

String de conexão:
<user_name>/<password>@<de_host_address>:<db_port>/<db_service>
Exemplo: 'usuario/senha@localhost:1521/orcl
'''

import oracledb

# criar (obter) uma conexão com o banco de dados Oracle
def getConnection():
    try:
        connection = oracledb.connect(user='rm563674',
                                       password="010207", 
                                       host="1521",
                                       service_name="orcl")
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
    return connection

def criar_tabela():
    cursor = connection.cursor()
    try:
        sql = """
            CREATE TABLE ceo_details(
            id number GENERATED ALWAYS AS IDENTITY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            company VARCHAR(30),
            age number(10)
            )
        """
        cursor.execute(sql)
        print(f'Tabela CEO_DETAILS foi criada com sucesso!')
    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')

#Programa Principal

connection = getConnection()
print(f'Conexão: {connection.version}')

criar_tabela(connection)

print(f'Fechando a conexão... {connection.close()}')
connection.close()