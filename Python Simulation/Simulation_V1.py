import random 
for i in range(10):
    CenterDistance = random.randint(20,31)
    if CenterDistance > 25:
        print(CenterDistance)
        print('Accelerating Straight')
    elif CenterDistance <= 25 :
        print(CenterDistance)
        for x in range(1):
            LeftDistance = random.randint(1,100)
            RightDistance = random.randint(1,100)
            if LeftDistance > RightDistance:
                print('Turning Left, ' + 'Left: ' + '(' + str(LeftDistance) + ') ' + 'Right: ' + '(' + str(RightDistance) + ')')
            elif RightDistance > LeftDistance :
                print('Turning Right, ' + 'Left: ' + '(' + str(LeftDistance) + ') ' + 'Right: ' + '(' + str(RightDistance) + ')')
            else:
                print('Turning Left(Default), ' + 'Left: ' + '(' + str(LeftDistance) + ') ' + 'Right: ' + '(' + str(RightDistance) + ')')
                 

   
        

