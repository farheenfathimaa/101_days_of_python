fruits = eval(input())

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")

    except IndexError:
        print("Fruit Pie")

make_pie(4)