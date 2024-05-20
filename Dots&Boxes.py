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
turtle.tracer(0, 0)

class Dots_and_Boxes:
    def __init__(self, t):
        self.t = t
        t.screen.setworldcoordinates(urx=1000,ury=1000, llx=0, lly=0)
        self.COLN, self.ROWN = 10, 10
        self.GAP = 100
        self.point_A = None
        self.point_B = None
        self.turn = True
        self.colors = {True: "red",
                       False: "blue"}

        self.grid = self.create_grid()
        self.valid_options = self.get_valid_lines()
        self.User_scores = {
            False: [],
            True: []
        }

    def new_turn(self):  # Occurs at the end of turn.
        self.turn = not self.turn  # New turn
        self.current_color = self.colors[self.turn]  # Information reflects new turn
        t.color(self.current_color)  # Sets new color.

    def create_grid(self):
        grid = list()
        for c in range(self.COLN):
            for r in range(self.ROWN):
                grid.append([c * self.GAP, r * self.GAP])
        return grid
        # return grid

    def get_valid_lines(self):
        lines = list()
        for x, y in self.grid:
            for x1, y1 in self.grid:
                if abs(x - x1) == 100 and y == y1 and x1 > x:
                    if [(x, y), (x1, y1)] not in lines :
                        lines.append([[x, y], [x1, y1]])
                elif abs(y - y1) == 100 and x == x1 and y1 > y:
                    if [(x, y), (x1, y1)] not in lines:
                        lines.append([[x, y], [x1, y1]])
        return lines

    def f(x, y):
        global col
        print(round(x), round(y))

        t.down()
        t.goto(x, y)
        t.up()

    def get_dot_index(self, x, y):
        # print(x, y)
        x = round(x//100)
        y = round(y//100)
        # print(x, y)
        index = int(f"{x}{y}")
        # print(index)
        return index
        # t.goto(min(grid, lambda a: abs(a - (x, y))))

    def create_dots(self):
        #  Creates dots.
        for index, l in enumerate(self.grid):
            self.t.up()
            self.t.goto(l[0], l[1])
            self.t.dot()
            print(index)
            self.t.write(index)

        #  Changes from black to user turn colors.
        t.color(self.colors[self.turn])
            # if (index + 1) % 10 == 0 and index != 0:
            #     t.write(int((index + 1) / 10))

    def draw_all_Lines(self):
        #  SHOWS LINE GENERATION
        lines = self.get_valid_lines()
        self.t.color("red")
        self.t.screen.tracer(1, 2)
        self.t.screen.tracer(1, 0)
        self.t.speed(1)
        for i in lines:
            self.t.up()
            self.t.goto(i[0])
            self.t.down()
            self.t.goto(i[1])
            print(i)

    def release_input(event):
        # print(event)
        # print(event.state)
        # Mouse left-key.
        if event.num == 1:
            # print(event)
            return [event.x, event.y]
        
    def set_Point(self, x, y):
        # print(x, y)
        index = self.get_dot_index(x, y)  # Gets the index.
        if index <= len(self.grid):
            print(f"{index} found in grid.")

            # Sets the location. Alternate method: Use just the index, instead of the value.
            if self.point_B != None and self.point_A != None:
                self.point_A, self.point_B = None, None
            if self.point_A == None:
                self.point_A = self.grid[index]
                # print(f"set_pointA: {self.point_A}")
            elif self.point_B == None:
                self.point_B = self.grid[index]
                # print(f"set_pointB: {self.point_B}")
        # print("HERE:", point_A, point_B)
        
    def correct_points(self):
        #  Sorts point A and point B order, so that it can be found in the array
        # print("Here", self.point_B[0])
        if (self.point_A[0] > self.point_B[0]) or (self.point_A[1] > self.point_B[1]):
            self.point_A, self.point_B = self.point_B, self.point_A

    def draw_line(self, x, y):
        # x, y = event.x, event.y
        self.set_Point(x, y)
        self.t.color
        
        if self.point_A != None and self.point_B != None:  #  Both locations must be set.
            self.correct_points()
            if [self.point_A, self.point_B] in self.valid_options:  # Must be a valid location.
                self.valid_options.remove([self.point_A, self.point_B])
                print(True)
                t.up()
                t.goto(self.point_A)
                t.down()
                t.goto(self.point_B)
                t.up()
                self.new_turn()
                # print("Done")
            else:
                print([self.point_A, self.point_B])
                print(self.valid_options)


#  Check whether dots are near

    


#  Who filled in the last line.

#  Adds box to user score.

game = Dots_and_Boxes(t)
game.create_grid()
game.create_dots()

game.t.screen.onclick(game.draw_line)

t.screen.mainloop()

# lines = game.get_valid_lines(grid)
# valid_lines = copy.deepcopy(lines)
# game.create_dots(t)
# print(grid)
# t.screen.onclick(game.draw_line)





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
