import oracledb
from datetime import datetime

# --- Configurações de Conexão ---
USER = "rm563674"
PASSWORD = "010207"
HOST = "oracle.fiap.com.br"
PORT = "1521"
SERVICE_NAME = "orcl"


def get_conexao():
    """
    Tenta estabelecer uma conexão com o banco de dados Oracle.
    """
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
    except oracledb.Error as e:
        print(f'Erro ao obter a conexão: {e}')
        return None


def criar_tabelas():
    """
    Cria todas as tabelas necessárias no banco de dados.
    """
    conn = get_conexao()
    if conn is None:
        return

    try:
        sql_commands = [
            """
            CREATE TABLE usuario (
                id_usuario INTEGER GENERATED ALWAYS AS IDENTITY,
                cpf_usuario INTEGER NOT NULL,
                nome_usuario VARCHAR2(50),
                data_nasc DATE NOT NULL,
                user_admin CHAR(1) NOT NULL,
                CONSTRAINT usuario_pk PRIMARY KEY (id_usuario),
                CONSTRAINT usuario_cpf_un UNIQUE (cpf_usuario)
            )
            """,
            "ALTER TABLE usuario ADD CONSTRAINT usuario_admin_ck CHECK (user_admin IN ('S', 'N'))",
            """
            CREATE TABLE perfil(
                id_perfil INTEGER GENERATED ALWAYS AS IDENTITY,
                descricao VARCHAR2(20) NOT NULL,
                modo_acesso VARCHAR2(30) NOT NULL,
                CONSTRAINT perfil_pk PRIMARY KEY (id_perfil)
            )
            """,
            """
            CREATE TABLE acesso (
                id_acesso INTEGER GENERATED ALWAYS AS IDENTITY,
                data_acesso DATE NOT NULL,
                id_usuario INTEGER,
                CONSTRAINT acesso_pk PRIMARY KEY (id_acesso),
                CONSTRAINT acesso_usuario_fk FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
            )
            """,
            """
            CREATE TABLE categoria_tutorial(
                id_categoria INTEGER GENERATED ALWAYS AS IDENTITY,
                nome_categoria VARCHAR2(50) NOT NULL,
                desc_categoria VARCHAR2(100) NOT NULL,
                CONSTRAINT categoria_tuto_pk PRIMARY KEY (id_categoria)
            )
            """,
            """
            CREATE TABLE video_tutoriais(
                id_tutorial INTEGER GENERATED ALWAYS AS IDENTITY,
                titulo VARCHAR2(50) NOT NULL,
                url_video VARCHAR2(255) NOT NULL,
                id_categoria INTEGER,
                CONSTRAINT videos_tuto_pk PRIMARY KEY (id_tutorial),
                CONSTRAINT id_categoria_fk FOREIGN KEY (id_categoria) REFERENCES categoria_tutorial (id_categoria)
            )
            """,
            """
            CREATE TABLE lembretes(
                id_lembrete INTEGER GENERATED ALWAYS AS IDENTITY,
                nome_lembrete VARCHAR2(20) NOT NULL,
                data_lembrete DATE NOT NULL,
                desc_lembrete VARCHAR2(200) NOT NULL,
                CONSTRAINT id_lembrete_pk PRIMARY KEY (id_lembrete)
            )
            """,
            """
            CREATE TABLE suporte(
                id_suporte INTEGER GENERATED ALWAYS AS IDENTITY,
                duvida VARCHAR2(200) NOT NULL,
                CONSTRAINT id_suporte_pk PRIMARY KEY (id_suporte)
            )
            """
        ]

        with conn.cursor() as cursor:
            for command in sql_commands:
                try:
                    cursor.execute(command)
                    print(f"Comando executado: {command.split()[2]}...")
                except oracledb.Error as e:
                    # Ignore "table or view already exists" error
                    if e.args[0].code == 955:
                        print("Tabela já existe. Continuando...")
                    else:
                        print(f"Erro ao executar o comando: {e}")
                        conn.rollback()
                        raise
        conn.commit()
        print('Todas as tabelas foram criadas/verificadas com sucesso!')
    except oracledb.Error as e:
        print(f'Erro no processo de criação de tabelas: {e}')
    finally:
        if conn:
            conn.close()

