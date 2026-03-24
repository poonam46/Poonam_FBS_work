from Q1 import Emp

def addRecord():
        id = input("Enter ID : ")
        name = input("Enter NAME : ")
        basic = input("Enter BASIC : ")

        emp_obj = Emp(id, name, basic)
        str_obj = str(emp_obj)

        with open( root + 'empInfo', 'a') as fp:
            fp.write(str_obj + '\n')
            print('Data added successfully...')


def searchRecord():
    id = input("Enter ID : ")
    fp = open(root + 'empInfo' , 'r' ) 
    for emp in fp:
        emp_list = emp.split(', ')
        if(emp_list[0] == id):
            print('Employee Found')
            print(emp)
            #found = True
            break
    else:
        print('Employee not found')

def deleteRecord():
    id = input("Enter ID : ")
    fp = open(root + 'empInfo' , 'r' ) 
    chk_id = False
    all_emp_list = []
    for emp in fp:
        emp_list =  emp.split(', ')
        if(emp_list[0] == id):
            chk_id = True
            continue
        else:
            all_emp_list.append(emp)
    if(chk_id):
        fp1 = open(root + 'empInfo' , 'w' ) 
        for emp in all_emp_list:
            fp1.write(emp)
        print('Data deleted successfully...')
    else:
        print(f'{id} employee not exist.')

def updateRecord():
    id = input('Enter ID : ')
    fp = open(root + 'empInfo' , 'r')
    chk_id = False
    all_emp_list = []
    print("NOTE : If don't want to change the field, leave field blank")
    for emp in fp:
        emp_list =  emp.split(', ')
        if(emp_list[0] == id):
            chk_id = True
            emp_list[1] = input(f'Enter new Name ({emp_list[1]}) : ') or emp_list[1]
            emp_list[2] = (input(f'Enter new Basic ({emp_list[2].strip('\n')}) : ') + '\n') or emp_list[2]

            emp_obj = Emp(emp_list[0], emp_list[1], emp_list[2])
            all_emp_list.append(str(emp_obj))
        else:
            all_emp_list.append(emp)
    if(chk_id):
        fp1 = open(root + 'empInfo' , 'w' ) 
        for emp in all_emp_list:
            fp1.write(emp)
        print('Data updated successfully...')
    else:
        return f'{id} employee not exist.'



def displayAllRecord():
    fp = open(root + 'empInfo' , 'r')
    for line in fp:
        print(line)


def main():
    global root
    root = 'Core Python/Python  Assignments/Assignment 22/'
    
    ch = 0
    while(ch != '6'):
        print('''Select the option : 
              1. Add a record
              2. Search record using id
              3. Delete record using id
              4. Edit record using id
              5. Display all records
              6. Exit ''')
        
        ch = input("Enter the your choice : ")

        if(ch == '1'):
            addRecord()
        elif(ch == '2'):
            searchRecord()
        elif(ch == '3'):
            deleteRecord()
        elif(ch == '4'):
            updateRecord()
        elif(ch == '5'):
            displayAllRecord()
        elif(ch == '6'):
            print("Thank you...!")
        else:
            print("Invalid Choice")



main()