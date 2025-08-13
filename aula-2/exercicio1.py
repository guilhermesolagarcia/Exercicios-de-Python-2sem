'''
1) Escreva uma função para criar e retornar uma matriz
 numérica n x m (linhas e colunas)
2) Escreva uma função que receba uma matriz, some todos os
elementos contidos na matriz e retorne sua soma
3) Escreva uma função para imprimir a soma(resultado)
4) Escreva uma função main para testar o programa
'''

def criar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = int(input('Número: '))
            linha.append(n)
        matriz.append(linha)
    return matriz


def somar_matriz(matriz):
    soma = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]
        return soma

def imprimir(soma):
    print(f'Soma Total: {soma}')

    

def main():
    matriz = criar_matriz(3, 3)
    soma = somar_matriz(matriz)
    imprimir(soma) 

main()