from random import randint
import time

name_list = []
password_list = []
camlp = "1"
pswdlp = 1
inval = randint(0, 10)

#systems
global auxpwr
auxpwr = True

for _ in range(1):
    #SLEEPS
    value1 = randint (1, 7)
    value2 = randint (1, 7)
    value3 = randint (1, 7)
    value4 = randint (1, 7)
    value5 = randint (1, 7)
    value6 = randint (1, 7)
    value7 = randint (1, 7)
    value8 = randint (1, 7)
    value9 = randint (1, 7)
    value10 = randint (1, 7)
    value11 = randint (1, 7)
    value12 = randint (1, 7)
    value13 = randint (1, 7)
    value14 = randint (1, 7)
    value15 = randint (1, 7)
    value16 = randint (1, 7)
    value17 = randint (1, 7)
    value18 = randint (1, 7)
    value19 = randint (1, 7)
    value20 = randint (1, 7)
    value21 = randint (1, 7)
    value22 = randint (1, 7)
    value23 = randint (1, 7)
    value24 = randint (1, 7)
    value25 = randint (1, 7)
    value26 = randint (1, 7)
    value27 = randint (1, 7)
    value28 = randint (1, 7)
    value29 = randint (1, 7)
    value30 = randint (1, 7)
    value31 = randint (1, 7)
    value32 = randint (1, 7)
    value33 = randint (1, 7)
    value34 = randint (1, 7)
    value35 = randint (1, 7)
    value36 = randint (1, 7)
    value37 = randint (1, 7)
    value38 = randint (1, 7)

#INTRO
print("Hello, and welcome to FirstEmbassy 3.0")

#HOMEPAGE
def home():
    while True:
        hmpg = input("Where would you like to go? Calendar, News, Security Cameras, Settings, or Log Out? ")
        if hmpg.lower() == "calendar":
            #CALENDAR
            #GET INPUT FROM THE CAST ON WHAT TO PUT ON EACH DAY
            calendar()   
        elif hmpg.lower() == "news":
            #NEWS
            #GET INPUT FROM CAST ON WHAT KIND OF INFO
            print("NEWS")
        elif hmpg.lower() == "security cameras" or hmpg.lower() == "security camera" or hmpg.lower() == "security cams" or hmpg.lower() == "security cam":
            #SECURITY CAMS
            clrcde = input("Please enter clearance code: ")
            if clrcde == "075139855622093457122678440628" or clrcde == "valcd:05761": 
                print("please wait...")
                time.sleep(value5)
                print("code accepted")  
                security_cameras()
            else: 
                print("invalid code, please wait while we alert authorities near your location")
                while inval < 10:
                    print("please wait...")
                    time.sleep(5)
                    inval = inval + 1
                camlp == "invalid"
                print("authorities alerted")
                exit()
        elif hmpg.lower() == "settings":
            #SETTINGS
            #GET INPUT FROM CAST ON WHAT SETTINGS
            print("SETTINGS")
        elif hmpg.lower() == "log out" or hmpg.lower() == "logout":
            #LOG OUT
            print("logging out...")
            time.sleep(value28)
            create_or_login()
        if hmpg.lower() == "missile strike":
            misadtest = input("verify identity: ")
            if misadtest == "Admin":
                misadtest2 = input("enter Admin password: ")
                if misadtest2 == "7795Az3*":
                    print("prepare for 5 step validation")
                    missileval1 = input("enter code: ")
                    if missileval1 == "10723581293571985314571897517458124582":
                        print("code accepted")
                        missileval2 = input("enter biometric scan: ")
                        if missileval2 == "bioscan-952_88752":
                            print("biometric scan accepted")
                            missileval3 = input("enter cone cell scale supplement: ")
                            if missileval3 == "ccss-952_88712" or "ccss-772_3302":
                                missileval4 = input("enter rod cell orientation supplement: ")
                                if missileval4 == "rcos-952_93725":
                                    missileval5 = input("validate: ")
                                    if missileval5 == "valcd:95281":
                                        print("valid; please wait...")
                                        time.sleep(value35)
                                        missilecoords = input("enter coordinates: ")
                                        missileconf = input("validate: ")
                                        if missileconf == "valcd:99732":
                                            missileconf2 = input("confirmation required: ")
                                            if missileconf2 == "affirmative":
                                                print("launching to affirmed coordinates: " + missilecoords)
                                            elif missileconf2 == "negative":
                                                print("cancelling...")
                                        else: 
                                            print("invalid code, please wait while we alert authorities near your location")
                                            while inval < 10:
                                                print("please wait...")
                                                time.sleep(5)
                                                inval = inval + 1
                                            print("authorities alerted")
                                    else: 
                                        print("invalid code, please wait while we alert authorities near your location")
                                        while inval < 10:
                                            print("please wait...")
                                            time.sleep(5)
                                            inval = inval + 1
                                        print("authorities alerted")
                            else: 
                                print("invalid code, please wait while we alert authorities near your location")
                                while inval < 10:
                                    print("please wait...")
                                    time.sleep(5)
                                    inval = inval + 1
                                print("authorities alerted")
                        else: 
                            print("invalid biometric scan, please wait while we alert authorities near your location")
                            while inval < 10:
                                print("please wait...")
                                time.sleep(5)
                                inval = inval + 1
                            print("authorities alerted")
                    else: 
                        print("invalid code, please wait while we alert authorities near your location")
                        while inval < 10:
                            print("please wait...")
                            time.sleep(5)
                            inval = inval + 1
                        print("authorities alerted")
                else: 
                    print("invalid password, please wait while we alert authorities near your location")
                    while inval < 10:
                        print("please wait...")
                        time.sleep(5)
                        inval = inval + 1
                    print("authorities alerted")
            else: 
                print("invalid identity, please wait while we alert authorities near your location")
                while inval < 10:
                    print("please wait...")
                    time.sleep(5)
                    inval = inval + 1
                print("authorities alerted")
        else:
            print("that is not an option")

