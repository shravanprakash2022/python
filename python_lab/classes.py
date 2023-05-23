

class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
       pass
       # print(p3 ** 2)

p = ClassOne(4, 3)
#print(type(p))


#print(p.p1)
p.square(6)

 
setattr(p, 'p2', 50)
#print("hahaha", getattr(p, 'p2'))
setattr

#########################

class Animal:
    __name =""
    __height= 0
    __weight= 0
    __sound= 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight= weight
        self.__sound= sound
   
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name    
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height
    def set_weight(self, weight):
        self.__weight = weight
    def get_weight(self):
        return self.__weight  
    def set_sound(self, sound):
        self.__sound = sound
    def get_sound(self):
        return self.__sound
    
    def get_type(self):
        return "Animal"
        
    def to_string(self):
        return "{} is {} mts tall and {} kg's  and sounds {}".format(
            self.__name, self.__height, self.__weight, self.__sound
        )

cat = Animal("pilli", 20, 30, "meow")
print(cat.get_type())
print(cat.to_string())

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        #super(Dog, self).__init__(name, height, weight, sound)
        super().__init__(name, height, weight, sound)
    def set_owner(self, owner):
        self.__owner = owner
    def get_owner(self):
        return self.__owner
    def get_type(self):
        return "Dog"
    def to_string(self):
        return "{} is {} mts tall and {} kg's and sounds {} and owner is {}".format(
            self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.get_owner()
        )
    
spot = Dog("Kukka", 20, 30, "meow", "idiot")
print(spot.get_type())
print(spot.to_string())