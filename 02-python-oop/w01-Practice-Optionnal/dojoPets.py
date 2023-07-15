class ninja :
    def __init__(self, first_name , last_name , treats , pet_food , pet) :
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet


    def walk (self):
        self.pet.play()

    def feed (self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

class pet :
    def __init__(self,name , type ,tricks , health = 100 , energy = 50) :
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep (self):
        self.energy += 25
        return (self)

    def eat(self):
        self.energy +=5
        self.health+= 10
        return(self)
    
    def play(self):
        self.health+=5

    def noise(self):
        print(f"it's the sound of an {self.type}")
    

pet = pet("Fluffy", "cat", "sit")

ninja = ninja("John", "Doe", "cookie", "fish", pet)

ninja.feed().walk().bath()