import random


def welcome():
    print("Welcome to Tic Tac Toe!")


def display_board(board):
    """
    prints out tic tac toe board
    :param board: list of values in tic tac toe board
    :return: None
    """
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    pass


def player_input():
    pl1 = ""
    while pl1 != "X" and pl1 != "O":
        pl1 = input('Player 1 choose X or O: ')
    if pl1 == "X":
        pl2 = "O"
    else:
        pl2 = "X"
    return pl1, pl2


def place_marker(board, score, marker, position):
    """
    takes in a board list obj, score arr, marker, and a position and assigns it to a board
    updates score table
    :param board: list
    :param score: list
    :param marker: 'X' or 'O'
    :param position: int 1-9
    :return:
    """
    board[position] = marker
    inc = 0
    if marker == "X":
        inc = 1
    else:
        inc = -1
    if position == 7:
        score[0] += inc
        score[3] += inc
        score[6] += inc
    elif position == 8:
        score[0] += inc
        score[4] += inc
    elif position == 9:
        score[0] += inc
        score[5] += inc
        score[7] += inc
    elif position == 4:
        score[1] += inc
        score[3] += inc
    elif position == 5:
        score[1] += inc
        score[4] += inc
        score[6] += inc
        score[7] += inc
    elif position == 6:
        score[1] += inc
        score[5] += inc
    elif position == 1:
        score[2] += inc
        score[3] += inc
        score[7] += inc
    elif position == 2:
        score[2] += inc
        score[4] += inc
    elif position == 3:
        score[2] += inc
        score[5] += inc
        score[6] += inc


def check_winner(board, score):
    """
    if any of the values in score array are == 3 then player 1 wins
    if any of the values in score array are == -3 then player 2 wins
    if board is full and no one has one then it's a tie
    return True if game has ended otherwise return False
    :param board: list
    :param score: list
    :return: True
    """
    if 3 in score:
        display_board(board)
        print("Player 1 Wins!")
    elif -3 in score:
        display_board(board)
        print("Player 2 Wins!")
    elif " " not in board:
        display_board(board)
        print("It's a Tie!")
    else:
        return False
    return True


def choose_first():
    res = random.randint(0, 1)
    if res == 0:
        return 'Player 1'
    return 'Player 2'


def space_check(board, pos):
    return board[pos] == " "


def player_turn(board):
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        pos = int(input("Choose a position 1-9: "))
    return pos


def replay():
    playAgain = ""
    while playAgain != "Yes" and playAgain != "No":
        playAgain = input("Do you want to play again? Yes or No? ")
    return playAgain == "Yes"


if __name__ == '__main__':
    welcome()
    while True:
        p1, p2 = player_input()
        print(f'Player 1 is {p1}')
        print(f'Player 2 is {p2}')
        # [r1,r2,r3,c1,c2,c3,d1,d2]
        currScore = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        currBoard = ["#"] + [" "] * 9
        turn = choose_first()
        print(turn + " will go first")
        play_game = input("Ready? Yes or No? ")
        if play_game == "Yes":
            game_on = True
        else:
            game_on = False
        while game_on:
            if turn == "Player 1":
                display_board(currBoard)
                position = player_turn(currBoard)
                place_marker(currBoard, currScore, p1, position)
                if check_winner(currBoard, currScore):
                    game_on = False
                else:
                    turn = "Player 2"
            else:
                display_board(currBoard)
                position = player_turn(currBoard)
                place_marker(currBoard, currScore, p2, position)
                if check_winner(currBoard, currScore):
                    game_on = False
                else:
                    turn = "Player 1"
        if not replay():
            break
