l = int(input("Enter the length : "))
b = int(input("Enter the breadth : "))
r = int(input("Enter the radius : "))

r_area = l * b
semi_cir_area = (3.14 * r * r) / 2

total_area = r_area + semi_cir_area

print(f"Area of given figure is {total_area}")

r_peri = 2 * l + b
semi_cir_peri = 3.14 * r

total_peri = r_peri + semi_cir_peri

print(f"Perimeter of given figure is {total_peri}")


