import os    
import time  
import random  
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
Player = 1 
flag = 99
previous = 0  
   
#Flags for the game     
Win = 1    
Draw = -1    
Running = 0       
  
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
#This Function Checks player has won or not    
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win
        return 1    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win
        return 1     
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win  
        return 1   
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win
        return 1     
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win 
        return 1    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game = Win
        return 1     
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win 
        return 1    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game = Win 
        return 1    
    #Match Tie or Draw Condition    
    elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):    
        Game = Draw 
        return 0   
    else:            
        Game = Running 

def IntelligentComputer():
    global Player
    global flag
    global previous
    flag = 99
    if(CheckPosition(7)):
            print("Player 1's chance")
            Mark = 'X'  
            board[7] = Mark       
            flag = CheckWin()
            if(flag == 1):
                return 1
            DrawBoard() 
            DumbHuman()
            #If O plays center
            if(CheckPosition(5) == False):
                print("X Played")
                Mark = 'X'  
                board[3] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                #If O plays middle down
                if(CheckPosition(8) == False):
                    print("X Played")
                    Mark = 'X'  
                    board[2] = Mark       
                    flag = CheckWin()
                    if(flag == 1):
                        return 1
                    DrawBoard() 
                    DumbHuman()
                    if(CheckPosition(1)):
                        print("X Played")
                        Mark = 'X'  
                        board[1] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                    else:
                        print("X Played")
                        Mark = 'X'  
                        board[9] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                        if(CheckPosition(6)):
                            print("X Played")
                            Mark = 'X'  
                            board[6] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                        else:
                            print("X Played")
                            Mark = 'X'  
                            board[4] = Mark       
                            flag = CheckWin()
                            DrawBoard() 
                            if(flag == 1):
                                return 0
                #If O plays middle up
                if(CheckPosition(2) == False):
                    print("X Played")
                    Mark = 'X'  
                    board[8] = Mark       
                    flag = CheckWin()
                    if(flag == 1):
                        return 1
                    DrawBoard() 
                    DumbHuman()
                    if(CheckPosition(9)):
                        print("X Played")
                        Mark = 'X'  
                        board[9] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                    else:
                        print("X Played")
                        Mark = 'X'  
                        board[1] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                        if(CheckPosition(4)):
                            print("X Played")
                            Mark = 'X'  
                            board[4] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                        else:
                            print("X Played")
                            Mark = 'X'  
                            board[6] = Mark       
                            flag = CheckWin()
                            DrawBoard() 
                            if(flag == 1):
                                return 0
                #If O plays middle left
                if(CheckPosition(4) == False):
                    print("X Played")
                    Mark = 'X'  
                    board[6] = Mark       
                    flag = CheckWin()
                    if(flag == 1):
                        return 1
                    DrawBoard() 
                    DumbHuman()
                    if(CheckPosition(9)):
                        print("X Played")
                        Mark = 'X'  
                        board[9] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                    else:
                        print("X Played")
                        Mark = 'X'  
                        board[1] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                        if(CheckPosition(2)):
                            print("X Played")
                            Mark = 'X'  
                            board[2] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                        else:
                            print("X Played")
                            Mark = 'X'  
                            board[8] = Mark       
                            flag = CheckWin()
                            DrawBoard() 
                            if(flag == 1):
                                return 0
                #If O plays middle right
                if(CheckPosition(6) == False):
                    print("X Played")
                    Mark = 'X'  
                    board[4] = Mark       
                    flag = CheckWin()
                    if(flag == 1):
                        return 1
                    DrawBoard() 
                    DumbHuman()
                    if(CheckPosition(1)):
                        print("X Played")
                        Mark = 'X'  
                        board[1] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                    else:
                        print("X Played")
                        Mark = 'X'  
                        board[9] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                        if(CheckPosition(8)):
                            print("X Played")
                            Mark = 'X'  
                            board[8] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                        else:
                            print("X Played")
                            Mark = 'X'  
                            board[2] = Mark       
                            flag = CheckWin()
                            DrawBoard() 
                            if(flag == 1):
                                return 0   
                               
                ###################################
                elif(CheckPosition(1)):
                    print("X Played")
                    Mark = 'X'  
                    board[1] = Mark       
                    flag = CheckWin()
                    if(flag == 1):
                        return 1
                    DrawBoard() 
                    DumbHuman()
                    if(CheckPosition(2)):
                        print("X Played")
                        Mark = 'X'  
                        board[2] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                    else:
                        print("X Played")
                        Mark = 'X'  
                        board[4] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                else:
                    print("X Played")
                    Mark = 'X'  
                    board[9] = Mark       
                    flag = CheckWin()
                    if(flag == 1):
                        return 1
                    DrawBoard() 
                    DumbHuman()
                    if(CheckPosition(6)):
                        print("X Played")
                        Mark = 'X'  
                        board[6] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                    else:
                        print("X Played")
                        Mark = 'X'  
                        board[8] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
            #If O plays adjacent up
            elif(CheckPosition(4) == False):
                print("X Played")
                Mark = 'X'  
                board[9] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(8)):
                        print("X Played")
                        Mark = 'X'  
                        board[8] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                else:
                        print("X Played")
                        Mark = 'X'  
                        board[3] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                        if(CheckPosition(5)):
                            print("X Played")
                            Mark = 'X'  
                            board[5] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                        else:
                            print("X Played")
                            Mark = 'X'  
                            board[6] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
            #If O plays adjacent right
            elif(CheckPosition(8) == False):
                print("X Played")
                Mark = 'X'  
                board[1] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(4)):
                        print("X Played")
                        Mark = 'X'  
                        board[4] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                else:
                        print("X Played")
                        Mark = 'X'  
                        board[3] = Mark       
                        flag = CheckWin()
                        if(flag == 1):
                            return 1
                        DrawBoard() 
                        DumbHuman()
                        if(CheckPosition(5)):
                            print("X Played")
                            Mark = 'X'  
                            board[5] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                        else:
                            print("X Played")
                            Mark = 'X'  
                            board[2] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
            #If O plays diagonal up
            elif(CheckPosition(1) == False):
                print("X Played")
                Mark = 'X'  
                board[9] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(8)):
                            print("X Played")
                            Mark = 'X'  
                            board[8] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                else:
                            print("X Played")
                            Mark = 'X'  
                            board[3] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                if(CheckPosition(5)):
                                print("X Played")
                                Mark = 'X'  
                                board[5] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[6] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
            #If O plays diagonal right
            elif(CheckPosition(9) == False):
                print("X Played")
                Mark = 'X'  
                board[1] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(4)):
                            print("X Played")
                            Mark = 'X'  
                            board[4] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                else:
                            print("X Played")
                            Mark = 'X'  
                            board[3] = Mark       
                            flag = CheckWin()
                            if(flag == 1):
                                return 1
                            DrawBoard() 
                            DumbHuman()
                if(CheckPosition(5)):
                                print("X Played")
                                Mark = 'X'  
                                board[5] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[2] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
            #If O plays middle right
            elif(CheckPosition(6) == False):
                print("X Played")
                Mark = 'X'  
                board[9] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(8)):
                                print("X Played")
                                Mark = 'X'  
                                board[8] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[1] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                if(CheckPosition(5)):
                                print("X Played")
                                Mark = 'X'  
                                board[5] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[4] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
            #If O plays middle top
            elif(CheckPosition(2) == False):
                print("X Played")
                Mark = 'X'  
                board[1] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(4)):
                                print("X Played")
                                Mark = 'X'  
                                board[4] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[9] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                if(CheckPosition(5)):
                                print("X Played")
                                Mark = 'X'  
                                board[5] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[8] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
            #If O plays opposite corner
            elif(CheckPosition(3) == False):
                print("X Played")
                Mark = 'X'  
                board[1] = Mark       
                flag = CheckWin()
                if(flag == 1):
                    return 1
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(4)):
                                print("X Played")
                                Mark = 'X'  
                                board[4] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[9] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                if(CheckPosition(5)):
                                print("X Played")
                                Mark = 'X'  
                                board[5] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()
                else:
                                print("X Played")
                                Mark = 'X'  
                                board[8] = Mark       
                                flag = CheckWin()
                                if(flag == 1):
                                    return 1
                                DrawBoard() 
                                DumbHuman()

def DumbHuman():
    print("Player 2's chance") 
    global Player
    global flag
    global previous
    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    if(CheckPosition(choice)): 
            Mark = 'O'    
            board[choice] = Mark    
            Player += 1 
            CheckWin()
    

print("Tic-Tac-Toe Game")    
print("Player 1 [X] & Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)    
while(Game == Running):    
    #os.system('cls')     
    if(Player % 2 != 0):        
        flag = IntelligentComputer()
        if(flag == 1):
            break
     
       
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    print("You Lost!")    