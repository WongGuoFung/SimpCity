import random


#============================================================
def welcome():
    print("Welcome, mayor of Simp City!")    
    print("----------------------------")
#==========================================
def main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print()
    print("0. Exit")
#=====================================
def play_game_menu(building1,building2):
    print("1. Build a {}".format(building1))
    print("2. Build a {}".format(building2))    #printing game menu
    print("3. See remaining buildings")
    print("4. See current score")
    print()
    print("5. Save game")
    print("0. Exit to main menu")
#=====================================
def displayCity(board):
    print("    {:^6}{:^6}{:^6}{:^6}".format("A","B","C","D"))        #displaying of city 
    print("   +-----+-----+-----+-----+")
    for row in range(1,(len(board)-1)):
        print("  {}".format(row), end = "")
        for column in range(1,(len(board[0])-1)):
            print("| {:3} ".format(board[row][column]),end="")
        print("|")
        print("   +-----+-----+-----+-----+")
#====================================
def start_new_game(turn,board):
    if turn <= 16:
        print("Turn {}".format(turn))   #printing turn
        displayCity(board)

#=======================================================
def drawBuildings(building_list):
    randomBuilding = building_list[random.randint(0,len(building_list) - 1)]  #draws from 0,39 inclusive(index)
    return randomBuilding
#=======================================================
def option1(choice2,board,b1,building_list): #done on 26/7
    global turn        #Global turn so that if option chosen dont build, turn remains 
    if choice2 == "1":                #build a random building
        location = input("Build where?")
        if (len(location) == 2 and location[0].isalpha() and location[1].isdigit()):
            
            i = int(location[1])
            j = ord(location[0].upper()) - ord("A") +1
            if (i in [1,2,3,4] and j in [1,2,3,4]):
                if (turn != 1 and board[i][j-1] == "   " and board[i][j+1] == "   " and  board[i-1][j] == "   " and board[i+1][j] == "   "):
                    isValid = False #validation of adj building
                    print("You must build next to an existing building.")
                else:
                    if board[i][j] == "   ":
                        board[i][j] = b1
                        index = building_list.index(b1)
                        building_list.pop(index)  #removing the building if built
                        turn += 1
                    else:
                        print("You can't replace building.")  #no replacing of building
                        option1(choice2,board,b1,building_list)
            else:
                print("Please enter a existing location.")
                option1(choice2,board,b1,building_list) 
            
        else:
            print("Please enter a existing location.")
            option1(choice2,board,b1,building_list)   
#========================================================
def option2(choice2,board,b2,building_list):     #done on 26/7
    global turn        #Global turn so that if option chosen dont build, turn remains 
    if choice2 == "2":                #build a random building
        location = input("Build where?")
        if (len(location) == 2 and location[0].isalpha() and location[1].isdigit()):
            
            i = int(location[1])
            j = ord(location[0].upper()) - ord("A") +1
            if (i in [1,2,3,4] and j in [1,2,3,4]):
                if (turn != 1 and board[i][j-1] == "   " and board[i][j+1] == "   " and  board[i-1][j] == "   " and board[i+1][j] == "   "):
                    isValid = False #validation of adj building
                    print("You must build next to an existing building.")
                else:
                    if board[i][j] == "   ":
                        board[i][j] = b2
                        index = building_list.index(b2)
                        building_list.pop(index)  #removing the building if built according to the building used
                        turn += 1
                    else:
                        print("You can't replace building.") #no replacing of building
                        option2(choice2,board,b2,building_list) 
            else:
                print("Please enter a existing location.")
                option2(choice2,board,b2,building_list) 
            
        else:
            print("Please enter a existing location.")
            option2(choice2,board,b2,building_list)   
#========================================================
def option3(printBuilding_list,building_list): #incase remaining building turn 0, buildings still can be printed
    print("{:20s}{:20s}".format("Building","Remaining"))#done on 29/7
    print("{:20s}{:20s}".format("--------","---------")) #["BCH","FAC","HSE","SHP","HWY"]
    remainingList = []
    remainingList.append(building_list.count("BCH"))
    remainingList.append(building_list.count("FAC"))
    remainingList.append(building_list.count("HSE"))
    remainingList.append(building_list.count("SHP"))
    remainingList.append(building_list.count("HWY"))
    for b in range(len(printBuilding_list)):
        print("{:20s}{:<20d}".format(printBuilding_list[b],remainingList[b] ))   
