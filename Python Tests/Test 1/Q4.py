area = float(input("Enter the area of wall :"))
int_cost = float(input("enter the Interior Cost of wall : "))
ext_cost = float(input("enter the Exterior Cost of wall : "))

total_int_cost = 8 * area * int_cost
total_ext_cost = 7 * area * ext_cost

total_cost = total_int_cost + total_ext_cost

print(f"The cost of to paint the building walls is {total_cost} Rs.")
