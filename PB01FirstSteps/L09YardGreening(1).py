area = float(input('Enter the area: '))

gross_cost = area * 7.61
discount = gross_cost * 0.18
net_cost = gross_cost - discount

print(f'The final price is : {net_cost:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')