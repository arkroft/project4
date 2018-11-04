import random
StIn = 'АЕНОСТ'
StOut = ""
SamePlace = 0
WrongPlace = 0
Tries = 1
i = 1
Space = ""
while i <= 4:
    k = random.randint(1, 6) - 1
    exist = 0

    for j in range(len(StOut)):
        if StIn[k] == StOut[j]:
            exist = 1

    if exist == 0:
        StOut = StOut + StIn[k]
        i = i + 1
while Tries >= 1:
    play = input("let's play a game! (input 'yes' or 'no')")
    if play == "no":
        print("Okay :( ")
    elif play == "yes":
        while Tries <= 10:
            print('Try №', Tries)
            Word = input("Input you word:").upper()
            if Word[0] == StOut[0]:
                SamePlace += 1
            if Word[1] == StOut[1]:
                SamePlace += 1
            if Word[2] == StOut[2]:
                SamePlace += 1
            if Word[3] == StOut[3]:
                SamePlace += 1
            for ch in StOut:
                if ch in Word:
                    if Space != ch:
                        WrongPlace += 1
                        Space += ch
                    else:
                        Space = ch
            print('On the right place":', SamePlace)
            print('On the wrong place": ', WrongPlace - SamePlace)
            if SamePlace == 4:
                print('You are win!')
            SamePlace = 0
            WrongPlace = 0
            Space = ''
            Tries += 1
            if Tries > 10:
                print('you are loose!')