# --- Funções de Operações com Banco de Dados ---

def inserir_usuario(cpf, nome, data_nasc, user_admin):
    """Insere um novo usuário."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO usuario (cpf_usuario, nome_usuario, data_nasc, user_admin) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)"
                cursor.execute(sql, [cpf, nome, data_nasc, user_admin])
            conn.commit()
            print(f'Usuário {nome} adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'Erro ao inserir usuário: {e}')
        # A linha "if conn: conn.rollback()" foi removida

def alterar_permissao_admin(id_usuario, permissao):
    """Altera a permissão de administrador de um usuário."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                sql = "UPDATE usuario SET user_admin = :1 WHERE id_usuario = :2"
                cursor.execute(sql, [permissao, id_usuario])
                if cursor.rowcount > 0:
                    conn.commit()
                    status = "concedida" if permissao == 'S' else "removida"
                    print(f"Permissão de administrador {status} para o usuário ID {id_usuario}.")
                else:
                    print(f"Nenhum usuário com ID {id_usuario} foi encontrado.")
    except oracledb.Error as e:
        print(f'Erro ao alterar permissão: {e}')
        if conn: conn.rollback()

def deletar_usuario(id_usuario):
    """Deleta um usuário e seus acessos associados."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                # Primeiro, deleta registros dependentes (acesso), se houver.
                cursor.execute("DELETE FROM acesso WHERE id_usuario = :1", [id_usuario])
                # Em seguida, deleta o usuário.
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :1", [id_usuario])
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"Usuário com ID {id_usuario} foi excluído com sucesso.")
                else:
                    print(f"Nenhum usuário com ID {id_usuario} foi encontrado.")
    except oracledb.Error as e:
        print(f'Erro ao deletar usuário: {e}')
        if conn: conn.rollback()

def criar_categoria_tutorial(nome, descricao):
    """Cria uma nova categoria de tutorial."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO categoria_tutorial (nome_categoria, desc_categoria) VALUES (:1, :2)"
                cursor.execute(sql, [nome, descricao])
            conn.commit()
            print(f"Categoria '{nome}' criada com sucesso.")
    except oracledb.Error as e:
        print(f'Erro ao criar categoria: {e}')
        if conn: conn.rollback()

def deletar_categoria_tutorial(id_categoria):
    """Deleta uma categoria de tutorial e seus vídeos associados."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                # Deleta vídeos associados primeiro devido à restrição de chave estrangeira
                cursor.execute("DELETE FROM video_tutoriais WHERE id_categoria = :1", [id_categoria])
                cursor.execute("DELETE FROM categoria_tutorial WHERE id_categoria = :1", [id_categoria])
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"Categoria com ID {id_categoria} excluída com sucesso.")
                else:
                    print("Nenhuma categoria encontrada.")
    except oracledb.Error as e:
        print(f'Erro ao deletar categoria: {e}')
        if conn: conn.rollback()

def criar_video_tutorial(titulo, url_video, id_categoria):
    """Cria um novo vídeo de tutorial."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO video_tutoriais (titulo, url_video, id_categoria) VALUES (:1, :2, :3)"
                cursor.execute(sql, [titulo, url_video, id_categoria])
            conn.commit()
            print(f"Tutorial '{titulo}' adicionado com sucesso!")
    except oracledb.Error as e:
        print(f'Erro ao criar vídeo tutorial: {e}')
        if conn: conn.rollback()

