#!/usr/bin/python3

# lista = ['Arroz', 'Feijão', 'Sal', 'Açúcar', 'Temperos']
# lista.append('Paçoca')





# print(lista[-2])

# lista.insert(1,'Sabão em pó')
# print(lista)
# #lista.pop(4)

# lista.sort()

# print(lista)
# lista3d = [
#     [2,3,4,5],
#     [3,4,5,6],
#     [7,5,7,8]

# ]

# print(len(lista))
# print(lista.index('Açúcar'))
#print(lista3d[2][0])
# print(lista[1:4:2])

# tupla = ('Maçã', 'Banana', 'Laranja', 'Abacaxi', 'Uva')

# tupla.append('Manga')
# print(tupla)

# Criando um dicionário

# apresentacoes = {
#     'Paulista': 'Salve',
#     'Carioca': 'Eae',
#     'Pirata': 'Argh',
#     'Mineiro': 'Pão de queijo',
#     'Acre': 'Barulhos de Dinossauro'
# }

# #Acessando índices em dicionários

# print(apresentacoes['Paulista'])

# #Criando um dicionário com multi-valores internos

# linguagem_favorita = {
#     'Daniel': {
#         'linguagem': 'Python',
#         'Tempo_de_experiencia': 4,
#     },
#     'Olympio': {
#         'linguagem': 'R',
#         'linguagem2': 'VBA',
#         'Tempo_de_experiencia':10,
#     },
   
# } 
# print(linguagem_favorita.get('Daniel')['linguagem'])

# #Acesso a todas as chaves

# print(linguagem_favorita.keys())

# #Acesso aos valores
# print(linguagem_favorita.values())

# #Acesso aos itens

# print(linguagem_favorita.items())


##########
###Números
##########

somar = 2+2
print(somar)

subtrair = somar -2

multiplicar = subtrair *3.5

divisao = multiplicar/5

print (f'Somar = {somar}, subtrair = {subtrair}, multiplicar = {multiplicar} e dividir = {divisao}')

potencia = 2**2
raiz = 2**(1/3)


print(f'Potência = {potencia}, raiz = {raiz}, prova real = {raiz**3}')

letras = 'abcdefghi'

print(letras.split('c')[0])