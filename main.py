moves = {str(i): "-" for i in range(1,10)}

def update_board():
    return f"""
             
      |     |     
   {moves["7"]}  |  {moves["8"]}  |  {moves["9"]}  
 _____|_____|_____
      |     |     
   {moves["4"]}  |  {moves["5"]}  |  {moves["6"]}  
 _____|_____|_____
      |     |     
   {moves["1"]}  |  {moves["2"]}  |  {moves["3"]}  
      |     |    
        """

def make_move(player, move):
    if moves[move] == "-":
        moves[move] = player
    else:
        move = input(f"That space is taken. chose again for player {player}: ")
        make_move(player, move)

def is_draw(moves):
    if "-" not in moves.values():
        return True
    else:
        return False

def is_win(player, moves):
    if (moves["1"] == player and moves["2"] == player and moves["3"] == player) or \
        (moves["4"]==player and moves["5"]==player and moves["6"]==player) or \
            (moves["7"]==player and moves["8"]==player and moves["9"]==player) or \
                (moves["1"]==player and moves["4"]==player and moves["7"] ==player) or \
                    (moves["2"]==player and moves["5"]==player and moves["8"]==player) or \
                        (moves["3"]==player and moves["6"]==player and moves["9"]==player) or \
                            (moves["1"]==player and moves["5"]==player and moves["9"]==player) or \
                                (moves["7"]==player and moves["5"]==player and moves["3"]==player):
        return True
    else:
        return False

def check_status(player, moves):
    if is_win(player, moves):
        print(f"{player} wins.")
        return True
    elif is_draw(moves):
        print("Its a draw")
        return True
    else:
        return False

print(update_board())
while True:
    player = "X"
    move = input(f"{player} plays now. Make a move using Num Keys. ")
    make_move(player, move)
    print(update_board())
    if check_status(player, moves):
        break
    player = "O"
    move = input(f"{player} plays now. Make a move using Num Keys. ")
    make_move(player, move)
    print(update_board())
    if check_status(player, moves):
        break
    