__author__ = 'EmployeeProjectGroup'

from time import localtime
import sys
from random import randint


class Employee:

    #Common base for all employees
    emp_counter = 0


    #Create constructor to initialise objects
    def __init__(self, name, id, pin, work_status):
        self.name = name
        self.id = id
        self.pin = pin
        self.work_status = work_status
        Employee.emp_counter += 1



    #Create login method to allow employees sign in
    def login(self):

        #Create variables to hold id and pin
        id = input("\nPlease enter your ID: ")
        pin = ""

        #Allow user to enter pin again when wrongly entered
        while True:
            try:
                pin = int(input("\nPlease enter your pin: "))
                break
            except ValueError:
                #Caution user to enter pin again
                print("\nThe pin must be a number.\n"
                      "PLEASE TRY AGAIN..\n")

        #Check for correct entry of id and pin entered
        if self.id == id and self.pin == pin:
            your_time = localtime()
            exact_time = str(your_time.tm_hour) + ":" + str(your_time.tm_min) + ":" + str(your_time.tm_sec)

            #Print message to screen telling user time logged in
            print("\nYou've logged in at exactly", exact_time, "\n")
        else:
            #Caution user to enter details again when wrongly entered
            print("\nWrong ID/Pin entered!!\n"
                  "ACCESS DENIED\n")



    #Create logout method to allow employees sign out
    def logout(self):

        #Create variables to hold id and pin
        id = input("\nPlease enter your ID: ")
        pin = ""

        #Allow user to enter pin again when wrongly entered
        while True:
            try:
                pin = int(input("\nPlease enter your pin: "))
                break
            except ValueError:
                #Caution user to enter pin again
                print("\nThe pin must be a number.\n"
                      "PLEASE TRY AGAIN..\n")

        #Check for correct entry of id and pin entered
        if self.id == id and self.pin == pin:
            your_time = localtime()
            exact_time = str(your_time.tm_hour) + ":" + str(your_time.tm_min) + ":" + str(your_time.tm_sec)

            #Print message to screen telling user time logged out
            print("\nYou've logged out at exactly", exact_time, "\n")
        else:
            #Caution user to enter details again when wrongly entered
            print("\nWrong ID/Pin entered!!\n"
                  "ACCESS DENIED\n")



    #Create method to allow employees access to view profiles
    def viewProfile(self, emp_no):
        while True:

            #Create variables to hold id and pin
            id = input("\nPlease enter your ID: ")
            pin = ""

            #Allow user to enter pin again when wrongly entered
            while True:
                try:
                    pin = int(input("\nPlease enter your pin: "))
                    break
                except ValueError:
                    #Caution user to enter pin again
                    print("\nThe pin must be a number.\n"
                          "PLEASE TRY AGAIN..\n")

            #Check for correct entry of id and pin
            if self.id == id and self.pin == pin:
                #Print profile to screen
                print("\nEmployee No.: ", emp_no,
                      "\nID No.:", self.id, "\n"
                      "Name:", self.name, "\n"
                      "Work Status:", self.work_status, "\n")
                break
            else:
                #Caution user to try enter details again when wrongly entered
                print("\nWrong ID/Pin entered!!\nACCESS DENIED\n")
                continue




