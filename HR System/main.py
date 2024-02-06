#imports --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import glob
import csv
import sys
from models import * 

# Global Variables -----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Months / Years for date validation for modules
Months = {'january' : 31, 'february' : 28, 'march' : 31, 'april' : 30, 'may' : 31, 'june' : 30, 'july' : 31,
 'august' : 31, 'september' : 30, 'october' : 32, 'november' : 30, 'december' : 31}
Years = range(1900, 2022)
#
# Empty Lists for List inside List movement
global Emp_Results
global Emp_CL
global fline
Emp_Results = []
Emp_CL = []
fline = ['First Name', 'Last Name', 'Birthday', 'Hire Date', 'Age', 'Sex (1 -  Male, 0 - Female)']
#
# Variables for Login Files, one for HR, one for other Employees
LoginDict = {'jhite1': 'josh123'}
LoginFile = LoginDict
HRLoginDict = {'cvindin2': 'carson123', 'adrian1': 'adrian123'}
HRLoginFile = HRLoginDict
#
# Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# SCREEN 1 ------ 
#
def screen1():
    print("Welcome to Hite's Hammers Onboarding System ")
    print("********************************************")
    print("1 - Login")
    print("2 - Exit")
    while True:
        so1 = input("Please input an option: ")
        if so1 == '1':
            screen2()
        elif so1 == '2':
            print("Closing Application...\n Thank You!")
            sys.exit()
        else:
            print("Please input a valid number (1-2) ")
            continue
#
# SCREEN 2 ------
def screen2():
    while True:
        print("Please select your login group!")
        print("1 - Employee Login ")
        print("2 - HR Login ")
        print("3 - Return to main menu ")
        so2 = input("Please input an option: ")
        if so2 == '1':
            ReadFile()
            validifyUsername()
            validifyPassword()
            eloginattempt()
        elif so2 == '2':
            HRReadFile()
            validifyUsername()
            validifyPassword()
            hrloginattempt()
        elif so2 == '3':
            screen1()
        else:
            print('Please input a valid number (1-3)')
            continue
#
# Screen for once Employee's are logged in
def escreen():
    while True:
        print("*****Employee Menu*****")
        print("1 - View Information")
        print("2 - New/Change Information")
        print("3 - View Intro Videos ")
        print("4 - Logout")
        print("5 - Exit Application")
        escreeno = input("Please input an option: ")
        if escreeno == '1':
            lname = input('Please verify by typing your last name: ')
            lname = lname.title()
            CallInfo(lname)
        elif escreeno == '2':
            while True:
                print('1 - New Information')
                print('2 - Change Information')
                print('3 - Exit')
                choice = input('Please enter an option: ')
                if choice == '1':
                    newinfo()
                    WriteFile()
                elif choice == '2':
                    print('Allow change of data here')
                elif choice == '3':
                    escreen()
                else:
                    print('please enter a valid choice...')
                    continue
        elif escreeno == '3':
            Employee.playvideo()
        elif escreeno == '4':
            print("Logging out...")
            screen1()
        elif escreeno == '5':
            print("Closing Application...\n Thank You!")
            sys.exit()           
#
# Screen for once HR is logged in
def hrscreen():
        print("*****HR Menu*****")
        print('1 - View Employee Data')
        print('2 - Create Employee Login')
        print('3 - Remove Employee Data')
        print('4 - Change Employee Data')
        print('5 - Logout')
        print('6 - Exit Application')
        hrscreeno = input('Please input an option: ')
        if hrscreeno == '1':
            lname = input('Please verify by typing your last name: ')
            lname = lname.title()
            CallInfo(lname)
        elif hrscreeno == '2':
            validifyUsername()
            validifyPassword()
            LoginDict[Username] = Password
            LoginWriteFile()
            print('New Account Added')
            print('UN: ' + Username)
            print('PW: ' + Password)
            hrscreen()
        elif hrscreeno == '3':
            Emp_Files = glob.glob('*.csv') 
            print("Available Employee Files:")
            for f in Emp_Files:
                print(f)
            nomore = input('Who\'s information would you like to remove?: ')
            nomore2 = (nomore + '.csv')
            os.remove(nomore2)
            print(nomore2+ '\'s Data has been removed! ')
            hrscreen()
        elif hrscreeno == '4':
            Emp_Files = glob.glob('*.csv') 
            print("Available Employee Files:")
            for f in Emp_Files:
                print(f)
            lname = input('Who\'s information would you like to change?: ')
            CallInfo(lname)
            print('| 0 - First Name | 1 - Last Name | 2 - Birthday | 3 - Hire Date | 4 - Age | 5 - Sex |')
            print(' Code will break soon, this part will be added in future updates :) ')
            while True:
                ChangeData(lname)
        elif hrscreeno == '5':
            print("Logging out...")
            screen1()
        elif hrscreeno == '6':
            print("Closing Application...\n Thank You!")
            sys.exit() 
