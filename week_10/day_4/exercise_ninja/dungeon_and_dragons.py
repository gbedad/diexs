from random import randint


class Character:
    count_characters = 0
    characters_list = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.strength = self.discard_min_and_sum(self.trow_dices())
        self.dexterity = self.discard_min_and_sum(self.trow_dices())
        self.constitution = self.discard_min_and_sum(self.trow_dices())
        self.intelligence = self.discard_min_and_sum(self.trow_dices())
        self.wisdom = self.discard_min_and_sum(self.trow_dices())
        self.charisma = self.discard_min_and_sum(self.trow_dices())
        Character.count_characters += 1
        Character.characters_list.append(self)

    @classmethod
    def discard_min_and_sum(cls, arr):
        minimum = min(arr)
        arr.remove(minimum)
        prop = sum(arr)
        return prop

    @staticmethod
    def trow_dices():
        dices = []
        for i in range(4):
            dice = randint(1, 6)
            dices.append(dice)
        return dices

    def __str__(self):
        text = f"name: {self.name}\nage: {self.age}\nIntelligence: {self.intelligence}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"
        return text


class Game:

    def __init__(self):
        self.characters = Character.characters_list

    def __str__(self):
        return Character.__str__(self)

    @staticmethod
    def show_how_many():
        print(f"Total number of players created: {Character.count_characters}")

    def characters_game(self):
        print("Characters of the Game\n----------------------")

        for item in self.characters:

            print(item)
            print("------------------")










player1 = Character("Joe", 24)
player2 = Character("James", 32)
player3 = Character("Jane", 22)
player4 = Character("Junior", 44)

game = Game()
game.show_how_many()
game.characters_game()
