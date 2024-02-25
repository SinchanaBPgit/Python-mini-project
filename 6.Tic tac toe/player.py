class Player:
    def __init__(self, marker):
        self.marker = marker

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, marker):
        super()._init_(marker)

    def get_move(self, game):
        import random
        return random.choice(game.available_moves())

class HumanPlayer(Player):
    def __init__(self, marker):
        super()._init_(marker)

    def get_move(self, game):
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (1-9): "))
                if move in game.available_moves():
                    valid_move = True
                    return move
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    pass
