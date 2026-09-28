#Exercício 5: leia watts por hora, horas por dia, dias e o preço do kWh. Mostre o consumo em Wh, em kWh e o valor a pagar

wattsHora = float(input("Quantos Watts por hora ? "))
horasDia = float(input("Horas de uso por dia ? "))
dias = int(input("Quantos dias de uso ?"))
precoKWh = float(input("Qual o preco do KWh na sua cidade ?"))

consumoWatts = wattsHora * horasDia * dias
consumoKWh = consumoWatts / 1000
valorConsumo = consumoKWh * precoKWh

print(f"Consumo em Wh: {consumoKWh}")
print(f"Consumo em KWh: {consumoWatts}")
print(f"Valor a pagar é de : {valorConsumo}")

#-----------------------------------------

"""Exercício 6:Seu exercício: leia uma temperatura em Celsius e mostre em Fahrenheit e em Kelvin. Depois leia uma em Fahrenheit e mostre em Celsius.
F = C × 9 ÷ 5 + 32
K = C + 273,15
C = (F − 32) × 5 ÷ 9
Para conferir: 0 °C = 32 °F = 273,15 K e 212 °F = 100 °C.
"""

celsius = float(input("Qual a temperatura em Celsius ? "))

print(f"A temperatura em Fahrenheit é de {celsius * 9 / 5 + 32}")
print(f"A temperatura em Kelvin é de {celsius + 273.15}")