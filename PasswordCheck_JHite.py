# Dictionary for Usernames and Passwords
LoginDict = {'george7': 'Myid79', 'maryb2': 'Watch809'}
LoginFile = LoginDict

# def Validation for usernames
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

# def Validation for passwords
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

# def function (write dictionary to file)
def WriteFile():
    global LIW
    LIW = open('LoginInfo', 'w')
    for x,y in LoginDict.items():
        LIW.write(x + ':' + y + '\n')

    LIW.close()

# def function (read file -> list -> dictionary)
def ReadFile():
    try: loaddict = open('LoginInfo', 'r')

    # If file not found set LoginFile to default dictionary
    except FileNotFoundError:
        print('Cannot find dictionary file... using default dictionary')
        # create file since it couldn't find one
        LIW = open('LoginInfo', 'w')
        LIW.close()
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


# Read File / If not found use default dictionary / create file for future use
ReadFile()

# Function for Username Input
validifyUsername()
# Function for Password Input
validifyPassword()

# Reference inputs that have been validated to Dictionary
while True:
    if Username.lower() in LoginDict.keys():
        if Password in LoginDict.get(Username, ):
            print('\nThank you...')
            print('\n ...your Userid and Password have been confirmed')
        break
    # If username now in Dictionary, ask to add or quit
    elif Username.lower() not in LoginDict.keys():
        YN = input('User not found. Do you wish to  add this user? (Y/N)\n')
        if YN.lower() == 'y':
            # Write Username / Password to Dictionary -> File
            LoginDict[Username] = Password
            WriteFile()
            print('User ' + Username + ' added.')
        elif YN.lower() == 'n':
            print('User ' + Username + ' not added.')
            break
        else:
            YN = input('Please type Y or N \n')
            continue
    else:
        # write login dictionary to file for future use
        print('\n******************')
        print('\nRequest Complete.')
        print('Writing the Dictionary....')
        WriteFile()
        print('....Dictionary update complete')
        break
print('\nThank you for using Password Check.')

