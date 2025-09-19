import oracledb

#conexao com o banco de dados
USER = "rm563674"
PASSWORD = "010207"
HOST = "oracle.fiap.com.br"
PORT = "1521"
SERVICE_NAME = "orcl"


#estabelecendo conexao com o banco
def get_conexao():
    try:
        conn = oracledb.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            service_name=SERVICE_NAME
        )
        print('Conexão com Oracle foi realizada!')
        return conn
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
        return None




#criar a tabela produto
def criar_tabela():
    conn = get_conexao()
    if not conn:
        return

    cursor = conn.cursor()
    try:
        sql = """
            CREATE TABLE PRODUTO (
                id NUMBER GENERATED ALWAYS AS IDENTITY,
                nome VARCHAR2(50) NOT NULL,
                descricao VARCHAR2(200),
                fornecedor VARCHAR2(50),
                preco NUMBER(10, 2),
                PRIMARY KEY (id)
            )
        """
        cursor.execute(sql)
        print('Tabela PRODUTO foi criada com sucesso!')
    except oracledb.Error as e:
        print(f'Erro ao criar tabela PRODUTO: {e}')
    finally:
        if conn:
            conn.close()





#criando a função para inserir o produto
def inserir_produto(nome, descricao, fornecedor, preco):
    conn = get_conexao()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO PRODUTO (nome, descricao, fornecedor, preco)
            VALUES (:nome, :descricao, :fornecedor, :preco)
        """
        cursor.execute(sql, {
            'nome': nome,
            'descricao': descricao,
            'fornecedor': fornecedor,
            'preco': preco
        })
        conn.commit()
        print(f'Produto adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'Erro ao inserir produto: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()



#recupera e lista todos os produtos cadastrados
def listar_produtos():
    conn = get_conexao()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = """
            SELECT id, nome, descricao, fornecedor, preco
            FROM PRODUTO ORDER BY id
        """
        cursor.execute(sql)
        print("\n--- Lista de Produtos ---")
        rows = cursor.fetchall()
        if not rows:
            print("Nenhum produto cadastrado")
        else:
            for row in rows:
                print(f'ID: {row[0]}, Nome: {row[1]}, Descrição: {row[2]}, Fornecedor: {row[3]}, Preço: R${row[4]:.2f}')
                print('----------------------------------')
    except oracledb.Error as e:
        print(f'Erro ao listar produtos: {e}')
    finally:
        if conn:
            conn.close()


#criando função para buscar e listar o produto com base no id recebido
def buscar_produto_por_id(produto_id):
    conn = get_conexao()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "SELECT id, nome, descricao, fornecedor, preco FROM PRODUTO WHERE id = :produto_id"
        cursor.execute(sql, {'produto_id': produto_id})
        row = cursor.fetchone()
        if row:
            print("\n--- Produto com o ID desejado ---")
            print(f'ID: {row[0]}, Nome: {row[1]}, Descrição: {row[2]}, Fornecedor: {row[3]}, Preço: R${row[4]:.2f}')
        else:
            print(f"Nenhum produto com ID {produto_id} foi encontrado.")
    except oracledb.Error as e:
        print(f'Erro ao buscar produto: {e}')
    finally:
        if conn:
            conn.close()



#atualiza o preço do produto que já existe
def atualizar_preco_produto(produto_id, novo_preco):
    conn = get_conexao()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "UPDATE PRODUTO SET preco = :novo_preco WHERE id = :produto_id"
        cursor.execute(sql, {'novo_preco': novo_preco, 'produto_id': produto_id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f"O preço do produto foi atualizado para R${novo_preco:.2f}")
        else:
            print(f"Nenhum produto com ID {produto_id} foi encontrado")
    except oracledb.Error as e:
        print(f"Erro ao atualizar o preço: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()



#remove o produto do banco
def deletar_produto(produto_id):
    conn = get_conexao()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM PRODUTO WHERE id = :produto_id"
        cursor.execute(sql, {'produto_id': produto_id})
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Produto com ID {produto_id} foi excluído com sucesso!")
        else:
            print(f"Nenhum produto com ID {produto_id} foi encontrado.")
    except oracledb.Error as e:
        print(f"Erro ao excluir o produto: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()




#Exibindo o menu com as funções criadas
def menu():
    while True:
        print("\n--- Menu de Produtos ---")
        print("1. Inserir novo produto")
        print("2. Listar os produtos")
        print("3. Buscar produto por ID")
        print("4. Atualizar o preço do produto")
        print("5. Excluir um produto")
        print("6. Sair")

        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                nome = input("Nome do produto: ")
                descricao = input("Descrição: ")
                fornecedor = input("Fornecedor: ")
                preco = float(input("Preço: "))
                inserir_produto(nome, descricao, fornecedor, preco)
            elif opcao == 2:
                listar_produtos()
            elif opcao == 3:
                produto_id = int(input("ID do produto a ser buscado: "))
                buscar_produto_por_id(produto_id)
            elif opcao == 4:
                produto_id = int(input("ID do produto para atualizar: "))
                novo_preco = float(input("Novo preço: "))
                atualizar_preco_produto(produto_id, novo_preco)
            elif opcao == 5:
                produto_id = int(input("ID do produto a ser excluído: "))
                deletar_produto(produto_id)
            elif opcao == 6:
                print("Fechando do programa.")
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


if __name__ == '__main__':
    criar_tabela()
    menu()