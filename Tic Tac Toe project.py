from IPython.display import clear_output

def display_board(board):
    clear_output()

    print('  |   |  ')
    print(board[7]+" | "+board[8]+" | "+board[9])
    print("  | "+"  |  ")
    print("---------")
    print("  | "+"  |  ")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("  | "+"  |  ")
    print("---------")
    print("  | "+"  |  ")
    print(board[1]+" | "+board[2]+" | "+board[3])
    print("  | "+"  |  ")

initial_board = ['#'," ",' ',' ',' ',' ',' ',' ',' ',' ']

def space_check(initial_board, position):

    return initial_board[position]==" "

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):

    return ((board[1]==board[2]==board[3]==mark) or
            (board[4]==board[5]==board[6]==mark) or
            (board[7]==board[8]==board[9]==mark) or

            (board[1]==board[4]==board[7]==mark) or
            (board[2]==board[5]==board[8]==mark) or
            (board[3]==board[6]==board[9]==mark) or

            (board[3]==board[5]==board[7]==mark) or
            (board[1]==board[5]==board[9]==mark))


def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def replay():

    replay_choice=input("Do you want to play again? Yes or No")
    if replay_choice.lower()=="yes":
        return True
    else:
        return False

display_board(initial_board)
print('Welcome to Tic Tac Toe!')
start_game=input("Are you ready to start the game?")
clear_output()
display_board(initial_board)


def game ():

    replay_choice =""

    if start_game.lower()=="yes" or replay_choice.lower()=="yes":
        clear_output()
        initial_board = ['#'," ",' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(initial_board)
        import random
        flip=random.randint(0,1)
        if flip==0:
            print("Player_1 you are going first!")
            y=1
        else:
            print("Player_2 you are going first!")
            y=2

        #player input
        player_choice=""
        while player_choice!="X" and player_choice!= "O":
            player_choice=input(f"Player {y} do you want to be X or O ?")

        player1=player_choice
        if player1=="X":
            player2="O"
        else:
            player2="X"

        #player_choice()
        position=0

        while position not in [1,2,3,4,5,6,7,8,9] or not space_check(initial_board,position):
            position=int(input("Choose a position:(1-9)"))

        clear_output()
        place_marker(initial_board,player1,position)
        display_board(initial_board)

        if y==1:
            print("Player_2 now is your turn!")
            z=2
        else:
            print("Player_1 now is your turn!")
            z=1


        while win_check(initial_board,'O')==False and win_check(initial_board,'X')==False:


            #player_choice()
            position=0

            while position not in [1,2,3,4,5,6,7,8,9] or not space_check(initial_board,position):
                position=int(input("Choose a position:(1-9)"))

            place_marker(initial_board,player2,position)
            display_board(initial_board)

            if y==1:
                print("Player_1 now is your turn!")
            else:
                print("Player_2 now is your turn!")

            if win_check(initial_board,'O')==True:
                print(f"End of the game! Player {z} wins!")
                break
            elif win_check(initial_board,'X')==True:
                print(f"End of the game! Player {z} wins!")
                break

            if full_board_check(initial_board)==True:
                clear_output()
                replay_choice1=input("Tie game! Want to play again to see who wins?")
                if replay_choice1.lower()=="yes":
                    clear_output()
                    game ()
                else:
                    clear_output()
                    print("End of Game! Thank you for playing :)")
                    break
                break

            #player_choice()
            position=0

            while position not in [1,2,3,4,5,6,7,8,9] or not space_check(initial_board,position):
                position=int(input("Choose a position:(1-9)"))

            place_marker(initial_board,player1,position)
            display_board(initial_board)

            if y==1:
                print("Player_2 now is your turn!")
            else:
                print("Player_1 now is your turn!")

            if win_check(initial_board,'O')==True:
                print(f"End of the game! Player {y} wins!")
                break
            elif win_check(initial_board,'X')==True:
                print(f"End of the game! Player {y} wins!")
                break

            if full_board_check(initial_board)==True:
                clear_output()
                replay_choice1=input("Tie game! Want to play again to see who wins?")
                if replay_choice1.lower()=="yes":
                    clear_output()
                    game ()
                else:
                    clear_output()
                    print("End of Game! Thank you for playing :)")
                    break
                break

        if win_check(initial_board,'O')==True or win_check(initial_board,'X')==True:

            replay_choice=input("Do you want to play again? Yes or No")
            if replay_choice.lower()=="yes":
                print("Allright")
                game ()
            else:
                clear_output()

                print("End of Game! Thank you for playing :)")


    else:
        print("End of Game! Thank you for playing :)")

game ()  
