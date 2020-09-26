import os  
import shutil as shut
import itertools as it
import csv

textfile = "python_assessment.txt"

#Function to read data fom file and print in one statement
def readFile():
    file = open(textfile, 'r')
    lines = file.read()
    print(lines)
    file.close()

#Function to add user
def addnewid():
    idList = []

    with open(textfile, newline = '') as users:
        user_reader = csv.reader(users, delimiter='\t')
        for user in enumerate(user_reader):
            idList.append(int(user[1][0]))

    idList.sort()
    newId = idList[-1]
    addUserDetail(newId + 1)
    

#Function to input new user details
def addUserDetail(newid):
    firstname = input("Please enter first name: ")
    secondname = input("Please enter surname: ")
    address1 = input("Please enter house number and street name: ")
    address2 = input("Please enter city: ")
    postcode = input("Please enter postcode: ")
    telephonenumber = input("Please enter telephone number: ")
   
    newline=("\n" + str(newid) + "\t" + firstname + "\t" + secondname + "\t" + address1 + "\t" + address2 + "\t" + postcode + "\t" + telephonenumber)

    file = open(textfile, 'a')
    file.write(newline)
    file.close()

#Function to remove User
def RemoveUser():

    userID = input("Please enter the ID of the user you want to remove: ")

    with open(textfile, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not line.startswith(userID):
                file.write(line)
        file.truncate()

#Function to find information about an User
#Created as a menu so each different field can be searched
def UserInfomenu():

#Nested function created for options 1-6 as they follow the same logic and procedure
#Option 7 is unique because function kept returning "index out of range"    
    def columnsearch():
        results = []

        file = open(textfile, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            if value == line.split("\t")[option-1]:
                results.append(line)

        for result in results:
            print(result)
        
    while True:
        print("--User Search Menu--")
        print("1 - ID")
        print("2 - First Name")
        print("3 - Surname")
        print("4 - Street")
        print("5 - City")
        print("6 - Postcode")
        print("7 - Telephone Number")
        print("8 - Return to main menu")
    
        option = int(input("Select Option: "))
        
        if option == 1:
            value = input("Please enter ID: ")
            columnsearch()
                  
        elif option == 2:
            value = input("Please enter first name: ")
            columnsearch()
            
        elif option == 3:
            value = input("Please enter surname: ")
            columnsearch()
                
        elif option == 4:
            value = input("Please enter Street: ")
            columnsearch()
                        
        elif option == 5:
            value = input("Please enter City: ")
            columnsearch()
                        
        elif option == 6:
            value = input("Please enter Postcode: ")
            columnsearch()
                        
        elif option == 7:
            teleno = input("Please enter Telephone Number: ")
            for line in lines:
                line = line.rstrip()  
                if teleno in line:
                    print(line)

        elif option == 8:
            break
        else:
            print("INVALID OPTION! Please choose a valid option")

  
#Function to make a copy of file to be used as backup
def copyFile():
    source = textfile
    destination = "python_assessment(copy).txt"
    shut.copy(source, destination) 

    print("File copied successfully.") 
    print("Destination path:", destination)


#Function to find update information about an User
#Created as a menu so each different field can be searched and updated
def UpdateUserInfomenu():
    while True:
        print("--Update User Info Menu--")
        print("1 - First Name")
        print("2 - Surname")
        print("3 - Street")
        print("4 - City")
        print("5 - Postcode")
        print("6 - Telephone Number")
        print("7 - Return to main menu")

        option = int(input("Select Option: "))
        
        if option == 1:
            oldfirstname = input("Please enter first name to replace: ")
            newfirstname = input("Please enter new first name: ")
            with open(textfile, "r") as file:
                lines = file.read()
                file.close()
                
                newline = lines.replace(oldfirstname, newfirstname)

            with open(textfile, "w") as file:
                file.write(newline)
                file.close()
                
            print("Information updated successfully!")
                
        elif option == 2:
            oldsurname = input("Please enter surname to replace: ")
            newsurname = input("Please enter new surname: ")

            with open(textfile, "r") as file:
                lines = file.read()
                file.close()
                
                newline = lines.replace(oldsurname, newsurname)

            with open(textfile, "w") as file:
                file.write(newline)
                file.close()

            print("Information updated successfully!")
 
        elif option == 3:
            oldadd = input("Please enter address to replace: ")
            newadd = input("Please enter new address: ")

            with open(textfile, "r") as file:
                lines = file.read()
                file.close()
                
                newline = lines.replace(oldadd, newadd)

            with open(textfile, "w") as file:
                file.write(newline)
                file.close()

            print("Information updated successfully!")
                
        elif option == 4:
            oldcity = input("Please enter city to replace: ")
            newcity = input("Please enter new city: ")

            with open(textfile, "r") as file:
                lines = file.read()
                file.close()
                
                newline = lines.replace(oldcity, newcity)

            with open(textfile, "w") as file:
                file.write(newline)
                file.close()

            print("Information updated successfully!")

        elif option == 5:
            oldcode = input("Please enter postcode to replace: ")
            newcode = input("Please enter new postcode: ")

            with open(textfile, "r") as file:
                lines = file.read()
                file.close()
                
                newline = lines.replace(oldcode, newcode)

            with open(textfile, "w") as file:
                file.write(newline)
                file.close()

            print("Information updated successfully!")

        elif option == 6:
            oldnumber = input("Please enter telephone number to replace: ")
            newnumber = input("Please enter new telephone number: ")

            with open(textfile, "r") as file:
                lines = file.read()
                file.close()
                
                newline = lines.replace(oldnumber, newnumber)

            with open(textfile, "w") as file:
                file.write(newline)
                file.close()

            print("Information updated successfully!")

        elif option == 7:
            break
        else:
            print("INVALID OPTION! Please choose a valid option")

#Menu placing all functions together to work more efficiently
while True:
    print("*****MAIN MENU*****")
    print("1 - Read data")
    print("2 - Add user")
    print("3 - Remove user")
    print("4 - Find an user")
    print("5 - Backup")
    print("6 - Update user details")
    print("7 - Exit program")
    
    option = int(input("Select Option: "))
    if option == 1:
        readFile()
    elif option == 2:
        addnewid()
    elif option == 3:
        RemoveUser()
    elif option == 4:
        UserInfomenu()
    elif option == 5:
        copyFile()
    elif option == 6:
        UpdateUserInfomenu()
    elif option == 7:
        print("Bye")
        exit(2)
    else:
        print("INVALID OPTION! Please choose a valid option")
