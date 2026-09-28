#8. Trocar A e B
a = int(input("Digite um valor : "))
b = int(input("Digite um valor : "))
aux = a

a = b
b = aux

print(f" A virou B e seu valor é {a} e B manteve o valor de A é {b} !")


# 14 exercício: leia os dois catetos e mostre a hipotenusa.
cat1 = float(input("Digite o valor do cateto1: "))
cat2 = float(input("Digite o valor do cateto2: "))

print(f"o valor da hipotenusa é {((cat1 ** 2) + (cat2 ** 2))** (1/2):.2f} !")


