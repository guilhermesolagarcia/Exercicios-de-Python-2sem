'''
Principais metodos (mais comuns)
- keys(): retorna uma "visao" de todas as chaves do dicionario
- values(): retorna uma "visao" de todos os valores do dicionário
- itens(): retorna uma "visão" dos pares de chave valor
- get(): retorna um valor (de forma segura) | retorna um valor padrão, caso a chave não seja encontrada
 
'''
 

carro = {
    "marca" : "Jeep",
    "modelo" : "Compass",
    "ano" : 2025
}

#iterando sobre as chaves do dicionário
for chave in carro.keys():
    print(carro)

#iterando sobre os valores do dicionário
for valor in carro.values():
    print(valor)

#iterando sobre os pares de chave-valor do dicionário
for chave, valor in carro.items():
    print(f'{chave} : {valor}')

#acesso ao dicionário com chave inexistente
#print(carro['motor'])


#acesso a um elemento do dicionário com método get() - evita o erro
print(f'cor: {carro.get('motor', 'Não Definido!')}')

print(f'marca: {carro.get('marca', 'Não Definido!')}')