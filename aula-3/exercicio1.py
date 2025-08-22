'''
Dicionários

- Construtor: dict()
- Sintaxe: nome = {"chave" : valor}
'''

aluno = {'nome':'João','idade':25,'cidade':'São Paulo'}


'''
Outro exemplo: 

aluno = {'nome':'João',
          'idade':25,
          'cidade':'São Paulo'}
'''

#Imprimindo os dados do aluno
print(aluno)

#Acesso a um valor através da chave
print(f'Nome: {aluno['nome']}')

#Adicionar um novo elemento no dicionário
aluno['area'] = 'Desenvolvedor'

print(aluno)


#Alterando um valor de uma chave
aluno['idade'] = 30
print(f'Nova idade: {aluno['idade']}')

#Removendo um elemento do dicionário
del aluno['cidade']
print(aluno)