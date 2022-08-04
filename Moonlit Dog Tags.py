import time
import random
global lp 
lp = True
global ch1lp
ch1lp = True
global ch2lp
ch2lp = True
global bnk1lp
bnk1lp = True
global bnk2lp
bnk2lp = True
global dun1lp
dun1lp = True
inventory = []
global squad
squad = []
global ch1comp
ch1comp = False
global ch2comp
ch2comp = False
def gmovr():
    #game over
    print('\033[1;31m GAME OVER\033[1;37m')
    retry = input("Do you want to play again? ")
    if retry.lower() == "no":
        global ch1lp
        ch1lp = False
        global ch2lp
        ch2lp = False
        global bnk1lp
        bnk1lp = False
        global bnk2lp
        bnk2lp = False
        global dun1lp
        dun1lp = False
    elif retry.lower() == "yes" and ch1lp == True:
        ch1()
    elif retry.lower() == "yes" and ch2lp == True:
        ch2()
def sqddeth():
    #squad death
    global randsqd
    randsqd = random.randint(0,len(squad)-1)
    print("\033[1;31m**Squad " + squad[randsqd] + " Lost**\033[1;37m You need to find a new " + squad[randsqd] + " before performing a task that would require one.")
    del squad[randsqd]
    time.sleep(2)
    print("Squad: " + str(squad))
def bunk2ins():
    cseaob = input("Inside, there is a case marked \033[3;37mAchtung! Nicht Explodierte Kampfmittel\033[0;37m \033[1;37mand one that says \033[3;37mNeue Sichere Kampfmittel\033[0;37m. \033[1;37mType \033[1;34mCase A\033[1;37m to open the first case and \033[1;34mCase B\033[1;37m to open the second. ")
    if cseaob.lower() == "case a":
        print("As you open the case, you hear Johnny yelling.")
        time.sleep(1)
        print("Johnny >> Wait that's the Unexpl-")
        time.sleep(1)
        print("It's too late. The case, labeled \033[3;37mDanger! Unexploded Ordnance\033[0;37m \033[1;37mcombusts as you open it.")
        gmovr()
    elif cseaob.lower() == "case b":
        print("Inside the case is a large Panzerfaust and 3 rockets for ammo.")
        time.sleep(1)
        print("Johnny >> Oooh! Let me get my hands on those!")
        time.sleep(1)
        inventory.append("Panzerfaust")
        inventory.append("Rocket")
        inventory.append("Rocket")
        inventory.append("Rocket")
        print("\033[1;32m**Acquired Panzerfaust!**")
        time.sleep(1)
        print("**Acquired Rocket x3!**\033[1;37m")
        time.sleep(1)
        print("Inventory: " + str(inventory))
        time.sleep(2)
        print("Johnny >> I think it's right about time we blow this pop stand.")
        time.sleep(2)
        blwbunk1 = input("Type \033[1;34mdemolitionist\033[1;37m to order the demolitionist to blow up the bunker. ")
        time.sleep(2)
        if blwbunk1.lower() == "demolitionist":
            print("Johnny >> Oh yeah! Let's do this!")
            time.sleep(2)
            print("As you walk away, the bunker crumbles behind you and your squad.")
            time.sleep(2)
            print("\033[1;33m**Objective Completed: Destroy Bunker**\033[1;37m")
            time.sleep(2)
            next()
