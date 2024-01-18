class Arithmetic:
    def addition(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:
            result = a + b + c
            print(result)
        elif a != None and b != None:
            result = a + b
            print(result)
        else:
            result = a
            print(result)


obj = Arithmetic()
obj.addition(1)
