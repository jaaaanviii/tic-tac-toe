#creating a custom exception class if the user enters a value less than 0 or greater than 8
class valueError(Exception):
    pass
#function to print tic tac toe board
def printBoard(x,y):
    #condition to check if user entered something at 0 position if user enters nothing on this position then printing the position number
    if(x[0] ==1):
        zero = "X"
    else:
        if(y[0] ==1):
            zero = "O"
        else:
            zero = "0"
    #condition to check if user entered something at 1 position if user enters nothing on this position then printing the position number        
    if(x[1] ==1):
        one = "X"
    else:
        if(y[1] ==1):
            one = "O"
        else:
            one = "1"
    #condition to check if user entered something at 2 position if user enters nothing on this position then printing the position number        
    if(x[2] ==1):
        two = "X"
    else:
        if(y[2] ==1):
            two = "O"
        else:
            two = "2"
    #condition to check if user entered something at 3 position if user enters nothing on this position then printing the position number        
    if(x[3] ==1):
        three = "X"
    else:
        if(y[3] ==1):
            three = "O"
        else:
            three = "3"
    #condition to check if user entered something at 4 position if user enters nothing on this position then printing the position number        
    if(x[4] ==1):
        four = "X"
    else:
        if(y[4] ==1):
            four = "O"
        else:
            four = "4"
    #condition to check if user entered something at 5 position if user enters nothing on this position then printing the position number        
    if(x[5] ==1):
        five = "X"
    else:
        if(y[5] ==1):
            five = "O"
        else:
            five = "5"
    #condition to check if user entered something at 6 position if user enters nothing on this position then printing the position number
    if(x[6] ==1):
        six = "X"
    else:
        if(y[6] ==1):
            six = "O"
        else:
            six = "6"
    #condition to check if user entered something at 7 position if user enters nothing on this position then printing the position number        
    if(x[7] ==1):
        seven = "X"
    else:
        if(y[7] ==1):
            seven = "O"
        else:
            seven = "7"
    #condition to check if user entered something at 8 position if user enters nothing on this position then printing the position number    
    if(x[8] ==1):
        eight = "X"
    else:
        if(y[8] ==1):
            eight = "O"
        else:
            eight = "8"
            
    #printing board with 9 values 
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
#function to check if a user won the game
def win(x,y):
    #created a list of lists with all win conditions
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    #a loop on wins to check if a user won the game
    for win in wins:
        #checking if X wins 
        if(x[win[0]]+x[win[1]]+x[win[2]]==3):
            print("\nCongratulations!! X wins")
            return True
        #checking if O wins
        if(y[win[0]]+y[win[1]]+y[win[2]]==3):
            print("\nCongratulations!! O wins")
            return True
    #returning false if no one wins
    return False
#main function    
if __name__ == "__main__":
    #two lists to keep track of where the users entered their input
    xMove = [0,0,0,0,0,0,0,0,0]
    oMove = [0,0,0,0,0,0,0,0,0]
    #printing welcome message
    print("Welcome to Tic Tac Toe\n")
    #printing the tic tac toe board for the first time 
    printBoard(xMove, oMove)
    #turn variable to check who's turn it is
    turn = 1
    #a counter for how many moves has been made by both the users
    i=0
    #while loop for changing turns for users until someone wins or all the moves has been exhausted by both users
    while(True):
        #incrementing i for one move made
        i+=1
        #checking if all the moves has been exhausted by both the users if yes then ending the game
        if(i==10):
            print("\nIt's a tie!!\nThe match is over.\n\n")
            break
        #checking if it's X's turn and taking input from X user to mark their move
        if(turn==1):
            print("\nX's turn")
            #loop for exception handling if the user keeps triggering the exception
            while(True):
                #exception try block 
                try:
                    x = int(input("Please enter the position number where you want to mark X: "))
                    #checking if the user entered value below 0 or above 8 and raise the exception if he did
                    if(x<0 or x>8):
                        raise valueError("Invalid input, value must be between 0 and 8")
                    #checking if the place is already taken if it is then raising an exception
                    if(xMove[x]==1 or oMove[x]==1):
                        raise valueError("This position has already been marked, please choose another")
                    xMove[x] = 1
                    break
                except valueError as e:
                    print("Error: ",e)
        #checking if it's O's turn and taking input from O user to mark their move
        if(turn==0):
            print("\nO's turn")
            #loop for exception handling if the user keeps triggering the exception
            while(True):
                #exception try block 
                try:
                    y = int(input("Please enter the position number where you want to mark O: "))
                    #checking if the user entered value below 0 or above 8 and raise the exception if he did
                    if(y<0 or y>8):
                        raise valueError("Invalid input, value must be between 0 and 8")
                    #checking if the place is already taken if it is then raising an exception
                    if(oMove[y]==1 or xMove[y]==1):
                        raise valueError("This position has already been marked, please choose another")            
                    oMove[y] = 1
                    break
                except valueError as e:
                    print("Error: ",e)
        #calling function to check if any user won
        w = win(xMove,oMove)
        #printing match over if one of the user wins
        if(w):
            print("The match is over.\n\n")
            printBoard(xMove, oMove)
            break
        #Changing the turn of the user's
        turn = 1-turn
        #calling function to print board with latest values
        printBoard(xMove, oMove)
