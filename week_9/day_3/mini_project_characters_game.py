class Character:
    def __init__(self, name, attack=10):

        self.name = name
        self.life = 20
        self.attack = attack
        print(f"I am a {self.__class__.__name__}, my name is {self.name} and I have just been created")

    def basic_attack(self, other):
        other.life -= self.attack
        return other.life


class Druid(Character):

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other_char):
        other_char.life -= (0.75*self.life + 0.75*self.attack)


class Warrior(Character):

    def brawl(self, other_char):
        other_char -= self.attack * 2
        self.life += 0.5*self.attack

    def train(self):
        self.attack += 2
        self.life += 2

    @staticmethod
    def roar(other_char):
        other_char.life -= 3


class Mage(Character):

    @staticmethod
    def curse(other_char):
        other_char.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other_char):
        other_char.life -= self.life / self.attack
        print(f"You have decreased {other_char.name} life by {self.life / self.attack} ")


djeddai = Character("Djeddai")
enemy1 = Character("Enemy")

djeddai.basic_attack(enemy1)


druid1 = Druid('Panoramix')

mage1 = Mage("Ajax")

print("druid1 life", druid1.life)
mage1.cast_spell(druid1)
print("druid1 life after", druid1.life)

print("warrior", mage1.life)
print("druid", druid1.attack)
print(druid1.basic_attack(mage1))
print("test", mage1.life)

print(druid1.life, druid1.attack)

druid1.fight(enemy1)
print(enemy1.life)
print(druid1.life)
druid1.meditate()

print(druid1.life)
print(druid1.attack)




