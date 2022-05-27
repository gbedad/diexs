class Human:
    def __init__(self, id_number, name, age, blood_type, priority=False):
        self.id = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        if person.id not in self.family:
            self.family.append(person)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):

        if person.age > 60 or person.priority is True:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
        return self.humans

    def find_in_queue(self, person):
        if person not in self.humans:
            raise IndexError("That person is not in the queue")
        for index in range(len(self.humans)):

            if self.humans[index].id == person.id:
                return index

    def swap(self, person1, person2):
        index1 = self.humans.index(person1)
        index2 = self.humans.index(person2)
        self.humans[index1] = person2
        self.humans[index2] = person1
        return self.humans

    def get_next(self):
        if len(self.humans) > 0:
            next_in_queue = self.humans[0]
            self.humans.remove(next_in_queue)
            return next_in_queue.id
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for h in self.humans:
            if h.blood_type == blood_type:
                self.humans.remove(h)
                return h
        else:
            if blood_type not in ["A", "B", "AB", "O"]:
                raise ValueError("Blood type doesn't exist")
            return None

    def sort_by_age(self):
        self.humans.sort(key=lambda x: (x.priority, x.age), reverse=True)
        return self.humans

    def rearrange_queue(self):
        for i in range(1, len(self.humans)):
            print(self.humans[i].name)
            if self.humans[i-1] in self.humans[i].family:
                self.swap(self.humans[i-1], self.humans[i])
        return self.humans





bob = Human(id_number=23, name="Bob", age=23, blood_type="AB", priority=True)
tom = Human(id_number=24, name="Tom", age=61, blood_type="O")
rex = Human(id_number=25, name="Rex", age=67, blood_type="A")
alice = Human(id_number=26, name="Alice", age=45, priority=True, blood_type="A")
victor = Human(id_number=27, name="Victor", age=63, blood_type="A")

victor.add_family_member(rex)
# victor.add_family_member(tom)
tom.add_family_member(rex)
victor.add_family_member(bob)



print(victor.family[0].name)
print(alice.family)


queue = Queue()
queue.add_person(bob)
queue.add_person(tom)
queue.add_person(alice)
queue.add_person(rex)
queue.add_person(victor)

for item in queue.humans:
    print(item.name)

# list_i = [1, 3, 5, 8]
# print(list_i.index(5))

# print(queue.find_in_queue(rex))
# queue.swap(tom, bob)

# print(queue.find_in_queue(tom))

# queue.get_next()
# print(queue.get_next())
for human in queue.humans:
    print(human.id, human.name)
# who = queue.get_next_blood_type("AB")
# print("Who:", who.name if who else "No one in queue")

print("After next in queue")

queue.sort_by_age()

for h in queue.humans:
    print(h.priority, h.age)

queue.rearrange_queue()

for h in queue.humans:
    print(h.name, h.age)

