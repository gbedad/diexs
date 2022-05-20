import random


class Game:
    def __init__(self):
        self.dict_results = {}

    def get_user_item(self):
        user_input = input("Enter (r)ock, (p)aper or (s)issors: ")
        return user_input

    def get_computer_item(self):
        return random.choice(["r", "p", "s"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif user_item == 'r':
            if computer_item == 'p':
                return 'loss'
            else:
                return 'win'
        elif user_item == 'p':
            if computer_item == 'r':
                return 'win'
            else:
                return 'loss'
        elif user_item == 's':
            if computer_item == 'r':
                return 'loss'
            else:
                return 'win'

        elif user_item == 'q':
            return 'quit'

    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        result = self.get_game_result(user, computer)
        if user == 'r' or user == 's' or user == 'p':
            print(f"You choose {user} and the computer {computer}: {result}")
        else:
            print("You have chosen to quit, bye.")
        if result in self.dict_results.keys():
            self.dict_results[result] += 1
        else:
            self.dict_results[result] = 1
        return result, self.dict_results


def print_results(results):
    conjugate = {'win': 'won', 'loss': 'lost', 'draw': 'drew'}
    for k, v in results.items():
        if k != 'quit':
            print(f"You {conjugate[k]} {results[k]} times")
      

def get_user_menu_choice():
    print("\n1- Play a new game\n2- Show scores and Quit")
    user_choice = input("Enter your choice (1 or 2): ")
    return user_choice


def main():
    user_play = True
    while user_play:
        user_choice = get_user_menu_choice()
        if user_choice == '1':
            new_game = Game()

            print("\ntype 'q' to end the game")
            while new_game.play()[0] != 'quit':
                my_game = new_game.play()
                if my_game[0] == 'quit':
                    break

        elif user_choice == '2':
            # TODO raise an exception if option before playing a game
            print("Results")
            print_results(my_game[1])
            print("Thanks for playing")
            break


main()
