def adicionar_produto(nome, preco, quantidade):
    """
    Adiciona um novo produto ao arquivo 'inventario.txt'.

    Args:
        nome (str): O nome do produto.
        preco (str ou float): O preço do produto.
        quantidade (str ou int): A quantidade em estoque.
    """
    try:
        # Tenta converter o preço para float e a quantidade para int
        preco_numerico = float(preco)
        quantidade_numerica = int(quantidade)
        
        # Formata a string com os dados do produto
        linha_produto = f"{nome},{preco_numerico:.2f},{quantidade_numerica}\n"
        
        # Abre o arquivo em modo de adição ('a') para escrever no final
        with open('inventario.txt', 'a') as arquivo:
            arquivo.write(linha_produto)
        
        print(f"Produto '{nome}' adicionado com sucesso ao inventário.")

    except ValueError:
        print("Erro: O preço e a quantidade devem ser números válidos.")
    except IOError:
        print("Erro: Não foi possível escrever no arquivo 'inventario.txt'.")

# --- Exemplos de uso ---

# Exemplo de adição bem-sucedida
adicionar_produto("Camiseta", 29.90, 50)
adicionar_produto("Calça Jeans", 89.50, 25)

# Exemplo com erro (preço não é um número)
adicionar_produto("Tênis", "oitenta", 10)

# Exemplo com erro (quantidade não é um número)
adicionar_produto("Meia", 5.00, "dez")



def listar_produtos():
    """
    Lê o arquivo 'inventario.txt' e exibe os produtos formatados.
    Trata o erro se o arquivo não for encontrado.
    """
    try:
        # Tenta abrir o arquivo em modo de leitura ('r')
        with open('inventario.txt', 'r') as arquivo:
            # Lê todas as linhas do arquivo
            linhas = arquivo.readlines()
            
            # Verifica se o arquivo está vazio
            if not linhas:
                print("O inventário está vazio.")
                return

            print("--- Inventário de Produtos ---")
            print("{:<20} | {:<10} | {:<10}".format("Nome", "Preço", "Quantidade"))
            print("-" * 45)

            # Itera sobre cada linha e exibe os dados formatados
            for linha in linhas:
                # Remove espaços em branco e quebras de linha da string
                linha = linha.strip()
                # Divide a linha em partes usando a vírgula como separador
                partes = linha.split(',')
                
                # Garante que a linha tem 3 partes (nome, preco, quantidade)
                if len(partes) == 3:
                    nome, preco, quantidade = partes
                    print("{:<20} | {:<10} | {:<10}".format(nome, preco, quantidade))
        
    except FileNotFoundError:
        # Se o arquivo não existir, este bloco é executado
        print("Erro: O arquivo 'inventario.txt' não foi encontrado.")
        print("Certifique-se de que o arquivo existe ou adicione produtos primeiro.")

# --- Exemplo de uso ---

# Antes de executar, certifique-se de que o arquivo inventario.txt foi criado
# usando a função adicionar_produto do exemplo anterior.

# Exemplo de listagem bem-sucedida (se o arquivo existir e tiver conteúdo)
listar_produtos()

# Exemplo de erro (se o arquivo for deletado ou não existir)
# Supondo que você execute a função sem o arquivo, ela exibirá a mensagem de erro




import os

