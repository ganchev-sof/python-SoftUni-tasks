price_pens = 5.80
price_markers = 7.20
price_chemicals = 1.20

packet_of_pens = int(input())
packet_of_markers = int(input())
chemicals = int(input())
discount = int(input()) / 100

sum_supplies = ((packet_of_pens * price_pens)
                + (price_markers * packet_of_markers)
                + (chemicals * price_chemicals))
total_sum = sum_supplies - (sum_supplies * discount)

print(total_sum)