#========================================================
def option4(b_dict,board):   #done on 1/8
    b_dict = {"HSE": [] ,"FAC": [],"SHP": [] ,"HWY": [] , "BCH": [] }
    global turn
    countFAC = 0   
    for i in range(len(board)):
        for j in range(len(board[0])):
            
        #--------------Calculating BCH---------------
            if board[i][j] == "BCH":
                if j == 1 or j == 4:
                    b_dict["BCH"].append(3)
                else:
                    b_dict["BCH"].append(1)
                    
        #--------------Calculating SHP---------------
            elif board[i][j] == "SHP":
                beside_list = []
                #Putting those buildings that are adjacent into list provided they are different, for each SHP found
                beside_list.append(board[i-1][j])
                if board[i+1][j] not in beside_list:
                    beside_list.append(board[i+1][j])
                if board[i][j+1] not in beside_list:
                    beside_list.append(board[i][j+1])
                if board[i][j-1] not in beside_list:
                    beside_list.append(board[i][j-1])
                #"   "  3 spaces may be mistaken as a building so remove
                if "   " in beside_list:
                    beside_list.remove("   ")
                b_dict["SHP"].append(len(beside_list))
                               
        #--------------Calculating HWY---------------
            elif board[i][j] == "HWY":
                if board[i][j-1] != "HWY":
                    score = 0 
                    while board[i][j] == "HWY":
                        score += 1
                        j += 1
                    for multiply in range(score):#print the scores the number of times
                        b_dict["HWY"].append(score)

        #--------------Calculating HSE---------------  
            elif board[i][j] == "HSE":
                next_list = []
                hseCounter = 0
                shpCounter = 0 
                bchCounter = 0 
                score = 0
                next_list.append(board[i][j-1]) #putting builings one the left into the list
                next_list.append(board[i][j+1])
                next_list.append(board[i-1][j])
                next_list.append(board[i+1][j])
             
                for adjBuildings in next_list:

                    if adjBuildings == "HSE":    #score 1 pt
                        hseCounter += 1
                    elif adjBuildings == "SHP":  #score 1 pt
                        shpCounter += 1 
                    elif adjBuildings == "BCH":  #score 2 pt
                        bchCounter += 1
                    score = hseCounter * 1 + shpCounter * 1 + bchCounter *2 
                        
                    if adjBuildings == "FAC":  #only score 1 pt
                        score = 1 
                        break       #if FAC is found, score is 1 straight away
                b_dict["HSE"].append(score)
                
        #--------------Calculating FAC---------------
            elif board[i][j] == "FAC":
                countFAC += 1
    #Outside for loop as need to wait for loop over to calculate
    if countFAC >= 4:
        remainingFAC = countFAC -4
        for multiply in range(4):
            b_dict["FAC"].append(4)
        for multiply in range(remainingFAC):
            b_dict["FAC"].append(1)
    else:
        for multiply in range(countFAC):
            b_dict["FAC"].append(countFAC)
   
    #======Printing format=====
    finalScore = 0
    for key in b_dict:
        totalPerBuilding = 0 
        score_list = b_dict[key]
        print(key, end = ":")
        if score_list == []:
            print()
        else:
            for i in range(len(score_list)):
                totalPerBuilding += score_list[i]
                print("{}".format(score_list[i]),end="")
                if i == (len(score_list) -1):
                    print(" = {}".format(totalPerBuilding))
                    continue
                print("+",end="")
        finalScore += totalPerBuilding
    if turn <= 16:
        print("Current Score:",finalScore)
    else:
        print("Total Score:",finalScore)

#============================================================
def option5(printBuilding_list,building_list,board):#savegame
    global turn  #done on 6/8
    file = open("simpcity.txt","w")

    file.write(str(turn) + "\n") # write number of turn and then new line
    #writing current layout(board)
    for i in range(len(board)):                 #board
        data = ""
        for j in range(len(board[0])):
            data = data + board[i][j] + ","
        file.write(data + "\n")

    #writing printBuildingList for option3  
    printData = ""
    for buildingForPrint in printBuilding_list:
        printData = printData + buildingForPrint + ","
    file.write(str(printData) + "\n")  
    #writing remaining building in the pool 
    remainingList = ""
    for remainingBuildingInList in (building_list):
        remainingList = remainingList + remainingBuildingInList + ","
    file.write(str(remainingList) + "\n")       
             
        
    file.close()
    
    
#============================================================
def playgame(choice2,board,b1,b2,building_list,b_dict,printBuilding_list):   # all the  building and remaning and calculate score
    #last edit on 6/8
    if choice2 == "1":
        option1(choice2,board,b1,building_list)     #onyly b1 included   
    
    elif choice2 == "2":               #build a random building
        option2(choice2,board,b2,building_list)   #only b2 included
       
    elif choice2 == "3":       #Show remaining buildings
        option3(printBuilding_list,building_list)      
        
    elif choice2 == "4":
        option4(b_dict,board)
