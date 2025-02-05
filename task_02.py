import turtle
import math


def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)

    turtle.left(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    turtle.right(90)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    turtle.left(45)
    turtle.backward(branch_length)


def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()

    try:
        level = int(input("Enter the recursion level: "))
        if level < 0:
            raise ValueError("Recursion level cannot be negative")

    except ValueError as e:
        print(f"Error: {e}")
        exit()

    draw_pythagoras_tree(100, level)
    turtle.done()


if __name__ == "__main__":
    main()