def ch1():
    print("\033[1;30;47mChapter I\033[1;37;0m")
    global ch1lp
    while ch1lp == True:
        print("\033[0;37m\033[1;37mYou awake to the sound of explosions and shouting.")
        time.sleep(2)
        print("Soldier >> Mines! The Krauts mined the water!")
        time.sleep(2)
        print("As you look around, everything starts to come back to you:") 
        time.sleep(2)
        print("Your name is Ace, and you are a Lieutenant of the Canadian 3rd Infantry division, 7th Brigade, A Company, Regina Rifles")
        time.sleep(2)
        print("you were assigned to take Juno beach, Nan green sector and ultimately connect the forces at Sword and Gold beach.")
        time.sleep(2)
        print("Commander >> Look alive soldiers, ramp down by Juno beach in 10!")
        time.sleep(2)
        print("Commander >> GO,GO,GO!")
        time.sleep(2)
        print("As the ramp drops down into the water, the fire of MG-42s whizzes all around you.")
        time.sleep(2)
        upordown = input("Do you swim with your head \033[1;34mabove\033[1;37m the water, risking being shot, or \033[1;34mbelow\033[1;37m, risking drowning due to your heavy gear? ")
        time.sleep(2)
        if upordown.lower() == "above":
            print("Despite your heavy gear and the thousands of bullets raining down around you, you manage to reach the sandy shores of Juno beach.")
            time.sleep(2)
            print("You dive into cover and not a second too soon. The 10 and 15.5cm Howitzers unload a barrage, the blast narrowly missing your hiding spot. In a few seconds, the Howitzer will be able to fire again, hitting your hiding spot.")
            time.sleep(2)
            covorcral = input("Do you continue to \033[1;34mcrawl\033[1;37m up the beaches, hiding behind the dunes or do you stay hidden in \033[1;34mcover\033[1;37m? ")
            if covorcral.lower() == "cover":
                time.sleep(2)
                print("The shell from a 15.5cm gun lands near your hiding spot and blasts you to bits.")
                gmovr()
            elif covorcral.lower() == "crawl":
                time.sleep(2)
                print("You crawl forwards to a crater in the sand.")
                time.sleep(2)
                wreclip = input("In the crater you find a pair of wire clippers. Type '\033[1;34mgrab\033[1;37m' to pick up or '\033[1;34mleave\033[1;37m' to move on. Type inventory at any time to view your items and type '\033[1;34muse\033[1;37m' and the item you want to use to use something. ")
                if wreclip.lower() == "grab":
                    time.sleep(2)
                    inventory.append("Wire Clippers")
                    print("\033[1;32m**Acquired wire clippers!**\033[1;37m")
                    print("Inventory: " + str(inventory))
                bwre = input("You continue moving up the beach until you reach the crest where you are met with lines upon lines of barbed wire. Those wire clippers would sure come in handy! If you don't have the clippers the Engineer would do the job as well. To call him, type \033[1;34mengineer\033[1;37m. ")
                time.sleep(2)
                squad.append("Engineer")
                if bwre.lower() == "use wire clippers":
                    for i in inventory:
                        if(i == "Wire Clippers"):
                            time.sleep(2)
                            print("You make quick work of the barbed wire and move on.")
                        else:
                            time.sleep(2)
                            input("You have no wire clippers! You need to call the engineer over. To call over someone from your squad type their job. Type \033[1;34mengineer\033[1;37m now. ")
                            time.sleep(2)
                            print("It takes a while but your engineer eventually gets to you and cuts through the barbed wire.")
                elif bwre.lower() == "engineer":
                    time.sleep(2)
                    print("It takes a while but your engineer eventually gets to you and cuts through the barbed wire.")
                print("Inventory: " + str(inventory))
                #add more pause later somewhere near here
                time.sleep(2)
                print("\033[1;32m**Engineer added to squad!**\033[1;37m At any point when the engineer would be helpful, type engineer and your engineer will come and perform the required task.")
                time.sleep(2)
                print("Squad: " + str(squad))
                time.sleep(2)
                print("Soon after, you see a bunker a ways away nestled neatly on a hill. \033[1;33m**New Objective: Destroy the Bunker**\033[1;37m ")
                time.sleep(2)
                while bnk1lp == True:
                    bunk1 = input("You see three approaches: A long road to the left with lots of cover, a short path in front of you with little cover, and a shallow stream on your right. Type \033[1;34mleft\033[1;37m to go on the winding path, \033[1;34mcenter\033[1;37m to go on the short path, and \033[1;34mright\033[1;37m to go down the stream. ")
                    if bunk1.lower() == "left":
                        time.sleep(2)
                        print("While traveling down the winding path, you encounter a tall man sitting beneath an Anti-Tank emplacement.")
                        time.sleep(2)
                        print("Johnny >> Howdy there, Ace. The name's Johnny but everyone calls me Big Red. To give you the long-short, I make things go BOOM!")
                        time.sleep(2)
                        squad.append("Demolitionist")
                        print("\033[1;32m**Demolitionist added to squad!**\033[1;37m")
                        time.sleep(2)
                        print("Squad: " + str(squad))
                        time.sleep(2)
                        bunk2 = input("Do you \033[1;34mgo back\033[1;37m and re-evaluate your options or do you \033[1;34mcontinue\033[1;37m further down the long path to try to reach the bunker that way? ")
                        if bunk2.lower() == "go back":
                            time.sleep(2)
                            continue
                        elif bunk2.lower() == "continue":
                            time.sleep(2)
                            print("You continue on the path, the Anti-tank emplacements slowly becoming further apart. After a long walk, you are on slightly elevated hill next to the bunker. You can see the gunner sitting by his MG-42.")
                            while bnk2lp == True:
                                bunk2cap = input("Do you try to \033[1;34mshoot\033[1;37m the gunner, \033[1;34msneak\033[1;37m around and try to find an entrance, or call a squad member? ")
                                time.sleep(2)
                                if bunk2cap.lower() == "engineer":
                                    for i in squad:
                                        if(i=="Engineer"): 
                                            time.sleep(2)
                                            print("Jack >> Not sure what I could do here, Ace.")
                                elif bunk2cap.lower() == "demolitionist":
                                    for i in squad:
                                        if(i=="Demolitionist"):
                                            time.sleep(2)
                                            #demo throws grenade
                                            print("The demolitionist throws a grenade at the gunner's opening.")
                                            time.sleep(2)
                                            bk2cpgr = random.randint(1,20)
                                            if bk2cpgr == 1:
                                                time.sleep(2)
                                                print("The Demolitionist yanks the grenade pin, but forgets to throw it.")
                                                gmovr()
                                            elif bk2cpgr >= 10:
                                                #success
                                                time.sleep(2)
                                                print("The Demolitionist throws the grenade in a beautiful arc and it lands neatly in the bunker; the gunner won't be bothering you any more.")
                                                bunk2ins()
                                                break
                                            else:
                                                time.sleep(2)
                                                #fail
                                                print("The Demoltitionist throws the grenade but he misses the hole and it bounces off the side, attracting the gunner's fire.")
                                                gmovr()
                                elif bunk2cap.lower() == "shoot":
                                    #perchance shoot perchance miss
                                    bk2cpsht = random.randint(1,20)
                                    if bk2cpsht == 1:
                                        #nat1
                                        time.sleep(2)
                                        print("You line up the shot, but your gun malfunctions and blows up in your face.")
                                        gmovr()
                                        break
                                    elif bk2cpsht >= 10:
                                        #success
                                        time.sleep(2)
                                        print("You line up the shot, and you take out the gunner; he won't be bothering you any more.")
                                        bunk2ins()
                                        break
                                    else:
                                        #fail
                                        time.sleep(2)
                                        print("You do your best to line up the shot, but you still miss, attracting the gunner's fire.")
                                        gmovr()
                                elif bunk2cap.lower() == "sneak":
                                    #find back entrance perchance wack perchance get wacked
                                    time.sleep(2)
                                    print("You find a back entrance and you try to sneak up on the gunner.")
                                    bk2gnsnk = random.randint(1,20)
                                    if bk2gnsnk == 1:
                                        time.sleep(2)
                                        print("You immediately trip and fall and the gunner whips around and shoots you.")
                                        gmovr()
                                    elif bk2gnsnk >= 13:
                                        time.sleep(2)
                                        print("You successfully sneak up on the gunner and knock him out; he won't be bothering you any more.")
                                        bunk2ins()
                                        break
                                    else:
                                        time.sleep(2)
                                        print("You accidentally make noise while shuffling towards the gunner. He whips around and the two of you have a standoff.")
                                        bk2stdof = random.randint(1,20)
                                        if bk2stdof == 1:
                                            time.sleep(2)
                                            print("Before you can even react, the gunner pulls out his Luger and fires.")
                                            gmovr()
                                        elif bk2stdof >= 12:
                                            time.sleep(2)
                                            print("You manage to fire your Browning before the gunner; he won't be bothering you any longer.")
                                            bunk2ins()
                                            break
                                        else:
                                            time.sleep(2)
                                            print("The gunner barely beats you to the punch.")
                                            gmovr()
                    elif bunk1.lower() == "center":
                        time.sleep(2)
                        time.sleep(2)
                        print("As you start down the path, the MG-42 in the bunker comes to life, littering the sand around your squad with 7.92mm Mauser bullets.")
                        time.sleep(2)
                        cent1 = input("You barely make it to the first of scarcely apparent sand dunes. Do you \033[1;34mrun\033[1;37m to the next dune or do you try to \033[1;34mturn back\033[1;37m? ")
                        if cent1.lower() == "turn back":
                            time.sleep(2)
                            print("The MG-42 once again roars into action filling your squad with lead.")
                            gmovr()
                        elif cent1.lower() == "run":
                            time.sleep(2)
                            print("As you sprint, it takes the gunner a second to spring into action, but before you are even halfway there, the gun starts blasting.")
                            cent1rand = random.randint(1,11)
                            if cent1rand >= 6 and cent1rand <= 10:
                                time.sleep(2)
                                print("You barely make it behind the next dune, but as you look around you, you realize someone is missing.")
                                sqddeth()
                            elif cent1rand >= 11:
                                time.sleep(2)
                                print("You start sprinting, but you can't outrun the bullets.")
                                gmovr()
                            elif cent1rand <= 5:
                                time.sleep(2)
                                print("You barely make it behind the next dune, and you hear the shooting come to an abrupt stop.")
                            global dun1lp
                            while dun1lp == True:
                                time.sleep(2)
                                dun1 = input("Do you take advantage of the pause and \033[1;34mcontinue\033[1;37m on or do you stop and \033[1;34msearch\033[1;37m around the dune? ")
                                if dun1.lower() == "continue":
                                    time.sleep(2)
                                    print("Luckily, the pause meant that the gunner was reloading and you make it to the next dune without resistance.")
                                    dun1lp = False
                                elif dun1.lower() == "search":
                                    time.sleep(2)
                                    print("You dig through the sand and find a couple of sandy pineapples. \033[1;32m**Item get: 3x Grenade**\033[1;37m")
                                    inventory.append("grenade")
                                    inventory.append("grenade")
                                    inventory.append("grenade")
                                    time.sleep(2)
                                    print("Inventory: " + str(inventory))
                                    time.sleep(2)
                                    print("You press on, but you lost the advantage of avoiding the machine gun fire.")
                                    dun1rand = random.randint(1,12)
                                    if dun1rand >= 6 and dun1rand <= 10:
                                        time.sleep(2)
                                        print("You barely make it behind the next dune, but as you look around you, you realize someone is missing.")
                                        sqddeth()
                                        dun1lp = False
                                    elif dun1rand <= 5:
                                        time.sleep(2)
                                        print("You barely make it behind the next dune, but your squad seems intact")
                                        dun1lp = False
                                    elif dun1rand >= 11:
                                        time.sleep(2)
                                        ("You start sprinting, but you can't outrun the bullets.")
                                        gmovr()
                                    print("Now behind the dune, you see a small entrance for you to go into.")
                                else:
                                    continue
                            #get to bunker - blow up
                            for i in squad:
                                if (i == "Demolitionist"):
                                    print("You get to the bunker and quickly dispatch the gunner.")
                                else:
                                    print("You get to the bunker, and luckily the only person inside is an ally canadian with the markings of a demolitionist.")
                                    time.sleep(2)
                                    print("Johnny >> Howdy there, Ace. The name's Johnny but everyone calls me Big Red. To give you the long-short, I make things go BOOM!")
                                    time.sleep(2)
                                    print("You look around, confused, trying to find the machine gunner.")
                                    time.sleep(2)
                                    print("Johnny >> If you're wondering about the gunner, I took care of him.")
                                    time.sleep(2)
                                    squad.append("Demolitionist")
                                    print("\033[1;32m**Demolitionist added to squad**\033[1;37m")
                                    time.sleep(2)
                                    print("Squad: " + str(squad))
                            bunk2ins()
                            break
                    elif bunk1.lower() == "right":
                        time.sleep(2)
                        print("The stream is shallow enough that you can stay just below the water line but still come up to breathe without much resistance.")
                        time.sleep(2)
                        rght1 = input("Do you want to \033[1;34mwade\033[1;37m downstream to the bunker, \033[1;34mcross\033[1;37m the river and continue to search for more approaches, or \033[34mgo back\033[37m? ")
                        if rght1.lower() == "wade":
                            time.sleep(2)
                            print("You start to swim towards the bunker, and at first, nobody seems to see you, but soon enough, the you hear the telltale sound of a machine gunner getting ready to blast your squad into oblivion.")
                            gmovr()
                        elif rght1.lower() == "cross":
                            time.sleep(2)
                            #easter egg - joseph
                            print("On the other side of the stream, you find a small camp with two tents and a campfire, seemingly abandoned.")
                            time.sleep(2)
                            print("You check inside one of the tents and you find a medium german Kampfmesser.")
                            time.sleep(2)
                            inventory.append("Combat Knife")
                            print("\033[33m**Combat Knife Acquired**\033[37m")
                            time.sleep(2)
                            print(str(inventory))
                            time.sleep(2)
                            print("In the other tent, you find a book of poetry.")
                            time.sleep(2)
                            print("Joseph >> Hey, Sam. It's been a while.")
                            time.sleep(2)
                            print("You turn around. You could have sworn you had heard Joseph clear as day. But you didn't. He's gone. And all you can hear right now is your squadmates calling for you to come back.")
                            time.sleep(2)
                            continue
                        elif rght1.lower() == "go back":
                            continue
        elif upordown.lower() == "below":
            time.sleep(2)
            print("You dive down below the surface, but your 20kg of equipment drags you down to the murky depths.")
            gmovr()
