# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Person import Person
from modifiablePerson import ModifiablePerson
from Child import Child


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    p = Person()
    print(p)

    print("Person name is " + p.getName())
    print("Person age is " + str(p.getAge()))

    m = ModifiablePerson("Lakshya", 18)

    print("Person name is " + m.getName())
    print("Person age is " + str(m.getAge()))


    c = Child()
    c.childFunc()
    # inheritence from parent class
    c.parentFunc()
    #Overridden method-> child method will run
    c.overridingMethodTest()

