#Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Solicitar a palavra ao usuário
palavra = input("Digite uma palavra: ")

# Inverter a palavra
palavra_invertida = palavra[::-1]

# Verificar se a palavra é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")