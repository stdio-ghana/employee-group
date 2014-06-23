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
        while True:
            try:
                opt = input("Do you want to login? (y/n): ")
                if opt == 'n' or 'N':
                    break
                elif opt == 'y' or 'Y':

                    #Create variables to hold id and pin
                    id = input("\nPlease enter your ID: ")
                    pin = input("\nPlease enter your pin: ")


                    #Check for correct entry of id and pin entered
                    a = open("Employee Details.txt", 'r')
                    data = a.read()
                    a.close()
                    datalist = data.split("\n")
                    access = False
                    for i in datalist:
                        if id == i[:7] and pin == i[9:14]:
                            access = True


                    if access == True:
                        your_time = localtime()
                        hour = your_time.tm_hour
                        min = your_time.tm_min
                        sec = your_time.tm_sec
                        month = your_time.tm_mon
                        day = your_time.tm_mday
                        if min in range(10):
                            minutes = "0" + str(min)
                        else:
                            minutes = str(min)
                        if sec in range(10):
                            seconds = "0" + str(sec)
                        else:
                            seconds = str(sec)
                        if hour in range(10):
                            hour = "0" + str(hour)
                        else:
                            hour = str(hour)
                        if month in range(10):
                            month = "0" + str(month)
                        else:
                            month = str(month)
                        if day in range(10):
                            day = "0" + str(day)
                        else:
                            day = str(day)
                        date_now = str(your_time.tm_year) + "-" + month + "-" + day
                        exact_time = hour + ":" + minutes + ":" + seconds

                        print("\nWriting time to log book..........\n")

                        #Send data to log book
                        fread = open("Employee Log Book.txt", 'a')
                        fread.write("\n" + id + "\t\t" + date_now + "\t\t" + exact_time)
                        fread.close()

                        #Print message to screen telling user time logged in
                        print("\nYou've logged in at exactly", exact_time, "\n")
                        break
                    else:
                        #Caution user to enter details again when wrongly entered
                        print("\nWrong ID OR Pin entered!!\n"
                              "ACCESS DENIED\nPlease Try again\n")
                        continue
                else:
                    print("\nPlease enter a y or n and try again\n")
                    continue
            except IOError:
                print("\nUnable to read file.\nPleae try agian\n")
                continue



    #Create logout method to allow employees sign out
    def logout(self):
        while True:
            try:
                opt = input("Do you want to logout? (y/n): ")
                if opt == "n":
                    break
                elif opt == 'y':
                    #Create variables to hold id and pin
                    id = input("\nPlease enter your ID: ")
                    pin = input("Please enter you pin: ")

                    #Check for correct entry of id and pin entered
                    a = open("Employee Details.txt", 'r')
                    data = a.read()
                    a.close()
                    datalist = data.split("\n")
                    access = False
                    for i in datalist:
                        if id == i[:7] and pin == i[9:14]:
                            access = True

                    if access == True:
                        your_time = localtime()
                        hour = your_time.tm_hour
                        min = your_time.tm_min
                        sec = your_time.tm_sec
                        if min in range(10):
                            minutes = "0" + str(min)
                        else:
                            minutes = str(min)
                        if sec in range(10):
                            seconds = "0" + str(sec)
                        else:
                            seconds = str(sec)
                        if hour in range(10):
                            hour = "0" + str(hour)
                        else:
                            hour = str(hour)
                        exact_time = hour + ":" + minutes + ":" + seconds

                        print("\nWriting to Log Book........\n")

                        #Send data to log book
                        f = open("Employee Log Book.txt", 'r')
                        LogData = f.read()
                        f.close()
                        linelist = LogData.split('\n')
                        for i in linelist:
                            if id == i[:7]:
                                a = i + "\t\t" + exact_time
                                linelist[linelist.index(i)] = a

                        datagain = ""
                        for j in linelist:
                            datagain = datagain + j + "\n"

                        f = open("Employee Log Book.txt", 'w')
                        f.write(datagain)
                        f.close()
                        #Print message to screen telling user time logged out
                        print("\nYou've logged out at exactly", exact_time, "\n")
                        break
                    else:
                        #Caution user to enter details again when wrongly entered
                        print("\nWrong ID/Pin entered!!\n"
                              "ACCESS DENIED\nPlease Try again\n")
                        continue
                else:
                    print("\nPlease enter a y or n and try again\n")
                    continue
            except IOError:
                print("\nUnable to read file.\nPlease Try again\n")
                continue



    #Create method to allow employees access to view profiles
    def viewProfile(self):
        while True:
            try:
                #Create variables to hold id and pin
                id = input("\nPlease enter your ID: ")
                pin = input("Please enter you pin: ")

                #Check for correct entry of id and pin entered
                a = open("Employee Details.txt", 'r')
                data = a.read()
                a.close()
                datalist = data.split("\n")
                access = False
                index = 0
                for i in datalist:
                    if id == i[:7] and pin == i[9:14]:
                        access = True
                        index = datalist.index(i)
                detail = datalist[index]
                if access == True:
                    #Print profile to screen
                    print("\nID No.:" + detail[:7] + "\n"
                          "Pin: " + detail[9:14] + "\n" +
                          "Name:" + detail[16:46] + "\n"
                          "Work Status:" + detail[48:63] + "\n")
                    break
                else:
                    #Caution user to try enter details again when wrongly entered
                    print("\nWrong ID OR Pin entered!!\nACCESS DENIED\n")
                    continue
            except IOError:
                print("\nUnable to read file.\nPlease Try again\n")
                continue




