price_per_kg_skumriq = float((input()))
price_per_kg_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

price_palamud = price_per_kg_skumriq + price_per_kg_skumriq * 0.60
price_safrid = price_per_kg_caca + price_per_kg_caca * 0.80
price_midi = 7.50

total_palamud = price_palamud * kg_palamud
total_safrid = price_safrid * kg_safrid
total_midi = price_midi * kg_midi

total_sum = total_palamud + total_safrid + total_midi

print(f"{total_sum:.2f}")