def next():
    print("With the bunker destroyed, your squad continues past the beach, and reaches a fork in the road. To the \033[1;34mleft\033[1;37m, you see a densely wooded path, and to the \033[1;34mright\033[1;37m, you see a path leading into a civilian area of Normandy. Both paths lead to the Caen-Bayeux road. \033[1;33m**New Object: Cut the Caen-Bayeux Road**\033[1;37m ")
    time.sleep(2)
    frk1 = input("Do you go \033[1;34mleft\033[1;37m or \033[1;34mright\033[1;37m? ")
    if frk1.lower() == "left":
        print("As you enter the woods, the sun is almost completely blotted out. In the darkness, you can hear German soldiers scurrying around. Before you can react, you are hit over the head, and as you fall to the ground, you hear faint shouting.")
        time.sleep(2)
        print("Johnny >> They got Ace!")
        time.sleep(1)
        print("Jack >> Get 'em!")
        time.sleep(1)
        print("German Soldier >> Feuer! Zum Ruhme des Führers!")
        time.sleep(2)
    elif frk1.lower() == "right": 
        time.sleep(2) 
        cit1 = input("As you enter the city, the windows of the homes all burst open simultaneously and German guns open fire. Do you \033[1;34mfire back\033[1;37m or do you \033[1;34mfind cover\033[1;37m? ")
        if cit1.lower() == "fire back":
            time.sleep(2)
            print("You raise your gun but you aren't fast enough.")
            gmovr()
        elif cit1.lower() == "find cover":
            time.sleep(2)
            print("You dash into a building, and just as you do, you pass out. As you fall, you hear shouting.")
            time.sleep(2)
            print("Johnny(demolitionist) >> Ace is down!")
            time.sleep(2)
            print("Jack(engineer) >> We need a medic!")
            time.sleep(2)
    print("You awake in a bright white room that smells suspiciously of rubbing alcohol.")
    time.sleep(2)
    print("??? >> You awake?")
    time.sleep(2)
    print("You look around and find yourself in a hospital bed. A kind looking man stands next to your bed. Overwhelmed by your new surroundings, you try to jump out of bed, but you feel weak and drained of strenght.")
    time.sleep(2)
    print("??? >> You shouldn't try to move for awhile; a kraut got you real good.")
    time.sleep(2)
    print("Your memories slowly start to come back to you.")
    if frk1.lower() == "left":
        time.sleep(2)
        print("After entering the forest, a German Soldier hit your head with the butt of a rifle. Outnumbered, your squad fought back valiantly, but you only made it out because a strange man managed to pull you out. The rest of your squad was killed.")
        print("\033[1;31m**Squad Members " + str(squad) + "lost**\033[1;37m")
    elif frk1.lower() == "right":
        time.sleep(2)
        print("When hiding in the building, you were shot in an important artery and passed out from blood loss. Your squad was able to call a medic, but you were the only one who made it out.")
    time.sleep(2)
    print("Johansen >> My name's Johansen; I was the one who pulled you out of there and helped you regain your strength. Shame about your squad.")
    time.sleep(2)
    print("You slowly sit up and try to adjust to your new sedentary life.")
    time.sleep(2)
    print("\033[1;30;47mEnd Chapter I\033[1;37;0m")
    ch1lp = False
    global ch1comp
    ch1comp = True
    ch2()
