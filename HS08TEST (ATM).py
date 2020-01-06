withdraw, balance = input().split()
withdraw = int(withdraw)
balance = float(balance)
if withdraw % 5 == 0 and withdraw < balance:
    remaining_amt = balance - withdraw - 0.5
    print("%.2f" % remaining_amt)
else:
    print("%.2f" % balance)
