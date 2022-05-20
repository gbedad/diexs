import random


class Game:
    def __init__(self):
        self.dict_results = {}

    def get_user_item(self):
        return input("Enter (r)ock, (p)aper or (s)issors: ")

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

    def play(self):
        user_choice = self.get_user_menu_choice()
        if user_choice == 'q':
            return False

        if user_choice == '1':
            user_choice = self.get_user_item()
            computer = self.get_computer_item()
            result = self.get_game_result(user_choice, computer)

            if user_choice == 'r' or user_choice == 's' or user_choice == 'p':
                print(f"You choose {user_choice} and the computer {computer}: {result}")
            else:
                print("You have chosen to quit, bye.")
            if result in self.dict_results.keys():
                self.dict_results[result] += 1
            else:
                self.dict_results[result] = 1

        elif user_choice == '2':
            print("Results")
            self.print_results(self.dict_results)
            print("Thanks for playing")

        return True

    def print_results(self, results):
        conjugate = {'win': 'won', 'loss': 'lost', 'draw': 'drew'}
        for k, v in results.items():

            print(f"You {conjugate[k]} {results[k]} times")

    def get_user_menu_choice(self):
        print("\nMenu:\n1- Play a new game\n2- Show scores\nq- Quit")
        user_choice = input("Enter your choice (1, 2 or q): ")
        return user_choice


def main():
    keep_play = True

    new_game = Game()
    while keep_play:
        keep_play = new_game.play()


main()