def ch2():
    global ch2lp
    while ch2lp == True:
        print("\033[1;30;47mChapter II\033[1;37;0m")
        time.sleep(2)
        print("\033[1;30;47m3 Months Later\033[1;37;0m")
        time.sleep(2)
        print("\033[3mJohnny >> You should have been there.")
        time.sleep(2)
        print("Jack >> You abandoned us!")
        time.sleep(2)
        print("Joseph >> We died because of you!")
        time.sleep(2)
        print("??? >> It's all your fault!")
        time.sleep(2)
        print("??? >> \033[4mIt's all your fault!\033[0m")
        time.sleep(2)
        print("??? >> \033[4;31m\033[3mIt's all your fault!\033[0m")
        time.sleep(2)
        print("??? >> \033[4;31m\033[1m\033[3mIT'S ALL YOUR FAULT!\033[0m")
        time.sleep(2)
        print("\033[1;37mYou awake, drenched in a cold sweat.")
        time.sleep(2)
        print("You try to tell yourself that it wasn't your fault, that there was nothing you could do, but your dreams keep getting worse, and you don't know how much more you can take.")
        time.sleep(2)
        rnortlk = input("Do you \033[34mrun away\033[37m or do you \033[34mtalk\033[37m to Johansen about your dreams? ")
        if rnortlk.lower() == "talk":
            time.sleep(2)
            print("You approach Johansen to talk to him about your dreams that keep invading your mind.")
            time.sleep(2)
            print("Johansen >> Listen Ace, there was nothing you could have done...")
            time.sleep(2)
            print("It takes many months, but you eventually come to terms with yourself and the death of your squad.")
            time.sleep(2)
            print("\033[1;32mPeaceful Ending\033[37m")
            time.sleep(2)
            gmovr()
        elif rnortlk.lower() == "run away":
            time.sleep(2)
            print("You pack up everything you would need for trip: A bright-red tartan jacket, matches, a flashlight, a rain poncho, and peanut butter sandwiches, apples, hard-boiled eggs, and canned beans.")
            time.sleep(2)
            print("Not to mention the compass, map, pocketknife, rope, canteen, jar of honey, tobacco pouch, pack of gum, jelly bean jar, and wad of cash, stuffed into an empty can of beans.")
            time.sleep(2)
            rnawy = input("Do you try to sneak out the \033[34mwindow\033[37m or the \033[34mfront door?\033[37m ")
            if rnawy.lower() == "window":
                time.sleep(2)
                print("As you open the window, you remember when you first moved into this log cabin with Johansen. You opened this same window and it made the same obnoxious creaking noise that it always does. You'll miss Johansen, but you would just be a hinderance to him. After all, you couldn't even save your squad. You couldn't even save Joseph.")
            elif rnawy.lower() == "front door":
                time.sleep(2)
                print("You sneak through the room, you remember and avoid the creaky boards in this log cabin that you have come to love so much. Johansen took such good care of you. It's a shame you have to leave him, but you'd just be a hinderance. After all, you couldn't even save your squad. You couldn't even save Joseph.")
        lr1 = input("Now outside the cabin, do you turn \033[34mleft\033[37m down the path that soon leads to a covered bridge or do you take a \033[34mright\033[37m down the path that crosses a stream, requiring you to climb across a slippery log? ")
        time.sleep(2)
        if lr1.lower() == "left":
            time.sleep(2)
            swm = input("You head on to the covered bridge, and as you look into the rusing river below it, you see something glinting. Do you want to go for a \033[34mswim\033[37m or do you want to \033[34mstay dry\033[37m? ")
            if swm == "swim":
                time.sleep(2)
                print("You dive in and find a shiny ring at the bottom of the river.")
                inventory.append("Strange Ring")
                time.sleep(2)
                print("\033[33m**Strange Ring Acquired!**\033[37m")
                time.sleep(2)
                print(str(inventory))
            print("You continue on, and happen upon an old Sycamore tree. Beneath the tree lie two graves.")
            time.sleep(2)
            print("You pay your respects and move on.")
            time.sleep(2)
            print("Past the tree you find a spot where two trails converge, heading towards a decent sized building in the distance. As you look overhead, you see Polaris shinging bright above the building.")
            time.sleep(2)
        elif lr1.lower() == "right":
            print("Moving towards the right, you are confronted with the task of crossing a long, slippery long spanning a rushing river.")
            time.sleep(2)
            dlog = random.randint(1,20)
            if dlog >=11:
                print("You succesfully make it to the other end, despite a few slips.")
                time.sleep(2)
            elif dlog <=10:
                print("You fall into the water, but as your last bits of air are battered out of your lungs by the current, a strong man lifts you out of the water. He gifts you a new jacket and flashlight then disappears just as mysteriously as he appeared.")
                time.sleep(2)
                inventory.append("Flashlight")
                inventory.append("Jacket")
                print("\033[34m**Jacket and Flashlight Acquired!**")
                time.sleep(2)
                print(str(inventory))
                time.sleep(2)
                print("Now past the trial of the river, you find a spot where two trails converge, heading towards a decent sized building in the distance. As you look overhead, you see Polaris shinging bright above the building.")
                time.sleep(2)
        print("As you approach the building, you smell good food and hear boisterous laughter.")
        time.sleep(2)
        inn = input("Do you \033[34mgo in\033[37mto the building or do you \033[34mcontinue\033[37m on with your aimless, regretful wandering? ")
        time.sleep(2)
        if inn.lower() == "go in" or inn.lower() == "go into":
            print("As you open the door, everyone inside stops what they are doing and stares at you. It's very clear that you don't belong here, but you are tired and you are almost out of peanut butter sandwiches.")
            time.sleep(2)
            print("You sit down at the counter and order a corned beef sandwich, but before you can dig in, you hear the telltale click of an 1894 Winchester Rifle.")
            time.sleep(2)
            print("\033[31mBad Ending\033[37m")
            time.sleep(2)
            gmovr()
        elif inn.lower() == "continue":
            print("You continue further down and come a cross a much bigger river. You see a small one person boat with a coxswain seat. As you climb in the boat, you hear his voice faintly.")
            time.sleep(2)
            print("Joseph >> \033[0mPick it! Firm it up! Weigh enough! Let it run!\033[1m")
            time.sleep(2)
            print("You shake your head; you left him. He isn't here anymore")
            time.sleep(2)
            print("\033[1;30;47m1 Week Later\033[1;37;0m")
            time.sleep(2)
            print("After rowing for days, your food sources are nigh exhausted and your arms are sore.")
            time.sleep(2)
            print("In the distance you see a small cabin with a light on: Hope!")
            time.sleep(2)
            print("As you stand on dry land for the first time in a week, your knees buckle beneath you.")
            time.sleep(2)
            print("When you come to, you find yourself in yet another hospital. This time, instead of a strange man, you see familiar faces.")
            time.sleep(2)
            print("Mother >> Look he's waking up.")
            time.sleep(2)
            print("Father >> There's my kid.")
            time.sleep(2)
            print("Brother >> I thought you weren't coming back.")
            time.sleep(2)
            print("Looking at your family, tears well in your eyes. When you left to fight in the war you thought you would never get to see them again, but here you are.")
            time.sleep(2)
            print("Father >> We'll let you get back to rest, but first, your brother has something for you.")
            time.sleep(2)
            print("You look at your brother, but you don't see him. You see Joseph. You always see Joseph.")
            time.sleep(2)
            print("He hands you your dog tags, the moonlight reflecting off the raised letters.")
            time.sleep(2)
            print("FRANCIS BAKER - QUEBEC, CANADA")
            time.sleep(2)
            print("You >> I missed all of you.")
            time.sleep(2)
            print("You burst into tears. Your family never forgot about you, but somehow you forgot about them. All of them. Except Joseph.")
            ch2lp = False
            global ch2comp
            ch2comp = True
ch1()