import turtle
import math
import random

def draw_pythagoras_tree(length, level, angle, color, thickness):
    if level == 0:
        return

    turtle.pencolor(color)
    turtle.pensize(thickness)

    turtle.forward(length)

    turtle.left(angle)
    draw_pythagoras_tree(length * math.sqrt(2) / 2, level - 1, angle, color, thickness * 0.8)
    turtle.right(angle)

    turtle.right(angle)
    draw_pythagoras_tree(length * math.sqrt(2) / 2, level - 1, angle, color, thickness * 0.8)
    turtle.left(angle)

    turtle.backward(length)

def main():
    screen = turtle.Screen()
    turtle.speed('fastest')

    # Отримання параметрів від користувача
    level = int(screen.numinput("Введіть рівень рекурсії", "Рівень рекурсії (0-10):", default=5, minval=0, maxval=10))
    length = 200
    angle = int(screen.numinput("Введіть кут повороту", "Кут повороту (в градусах):", default=45, minval=1, maxval=89))
    thickness = int(screen.numinput("Введіть товщину лінії", "Товщина лінії:", default=3, minval=1))

    # Вибір випадкового кольору
    colors = ["red", "green", "blue", "purple", "orange", "yellow"]
    color = random.choice(colors)

    turtle.left(90)
    turtle.backward(200)
    turtle.down()

    draw_pythagoras_tree(length, level, angle, color, thickness)

    turtle.done()

if __name__ == "__main__":
    main()