# Tic-Tac-Toe: Human vs Computer
import random

board = [" "] * 9

human = input("Choose X or O: ").upper()

if human == "X":
    computer = "O"
else:
    computer = "X"


def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def win(x):

    if (board[0] == x and board[1] == x and board[2] == x) or \
       (board[3] == x and board[4] == x and board[5] == x) or \
       (board[6] == x and board[7] == x and board[8] == x) or \
       (board[0] == x and board[3] == x and board[6] == x) or \
       (board[1] == x and board[4] == x and board[7] == x) or \
       (board[2] == x and board[5] == x and board[8] == x) or \
       (board[0] == x and board[4] == x and board[8] == x) or \
       (board[2] == x and board[4] == x and board[6] == x):

        return True

    return False


# Goal-Based Agent
def computerChoice():

    # Try to win
    for i in range(9):

        if board[i] == " ":

            board[i] = computer

            if win(computer):
                board[i] = " "
                return i

            board[i] = " "

    # Try to block HUMAN
    for i in range(9):

        if board[i] == " ":

            board[i] = human

            if win(human):
                board[i] = " "
                return i

            board[i] = " "

    # Choose any empty position
    while True:

        pos = random.randint(0, 8)

        if board[pos] == " ":
            return pos


# Main game
for turn in range(9):

    display()

    # HUMAN TURN
    if turn % 2 == 0:

        while True:

            position = int(input("Enter position (1-9): ")) - 1

            if board[position] == " ":
                board[position] = human
                break

            else:
                print("Position already occupied! Try again.")

        if win(human):
            display()
            print("Human Wins!")
            print("1BF24CS261 Sagarmatha Khatri")
            break

    # COMPUTER TURN
    else:

        pos= computerChoice()

        board[pos] = computer

        print("Computer chose:", pos + 1)

        if win(computer):
            display()
            print("Computer Wins!")
            print("1BF24CS261 Sagarmatha Khatri")
            break

else:

    display()
    print("Game is a Draw!")
    print("1BF24CS261 Sagarmatha Khatri")