class Administrator(Employee):

    #Create constructor to initialise objects
    def __init__(self, name, id, pin, work_status, system_password):
        Employee.__init__(self, name, id, pin, work_status)
        self.system_password = system_password



    #Create method to allow administrator access to view all employee profiles
    def viewAllProfiles(self):
        while True:
            try:
                #Print details of all employees in the Employee Detail file
                a = open("Employee Details.txt", 'r')
                data = a.read()
                a.close()
                print(data)
                break
            except IOError:
                print("\nUnable to read file.\nPlease Try again\n")
                continue


    #Create method to view log book
    def viewLogBook(self):

        f = open("Employee Log Book.txt", 'r')
        logDetails = f.read()
        f.close()
        print(logDetails)



    #Create method to add employees
    def addEmployee(self):

            #Create variables to hold and receive employee details
            name = input("\nPlease enter the name of the employee: ")
            name = name.upper()
            name = fillString(name)
            ob = 0
            while True:
                try:
                    the_type = int(input("\nPlease the employee type.\n1. Doctor\n2. Nurse \nOption: "))
                    if the_type == 1:
                        ob = 1
                        break
                    elif the_type == 2:
                        ob = 2
                        break
                    else:
                        print("\nEnter a number in the list and Try again\n")
                        continue
                except:
                    print("\nPlease Try again and enter a number.\n")
                    continue

            id = generateEmployeeID(ob)
            pin = generateEmployeePin(ob)
            workStatus = "INSERVICE"
            workStatus = fil(workStatus)

            #Check for type of worker so as to receive necessary details
            speciality = input("\nPlease enter the speciality: ")
            speciality = speciality.upper()
            worktype = ""
            if ob == 1:
                emp = Doctor(name, id, pin, workStatus, speciality)
                worktype = emp.id[:3].upper() + "TOR"
            else:
                emp = Nurse(name, id, pin, workStatus, speciality)
                worktype += emp.id[:3].upper() + "SE"

            while True:
                try:
                    #Add employee to list
                    a = open("Employee Details.txt", 'a')
                    a.write("\n" + emp.id + "\t\t" + emp.pin + "\t\t" + emp.name + "\t\t" + emp.work_status + "\t\t" + worktype + "\t\t" +
                            emp.speciality)
                    a.close()
                    break
                except IOError:
                    print("\nUnable to read file.\nPlease Try again\n")
                    continue

            print("\nAdding Employee to Employees........\n\n"
                  "Employee has been successfully added\n")



    #Create method to edit employee profiles
    def editEmployeeProfile(self):
        while True:
            id = input("Enter the ID of the Employee you would like to edit his/her profile: ")
            end_all_emp = False
            wrong_id = False
            end_ind_emp = False

            while True:
                try:
                    a = open("Employee Details.txt", 'r')
                    data = a.read()
                    a.close()
                    data_list = data.split("\n")

                    for i in data_list:
                        if id == i[:7]:
                            index = data_list.index(i)
                            while True:
                                option = int(input("\nWhich portion of the employee profile would you like to change?\n"
                                                   "1. Name\n"
                                                   "2. Pin\n"
                                                   "3. Work Status\n"
                                                   "4. End editing all employee profile\n\n"
                                                   "Option: "))

                                detail = data_list[index]
                                #Edit employee profile based on the option selected
                                if option == 1:
                                    new_name = input("\nThe employee's name is " + detail[16:46] + "\n" +
                                                     "Enter new employee name: ")
                                    new_name = new_name.upper()
                                    new_name = fillString(new_name)
                                    detail = detail[:16] + new_name + detail[46:]
                                    print("\nEmployee name has been successfully changed to " + new_name +
                                          ".\nThank you\n")
                                    data_list[index] = detail
                                elif option == 2:
                                    print("\nThe employee's pin is " + detail[9:14] + ".\n")
                                    optn = 0
                                    while True:
                                        try:
                                            op = int(input('\nPlease select an option below for employee type\n'
                                                           '1. Doctor\n2. Nurse\noption: '))
                                            if op == 1:
                                                optn = 1
                                                break
                                            elif op == 2:
                                                optn = 2
                                                break
                                            else:
                                                print("\nPlease try again and enter a number in range.\n")
                                                continue
                                        except ValueError:
                                            print("\nPlease try again and enter a number.\n")
                                            continue
                                    newPin = generateEmployeePin(optn)
                                    print("\nEmployee pin has been successfully changed to " + newPin +
                                          ".\nThank you\n")
                                    detail = detail[:9] + newPin + detail[14:]
                                    data_list[index] = detail
                                    print(data_list)
                                elif option == 3:
                                    newWorkStatus = input("The employee's work status is " + detail[48:63] + "\n" +
                                                          "Enter new work Status: ")
                                    newWorkStatus = newWorkStatus.upper()
                                    print("\nEmployee work status has been successfully changed to" + newWorkStatus +
                                          ".\nThank you!!\n")
                                    detail = detail[:48] + newWorkStatus + detail[63:]
                                    data_list[index] = detail
                                elif option == 4:
                                    end_all_emp = True
                                    break
                                else:
                                    print("\nOops!! Please try again and enter a number "
                                          "that falls within the option list!")
                                    continue

                        if i == data_list[-1] and end_ind_emp:
                            if id != i[:7]:
                                print("\nWRONG ID ENTERED\nACCESS DENIED\nPlease try again\n")
                                wrong_id = True
                                end_ind_emp = True
                                break

                    if end_all_emp:
                        # all_details = ""
                        # for j in data_list:
                        #     all_details = all_details + j + "\n"
                        #
                        # f = open("Employee Details.txt", 'w')
                        # f.write(all_details)
                        # f.close()
                        break
                    else:
                        break
                except ValueError:
                    print("\nOops!! Please try again and enter a number within the option list!")
                    continue
                except IOError:
                    print("\nFile Not Found\nPlease check the path of file and try again\n")
                    continue
                finally:
                    all_details = ""
                    for j in data_list:
                        all_details = all_details + j + "\n"

                        f = open("Employee Details.txt", 'w')
                        f.write(all_details)
                        f.close()

            if wrong_id and end_ind_emp:
                continue

            if end_all_emp:
                #Notify administrator of successful edit of employee profiles
                print("\nEmployee profile(s) have been successfully edited.\n")
                break





