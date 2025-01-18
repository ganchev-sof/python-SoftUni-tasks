deposit_money = float(input())
deposit_term = int(input())
annually_percent = float(input()) / 100

total_sum = deposit_money + deposit_term * ((deposit_money * annually_percent) / 12)

print(total_sum)