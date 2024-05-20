# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:04:04 2024

@author: user
"""
#  Creator: Me
#  Complete: False

import turtle, copy

t = turtle.Turtle()
# background = turtle.Screen()
# background = t.screen.getcanvas()
cavset = t.screen.getcanvas()
turtle.tracer(0, 0)
print(t.screen.screensize())
t.screen.setworldcoordinates(urx=1000,ury=1000, llx=0, lly=0)

COLN, ROWN = 10, 10
point_A = None
point_B = None
turn = None

def create_grid(COLN, ROWN, gap):
    grid = list()
    for c in range(COLN):
        for r in range(ROWN):
            grid.append([c * gap, r * gap])
    return grid

def get_valid_lines(grid):
    lines = list()
    for x, y in grid:
        for x1, y1 in grid:
            if abs(x - x1) == 100 and y == y1 and x1 > x:
                if [(x, y), (x1, y1)] not in lines :
                    lines.append([(x, y), (x1, y1)])
            elif abs(y - y1) == 100 and x == x1 and y1 > y:
                if [(x, y), (x1, y1)] not in lines:
                    lines.append([(x, y), (x1, y1)])
    return lines

def f(x, y):
    global col
    print(round(x), round(y))

    t.down()
    t.goto(x, y)
    t.up()

def get_dot_index(x, y):
    global grid
    # print(x, y)
    x = round(x//100)
    y = round(y//100)
    # print(x, y)
    index = int(f"{x}{y}")
    # print(index)
    return index
    # t.goto(min(grid, lambda a: abs(a - (x, y))))

def create_dots(turtle):
    for index, l in enumerate(grid):
        turtle.up()
        turtle.goto(l[0], l[1])
        turtle.dot()
        print(index)
        turtle.write(index)
        # if (index + 1) % 10 == 0 and index != 0:
        #     t.write(int((index + 1) / 10))

def draw_all_Lines(turtle):
    #  SHOWS LINE GENERATION
    turtle.color("red")
    turtle.screen.tracer(1, 2)
    turtle.screen.tracer(1, 0)
    turtle.speed(1)
    for i in lines:
        turtle.up()
        turtle.goto(i[0])
        turtle.down()
        turtle.goto(i[1])
        print(i)

def release_input(event):
    # print(event)
    # print(event.state)
    # Mouse left-key.
    if event.num == 1:
        # print(event)
        return [event.x, event.y]
    
def set_Point(x, y):
    global grid, lines, point_A, point_B

    # print(x, y)
    index = get_dot_index(x, y)
    if index <= len(grid):
        print(f"{index} found in grid.")

        if point_B != None and point_A != None:
            point_A, point_B = None, None
        if point_A == None:
            point_A = grid[index]
            print(f"set_pointA: {point_A}")
        elif point_B == None:
            point_B = grid[index]
            print(f"set_pointB: {point_B}")
    # print("HERE:", point_A, point_B)
    
# def set_PointA(x, y):
#     global grid, lines, point_A

#     # print(x, y)
#     index = get_dot_index(x, y)
#     if index <= len(grid):
#         print(f"{index} found in grid.")
    
#     point_A = grid[index]
#     print(f"set_pointA: {point_A}")

# def set_PointB(x, y):
#     global grid, lines, point_B

#     t.ondrag(0)
#     t.goto(x, y)
    
#     print(x, y)
#     index = get_dot_index(x, y)
#     print(index)

#     t.ondrag(set_PointB)
#     # if index <= len(grid):
#     #     print(f"{index} found in grid.")

#     # point_B = grid[index]
#     # print(f"set_pointA: {point_B}")
#     # draw_line()
def correct_points():
    global point_A, point_B
    #  Sorts point A and point B order, so that it can be found in the array
    if point_A[0] > point_B[0] or point_A[1] > point_B[1]:
        point_A, point_B = point_B, point_A

def draw_line(x, y, valid_options):
    # x, y = event.x, event.y
    set_Point(x, y)
    correct_points()
    if [point_A, point_B] in valid_options:
        print(True)
    if point_A != None and point_B != None:
        t.up()
        t.goto(point_A)
        t.down()
        t.goto(point_B)
        t.up()
        print("Done")


#  Check whether dots are near

    


#  Who filled in the last line.

#  Adds box to user score.
User_scores = {
    False: [],
    True: []
}

grid = create_grid(COLN, ROWN, 100)
lines = get_valid_lines(grid)
valid_lines = copy.deepcopy(lines)


create_dots(t)
print(grid)
t.screen.onclick(draw_line)





    # Works, but causes an issue with x and y coords.
    # Couldnt get ondrag to work or onrelease to give the correct coordinates.
# t.screen.getcanvas().bind("<ButtonRelease>", draw_line)
# cavset.bind("<Button-1>", f)
# t.screen.onclick(drawLines)  # Works
# t.screen.onclick(set_Point)  # Works
t.screen.onkeyrelease(draw_line, "1")
# t.ondrag(draw_line)


turtle.listen()
t.screen.mainloop()  
# background.onkeyrelease(f)
# background.onkeyrelease(f, key=1)

# cavset.bind("<Button-1>", f)


# t.onrelease(get_dot_index, 1)  # Doesnt work
# t.ondrag(t.goto, 1)  # Doesnt work

# t.ondrag(f)



#  Drawing lines:
# for x in range(len(col)):
#     gap = 100 * x
#     for y in [300]:
#         t.up()
#         t.goto(gap, 0)
#         t.down()
#         t.goto(gap, y)


# t.speed(5)
# t.up()
# t.goto(0, 0)
# t.down()
# t.goto(-500, 500)
