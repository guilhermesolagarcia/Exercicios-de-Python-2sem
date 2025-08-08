'''
Escreva um programa em Python, que simule o cálculo de notas de um aluno em diferentes disciplinas.
O programa deve modular e utilizar as estruturas de controle e funções.


1. Requisitos do Sistema
 - Função calcular_media(notas)
   - Deve receber uma LISTA de notas como parâmetro
   - Deve ter uma estrutura de repetição (for ou while) para percorrer a lista
   - retornar a média das notas (com validações)   
 -Função verificar_aprovação(media, media_minima)
   - Deve receber a média das notas e a média mínima para aprovação
   - Deve usar condicionais para verificar o status do aluno
   - Se a média for maior que a média mínima, retornar a String "Aprovado"
   - Se a média for maior ou igual a 5.0 e menor do que a média mínima, retornar a String "Recuperação"
   - Caso contrário, retorne a String "Reprovado"
 - Função Principal main()
   - Deve contar a lista com as disciplinas
   - Média mínima para aprovação 
   - Estrutura de repetição para iterar sobre as disciplinas
   - Para cada disciplina, o usuário deve inserir 3 notas
   - Chamar a função calcular_média() para obter a média da disciplina
   - Chamar a função verificar_aprovação para obter o status do aluno
   - Imprimir a média e o status para cada disciplina
'''

def calcular_media(notas):
    """
    Calcula a média de uma lista de notas
    - recebe por parâmetro de uma lista de notas
    - retorna a média das notas
    """
    soma = 0

    #percorrer a lista de notas
    # para cada nota na LISTA de notas/ uma boa prática é sempre colocar o valor como o singular da lista, por exemplo a lista NOTAS, colocamos NOTA
    for nota in notas: # pra cada variável na lista
        soma += nota # soma = soma + nota / a soma acumula o valor de nota, no segundo laço, ele vai ter o valor da primeira nota, depois na terceira vai ter o valor da primeira + segunda / acumular valor na variável soma

    if len(notas) >0:
        return soma / len(nota) # dividindo pelo tamanho da listinha de NOTAS / LEN 
    else:
        return 0
    

