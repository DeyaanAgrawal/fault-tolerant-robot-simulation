import random
from turtle import right

def center_distance():
    distance = random.randint(1,100)
    print(distance)
    if distance <= 25:
        print('Turning')
    elif distance > 25:
        print('Moving Forward')
    elif distance == 25:
        print('Stopping')
center_distance()

def Left_Right_distance():
    left_distance = random.randint(1,100)
    right_distance = random.randint(1,100)
    print('Left: ', left_distance, 'Right: ', right_distance )
    if left_distance > right_distance:
        print('Moving Towards the Direction Left')
    elif left_distance < right_distance:
        print('Moving Towards the Direction Right')
Left_Right_distance()