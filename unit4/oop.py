class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
    
    def introdcuce(self):
        print('hi')
        print("i am " + self.name)
        print("i am a" + self.breed + "dog")
        print("i am a" + str(self.age)+ ' years old')
        #fString
        print("i am a "+ self.color + " in colour")

    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def bark(self):
        print('Woof! Woof!')

    def sleep(self):
        print('Zzzz....')
        
    def eat(self):
        print("Nom nom nom!")
        
    def run(self, speed):
        print("i am", self.name)
        print("i am running at " + str(speed) + " miles per hour")

dog = Dog("pala","bhutanese", 20, 'black',)
petdog = Dog("sang",'pug', 10, 'white')
my_friend_dog = Dog("jack",'germna sheprad', 15, 'brown')

# print(dog.name)
# print(petdog.name)

dog.run(20)
petdog.run(100)

#     def introdcuce(self):
#         print('hi')
#         print("i am a" + self.breed + "dog")
#         print("i am a", str(sefl.age)+ ' years old')
#         #fString
#         print("i am a "+ self.clolr + " in colour")

# my_friend_dog.say_age()
# dog.eat()
# dog.sleep()
# petdog.bark()
# petdog.say_age()
# dog.introduce()
# petdog.introdcuce()
# # bild on to of the code provided 
# # create new behavoiour i the cass 
# # behaviour name: ; functrion)

# #ecpected output
# #dog.introducted()----> run this code. output show below :
# # # ia ma bhutanese dog
# # i am 20 years old
# # i ma black in color
# # 
  
      

# dog.introduce()
# petdog.introdcuce()

