# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello World")

name = input ("Whats is your name?")
print ("Hello," + name + "!")

# artihmetic operators
print(10 % 3)
print( 10 * 3)
print (10 // 3)

#exercise
weight = int (input ("weight:"))
unit = input ("(k)g or (L)bs: ")
if unit.upper () == "k":
    converted = weight / 0.45
    print ("weight in lbs: " + str(converted))
else:
    converted = weight *0.45
    print( "weight in kgs: " + str(converted))
