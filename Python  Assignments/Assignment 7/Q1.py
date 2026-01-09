for i in range(1,6):
    for j in range(1,6 - i):
        print(" ", end = " ")

    for j in range(1,2 * i):
        if j == (2 * i) - 1 or j == 1:
            print("*" , end = " ")
        else:
            print(" ", end = " ")

    print()


    #for lower part
for i in range(5,0,-1):
    for j in range(1,6 - i):
        print(" ", end = " ")

    for j in range(1,2 * i):
        if j == (2 * i) - 1 or j == 1:
            print("*" , end = " ")
        else:
            print(" ", end = " ")
    print()


#         *
#       *   *
#     *       *
#   *           *
# *               *
# *               *
#   *           *
#     *       *
#       *   *
#         *