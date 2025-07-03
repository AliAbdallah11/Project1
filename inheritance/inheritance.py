class Animal:
  def __init__(self, name):
    self.name = name
    self.__energy = 0

  def displayStats(self):
    print(f"{self.name} has {self.__energy} energy")

  def eat(self, amount):
    calculated = amount // 10
    self.__energy += calculated

  def set_energy(self, value):
    self.__energy = value

  def get_energy(self):
    return self.__energy


class Mammal(Animal):
  def __init__(self, name, is_pet):
    self.is_pet = is_pet
    super().__init__(name)

  def run(self, distance):
    calc = distance / 100
    e = self.get_energy()
    self.set_energy(e - calc)

  def eat(self, amount):
    calculated = amount // 8
    e = self.get_energy()
    self.set_energy(e + calculated)

    super().eat(amount)

class Bird(Animal):
  def __init__(self, name, can_fly):
    self.can_fly = can_fly
    super().__init__(name)

  def fly(self, distance):
    calc = distance/2
    e = self.get_energy()
    self.set_energy(e - calc)

class Fish(Animal):
  def __init__(self, name, school):
    self.school = school
    super().__init__(name)

  def swim(self, distance):
    calc = distance / 10
    e = self.get_energy()
    self.set_energy(e - calc)

lion = Mammal("Lion X", False)
parrot = Bird("Bird Y", True)
salmon = Fish("Fish Z", True)

def printAll():
  lion.displayStats()
  parrot.displayStats()
  salmon.displayStats()

def travel():
  lion.run(100)
  parrot.fly(100)
  salmon.swim(100)

def eat():
  lion.eat(500)
  parrot.eat(500)
  salmon.eat(500)


eat()
travel()
printAll()