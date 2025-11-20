class Animal:
    def speak(self):
        return self


class Dog(Animal):
    def speak(self):
        print("Woof Woof!")
        print("Aww Aww!")
        print("Arf Arf!")


class Cat(Animal):
    def speak(self):
        print("Meow Meow!")
        print("Ming Ming!")
        print("Puss Puss")


dog = Dog()
dog.speak() 

cat = Cat()
cat.speak()  
