# Exercício 1: leia o nome e o ano de nascimento e mostre: "Fulano, você tem X anos em 2026".
nome = input("Qual seu nome ?")
ano = int(input("Qual ano voce nasceu ?"))

print(f"{nome}, voce tem {2026 - ano} em 2026")



# Exercício 2: leia 4 notas e mostre a média. Se a média for 7 ou mais, mostre também a frase "Parabéns!"… brincadeira, condição é mais pra frente. Só a média mesmo.
n1 = float(input("Nota 1 :"))
n2 = float(input("Nota 2 :"))
n3 = float(input("Nota 3 :"))
n4 = float(input("Nota 4 :"))

media = float((n1 + n2 + n3 + n4)/4)

if media >= 7:
    print(f"Aprovado sua media é {media} !")

else: 
     print(f"Reprovado sua media é {media} !")
