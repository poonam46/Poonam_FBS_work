dict1 = {"Name" : "Poonam","Age" : 23, "City" : "Nashik" }

key = input("Enter the key to check : ")

if key in dict1:
    print(f"{key} is available")
else:
    print(f"{key} is not available")