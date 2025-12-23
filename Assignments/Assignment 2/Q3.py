# 1 foot = 12 x 2.4 cm => 30.48cm => 0.3048 meters 
# 1 inch = 2.54 cm
# 1 meter = 100 cm

feet = float(input('Enter Feet: '))
inches = float(input('Enter Inches: '))

meters = feet * 0.3048
centimeters = inches * 2.54

print(f'Distance in meters: {meters}')
print(f'Distance in centimeter: {centimeters}')