#CREATE ACCOUNT OR LOG IN
def create_or_login():
    while True:
        adduser = input("Would you like to create an account or log in? ")
        if adduser.lower() == "log in" or adduser.lower() == "login":
            #USERNAME
            user_name = input("enter username: ")
            print("validating username...")
            time.sleep(value1)
            print("please wait...")
            time.sleep(value2)
            for i in name_list:
                if(i == user_name):
                    userName = name_list.index(user_name)
                    #PASSWORD
                    entrpwd = input("enter password: ")
                    print("validating password...")
                    time.sleep(value3)
                    print("please wait...")
                    time.sleep(value4)
                    if entrpwd == password_list[userName] or entrpwd == "05761":
                        print("Welcome " + user_name)
                        home()
                    else:
                        print("invalid password")
                else:
                    print("invalid username")
                    break
        elif adduser.lower() == "create account" or adduser.lower() == "create an account":
            while True:
                username = input("Pick a username: ")
                if username == "quit":
                    print("quitting")
                    time.sleep(value34)
                    break
                elif username in name_list:
                    print("username already taken, please select a different one")
                else:
                    name_list.append(username)
                    pswd = input("Pick a password: ")
                    password_list.append(pswd)
                    print("creating account...")
                    time.sleep(value16)
                    print("account created, return to the home page and log in")
                    create_or_login()
        elif adduser.lower() == "bypass":
            bypcde = input("validate: ")
            if bypcde == ("valcd:05761"):
                home()
            else:
                print("invalid code")
        elif adduser.lower() == "dev":
            devcde = input("validate: ")
            if devcde == ("valcd:33670"):
                print("loading...")
                time.sleep(value33)
                while True:
                    devhme = input("enter command: ")
                    if devhme == ("ls users"):
                        print(name_list)
                    elif devhme == ("ls passwords"):
                        print(password_list)
                    elif devhme == "init":
                        init = input("enter system: ")
                        if init == "aux.power" and auxpwr == False:
                            auxpwrval = input("validate: ")
                            if auxpwrval == "valcd:71652":
                                print("aux.power-init...")
                                auxpwr = True
                                time.sleep(value36)
                                print("Auxiliary Power Initiated")
                    elif devhme == "deinit":
                        deinit = input("enter system: ")
                        if deinit == "aux.power" and auxpwr == True:
                            auxpwrval = input("validate: ")
                            if auxpwrval == "valcd:71652":
                                print("aux.power-deinit")
                                auxpwr = False
                                time.sleep(value37)
                                print("Auxiliary Power Deinitiated")
                    elif devhme == "test.sys":
                        testsys = input("enter system: ")
                        if testsys == "aux.power":
                            print(auxpwr)
                    elif devhme == "log_mhjl":
                        log_mhjl = input("validate: ")
                        if log_mhjl == "valcd:85102":
                            mhjl_home()
                        else:
                            break
                    elif devhme == ("quit"):
                        print("quitting...")
                        time.sleep(value32)
                        break
                    else:
                        print("not a valid command")
            else:
                print("not a valid code")
        else:
            print("that is not an option")

def security_cameras():
    #SECURITY CAMS
    while True:
        rmno = input("What room number would you like to surveil? ")
        if rmno == ("quit"):
            print("quitting...")
            time.sleep(value27)
            home()
        else:
            print("loading room number " + rmno + "...")
            if rmno == "666":
                while True:
                    print("")
                    print("X X X X X")
                    time.sleep(value17)
                    print("X X X X X")
                    time.sleep(value18)
                    print("X X X X X")
                    time.sleep(value19)
                    print("X X X X X")
                    time.sleep(value20)
                    print("X X X X X")
                    print("")
            elif rmno == "1":
                presrm_cam()
            elif rmno == "158":
                empty_cam()
            else:
                random_cams()
   
def random_cams():
    #RANDOM CAMS
    camera_list = ["0", "0", "0", "0", "X", "X", "0", "0"]
    print("")
    time.sleep(value21)
    print(camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] )
    time.sleep(value22)
    print(camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] )
    time.sleep(value23)
    print(camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] )
    time.sleep(value24)
    print(camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] )
    time.sleep(value25)
    print(camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] + " " + camera_list[randint(0, 7)] )
    time.sleep(value26)
    print("")
def presrm_cam():
    camera_list = ["0", "0", "0", "0","X", "0", "0", "0", "0", "0"]
    print("")
    time.sleep(value21)
    print(camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] )
    time.sleep(value22)
    print(camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] )
    time.sleep(value23)
    print(camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] )
    time.sleep(value24)
    print(camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] + " " + camera_list[randint(0, 9)] )
    time.sleep(value25)
    print("X" + " " + "0" + " " + "X" + " " + "0" + " " + "X" )
    time.sleep(value26)
    print("")
def empty_cam():
    print("")
    print("0 0 0 0 0")
    print("0 0 0 0 0")
    print("0 0 0 0 0")
    print("0 0 0 0 0")
    print("0 0 0 0 0")
    print("")
def calendar():
    day = input("what day would you like to view? ")
    if day == "quit":
        print("quitting...")
        time.sleep(value30)
        home()
    else:
        print("loading " + day + "...")
        time.sleep(value31)
        calact = input("would you like to set an event, edit an event, or go back? ")
        if calact == "set":
            print("")
        elif calact == "edit":
            print("")
        elif calact == "go back":
            calendar()
def mhjl_home():
    print("under development")
create_or_login()