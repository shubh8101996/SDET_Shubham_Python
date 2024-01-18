class Bird1:
    def chirp(self):
        print("Bird1 Chirp!")


class Bird2:
    def chirp(self):
        print("Bird2 Chirp!")


class Crow(Bird1, Bird2):
    def chirp(self):
        # Call the chirp method of Bird1
        Bird2.chirp(self)


if __name__ == "__main__":
    obj = Crow()
    obj.chirp()
    print(Crow.__mro__)

