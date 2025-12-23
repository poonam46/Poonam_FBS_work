basic = float(input("Enter basic salary: "))

da = 0.10 * basic      # Dearness Allowance (10%)
ta = 0.12 * basic      # Travel Allowance (12%)
hra = 0.15 * basic     # House Rent Allowance (15%)

total_salary = basic + da + ta + hra

print(f"Basic Salary: {basic}")
print(f"DA (10%): {da}")
print(f"TA (12%): {ta}")
print(f"HRA (15%): {hra}")
print(f"Total Salary: {total_salary}")