#-------------------------------------------------
#
# Input and Validation for usernames (1 number, 1 letter, min 6 char)
def validifyUsername():
    while True:
        global Username
        Username = input('Please Enter UserID: \n')
        if Username.isalpha() is True:
            print('Response does not contain at least one number')
            continue
        elif Username.isalpha() is False:
            if Username.isdecimal() is True:
                print('Response does not contain at least one letter')
                continue
            elif Username.isdecimal() is False:
                if len(Username) < 6:
                    print('Response is too short. Minimum 6 characters required')
                    continue
                elif len(Username) >= 6:
                    break
#
# Input and Validation for passwords (1 number, 1 letter, min 6 char)
def validifyPassword():
    while True:
        global Password
        Password = input('Please Enter Password (Case Sensitive): \n')
        if Password.isalpha() is True:
            print('Response does not contain at least one number')
            continue
        elif Password.isalpha() is False:
            if Password.isdecimal() is True:
                print('Response does not contain at least one letter')
                continue
            elif Password.isdecimal() is False:
                if len(Password) < 6:
                    print('Response is too short. Minimum 6 characters required')
                    continue
                elif len(Password) >= 6:
                    break
#
# Check Date sent for validation
def ValidifyDate(Emp_Month, Emp_Day, Emp_Year):
    while True:
        global d
        if Emp_Month.lower() in Months.keys():
            if int(Emp_Day) >= 1 and int(Emp_Day) <= Months[Emp_Month.lower()]:
                if int(Emp_Year) in Years:
                    d = 2
                    return Emp_Month, Emp_Day, Emp_Year, d
                else:
                    print('Invalid Date - Not a Valid Year')
                    d = 1 
                    return d
            else:
                print('Invalid Date - Not a Valid Day')
                d = 1
                return d
        else:
            print('Invalid Date - Not a Valid Month')
            d = 1
            return d
#
# Employee Login Attempt Check
def eloginattempt():
    if Username.lower() in LoginDict.keys():
        if Password in LoginDict.get(Username, ):
            escreen()
        else:
            # If login fails, return to screen2 login screen
            print('Incorrect Password, Please Try Again')
            screen2()
    else:
        # If login fails return to screen2 login screen
        print('Incorrect Username, Please Try Again')
        screen2()
#
# HR Login Attempt Check
def hrloginattempt():
    if Username.lower() in HRLoginDict.keys():
        if Password in HRLoginDict.get(Username, ):
            hrscreen()
        else:
            # If login fails, return to screen2 login screen
            print('Incorrect Password, Please Try Again')
            screen2()
    else:
        # If login fails return to screen2 login screen
        print('Incorrect Username, Please Try Again')
        screen2()
#
# Read login file for employees -> List -> Dictionary
def ReadFile():
    try: loaddict = open('LoginInfo', 'r')

    # If file not found set LoginFile to default dictionary
    except FileNotFoundError:
        print('Cannot find dictionary file... using default dictionary')
        # create file since it couldn't find one
        WriteFile()
    # If file loads...read it
    else:
        lines = loaddict.readlines()
        for x in lines:
            x.rstrip()
            slist = x.split(':')
            # If index error during List -> Dictionary, try removing \n again
            try: LoginFile[slist[0]] = slist[1]
            except IndexError:
                x.rstrip()

            loaddict.close()
#
# Read HR Login file -> List -> Dictionary
def HRReadFile():
    try: HRloaddict = open('HRLoginInfo', 'r')

    # If file not found set LoginFile to default dictionary
    except FileNotFoundError:
        print('Cannot find dictionary file... using default dictionary')
        # create file since it couldn't find one
        HRWriteFile()
    # If file loads...read it
    else:
        lines = HRloaddict.readlines()
        for x in lines:
            x.rstrip()
            slist = x.split(':')
            # If index error during List -> Dictionary, try removing \n again
            try: HRLoginFile[slist[0]] = slist[1]
            except IndexError:
                x.rstrip()

            HRloaddict.close()
#
# Write Employee Login Info to File
def LoginWriteFile():
    global LIW
    LIW = open('LoginInfo', 'w')
    for x,y in LoginDict.items():
        LIW.write(x + ':' + y + '\n')

    LIW.close()
