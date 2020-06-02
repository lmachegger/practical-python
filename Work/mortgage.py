# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

additionalPaymentStartMonth = 60
additionalPaymentEndMonth = 108
additionalPayment = 1000

while principal > 0:
    months += 1
    if(months <= additionalPaymentEndMonth and months > additionalPaymentStartMonth):
        principal = principal * (1+rate/12) - payment - additionalPayment
        total_paid = total_paid + payment + additionalPayment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    if(principal < 0):
        diff = abs(0 - principal)
        total_paid -= diff
        principal += diff

    print(months, round(total_paid, 2), round(principal, 2))

print('Total paid', total_paid)
print('months: ', months)
