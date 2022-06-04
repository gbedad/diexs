from random import randint


class Character:
    count_characters = 0

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


class Game(Character):
    def __init__(self):
        self.count = Character.count_characters

    def show_how_many(self):
        print(self.count)


player1 = Character("Joe", 24)
player2 = Character("James", 32)
player3 = Character("Jane", 22)
player4 = Character("Junior", 44)

game = Game()
print(game.count_characters)

print(player1.intelligence)