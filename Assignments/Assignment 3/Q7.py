userid = input("Enter the UserId :")
password = input("Enter the Password : ")

c_uid = "poonam123"
c_password = "alpha@135"

if(userid == c_uid and password == c_password):
    print("User entered correct userid and password")
elif(userid != c_uid and password != c_password):
    print("User entered incorrect userid and password")
elif(userid != c_uid):
    print("Incorrect Userid")
else:
    print("Incorrect password")
