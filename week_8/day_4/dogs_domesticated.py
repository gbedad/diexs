# Dogs domesticated
import random
from exercise_xp import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True
        print(f"{self.name} is trained")

    def play(self, *args):
        print(f"{self.name},{','.join(x for x in args)} all play together")

    def do_a_trick(self):
        trick = random.choice(["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"])
        print(f"{self.name} {trick}")


new_pet = PetDog("Charlie", 4, 56)

new_pet.train()
new_pet.play("tom", "bob", "rex")
new_pet.do_a_trick()


