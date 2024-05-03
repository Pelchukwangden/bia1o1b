class Cat:
    def __init__(self, name, species, age, home_location, behavior):
        self.name = name
        self.species = species
        self.age = age
        self.home_location = home_location
    
    # def eat(self):
    #     print("i am eating")
    
    # def sleep(self):
    #     print("i am sleeping")

    # def hunt(self):
    #     print('i amgoing for hunting')

    # def introduce(self):
    #     print("hi")
    #     print("my nname is " + self.name)
    #     print("my species is " + self.species)
    #     print("i am", self.age, "years old")
    def can_vote(self):
        return self.age >= 18

tiger = Cat("Tiger", "wild", 31, "Jungle", ["hunt"])
tiger1 = Cat("Tiger1", "wild", 19, "Forest", ["hunt"])
home_pet = Cat("HomePet", "domestic", 2, "House", ["eat", "sleep"])
home_pet1 = Cat("HomePet1", "domestic", 4, "Apartment", ["eat", "sleep", "introduce"])

cats = [tiger, tiger1, home_pet, home_pet1]

for cat in cats:
    print(cat.name, "can vote:", cat.can_vote())

