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
   - Se a média for maior que a média mínima (7), retornar a String "Aprovado"
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
        return soma / len(notas) # dividindo pelo tamanho da listinha de NOTAS / LEN 
    else:
        return 0
    
def verificar_aprovacao(media, media_minima):
    """
    Verifica o status de aprovação do aluno
    - recebe a média e a média mínima por parâmetro
    - retorna o status do aluno - Aprovado - Recuperação - Reprovado
    """
    if media >= media_minima:
        return "Aprovado"
    elif media >= 5 and media < media_minima:
        return "Recuperação"
    else:
        return "Reprovado"
    


def main():
    """
    Função principal do programa
    - Lista com as disciplinas
    - Média mínima de aprovação 
    """

    #lista com as disciplinas
    disciplinas = ["Python", "Java", "Banco de Dados"]
    media_aprovacao = 7.0

    print( f'\n*--Sistema de Cálculo de Notas--*')
    #percorre a lista de disciplinas
    for disciplina in disciplinas:
        print(f'Disciplina de: {disciplina}')

        #lista com as notas
        notas = []

        #obter as notas por disciplina, 3 notas por disciplina
        for i in range(3):
            nota = float(input(f"Digite a {i+1}º nota: ")) #pegando as notas conforme a pessoa digita / o contador começa com 0 sempre, então o +1 faz ficar com a ordem certa
            notas.append(nota) #coloca a nota na lista
        
        #chamar as funções calcular média e verificar aprovação
        media_final = calcular_media(notas)
        status = verificar_aprovacao(media_final, media_aprovacao)
        print(f" A média final em {disciplina}: foi de {media_final:.2f}")
        print(f"Status: {status}")

#Programa Principal
main()