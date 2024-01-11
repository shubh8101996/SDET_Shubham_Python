class Car:
    def __init__(self, n="unknown", m="unknown", y=0):
        self.name = n
        self.model = m
        self.year = y

    def display(self):
        print(self.name)
        print(self.model)
        print(self.year)


# if __name__ == "__main__":     act as main method in python
#     pass

if __name__ == "__main__":
    obj = Car("maruti suzuki", "brezza")
    obj1 = Car("maruti suzuki", "brezza", 1090)

    obj.display()
    obj1.display()
