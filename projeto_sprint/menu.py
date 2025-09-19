import os

# --- Funções CRUD para o gerenciamento de inventário ---

def adicionar_produto(nome, preco, quantidade):
    """
    Adiciona um novo produto ao arquivo 'inventario.txt'.

    Args:
        nome (str): O nome do produto.
        preco (str ou float): O preço do produto, que será convertido para float.
        quantidade (str ou int): A quantidade em estoque, que será convertida para int.
    """
    try:
        # Converte os valores de preço e quantidade para tipos numéricos
        preco_numerico = float(preco)
        quantidade_numerica = int(quantidade)
        
        # Formata a string para ser escrita no arquivo, com o preço formatado
        linha_produto = f"{nome},{preco_numerico:.2f},{quantidade_numerica}\n"
        
        # 'a' abre o arquivo em modo de adição, criando-o se não existir
        with open('inventario.txt', 'a') as arquivo:
            arquivo.write(linha_produto)
        
        print(f"\nProduto '{nome}' adicionado com sucesso ao inventário.")

    except ValueError:
        # Captura erros se o preço ou a quantidade não puderem ser convertidos
        print("\nErro: O preço e a quantidade devem ser números válidos.")
    except IOError:
        # Captura erros de permissão de escrita no arquivo
        print("\nErro: Não foi possível escrever no arquivo 'inventario.txt'.")

def listar_produtos():
    """
    Lê e exibe todos os produtos do arquivo 'inventario.txt' de forma formatada.
    """
    try:
        # 'r' abre o arquivo em modo de leitura
        with open('inventario.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
            if not linhas:
                print("\nO inventário está vazio.")
                return

            print("\n--- Inventário de Produtos ---")
            print("{:<20} | {:<10} | {:<10}".format("Nome", "Preço", "Quantidade"))
            print("-" * 45)

            for linha in linhas:
                # Remove espaços em branco e quebras de linha
                linha_limpa = linha.strip()
                # Divide a linha em partes usando a vírgula como delimitador
                partes = linha_limpa.split(',')
                
                # Garante que a linha tem o formato esperado
                if len(partes) == 3:
                    nome, preco, quantidade = partes
                    print("{:<20} | {:<10} | {:<10}".format(nome, preco, quantidade))
        
    except FileNotFoundError:
        # Captura o erro se o arquivo não existir
        print("\nErro: O arquivo 'inventario.txt' não foi encontrado.")

def atualizar_produto(nome_busca):
    """
    Atualiza o preço e/ou a quantidade de um produto existente.

    Args:
        nome_busca (str): O nome do produto a ser atualizado. A busca é case-insensitive.
    """
    try:
        linhas_atualizadas = []
        produto_encontrado = False
        
        # 1. Lê todo o arquivo e armazena as linhas em uma lista na memória
        with open('inventario.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                
                # Compara o nome do produto na linha com o nome buscado (case-insensitive)
                if len(partes) > 0 and partes[0].lower() == nome_busca.lower():
                    produto_encontrado = True
                    nome_antigo, preco_antigo, quant_antiga = partes
                    
                    print(f"\nProduto '{nome_antigo}' encontrado. Dados atuais: Preço={preco_antigo}, Quantidade={quant_antiga}")
                    
                    # 2. Coleta os novos dados do usuário
                    novo_preco_str = input("Digite o novo preço (deixe em branco para não alterar): ")
                    nova_quant_str = input("Digite a nova quantidade (deixe em branco para não alterar): ")
                    
                    # Usa os novos valores se foram informados; caso contrário, mantém os antigos
                    novo_preco = novo_preco_str if novo_preco_str else preco_antigo
                    nova_quant = nova_quant_str if nova_quant_str else quant_antiga
                    
                    # Adiciona a linha modificada à lista
                    linhas_atualizadas.append(f"{nome_antigo},{novo_preco},{nova_quant}\n")
                else:
                    # Adiciona as linhas que não serão modificadas à lista
                    linhas_atualizadas.append(linha)
        
        # 3. Reescreve o arquivo com a lista de linhas atualizadas
        if produto_encontrado:
            # 'w' abre o arquivo em modo de escrita, sobrescrevendo o conteúdo anterior
            with open('inventario.txt', 'w') as arquivo:
                arquivo.writelines(linhas_atualizadas)
            print("\nInventário atualizado com sucesso!")
        else:
            print(f"\nErro: Produto '{nome_busca}' não encontrado no inventário.")

    except FileNotFoundError:
        print("\nErro: O arquivo 'inventario.txt' não foi encontrado.")

def remover_produto(nome_a_remover):
    """
    Remove um produto do arquivo 'inventario.txt' com base no nome.

    Args:
        nome_a_remover (str): O nome do produto a ser removido (case-insensitive).
    """
    try:
        linhas_para_salvar = []
        produto_encontrado = False
        
        # 1. Lê o arquivo e filtra as linhas que devem ser mantidas
        with open('inventario.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                
                # Se a linha não for o produto a ser removido, adicione-a à lista
                if len(partes) > 0 and partes[0].lower() != nome_a_remover.lower():
                    linhas_para_salvar.append(linha)
                else:
                    produto_encontrado = True
        
        # 2. Se o produto foi encontrado, reescreve o arquivo com as linhas restantes
        if produto_encontrado:
            with open('inventario.txt', 'w') as arquivo:
                arquivo.writelines(linhas_para_salvar)
            print(f"\nProduto '{nome_a_remover}' removido com sucesso.")
        else:
            print(f"\nErro: Produto '{nome_a_remover}' não encontrado no inventário.")
    
    except FileNotFoundError:
        print("\nErro: O arquivo 'inventario.txt' não foi encontrado.")

# --- Menu Principal do Programa ---

def menu_principal():
    """
    Exibe o menu interativo e processa a escolha do usuário em um loop contínuo.
    """
    while True:
        print("\n" + "="*40)
        print(" Menu Principal - Gerenciamento de Inventário")
        print("="*40)
        print("1. Adicionar novo produto")
        print("2. Listar todos os produtos")
        print("3. Atualizar um produto existente")
        print("4. Remover um produto")
        print("5. Sair do programa")
        print("="*40)

        escolha = input("Digite sua opção (1-5): ")

        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            preco = input("Digite o preço: ")
            quantidade = input("Digite a quantidade: ")
            adicionar_produto(nome, preco, quantidade)
        
        elif escolha == '2':
            listar_produtos()
        
        elif escolha == '3':
            nome_busca = input("Digite o nome do produto que deseja atualizar: ")
            atualizar_produto(nome_busca)
        
        elif escolha == '4':
            nome_remover = input("Digite o nome do produto que deseja remover: ")
            remover_produto(nome_remover)
            
        elif escolha == '5':
            print("\nSaindo do programa. Até mais!")
            break
        
        else:
            print("\nOpção inválida. Por favor, digite um número de 1 a 5.")

# Inicia o programa
if __name__ == "__main__":
    menu_principal()