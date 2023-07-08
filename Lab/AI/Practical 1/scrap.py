if(CheckPosition(1) and (CheckPosition(3) or CheckPosition(7))):
        print("Player 2's chance")
        Mark = 'O'  
        board[1] = Mark      
        CheckWin()
        DrawBoard() 
        DumbHuman()
        if(CheckPosition(7)):
            print("Player 2's chance")
            Mark = 'O'  
            board[7] = Mark       
            CheckWin()
            DrawBoard() 
            DumbHuman()
            if(CheckPosition(3)):
                print("Player 2's chance")
                Mark = 'O'  
                board[3] = Mark       
                CheckWin()
                DrawBoard() 
                DumbHuman()
            elif(CheckPosition(9)):
                print("Player 2's chance")
                Mark = 'O'  
                board[9] = Mark       
                CheckWin()
                DrawBoard() 
                DumbHuman()
        if(CheckPosition(3)):
                print("Player 2's chance")
                Mark = 'O'  
                board[3] = Mark       
                CheckWin()
                DrawBoard() 
                DumbHuman()
                if(CheckPosition(9)):
                    print("Player 2's chance")
                    Mark = 'O'  
                    board[9] = Mark       
                    CheckWin()
                    DrawBoard() 
                    DumbHuman()