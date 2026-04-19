# Write code below 💖

pesos = int(input("What do you have left in pesos: "))
soles = int(input("What do you have left in soles: "))
reais = int(input("What do you have left in reais: "))

pesos_to_usd_rate = 0.00028
soles_to_usd_rate = 0.29
reais_to_usd_rate = 0.20

left_in_USD = (pesos * pesos_to_usd_rate
  + soles * soles_to_usd_rate
  + reais * reais_to_usd_rate)

print(left_in_USD)
