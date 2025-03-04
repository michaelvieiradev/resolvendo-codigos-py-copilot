# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitar os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizar uma operação simples (exemplo: soma)
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Divisão por zero não é permitida"

# Exibir os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
