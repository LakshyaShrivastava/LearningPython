from Parent import Parent


class Child(Parent):
    def __init__(self):
        print("This is the child class")

    def childFunc(self):
        print("This is the child function")

    def overridingMethodTest(self):
        print("Child")
