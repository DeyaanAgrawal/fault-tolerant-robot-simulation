import random

def left_right_distance():
    left = random.randint(1, 100)
    right = random.randint(1, 100)

    print("Left:", left, "Right:", right)

    if left > right:
        print("Turning LEFT")

    elif right > left:
        print("Turning RIGHT")

    else:
        print("Turning LEFT (default)")

def center_distance():
    center = random.randint(1, 100)

    print("Center:", center)

    if center > 25:
        print("Moving Forward")

    else:
        print("Obstacle Ahead → STOP")
        left_right_distance()

for i in range(10):
    center_distance()
    print("-----")