#============================================================
def loadgame(): #need to read line by line, no skipping line
    #done on 6/8
    global turn
    try: 
        file = open("simpcity.txt","r")
        #----------reading first line to get turn and transform it to integer------
        turn = int(file.readline())
        #----------reading line by line for making board a list again. ---------
        board = [["   ","   ","   ","   ","   ","   "],   # 6 by 6 
                     ["   ","   ","   ","   ","   ","   "],
                     ["   ","   ","   ","   ","   ","   "],   # 3 spaces
                     ["   ","   ","   ","   ","   ","   "],
                     ["   ","   ","   ","   ","   ","   "],
                     ["   ","   ","   ","   ","   ","   "] ]
        row = 0
        for line in file: #reading it line by line
            line = line.strip("\n") #txt file have "\n" for next line 
            data_list = line.split(",")
            
            for column in range(len(board)):
                board[row][column] = data_list[column]
            row += 1
            if row == 6:
                break
        
        #---------read printBuilding string and make it into a list-----------------
        line = file.readline().strip(",\n") #"'BCH', 'FAC', 'HSE', 'SHP', 'HWY'"
        printBuildingList = line.split(",")  #['BCH', 'FAC', 'HSE', 'SHP', 'HWY']
        
        #---------read buildingList for remainingList, transform it into a list--------
        line = file.readline().strip(",\n") #include a comma(,) so that list will not have another value behind
        buildingList = line.split(",")

        file.close()
    except:
        print("There is no saved game, hence a new game has been loaded.")
        #newgame setting
        turn = 1
        board = [["   ","   ","   ","   ","   ","   "],   
                 ["   ","   ","   ","   ","   ","   "],
                 ["   ","   ","   ","   ","   ","   "],   
                 ["   ","   ","   ","   ","   ","   "],
                 ["   ","   ","   ","   ","   ","   "],
                 ["   ","   ","   ","   ","   ","   "] ]
        buildingList = ["BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY"]
        printBuildingList = ["BCH","FAC","HSE","SHP","HWY"] 
    #------------------scoringDict--------------------------
    scoringDict = {"HSE": [] ,"FAC": [],"SHP": [] ,"HWY": [] , "BCH": [] } #new
    #--------------------after loading--------------------
    while turn <=16:
        start_new_game(turn,board)  #prints turn no. and city
        building1 = drawBuildings(buildingList)                         #drawing random buildings
        building2 = drawBuildings(buildingList) 
        play_game_menu(building1,building2)  #game option 1-5 & 0
        choice2 = input("Your choice?") #related to playgame choice(pick 1-5,0)
        if choice2 == '0':
            break
        elif choice2 == "5":
            option5(printBuildingList,buildingList,board)
            break
                
        playgame(choice2,board,building1,building2,buildingList,scoringDict,printBuildingList)                   
        print() #for ease of playing

        if turn > 16:
            print("Final layout of city")
            displayCity(board)
            option4(scoringDict,board)
#=========================================================
'''
This main program is made out of two while loops, when the python file first runs it enters the first while loop, causing it to display main menu and prompts user for input.
In the case, whereby input is 1 or 2, it plays the game. With input 1 giving a new game setting, a new city, buildingList and score_dict.
While playing the game, it enters a second while loop, whereby turn will only be added if choice 1 or 2 is chosen, which is building.
Else, if choice chosen is 3 4 or 5 turn number will stay. When turn is > 16, it runs the calculation for scores and display the total score for the game.
Input 2 with loading then game and playing it. 
Else, user will exits the inner while loop to go to the outer while loop
it detects which turn it is in, and plays the game. 

'''
#Main program
while True:
    welcome()
    main_menu()
    try: 
        choice = input("Your choice?")
    except:
        print("Please enter appropriately")
        
    if choice == "1":     #1. start new game
        
        exit = False
        score_dict = {"HSE": [] ,"FAC": [],"SHP": [] ,"HWY": [] , "BCH": [] }
        printBuilding_list = ["BCH","FAC","HSE","SHP","HWY"]  #for printing in option 3
        buildings_list = ["BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY",
                            "BCH","FAC","HSE","SHP","HWY"]
        city = [["   ","   ","   ","   ","   ","   "],   # 6 by 6 
                 ["   ","   ","   ","   ","   ","   "],
                 ["   ","   ","   ","   ","   ","   "],   # 3 spaces
                 ["   ","   ","   ","   ","   ","   "],
                 ["   ","   ","   ","   ","   ","   "],
                 ["   ","   ","   ","   ","   ","   "] ]
        turn = 1
        while turn <= 16:
            start_new_game(turn,city)  #prints turn no. and city
            building1 = drawBuildings(buildings_list)                         #drawing random buildings
            building2 = drawBuildings(buildings_list) 
            play_game_menu(building1,building2)  #game option 1-5 & 0
            choice2 = input("Your choice?") #related to playgame choice(pick 1-5,0)
            if choice2 == '0':
                break
            elif choice2 == "5":
                option5(printBuilding_list,buildings_list,city)
                break
                
            playgame(choice2,city,building1,building2,buildings_list,score_dict,printBuilding_list)                   
            print() #for ease of playing

            if turn > 16:
                print("Final layout of city")
                displayCity(city)
                option4(score_dict,city)
    
    elif choice == "2":  #load game
        print("Loading game.")
        loadgame()
        
        
    elif choice == "0":  #exit game
        print("Bye.")
        break

    else:
        exit = False
        

