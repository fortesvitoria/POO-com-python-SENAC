#agenda {
# nome: [telefone]
# }
# agenda = {
#     "Ana": [51992117599],
#     "Vitoria":[51998884775, 5130296666]
# }

def print_agenda(agenda):
    if agenda: #se tenho algum elemento
        print(agenda)
    else:
        print("Agenda vazia.")

def add_agenda(agenda,key, value):
    if key in agenda:
        print("Existe")
        agenda[key].append(value)
    else:
        print("Não existe")
        agenda[key] = [value] #value vira lista

agenda = {
    "Ana": [51992117599],
    "Vitoria":[51998884775, 5130296666]
}

print(agenda[0])

# while True:
#     print("--- Menu ---")
#     print("1 - Adicionar")
#     print("2 - Exibir na tela")
#     escolha = input("Escolha: ")
#     if escolha == "1":
#         chave = input("Digite o nome")
#         telefone = input("Digite o telefone")
#         add_agenda(agenda, chave, telefone)
#     if escolha == "2":
#         print_agenda(agenda)