class Doctor(Employee):

    ##Create constructor to initialise objects
    def __init__(self, name, id, pin, work_status, speciality):
        Employee.__init__(self, name, id, pin, work_status)
        self.speciality = speciality




class Nurse(Employee):
    ##Create constructor to initialise objects
    def __init__(self, name, id, pin, work_status, speciality):
        Employee.__init__(self, name, id, pin, work_status)
        self.speciality = speciality



#Create method to fill strings to get a fixed length
def fillString(strings):
    for i in range(30):
        if len(strings) < 30:
            strings += " "
        continue
    return strings


#Create method to fill strings to get a fixed length of work status
def fil(strings):
    for i in range(15):
        if len(strings) < 15:
            strings += " "
        continue
    return strings


#Create method to generate employee id
def generateEmployeeID(the_type):
    print("\nGenerating Employee ID...................\n")
    if the_type == 1:
        baseID = "DOC/"
        numb = input("\nPlease enter last three pin number to add to base pin: ")
        id = baseID + numb
        return id
    elif the_type == 2:
        baseID = "NUR/"
        numb = input("\nPlease enter last three pin number to add to base pin: ")
        id = baseID + numb
        return id




#Create method to generate employee pin
def generateEmployeePin(the_type):
    print("\nGenerating Employee Pin...................\n")
    if the_type == 1:
        pin = randint(50000, 99999)
        return str(pin)
    elif the_type == 2:
        pin = randint(10000, 49999)
        return str(pin)





