P = int(input('Enter the Principal Amount: '))
T = int(input('Enter the Time: '))
R = int(input('Enter the Rate: '))

Compound_Interest = P * (1+ (R/100))**T - P

print(f'Compound Interest = {Compound_Interest} Rs.')