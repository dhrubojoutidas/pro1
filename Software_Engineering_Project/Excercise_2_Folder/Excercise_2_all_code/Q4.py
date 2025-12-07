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


def printvalue(value):
    #This prints the value passed as an argument.
    print("Value :", value)
    


def sizeofValue():
    #This function calculates the size (i.e. number of characters) in 
    #Stduent name and ID and store the size in global variables.
    global name_size 
    name_size = len(student_name)
    global ID_size
    ID_size = len(student_ID)



def printNameChar():
    #This function prints the stduent name charachter by character.
    for ch in student_name:
        print(ch, end=' ')
    print()

def printIDChar():
    #This funcation claculates the student ID charachter by character.
    for num in student_ID:
        print(num, end=' ')
    print()


def InputRecord():
    #This function takes input from user and store the student name and ID
    #in global variables. Call the other funcations for the printing and
    #size calculationa and printing character by character.
    global student_name
    global student_ID

    # taking input for student name and ID
    student_name = input("Enter student name: ")
    student_ID = input("Enter student ID: ")

    
if __name__ == "__main__":
    
    InputRecord()

    sizeofValue()

    printNameID(student_name, True)
    printNameID(student_ID, False)

    printvalue(name_size)
    printvalue(ID_size)

    printNameChar()
    printIDChar()

