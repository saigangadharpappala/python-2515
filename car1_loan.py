on_road = 1800000
down_payment = 550000
bank_interest = 10
P = total_loan = on_road - down_payment
N = loan_period_months = 18
R = interest_permonth = (bank_interest/12)/100
emi = (P*R*(1+R)**N) / ((1+R)**N-1)
print(emi)
