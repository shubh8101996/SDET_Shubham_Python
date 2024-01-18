class Animal:

    def __int__(self, sound):
        self.n = sound
        pass

    def speak(self):
        print("bhaww bhaww")


class Human(Animal):

    def speak(self):
        print("talk talk")

    pass


if __name__ == "__main__":
    obj = Human()
    obj2 = Animal()
    obj.speak()
    obj2.speak()