def remover_produto(nome_a_remover):
    """
    Remove um produto do arquivo 'inventario.txt' com base no nome.

    Args:
        nome_a_remover (str): O nome do produto a ser removido.
    """
    try:
        linhas_para_salvar = []
        produto_encontrado = False

        # 1. Lê o arquivo e armazena as linhas que NÃO serão removidas
        with open('inventario.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                # Verifica se a linha tem o formato esperado e se o nome não corresponde
                if len(partes) > 0 and partes[0].lower() != nome_a_remover.lower():
                    linhas_para_salvar.append(linha)
                else:
                    produto_encontrado = True
        
        # 2. Se o produto foi encontrado, reescreve o arquivo com as linhas restantes
        if produto_encontrado:
            with open('inventario.txt', 'w') as arquivo:
                arquivo.writelines(linhas_para_salvar)
            print(f"Produto '{nome_a_remover}' removido com sucesso.")
        else:
            print(f"Erro: Produto '{nome_a_remover}' não encontrado no inventário.")

    except FileNotFoundError:
        print("Erro: O arquivo 'inventario.txt' não foi encontrado.")
        print("Certifique-se de que o arquivo existe.")

# --- Exemplo de uso ---

# Suponha que o inventário.txt contenha:
# Camiseta,29.90,50
# Calça Jeans,89.50,25
# Meia,5.00,10

print("--- Tentando remover 'Calça Jeans' ---")
remover_produto("Calça Jeans")

print("\n--- Listando produtos após a remoção ---")
# Importe a função de listagem para verificar o resultado
# from sua_funcao_listar import listar_produtos
# listar_produtos()

print("\n--- Tentando remover um produto que não existe ---")
remover_produto("Sapato Social")

# O arquivo agora deve conter apenas:
# Camiseta,29.90,50
# Meia,5.00,10

listar_produtos()


def atualizar_produto(nome_busca):
    """
    Atualiza o preço e/ou a quantidade de um produto no arquivo 'inventario.txt'.

    Args:
        nome_busca (str): O nome do produto a ser atualizado.
    """
    try:
        linhas_atualizadas = []
        produto_encontrado = False
        
        # 1. Lê o arquivo e armazena as linhas na memória
        with open('inventario.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                # Verifica se o nome na linha corresponde ao nome buscado (ignorando maiúsculas/minúsculas)
                if len(partes) > 0 and partes[0].lower() == nome_busca.lower():
                    produto_encontrado = True
                    nome_antigo, preco_antigo, quant_antiga = partes
                    
                    print(f"Produto '{nome_antigo}' encontrado. Dados atuais: Preço={preco_antigo}, Quantidade={quant_antiga}")
                    
                    # 2. Solicita as novas informações
                    novo_preco_str = input("Digite o novo preço (deixe em branco para não alterar): ")
                    nova_quant_str = input("Digite a nova quantidade (deixe em branco para não alterar): ")
                    
                    # Usa os novos valores se foram informados, senão mantém os antigos
                    novo_preco = novo_preco_str if novo_preco_str else preco_antigo
                    nova_quant = nova_quant_str if nova_quant_str else quant_antiga
                    
                    # 3. Adiciona a linha atualizada à lista
                    linhas_atualizadas.append(f"{nome_antigo},{novo_preco},{nova_quant}\n")
                else:
                    # Se não for o produto buscado, adiciona a linha original
                    linhas_atualizadas.append(linha)
        
        # 4. Se o produto foi encontrado, reescreve o arquivo com as linhas atualizadas
        if produto_encontrado:
            with open('inventario.txt', 'w') as arquivo:
                arquivo.writelines(linhas_atualizadas)
            print("Inventário atualizado com sucesso!")
        else:
            print(f"Erro: Produto '{nome_busca}' não encontrado no inventário.")

    except FileNotFoundError:
        print("Erro: O arquivo 'inventario.txt' não foi encontrado.")
        print("Certifique-se de que o arquivo existe ou adicione produtos primeiro.")

# --- Exemplo de uso ---

# Suponha que o inventário.txt contenha:
# Camiseta,29.90,50
# Calça Jeans,89.50,25

# Tenta atualizar a quantidade da 'Camiseta'
atualizar_produto("Camiseta")

# Tenta atualizar a 'Calça Jeans' (preço e quantidade)
atualizar_produto("Calça Jeans")

# Tenta atualizar um produto que não existe
atualizar_produto("Sapato")



# Importe as funções das respostas anteriores.
# Supondo que as funções estão no mesmo arquivo.


import os

def adicionar_produto(nome, preco, quantidade):
    """
    Adiciona um novo produto ao arquivo 'inventario.txt'.
    (Código da resposta anterior)
    """
    try:
        preco_numerico = float(preco)
        quantidade_numerica = int(quantidade)
        linha_produto = f"{nome},{preco_numerico:.2f},{quantidade_numerica}\n"
        with open('inventario.txt', 'a') as arquivo:
            arquivo.write(linha_produto)
        print(f"\nProduto '{nome}' adicionado com sucesso ao inventário.")
    except ValueError:
        print("\nErro: O preço e a quantidade devem ser números válidos.")
    except IOError:
        print("\nErro: Não foi possível escrever no arquivo 'inventario.txt'.")

def listar_produtos():
    """
    Lê o arquivo 'inventario.txt' e exibe os produtos formatados.
    (Código da resposta anterior)
    """
    try:
        with open('inventario.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("\nO inventário está vazio.")
                return

            print("\n--- Inventário de Produtos ---")
            print("{:<20} | {:<10} | {:<10}".format("Nome", "Preço", "Quantidade"))
            print("-" * 45)

            for linha in linhas:
                linha = linha.strip()
                partes = linha.split(',')
                if len(partes) == 3:
                    nome, preco, quantidade = partes
                    print("{:<20} | {:<10} | {:<10}".format(nome, preco, quantidade))
        
    except FileNotFoundError:
        print("\nErro: O arquivo 'inventario.txt' não foi encontrado.")

def atualizar_produto(nome_busca):
    """
    Atualiza o preço e/ou a quantidade de um produto.
    (Código da resposta anterior)
    """
    try:
        linhas_atualizadas = []
        produto_encontrado = False
        with open('inventario.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                if len(partes) > 0 and partes[0].lower() == nome_busca.lower():
                    produto_encontrado = True
                    nome_antigo, preco_antigo, quant_antiga = partes
                    
                    print(f"\nProduto '{nome_antigo}' encontrado. Dados atuais: Preço={preco_antigo}, Quantidade={quant_antiga}")
                    novo_preco_str = input("Digite o novo preço (deixe em branco para não alterar): ")
                    nova_quant_str = input("Digite a nova quantidade (deixe em branco para não alterar): ")
                    
                    novo_preco = novo_preco_str if novo_preco_str else preco_antigo
                    nova_quant = nova_quant_str if nova_quant_str else quant_antiga
                    
                    linhas_atualizadas.append(f"{nome_antigo},{novo_preco},{nova_quant}\n")
                else:
                    linhas_atualizadas.append(linha)
        
        if produto_encontrado:
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
    (Código da resposta anterior)
    """
    try:
        linhas_para_salvar = []
        produto_encontrado = False
        with open('inventario.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                if len(partes) > 0 and partes[0].lower() != nome_a_remover.lower():
                    linhas_para_salvar.append(linha)
                else:
                    produto_encontrado = True
        
        if produto_encontrado:
            with open('inventario.txt', 'w') as arquivo:
                arquivo.writelines(linhas_para_salvar)
            print(f"\nProduto '{nome_a_remover}' removido com sucesso.")
        else:
            print(f"\nErro: Produto '{nome_a_remover}' não encontrado no inventário.")
    except FileNotFoundError:
        print("\nErro: O arquivo 'inventario.txt' não foi encontrado.")