class Administrator(Employee):

    #Create constructor to initialise objects
    def __init__(self, name, id, pin, work_status, system_password):
        Employee.__init__(self, name, id, pin, work_status)
        self.system_password = system_password



    #Create method to allow administrator access to view all employee profiles
    def viewAllProfiles(self, employee_list):

        print("\nProfile List\n____________")
        a = 0

        #Print details of all employees in the employee list
        for i in employee_list:
            if type(i) == Doctor:
                print("\nEmployee No: ", a, "\n"
                      "ID No.:", i.id, "\n"
                      "Name:", i.name, "\n"
                      "Work Status:", i.work_status, "\n"
                      "Speciality: ", i.speciality,
                      "\nWorktype: DOCTOR\n")
            else:
                if type(i) == Nurse:
                    print("\nEmployee No: ", a, "\n"
                          "ID No.:", i.id, "\n"
                          "Name:", i.name, "\n"
                          "Work Status:", i.work_status, "\n"
                          "Worktype: NURSE\n", )
                else:
                    print("\nEmployee No: ", a, "\n"
                          "ID No.:", i.id, "\n"
                          "Name:", i.name, "\n"
                          "Work Status:", i.work_status, "\n"
                          "Worktype: ADMINISTRATOR\n")

            a += 1



    #Create method to add employees
    def addEmployee(self, employee_list):

        #Create variables to hold and receive employee details
        name = input("\nPlease enter the name of the employee: ")
        name = name.upper()
        id = generateEmployeeID()
        pin = generateEmployeePin()
        workStatus = "INSERVICE"

        #Check for type of worker so as to receive necessary details
        speciality = input("\nPlease enter the speciality if it's a doctor otherwise enter none: ")
        speciality = speciality.upper()


        if speciality == "none":
            emp = Nurse(name, id, pin, workStatus)
        else:
            emp = Doctor(name, id, pin, workStatus, speciality)

        #Add employee to list
        employee_list.append(emp)
        print("\nEmployee has been successfully added!!!\n")


    #Create method to edit employee profiles
    def editEmployeeProfile(self, employeeList):

        while True:
            try:
                #Receive input to determine index of employee in list
                ans = int(input("\nPlease enter the employee's number: "))

                #Check to make sure number enter falls within index of employee list
                if ans >= len(employeeList):
                    print("\nNumber entered doesn't fall within the employee List\n"
                          "PLEASE TRY AGAIN!!\n")
                    continue

                while True:
                    try:
                        option = int(input("\nWhich portion of the employee profile would you like to change?\n"
                                           "1. Name\n"
                                           "2. ID\n"
                                           "3. Pin\n"
                                           "4. Work Status\n"
                                           "5. End editting employee profile\n\n"
                                           "Option: "))

                        #Edit employee profile based on the option selected
                        if option == 1:
                            Str = input("\nThe employee's name is " + employeeList[ans].name + "\n" +
                                        "Enter new employee name: ")
                            employeeList[ans].name = Str.upper()
                            print("\nEmployee name has been successfully changed to", employeeList[ans].name,
                                  "Thank you\n")
                        elif option == 2:
                            print("\nThe employee's ID is ", employeeList[ans].id)
                            employeeList[ans].id = generateEmployeeID()
                            print("\nEmployee ID has been successfully changed to" + employeeList[ans].id +
                                  "Thank you\n")
                        elif option == 3:
                            print("The employee's pin is ", employeeList[ans].pin)
                            employeeList[ans].pin = generateEmployeePin()
                            print("\nEmployee pin has been successfully changed to", employeeList[ans].pin,
                                  "Thank you\n")
                        elif option == 4:
                            wk_status = input("The employee's work status is " + employeeList[ans].work_status + "\n" +
                                              "Enter new work Status: ")
                            employeeList[ans].work_status = wk_status.upper()
                            print("\nEmployee work status has been successfully changed to",
                                  employeeList[ans].work_status, "Thank you!!\n")
                        elif option == 5:
                            break
                        else:
                            print("\nOops!! Please try again and enter a number that falls within the option list!")
                            continue
                    except ValueError:
                        print("\nOops!! Please try again and enter a number within the option list!")
                        continue
            except ValueError:
                print("\nPlease try again and enter a correct employee number\n")
                continue

            break

        #Notify administrator of successful edit of employee profiles
        print("\nEmployee profile(s) have been successfully edited.\n")



class Doctor(Employee):

    ##Create constructor to initialise objects
    def __init__(self, name, id, pin, work_status, speciality):
        Employee.__init__(self, name, id, pin, work_status)
        self.speciality = speciality




class Nurse(Employee):
    ##Create constructor to initialise objects
    def __init__(self, name, id, pin, work_status):
        Employee.__init__(self, name, id, pin, work_status)



    #Create method for Nurse to input patient vitals
    def takeVital(self):
        vital = input("\nEnter patient vital to send to patient folder")
        print("\nPatient vital entered is", vital)




