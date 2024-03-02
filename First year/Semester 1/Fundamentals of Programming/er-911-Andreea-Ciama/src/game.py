import Board
import Brain


while True:
    board = Board.Board()
    board.inputPlayerLetter()
    turn = board.firstMove()
    print('The %s will go first.' % turn)
    if turn == 'player':
        print(board.drawBoard())

    playing = True

    while playing:
        if turn == 'player':
            # Player's turn.
            board.getPlayerMove()

            outcome = board.isWinner()
            if outcome == 'win':
                print(board.drawBoard())
                print('Hooray! You have won the game!')
                playing = False
                break
            elif outcome == 'draw':

                print(board.drawBoard())
                print('The game is a tie!')
                playing = False
                break
            else:
                turn = 'computer'

        else:

            brain = Brain.Brain(Board.Board(), board.computer_token)
            board.makeComputerMove(brain)

            outcome = board.isWinner()
            if outcome == 'win':
                print(board.drawBoard())
                print('The computer has beaten you! You lose.')
                playing = False
                break
            elif outcome == 'draw':
                print(board.drawBoard())
                print('The game is a tie!')
                playing = False
                break
            else:
                turn = 'player'

    if not board.playAgain():
        break
