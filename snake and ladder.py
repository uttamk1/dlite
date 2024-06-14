import random

# Define snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to roll a die
def roll_die():
    return random.randint(1, 6)

# Function to move the player
def move_player(player, steps):
    new_position = player + steps
    if new_position in snakes:
        print("Oh no! You landed on a snake!")
        new_position = snakes[new_position]
    elif new_position in ladders:
        print("Yay! You climbed a ladder!")
        new_position = ladders[new_position]
    return new_position

# Function to play the game
def play_game():
    player1_position = 0
    player2_position = 0
    
    while True:
        input("Player 1, press Enter to roll the die: ")
        steps = roll_die()
        print("Player 1 rolled a", steps)
        player1_position = move_player(player1_position, steps)
        print("Player 1 is now at position", player1_position)
        if player1_position >= 100:
            print("Player 1 wins!")
            break

        input("Player 2, press Enter to roll the die: ")
        steps = roll_die()
        print("Player 2 rolled a", steps)
        player2_position = move_player(player2_position, steps)
        print("Player 2 is now at position", player2_position)
        if player2_position >= 100:
            print("Player 2 wins!")
            break

# Play the game
play_game()
