import random
import sys

#Created the class for the game
class Rock_Paper_Scissors:
    #Init the constructor
    def __init__(self) -> None:
        print("Welcome to Rock Paper Scissors Game")
        #Declared the moves for the game
        self.moves: dict = {
            'rock': '🗿',
            'paper':  '📰',
            'scissors': '✂'  
        }
        #Declared the valid moves
        self.valid_moves: list[str] = list(self.moves.keys())
    
    #Function to init the game
    def play_game(self):
        user_input: str = input("Choose betwenn rock, paper, scissors? ").lower()
        print('To exit please enter "exit"')
        if user_input == 'exit':
            print("Thanks for playing")
            #to exit the program
            sys.exit()

        if user_input not in self.valid_moves:
            print("Please introduce a valir move.")
            #Re call the function until the user enter a valid input
            return self.play_game()
        
        #The computer choose a move
        computer_move = random.choice(self.valid_moves)
        
        self.display_moves(user_input,computer_move)
        self.check_moves(user_input,computer_move)
    
    def display_moves(self, user_input: str, computer_move: str):
        print("--------------------")
        print(f"Player: {self.moves[user_input]}")
        print(f"Computer: {self.moves[computer_move]}")
        print("--------------------")

    def check_moves(self, user_input: str, computer_move:str):
        if user_input == computer_move:
            print("It's a Tie")
        elif user_input == 'rock' and computer_move == 'scissors':
            print("Congratulation!!!! You Win!!")
        elif user_input == 'paper' and computer_move == 'rock':
            print("Congratulation!!!! You Win!!")
        elif user_input == 'scissors' and computer_move == 'paper':
            print("Congratulation!!!! You Win!!")
        else: 
            print("Too bad! You Loose")

if __name__ == "__main__":
    rock_paper_scissors = Rock_Paper_Scissors()
    while True:
        rock_paper_scissors.play_game()