'''
dicionario = {key: value}
'''

d = {1: "Ana", 2: "Camila", 3:"Joao"}

print(d)
print(d[2])

print("*" * 15)
for x in d:
    print(x)
print("*" * 15)

for y in d.keys():
    print(y)
print("*" * 15)

for z in d.items():
    print(z)
print("*" * 15)

for w in d.values():
    print(w)
print("*" * 15)

d[40] = "Pedro" #nao precisa ser sequencial, posso colocar qualquer coisa como chave
d[3] = "Maria" #sobrescreve
print(d)



