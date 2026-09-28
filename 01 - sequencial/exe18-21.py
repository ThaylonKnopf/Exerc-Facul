#18 - Leia as 
# horas normais, as 
# horas extras, o 
# valor da hora e o 
# percentual de desconto. 
# A hora extra vale 50% a mais. 
# Mostre o salário bruto, o desconto e o salário líquido.

horasNormais = float(input("Quantas horas trabalhadas ? "))
horasExtras = float(input("Quantas horas extras trabalhadas ? "))
valorHora = float(input("Qual o valor da hora ? "))
percDesc = float(input("Qual o percentual de desconto ? "))
valBruto = ((horasNormais * valorHora) +  (horasExtras * (valorHora * 1.5)))
valDesc = ((horasNormais * valorHora) +  (horasExtras * (valorHora * 1.5)))* (percDesc/100)
valLiq = valBruto-valDesc


print(f"Salario bruto é de {valBruto} o valor do desconto é de {valDesc} e o salario liquido é de {valLiq}  ")

#------------------------------

#21.Leia uma quantidade de minutos e mostre no formato hh:mm e também em segundos.

minutos = int(input("Digite quantos minutos : "))
hora = minutos // 60
resto = minutos % 60
segundos = minutos * 60

print(f"{hora:02d}:{resto} = {segundos} segundos")