systemPassword = "ADMIN/h0sp1t@l"


# #Create instances of employees already in the workplace
emp1 = Employee("ANDY ALORWU", "DOC/123", 56789, "INSERVICE")
# emp2 = Nurse("DENNIS OPOKU BOADU", "NUR/256", 35421, "INSERVICE")
emp3 = Administrator("SAMANTHA TETTEH", "ADM/087", 82459, "INSERVICE", "ADMINh0sp1t@l")
# emp4 = Nurse("EUNICE AGYEI", "NUR/357", 86325, "INSERVICE")
# emp5 = Doctor("ANTHONY ALEXIS ADOASI", "DOC/489", 75684, "INERVICE", "NATUROPATHY")



# #Store instances created in employee list
# employeeList = [emp3, emp1, emp2, emp4, emp5]

print("\n#############################################################################################\n"
      "\t\t\t\t\t\t\tERASDA GROUP OF COMPANIES HOSPITAL\t\t\t\t\t\t\n"
      "Email: asdaem@yahoo.com\t\t\t\t\t\t\t\t\t\t\tTelephone: 0542345110\t\n"
      "Address: Computer Science Department, University of Ghana, P. O. Box 101, Legon, Accra\n"
      "#############################################################################################\n")

#Simulate the operation of employees in the workplace
if __name__ == "__main__":

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


            an = int(input("\nPlease select an option"
                           "\n1. Login\t\t\t2. View Profiles\t\t\t3. Logout\t\t\t4. Administrator\n\n"
                           "option: "))

            if an == 1:
                Employee.login(emp1)
                continue
            elif an == 2:
                Employee.viewProfile(emp1)
                continue
            elif an == 3:
                Employee.logout(emp1)
            elif an == 4:
                while True:
                    system_passwd = input("\nPlease enter the system password: ")

                    if system_passwd == systemPassword:
                        print("\nACCESS GRANTED\n")

                        while True:
                            try:
                                answ = int(input("\nPlease select another option\n\n"
                                                 "1. View All Profiles\n"
                                                 "2. Edit Profiles\n"
                                                 "3. Add Employee\n"
                                                 "4. View Log Book\n"
                                                 "5. End Administrator session\n"
                                                 "6. Shutdown System\n\n"
                                                 "Option: "))
                                #Reply based on option selected
                                if answ == 1:
                                    Administrator.viewAllProfiles(emp3)
                                elif answ == 2:
                                    Administrator.editEmployeeProfile(emp3)
                                elif answ == 3:
                                    Administrator.addEmployee(emp3)
                                elif answ == 4:
                                    Administrator.viewLogBook(emp3)
                                elif answ == 5:
                                    print("\nExiting Administrator mode.......\n")
                                    break
                                elif answ == 6:
                                    print("The system is shutting down\nBye!!!")
                                    sys.exit(0)
                                else:
                                    print("\nPlease try again and enter a number in range.\n")
                                    continue
                            except ValueError:
                                print("\nPlease try again and enter a correct number.")
                                continue
                    else:
                        print("\nACCESS DENIED!!\nTry Again\n")
                        continue
                    break
            else:
                print("\nPlease try again and enter a number in range\n")
                continue
        except ValueError:
            print("\nPlease try again and select an option in the list.\n")
            continue



