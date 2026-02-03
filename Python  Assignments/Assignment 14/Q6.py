numbers = [10,2,14,5,4,12,7]

product = set()
pairs = {}

for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        prod = numbers[i] * numbers[j]
        product.add(prod)
        pairs[prod] = (numbers[i],numbers[j])

        #print(pairs[prod])

max_prod = max(product)

print("Numbers whose product is maximum : ",pairs[max_prod])

        

# #print(product)
# mul_set = set(product)
# mul_list = list(mul_set)

# max = mul_list[0]

# for ele in mul_list:
#     if ele > max:
#         max = ele

# print(max)




