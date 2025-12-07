# 
#newQ4.py ---  updated code with improved modularity and fixed Error..
#

'''
The code in this software is designed to maintain the student records. 
See the details of ach funcation
'''


def printNameID(value, isName):
    #This funcation prints the value passed as an argument(parameter) based on
    # on the value of IsName
    if isName:
        print("Student Name: ", value)
    else:
        print("Student ID: ",value)


def printvalue(value, value_type):
    #This prints the value passed as an argument.
    print(f"{value_type} :", value)
    

def sizeofValue(value, value_type):
    #This function calculates the size (i.e. number of characters) in  
    # given  value and prints the size 
    
    size = len(value)
    print(f"Size of {value_type}:", size)
    return size


def printCharByChar(value, value_type): # change the methods name  "printNameChar" to this
    #This function prints the charachter  of the given value one by one.
    print(f"{value_type} characters:")
    for ch in value:
        print(ch, end=' ')
    print()


def InputRecord():
    #This function takes input from user and  returns the entered values.
    
    student_name = input ("Enter student name :")
    student_ID =input ("Enter student ID :")
    return student_name, student_ID

    
if __name__ == "__main__":
    # ask input ----
    student_name, student_ID = InputRecord()

  #process----------------
    name_size = sizeofValue(student_name, "student Name")
    ID_size = sizeofValue(student_ID, "student ID")
   # output will be __________
    
    printNameID(student_name, True)
    printNameID(student_ID,False)

    printvalue( name_size, "Name")
    printvalue(ID_size, "ID")

    printCharByChar (student_name, "Name")
    printCharByChar(student_ID, "ID")