def adicionar_lembrete(nome, data, descricao):
    """Adiciona um novo lembrete."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO lembretes (nome_lembrete, data_lembrete, desc_lembrete) VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3)"
                cursor.execute(sql, [nome, data, descricao])
            conn.commit()
            print(f"Lembrete '{nome}' adicionado com sucesso!")
    except oracledb.Error as e:
        print(f'Erro ao adicionar lembrete: {e}')
        if conn: conn.rollback()

# --- Funções de listagem para verificação ---

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_usuario, nome_usuario, user_admin FROM usuario ORDER BY id_usuario")
                print("\n--- Lista de Usuários ---")
                rows = cursor.fetchall()
                if not rows:
                    print("Nenhum usuário cadastrado.")
                else:
                    for row in rows:
                        admin_status = "Sim" if row[2] == 'S' else "Não"
                        print(f"ID: {row[0]}, Nome: {row[1]}, Admin: {admin_status}")
    except oracledb.Error as e:
        print(f"Erro ao listar usuários: {e}")

def listar_categorias():
    """Lista todas as categorias de tutoriais."""
    try:
        with get_conexao() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_categoria, nome_categoria FROM categoria_tutorial ORDER BY id_categoria")
                print("\n--- Lista de Categorias de Tutoriais ---")
                rows = cursor.fetchall()
                if not rows:
                    print("Nenhuma categoria cadastrada.")
                else:
                    for row in rows:
                        print(f"ID: {row[0]}, Nome: {row[1]}")
    except oracledb.Error as e:
        print(f"Erro ao listar categorias: {e}")

# --- Menu Interativo ---

def menu():
    """
    Exibe um menu interativo para o usuário.
    """
    while True:
        print("\n--- Menu de Gerenciamento de Sistema ---")
        print("1. Inserir novo usuário")
        print("2. Alterar permissão de admin (Dar ou Remover)")
        print("3. Deletar um usuário")
        print("4. Criar uma nova categoria de tutorial")
        print("5. Deletar uma categoria de tutorial")
        print("6. Adicionar um novo vídeo de tutorial")
        print("7. Adicionar um lembrete")
        print("8. Listar usuários")
        print("9. Listar categorias de tutoriais")
        print("10. Sair")

        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                cpf = int(input("CPF do usuário: "))
                nome = input("Nome do usuário: ")
                data_nasc = input("Data de nascimento (YYYY-MM-DD): ")
                user_admin = input("É admin? (S/N): ").upper()
                inserir_usuario(cpf, nome, data_nasc, user_admin)
            elif opcao == 2:
                id_usuario = int(input("ID do usuário para alterar: "))
                permissao = input("Nova permissão de admin (S/N): ").upper()
                alterar_permissao_admin(id_usuario, permissao)
            elif opcao == 3:
                id_usuario = int(input("ID do usuário para deletar: "))
                deletar_usuario(id_usuario)
            elif opcao == 4:
                nome_cat = input("Nome da categoria: ")
                desc_cat = input("Descrição da categoria: ")
                criar_categoria_tutorial(nome_cat, desc_cat)
            elif opcao == 5:
                id_categoria = int(input("ID da categoria para deletar: "))
                deletar_categoria_tutorial(id_categoria)
            elif opcao == 6:
                titulo = input("Título do vídeo: ")
                url = input("URL do vídeo: ")
                id_categoria = int(input("ID da categoria do vídeo: "))
                criar_video_tutorial(titulo, url, id_categoria)
            elif opcao == 7:
                nome_lembrete = input("Nome do lembrete: ")
                data_lembrete = input("Data do lembrete (YYYY-MM-DD): ")
                desc_lembrete = input("Descrição do lembrete: ")
                adicionar_lembrete(nome_lembrete, data_lembrete, desc_lembrete)
            elif opcao == 8:
                listar_usuarios()
            elif opcao == 9:
                listar_categorias()
            elif opcao == 10:
                print("Fechando o programa.")
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a opção.")
        except oracledb.DatabaseError as e:
            # Captura erros de banco de dados, como IDs inexistentes em chaves estrangeiras
            print(f"Erro no banco de dados: {e}")

if __name__ == '__main__':
    criar_tabelas()
    menu()