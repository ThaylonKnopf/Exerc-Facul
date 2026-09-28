#Exercício 3: leia um valor em dólares e a cotação, e mostre quanto dá em reais.

valorDolar = float(input("Qual o valor em Dólar $ ?"))
cotacaoDolar = 5.25
valorConvertido = 5.25 * valorDolar

print(f"Seu valor em real é : R$ {valorConvertido}")


#Exercício 4: leia um número e mostre o quadrado, o cubo, a raiz quadrada e a raiz cúbica.
n1 = float(input("Digite o valor a ser convertido : "))

valorCubo = n1 * n1 * n1
valorRaiz = n1 ** (1/2)
valorRaizCubica = n1 ** (1/3)

print(f"O valor do cubo é : {valorCubo}")
print(f"O valor da raiza quadrada é : {valorRaiz}")
print(f"O valor do raiz cubica é : {valorRaizCubica}")