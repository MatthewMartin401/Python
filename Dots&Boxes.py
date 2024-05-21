# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:04:04 2024

@author: user
"""
#  Creator: Me
#  Complete: False

import turtle, copy

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
        self.valid_options = self.get_valid_lines()  # Interactable lines - 2 values. One for each dot. 2 dots stored in 2 lists.
        self.boxes = self.get_all_boxes()  # Boxes - 4 values. One for each dot.
        self.User_scores = {
            False: [],
            True: []
        }
    
    def correct_points(self): # Puts points in Ascending order.
        #  Sorts point A and point B order, so that it can be found in the array
        # print("Here", self.point_B[0])
        if (self.point_A[0] > self.point_B[0]) or (self.point_A[1] > self.point_B[1]):
            self.point_A, self.point_B = self.point_B, self.point_A

    
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
    
    def fill_box(self, location):
        self.t.up()
        self.t.goto(location[0][0])  # Start location
        self.t.begin_fill()
        for line in location:
            for dot in line:
                # print("location: ", dot)
                self.t.goto(dot)
        self.t.goto
        self.t.fillcolor(self.colors[self.turn])
        self.t.end_fill()
    
    def get_all_boxes(self):
        boxes = list()
        print(self.grid)

        for i in range(0, self.COLN * self.ROWN - 10, 1):
            if (i + 1) % 10 != 0:
                print(f"{i} / {len(self.grid)-11}")
                boxes.append([
                    [self.grid[i], self.grid[i + (self.ROWN)]], # Bottom
                    [self.grid[i + (self.ROWN)], self.grid[i + (self.ROWN + 1)]],  # Right
                    [self.grid[i + 1], self.grid[i + (self.ROWN + 1)]],  # Top
                    [self.grid[i], self.grid[i + 1]]  # Left
                    ])
        
        return boxes

    def get_dot_index(self, x, y):
        # print(x, y)
        x = round(x//100)  # Might be replaced with self.GAP
        y = round(y//100)  # Might be replaced with self.GAP
        # print(x, y)
        index = int(f"{x}{y}")
        print(index)
        return index
        # t.goto(min(grid, lambda a: abs(a - (x, y))))

    def create_dots(self):
        #  Creates dots.
        for index, l in enumerate(self.grid):
            self.t.up()
            self.t.goto(l[0], l[1])
            self.t.dot()
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
        if index <= len(self.grid) and index >= 0:
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

    def draw_line(self, x, y):
        # x, y = event.x, event.y
        self.set_Point(x, y)
        self.t.color
        
        if self.point_A != None and self.point_B != None:  #  Both locations must be set.
            self.correct_points()  # Puts points in Ascending order.
            if [self.point_A, self.point_B] in self.valid_options:  # Must be a valid location. Draw lines.
                # print(True)
                t.up()
                t.goto(self.point_A)
                t.down()
                t.goto(self.point_B)
                t.up()

                # print(self.boxes)
                # print([self.point_A, self.point_B])
                # print(True in list([self.point_A, self.point_B] in x for x in self.boxes))  # There is a box containing the line.
                # print(list([self.point_A, self.point_B] in x for x in self.boxes))

                
                self.valid_options.remove([self.point_A, self.point_B])
                for x in self.boxes:  # Repeats per box that uses the selected line, meaning that more than one box can be filled in at once.
                    if [self.point_A, self.point_B] in x:  # Box contains the line.
                        # c = [a for a in x]
                        # print(c)
                        # print("check", [a not in self.valid_options for a in x])
                        if all([a not in self.valid_options for a in x]):
                            print("hi")
                            self.fill_box(x)
                            self.User_scores[self.turn].append(x)
                    
                    print(self.colors[self.turn], len(self.User_scores[self.turn]))

                self.new_turn()
                # print("Done")
                # for x in self.boxes:  # List of all lines within the box.
                    # print([self.point_A, self.point_B] in x)
                    # print("-", True in ([self.point_A, self.point_B] in x))
                    #  Checks if new lines are apart of a box, and whether all values have been removed from valid lines.

                    # apart_of_box = list([self.point_A, self.point_B] in i for i in x)
                    # if all(apart_of_box) and True in apart_of_box:  # Line apart of box?
                        # print("HERE - 1: ", all([val not in self.valid_options] for val in x))
                        
                        # print("hi")
                        # print(self.valid_options)
                        # for val in x:
                                # print(val in self.valid_options)  # Returns false, as values are stored in different structures.

                        # if all(list([val not in self.valid_options] for val in x)):
                        #     print("BOXES: ", x)
                        #     print("ALL LINES IN BOX: ", list([val not in self.valid_options] for val in x))
                        #     print("found")
                
            else:
                print([self.point_A, self.point_B])
                print(self.valid_options)


#  Check whether dots are near

    


#  Who filled in the last line.

#  Adds box to user score.

t = turtle.Turtle()
# background = turtle.Screen()
# background = t.screen.getcanvas()
turtle.tracer(0, 0)

game = Dots_and_Boxes(t)
game.create_grid()
game.create_dots()
turtle.tracer(2, 4)
# for v in game.boxes:
#     game.fill_box(v)
# game.fill_box(v)
# print(v)

# box = game.get_all_boxes()
# turtle.tracer(1, 2)
# for l in box:
#     t.up()
#     t.end_fill()
#     print(l)
#     t.goto(l[0])
#     for v in l:
#         t.begin_fill()
#         t.goto(v)
#     t.goto(l[0])
#     t.goto(l[1])
#     t.fillcolor(game.colors[game.turn])

game.t.screen.onclick(game.draw_line)
turtle.listen()
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
# t.screen.onkeyrelease(draw_line, "1")
# t.ondrag(draw_line)

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
