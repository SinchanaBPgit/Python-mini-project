Tic Tac Toe Game
This is a simple Tic Tac Toe game implemented in Python.

Overview
Tic Tac Toe is a classic two-player game where players take turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

Features
Player Classes: Two player classes are implemented - HumanPlayer for human players and RandomComputerPlayer for computer players making random moves.
Game Logic: The TicTacToe class handles the game logic, including checking for a winner, making moves, and printing the game board.
Game Playback: The play function orchestrates the game by alternating player turns until the game is won or ends in a tie.
How to Play
Run the player.py file to initialize the player classes.
Run the game.py file to start a game of Tic Tac Toe.
Enter moves according to the prompt (for HumanPlayer) or watch the computer make random moves (for RandomComputerPlayer).
The game will continue until a player wins or the board is full (resulting in a tie).
File Structure
player.py: Contains the Player, RandomComputerPlayer, and HumanPlayer classes for defining players.
game.py: Contains the TicTacToe class and the play function for executing the game.
Customization
Player Types: You can create custom player classes by inheriting from the Player class and implementing the get_move method.
Game Delay: Adjust the time delay between moves by modifying the sleep duration in the play function.
Contributing
Contributions are welcome! If you have any suggestions, bug reports, or enhancements, feel free to open an issue or submit a pull request.