#Create method to generate employee id
def generateEmployeeID():

    the_type = input("\nPlease the employee type: ")

    if the_type == "Doctor":
        baseID = "DOC/"
        numb = input("\nPlease enter last three pin number to add to base pin: ")
        id = baseID + numb
        return id
    else:
        baseID = "NUR/"
        numb = input("\nPlease enter last three pin number to add to base pin: ")
        id = baseID + numb
        return id




#Create method to generate employee pin
def generateEmployeePin():

    the_type = input("\nPlease the employee type: ")

    if the_type == "Doctor" or the_type == "DOCTOR" or the_type == "doctor":
        pin = randint(50000, 99999)
        return pin
    else:
        pin = randint(10000, 49999)
        return pin




#Create instances of employees already in the workplace
emp1 = Doctor("ANDY ALORWU", "DOC/123", 56789, "INSERVICE", "GYNAECOLOGIST")
emp2 = Nurse("DENNIS OPOKU BOADU", "NUR/256", 35421, "INSERVICE")
emp3 = Administrator("SAMANTHA TETTEH", "ADMIN/087", 82459, "INSERVICE", "ADMINh0sp1t@l")
emp4 = Nurse("EUNICE AGYEI", "NUR/357", 86325, "INSERVICE")
emp5 = Doctor("ANTHONY ALEXIS ADOASI", "DOC/489", 75684, "INERVICE", "NATUROPATHY")



#Store instances created in employee list
employeeList = [emp3, emp1, emp2, emp4, emp5]



#Simulate the operation of employees
while True:
    try:
        time_now = localtime()

        if time_now.tm_hour in [5, 6, 7, 8, 9, 10, 11]:
            print("\nGOOD MORNING\n"
                  "Welcome to the Office!!\n")
        elif time_now.tm_hour in [12, 13, 14, 15, 16]:
            print("\nGOOD AFTERNOON\n"
                  "Welcome to the Office!!\n")
        else:
            print("\nGOOD EVENING\n"
                  "Welcome to the Office!!\n")

        ans = int(input("\nWhat is your employee number: "))

        if ans >= len(employeeList):
            print("\nEmployee number is out of range!!\n"
                  "Try again\n")
            continue

        an = int(input("\nPlease select an option"
                       "\n1. Login\t\t\t2. View Profiles\t\t\t3. Logout\t\t\t4. Administrator\n\n"
                       "option: "))

        if an == 1:
            employeeList[ans].login()
            continue
        elif an == 2:
            employeeList[ans].viewProfile(ans)
            continue
        elif an == 3:
            islast = input("\nAre you the last employee? y/n\n"
                           "Reply here: ")

            if islast == 'y':
                employeeList[ans].logout()
                print("\nProcess shutting down.......")
                sys.exit(0)
            else:
                employeeList[ans].logout()
                continue
        elif an == 4:
            while True:
                system_passwd = input("\nPlease enter the system password: ")

                if system_passwd == employeeList[ans].system_password:
                    print("\nACCESS GRANTED\n")

                    while True:
                        try:
                            answ = int(input("\nPlease select another option\n\n"
                                             "1. View All Profiles\n"
                                             "2. Edit Profiles\n"
                                             "3. Add Employee\n"
                                             "4. End Administrator session\n\n"
                                             "Option: "))
                            #Reply based on option selected
                            if answ == 1:
                                employeeList[ans].viewAllProfiles(employeeList)
                            elif answ == 2:
                                employeeList[ans].editEmployeeProfile(employeeList)
                            elif answ == 3:
                                employeeList[ans].addEmployee(employeeList)
                            elif answ == 4:
                                print("\nExiting Administrator mode.......\n")
                                break
                            else:
                                print("\nPlease try again and enter a number in range.\n")
                                continue
                        except ValueError:
                            print("\nPlease try again and enter a correct number.")
                            continue
                else:
                    print("\nACCESS DENIED!!\n")
                    continue
                break
        else:
            print("\nPlease try again and enter a number in range\n")
            continue
    except ValueError:
        print("\nPlease try again and select an option in the list.\n")
        continue



