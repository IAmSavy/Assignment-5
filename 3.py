Sides = [float(input('Enter the side lengths: ')), float(input()), float(input())]

if ((Sides[0] + Sides[1] > Sides[2]) and (Sides[1] + Sides[2] > Sides[0]) and (Sides[0] + Sides[2] > Sides[1])): print('The area of the triange is: ', ((((Sides[0] + Sides[1] + Sides[2])/2) * (((Sides[0] + Sides[1] + Sides[2])/2) - Sides[0]) * (((Sides[0] + Sides[1] + Sides[2])/2) - Sides[1]) * (((Sides[0] + Sides[1] + Sides[2])/2) - Sides[2])) ** 0.5))
else: print('The sides lengths are invalid.')