import random

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print("This is", self.name)

class Employee(Human):
  def __init__(self, name, age, position, salary):
    self.__id = random.randrange(1, 100)
    self.__something = random.randrange(1, 100)

    self.position = position
    self.salary = salary
    # Human.__init__(self, name, age)
    super().__init__(name, age)

  def get_id(self):
    # logic auth
    return self.__id

  def set_id(self, id):
    # logic auth
    self.__id = id

class Manager(Employee):
  def __init__(self, name, age, salary, department):
    self.department = department
    super().__init__(name, age, "manager", salary)


h1 = Human("taha", 20)
e1 = Employee("taha", 20, "instructor", 1500)

m1 = Manager("taha", 35, 2000, "tech")

# Making sure that the user is an admin

id = e1.get_id()

e1.set_id(1)

id = e1.get_id()

print(id)
