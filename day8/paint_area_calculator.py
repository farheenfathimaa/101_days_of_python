import math
def paint_calc(height,width,cover):
    area=height * width
    num_of_cans = math.ceil(area / cover) 
    return num_of_cans

h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5

print(f"the number of required cans is {paint_calc(height=h, width=w, cover=coverage)}")