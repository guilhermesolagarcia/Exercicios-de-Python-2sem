
'''
Sistema simplificado de notas de alunos
Contexto: Criar um programa em Python para armazenar o nome
de cada aluno e suas respectivas notas. O programa deve ter
FUNÇÕES que permitem adicionar, remover, atualizar e calcular
a média das notas de cada aluno

Requisitos:
 - dicionário para armazenar os dados dos alunos - chave será o nome 
 do aluno
 - lista para armazenar as notas dos alunos - valores do dicionário
'''

#dicionário para simular a base de dados - alunos
notas_alunos = {
    'João' : [7.5, 8.0, 6.5],
    'Maria' : [9.0, 9.5, 10.0],
    'Pedro' : [5.0, 6.0, 7.0]
}

#Funções
def adicionar_aluno(nome, notas):
    print(f'*-- Adicionando o aluno {nome}')
    if nome not in notas_alunos:
        notas_alunos[nome] = notas
        print(f'Aluno {nome} adicionado com sucesso!')
    else:
        print(f'Aluno {nome} já existe!')

def remover_aluno(nome):
    print(f'*-- Removendo o aluno {nome}... --*')
    if nome in notas_alunos:
        del notas_alunos[nome]
        print(f'Aluno {nome} removido com sucesso!')
    else:
        print(f'Aluno {nome} não existe!')

def adicionar_nota(nome, nova_nota):
    print(f'*-- Adicionando a nota {nova_nota} para o aluno {nome} --*')
    if nome in notas_alunos:
        notas_alunos[nome].append(nova_nota)
        print(f'Nota {nova_nota} foi adicionada para o aluno {nome}')
    else:
        print(f'O aluno {nome} não foi encontrado!')

def calcular_media(nome):
    print(f'*-- Calculando a média das notas do aluno {nome} --*')

    if nome in notas_alunos:
        notas = notas_alunos[nome] #pegando a lista de notas
        
        #media = sum(notas) / len(lista)
        soma = 0
        cont = 0
        for nota in notas:
            soma+=nota
            cont+=1
        media = soma / cont
        return f'A média de {nome} é {media:.2f}'
    else:
        return f'Aluno {nome} não encontrado!'

def listar_alunos():
    print(f'*-- Imprimindo os dados dos alunos... --*')
    print(f' --- Lista de Alunos e Notas ---')
    for aluno, notas in notas_alunos.items():
        print(f'Aluno: {aluno} \nNotas: {notas}')
        print('--------------------------------')

#Programa Principal (teste)
listar_alunos()

adicionar_aluno('Ana', [8.0, 8.5])
listar_alunos()

adicionar_aluno('João', [10])

print(calcular_media('Fernando'))

remover_aluno('Pedro')
listar_alunos()

