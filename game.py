name = input('Enter your name: ')
print(f'Greetings {name}! Best of luck on your adventure!')
start = input("Would you like to \'play\' the game or \'perish\'? " )
if start == 'play':
    print("Great lets play the game!")
    setting = input("Want to go to \'The Abandoned Building\' or \'The Distressed Spaceship\' ")
else:
    print(f'Lame {name}! Okay your\'re dead now!')
    quit()

if setting == 'The Abandoned Building':
    print(f"Welcome {name} to the former headquarters to the parasol corporation. You were told to remain lookout while the other members of the team began exploring the building.")
    response = input("It has been awhile since team radioed in...do you \'stay\' at the front of the building or do you \'enter\'? ")
    if response == "stay":
        print("You wait another 30 minutes and you here nothing over the radio.")
        response = input("Do you \'wait\' longer or do you \'enter\'? ")
        if response == 'wait':
            print("You wait another 30 minutes then a cop comes up and tells you to put your hands up in the air.")
            response = input("Do you put your \'hands up\' or do you run and \'enter\' the building? ")
            if response == "hands up":
                print("You are arrested for trespassing. Later convicted of murder of your team members as they were all found dead in the building days later.")
                quit()
            elif response == 'enter':
                print("You enter the abandonded building. As you enter you see shattered glass and rubble all over the floors, the walls covered in graffiti and a you see a open door leading to a staircase to the next level.")
                response = input("Do you wait in the \'foyer\' or do you go up the \'stairs\'? ")
                if response == "foyer":
                    print("You are arrested for trespassing. Later convicted of murder of the team members as they were all found dead in the building days later.")
                    quit()
                elif response == "stairs":
                    print('You climb the staircase and see a madman with a bat about to beat your friends')
                    response = input("Do you \'attack\' the madman from behind or \'do nothing\'? ")
                    if response == 'attack':
                        print('You knockout the madman as he is about to kill one of your teammates just as you do a policeman arrives on scene and handcuffs the madman and lets you all of with a warning for tresspassing. Your friends are so grateful for you saving them that they buy you ice cream.')
                        print('       ()         ')
                        print('      (__)        ')
                        print('     (____)       ')
                        print('    (______)      ')
                        print('   (________)     ')
                        print('  (__________)    ')
                        print('  \/\/\/\/\/\/    ')
                        print('   \/\/\/\/\/     ')
                        print('    \/\/\/\/      ')
                        print('     \/\/\/       ')
                        print('      \/\/        ')
                        print('       \/         ')
                        quit()
                    elif response == 'do nothing':
                        print("You watch as all of team members are beaten to death and then a police officer arrives and arrests you and the madman for the murder.")
                        quit()
                    else:
                        print('invalid respone! You lose and your team was never seen again!')
                else:
                    print('invalid respone! You lose and your team was never seen again!')

            else:
                print('invalid respone! You lose and your team was never seen again!')
        elif response == 'enter':
            print("You enter the abandonded building. As you enter you see shattered glass and rubble all over the floors, the walls covered in graffiti and a you see a open door leading to a staircase to the next level.")
            response = input("Do you wait in the \'foyer\' or do you go up the \'stairs\'? ")
            if response == 'stairs':
                print('You climb the staircase and see a madman with a bat about to beat your friends')
                response = input("Do you \'attack\' the madman from behind or \'do nothing\'? ")
                if response == 'attack':
                    print('You knockout the madman as he is about to kill one of your teammates just as you do a policeman arrives on scene and handcuffs the madman and lets you all of with a warning for tresspassing. Your friends are so grateful for you saving them that they buy you ice cream.')
                    print('       ()         ')
                    print('      (__)        ')
                    print('     (____)       ')
                    print('    (______)      ')
                    print('   (________)     ')
                    print('  (__________)    ')
                    print('  \/\/\/\/\/\/    ')
                    print('   \/\/\/\/\/     ')
                    print('    \/\/\/\/      ')
                    print('     \/\/\/       ')
                    print('      \/\/        ')
                    print('       \/         ')
                    quit()
                elif response == 'do nothing':
                    print("You watch as all of team members are beaten to death and then a police officer arrives and arrests you and the madman for the murder.")
                    quit()
                else:
                    print('invalid response! You lose and your team was never seen again!')
            elif response == 'foyer':
                print(f"You are arrested for trespassing. Later convicted of murder of your team members as they were all found dead in the building days later.")
                quit()
            else:
                print(f'invalid response! You lose and your team was never seen again!')
        else:
            print(f'invalid response! You lose and your team was never seen again!')    
    elif response == "enter":
        print("You enter the abandonded building. As you enter you see shattered glass and rubble all over the floors, the walls covered in graffiti and a you see a open door leading to a staircase to the next level.")
        response = input("Do you wait in the \'foyer\' or do you go up the \'stairs\'? ")
        if response == 'stairs':
            print('You climb the staircase and see a madman with a bat about to beat your friends')
            response = input("Do you \'attack\' the madman from behind or \'do nothing\'? ")
            if response == 'attack':
                print('You knockout the madman as he is about to kill one of your teammates just as you do a policeman arrives on scene and handcuffs the madman and lets you all of with a warning for tresspassing. Your friends are so grateful for you saving them that they buy you ice cream.')
                print('       ()         ')
                print('      (__)        ')
                print('     (____)       ')
                print('    (______)      ')
                print('   (________)     ')
                print('  (__________)    ')
                print('  \/\/\/\/\/\/    ')
                print('   \/\/\/\/\/     ')
                print('    \/\/\/\/      ')
                print('     \/\/\/       ')
                print('      \/\/        ')
                print('       \/         ')
                quit()
            elif response == 'do nothing':
                print("You watch as all your team members are beaten to death and then a police officer arrives and arrests you and the madman for the murder.")
                quit()
            else:
                print('invalid response! You lose and your team was never seen again!')
        elif response == 'foyer':
            print(f"You are arrested for trespassing. Later convicted of murder of your team members as they were all found dead in the building days later.")
            quit()
        else:
            print(f'invalid response! You lose and your team was never seen again!')    
    else:
        print(f'invalid response! You lose and your team was never seen again!')
        quit()

