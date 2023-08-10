#Calculate exchange rate of diff currency🪙

#user pesos
pesos = int(input("What do you have left in pesos: "))
reais = int(input("What do you have left in reais: "))
soles = int(input("What do you have left in soles: "))

pesos_to_usd = pesos * 0.00025
reais_to_usd = reais * 0.2
soles_to_usd = soles * 0.27

usd_total = pesos_to_usd + reais_to_usd + soles_to_usd

print('You total left is')
print(usd_total)

