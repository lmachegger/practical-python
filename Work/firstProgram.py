# One morning, you go out and place a dollar bill
# on the sidewalk by the Sears tower in Chicago.
# Each day thereafter, you go out double the number of bills.
# How long does it take for the stack of bills to exceed the height of the tower?

bill_thickness = 0.11 * 0.001
sears_height = 442

days = 1
num_tickets = 1

while num_tickets * bill_thickness < sears_height:
    days += 1
    num_tickets *= 2

print('days: ', days)
print('number of bills: ', num_tickets)
print('height of stack:', num_tickets * bill_thickness)