elif setting == "The Distressed Spaceship":
    print(f"Are you sure {name} you would'nt rather go to The Abandoned Building?")
    response = input("Yes or No ")
    if response == "Yes":
        print("Great best of luck!")
        print(f"Welcome {name} to the former headquarters to the parasol corporation. You were told to remain lookout while the other members of the team began exploring the building.")
        response = input("It has been awhile since team radioed in...do you \'stay\' at the front of the building or do you \'enter\'? ")
        if response == "stay":
            print("You wait another 30 minutes and you here nothing over the radio.")
            response = input("Do you \'wait\' longer or do you \'enter\'? ")
            if response == 'wait':
                print("You wait another 30 minutes then a cop comes up and tells you to put your hands up in the air.")
                response = input("Do you put your \'hands up\' or do you run and \'enter\' the building? ")
                if response == "hands up":
                    print("You are arrested for trespassing. Later convicted of murder of your team members as they were all found dead in the building days later.")
                    quit()
                elif response == 'enter':
                    print("You enter the abandonded building. As you enter you see shattered glass and rubble all over the floors, the walls covered in graffiti and a you see a open door leading to a staircase to the next level.")
                    response = input("Do you wait in the \'foyer\' or do you go up the \'stairs\'? ")
                else:
                    print('invalid respone! You lose and your team was never seen again!')
                    if response == 'stairs':
                        print('You climb the staircase and see a madman with a bat about to beat your friends')
                        response = input("Do you \'attack\' the madman from behind or \'do nothing\'? ")
                        if response == 'attack':
                            print('You knockout the madman as he is about to kill one of your teammates just as you do a policeman arrives on scene and handcuffs the madman and lets you all of with a warning for tresspassing. Your friends are so grateful for you saving them that they buy you ice cream.')
                            print('       ()         ')
                            print('      (__)        ')
                            print('     (____)       ')
                            print('    (______)      ')
                            print('   (________)     ')
                            print('  (__________)    ')
                            print('  \/\/\/\/\/\/    ')
                            print('   \/\/\/\/\/     ')
                            print('    \/\/\/\/      ')
                            print('     \/\/\/       ')
                            print('      \/\/        ')
                            print('       \/         ')
                            quit()
                        elif response == 'do nothing':
                            print("You watch as all of team members are beaten to death and then a police officer arrives and arrests you and the madman for the murder.")
                            quit()
                        else:
                            print('invalid respone! You lose and your team was never seen again!')
                    elif response == 'foyer':
                        print("You are arrested for trespassing. Later convicted of murder of the team members as they were all found dead in the building days later.")
                        quit()
                    else:
                        print('invalid respone! You lose and your team was never seen again!')
            elif response == 'enter':
                print("You enter the abandonded building. As you enter you see shattered glass and rubble all over the floors, the walls covered in graffiti and a you see a open door leading to a staircase to the next level.")
                response = input("Do you wait in the \'foyer\' or do you go up the \'stairs\'? ")
                if response == 'stairs':
                    print('You climb the staircase and see a madman with a bat about to beat your friends')
                    response = input("Do you \'attack\' the madman from behind or \'do nothing\'? ")
                    if response == 'attack':
                        print('You knockout the madman as he is about to kill one of your teammates just as you do a policeman arrives on scene and handcuffs the madman and lets you all of with a warning for tresspassing. Your friends are so grateful for you saving them that they buy you ice cream.')
                        print('       ()         ')
                        print('      (__)        ')
                        print('     (____)       ')
                        print('    (______)      ')
                        print('   (________)     ')
                        print('  (__________)    ')
                        print('  \/\/\/\/\/\/    ')
                        print('   \/\/\/\/\/     ')
                        print('    \/\/\/\/      ')
                        print('     \/\/\/       ')
                        print('      \/\/        ')
                        print('       \/         ')
                        quit()
                    elif response == 'do nothing':
                        print("You watch as all of team members are beaten to death and then a police officer arrives and arrests you and the madman for the murder.")
                        quit()
                    else:
                        print('invalid response! You lose and your team was never seen again!')
                elif response == 'foyer':
                    print(f"You are arrested for trespassing. Later convicted of murder of your team members as they were all found dead in the building days later.")
                    quit()
                else:
                    print(f'invalid response! You lose and your team was never seen again!')
            else:
                print(f'invalid response! You lose and your team was never seen again!')    
        elif response == "enter":
            print("You enter the abandonded building. As you enter you see shattered glass and rubble all over the floors, the walls covered in graffiti and a you see a open door leading to a staircase to the next level.")
            response = input("Do you wait in the \'foyer\' or do you go up the \'stairs\'? ")
            if response == 'stairs':
                print('You climb the staircase and see a madman with a bat about to beat your friends')
                response = input("Do you \'attack\' the madman from behind or \'do nothing\'? ")
                if response == 'attack':
                    print('You knockout the madman as he is about to kill one of your teammates just as you do a policeman arrives on scene and handcuffs the madman and lets you all of with a warning for tresspassing. Your friends are so grateful for you saving them that they buy you ice cream.')
                    print('       ()         ')
                    print('      (__)        ')
                    print('     (____)       ')
                    print('    (______)      ')
                    print('   (________)     ')
                    print('  (__________)    ')
                    print('  \/\/\/\/\/\/    ')
                    print('   \/\/\/\/\/     ')
                    print('    \/\/\/\/      ')
                    print('     \/\/\/       ')
                    print('      \/\/        ')
                    print('       \/         ')
                    quit()
                elif response == 'do nothing':
                    print("You watch as all your team members are beaten to death and then a police officer arrives and arrests you and the madman for the murder.")
                    quit()
                else:
                    print('invalid response! You lose and your team was never seen again!')
            elif response == 'foyer':
                print(f"You are arrested for trespassing. Later convicted of murder of your team members as they were all found dead in the building days later.")
                quit()
            else:
                print(f'invalid response! You lose and your team was never seen again!')    
        else:
            print(f'invalid response! You lose and your team was never seen again!')
            quit()
    elif response == "No":
        print("Too bad cause no ticket to space for you and your team!")
        quit()
    else:
        print(f'invalid response! You lose!')
elif setting == "Ice Cream":
    print("You are a true hacker! You super win the game!")
    print('       ()         ')
    print('      (__)        ')
    print('     (____)       ')
    print('    (______)      ')
    print('   (________)     ')
    print('  (__________)    ')
    print('  \/\/\/\/\/\/    ')
    print('   \/\/\/\/\/     ')
    print('    \/\/\/\/      ')
    print('     \/\/\/       ')
    print('      \/\/        ')
    print('       \/         ')
else:
    print(f'invalid response! You lose!')