#
# Write HR Login Info to File
def HRWriteFile():
    global HRLIW
    HRLIW = open('HRLoginInfo', 'w')
    for x,y in HRLoginDict.items():
        HRLIW.write(x + ':' + y + '\n')

    HRLIW.close()
#

#
# Gather information and send to a list, start objects
def newinfo():
    while True:
        Emp_CL = []
        print(' *** NEW EMPLOYEE INFO FORM *** ')
        fname = input('Please Enter First Name: ')
        letters(fname.title())
        Emp_CL.append(fname)
        global lname
        lname = input('Please Enter Last Name: ')
        letters(lname.title())
        Emp_CL.append(lname)
        while True:
                ebmonth = input('Enter Employee Birthdate - month (January, February, etc.): ')
                ebday = (input('Enter Employee Birthdate - day (30,31, etc.): '))
                ebyear = (input('Enter Employee Birthdate - year (1965,1972, etc.): '))
                ValidifyDate(ebmonth, ebday, ebyear)
                if d == 2:
                    ndate = str(ebmonth + ' ' + ebday + ' ' + ebyear)
                    Emp_CL.append(ndate)
                    break
                elif d == 1:
                    continue
        while True:
                ehmonth = input('Enter Employee Hirthdate - month (January, February, etc.): ')
                ehday = (input('Enter Employee Hirthdate - day (30,31, etc.): '))
                ehyear = (input('Enter Employee Hirthdate - year (1965,1972, etc.): '))
                ValidifyDate(ehmonth, ehday, ehyear)
                if d == 2:
                    ndate = str(ehmonth + ' ' + ehday + ' ' + ehyear)
                    Emp_CL.append(ndate)
                    break
                elif d == 1:
                    continue
        eage = input('Please Enter Age: ')
        numbers(eage)
        Emp_CL.append(eage)
        esex = input('Please Enter Sex (1-Male 0-Female): ')
        numbers(esex)
        Emp_CL.append(esex)
        efname = Emp_CL[0]
        elname = Emp_CL[1]
        empbirthday = Emp_CL[2]
        emphiredate = Emp_CL[3]
        eage = Emp_CL[4]
        esex = Emp_CL[5]
        global info
        #info = Employee(efname, elname, empbirthday, emphiredate, eage, esex,)
        Emp_Results.append(fline)
        Emp_Results.append(Emp_CL)
        Emp_CL = []
        break
#
# Find file
def CallInfo(lname):
    lname = lname
    try: loadfile = open(lname+'.csv', 'r')

    except FileNotFoundError:
        print('File could not be found..Aborting')

    else:
        data = list(csv.reader(loadfile))
        print('**** Employee Info (FILE : ' + lname + '.csv ) ****')
        print(data[0][0].ljust(20,' ') + data[0][1].ljust(20,' ') + data[0][2].ljust(20,' ') + data[0][3].ljust(20,' ') + data[0][4].ljust(20,' ') + data[0][5].ljust(20,' '))
        for row in data[1:]:
            print(row[0].ljust(20,' ') + 
                row[1].ljust(20,' ') + 
                row[2].ljust(20,' ') +
                row[3].ljust(20,' ') +
                row[4].ljust(20,' ') +
                row[5].ljust(20,' ')
                )            

    loadfile.close()        
#
# Test if input is alphanumeric pt.1
def letters(test):
    f1 = 0
    while f1 == 0:
        if test.isalpha() == True:
            return test
        else:
            test = input('Please only enter letters: ')
            continue
#
# Test if input is numeric pt.1
def numbers(test):
    f1 = 0
    while f1 == 0:
        if test.isnumeric():
            return test
        else:
            test = input('Please only enter numbers: ')
            continue
#
# Write to CSV
def WriteFile():
    global LIW
    LIW = open(lname + '.csv', 'w', newline='')
    output=csv.writer(LIW)
    output.writerows(Emp_Results)
    LIW.close()
#
# Append CSV
def ReWriteFile():
    global LIW
    LIW = open(lname + '.csv', 'a', newline='')
    output=csv.writer(LIW)
    output.writerows(Emp_Results)
    LIW.close()
#
# Change Infor
def ChangeData(lname):
            while True:
                section = input('Which item would you like to edit?: ')
                try: loadfile = open(lname+'.csv', 'a')
                except FileNotFoundError:
                        print('File could not be found..Aborting')
                else:
                    d1 = (csv.reader(loadfile))
                    d2 = list(d1)
                    nv = input('What would you like the new value to be?: ')
                    d2[int(section)] = [nv]
                    print(d1)

# APPLICATION RUNNING -----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# READ / CREATE REQUIRED FILES
ReadFile()
HRReadFile()

# Run screens
screen1()



