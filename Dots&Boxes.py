# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:04:04 2024

@author: user
"""
#  Coder: Me
#  Complete: True

import tkinter.messagebox
import turtle
from math import ceil

class Dots_and_Boxes:
    def __init__(self, t):
        self.t = t
        
        t.screen.title("Dots and Boxes.")
        t.screen.setworldcoordinates(urx=905,ury=1000, llx=0, lly=0)
        t.screen.setup(width = 1000, height = 850)
        self.COLN, self.ROWN = 10, 10
        self.GAP = 100
        self.point_A = None
        self.point_B = None
        self.turn = True
        self.colors = {True: "red",
                       False: "blue"}
        self.h = turtle.Turtle()

        self.grid = self.create_grid()
        self.valid_options = self.get_valid_lines()  # Interactable lines - 2 values. One for each dot. 2 dots stored in 2 lists.
        self.boxes = self.get_all_boxes()  # Boxes - 4 values. One for each dot.
        self.User_scores = {
            False: [],
            True: []
        }
        self.play = True

    def reset(self):
        self.t.clear()
        self.t.color("black")
        self.create_dots()
        self.valid_options = self.get_valid_lines() 
        self.User_scores = {
            False: [],
            True: []
        }

    def update_hud(self):
        self.h.clear()
        self.h.color("black")
        self.h.up()
        self.h.goto(0, 950)
        self.h.write(f"{str(self.colors[True]).title()}: {len(self.User_scores[True])} {str(self.colors[False]).title()}: {len(self.User_scores[False])}", font=("Ariel", 20, "normal"))
    
    def main(self):
        self.t.clear()
        self.update_hud()
        self.create_dots()
        turtle.tracer(2, 4)
        self.t.screen.onclick(game.draw_line)
        turtle.listen()
        self.t.screen.mainloop()

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
    
    def get_winner(self):
        return "Draw" if len(self.User_scores[True]) == len(self.User_scores[False]) else (str(self.colors[True]).title() if len(self.User_scores[True]) > len(self.User_scores[False]) else str(self.colors[False]).title())
    
    def fill_box(self, box):
        self.t.up()
        self.t.goto(box[0][0])  # Start location
        self.t.begin_fill()
        for line in box:
            for dot in line:
                # print("location: ", dot)
                self.t.goto(dot)
        print(box[0][0])
        self.t.goto(box[2][0])
        self.t.goto(box[2][1])
        self.t.fillcolor(self.colors[self.turn])
        self.t.end_fill()
    
    def get_all_boxes(self):
        boxes = list()
        print(self.grid)

        for i in range(0, (self.COLN * self.ROWN) - self.ROWN, 1):
            if (i + 1) % self.ROWN != 0:
                print(f"{i} / {len(self.grid)-11}")
                boxes.append([
                    [self.grid[i], self.grid[i + (self.ROWN)]], # Bottom
                    [self.grid[i + (self.ROWN)], self.grid[i + (self.ROWN + 1)]],  # Right
                    [self.grid[i + 1], self.grid[i + (self.ROWN + 1)]],  # Top
                    [self.grid[i], self.grid[i + 1]]  # Left
                    ])
        
        return boxes

    def get_dot_index(self, x, y):
        print(x, y)
        
        # Round x up condition
        print((int(x // self.GAP) * self.GAP) + (self.GAP / 2), (int(y // self.GAP) * self.GAP) + (self.GAP / 2))
        if x >= (int(x // self.GAP) * self.GAP) + (self.GAP / 2):
            x = (ceil(x / 100) * 100) // self.GAP
            print("ceil: ", x)
        else:#
            x = int(x // self.GAP)  # Rounds down.
        
        # Round y up condition
        if y >= (int(y // self.GAP) * self.GAP) + (self.GAP / 2):
            y = (ceil(y / 100) * 100) // self.GAP
            print("ceil: ", y)
        else:
            y = int(y // self.GAP)  # Rounds down.
        print((int(x // self.GAP) * self.GAP))
        
       
        
        # index = x + (y % 9)

        #  Works as long as its 10 x 10 dots.
        # index = int(f"{x}{y}")

        if (y + 1) <= self.ROWN:
            index = (self.ROWN * x)+ y  # Number of rows multiplied by grid index. Plus y (y is the height on the grid.)
            # print("coln * x: ", self.COLN * x, "y :", y)
            # print("INDEX: ", index)

            return index
        # t.goto(min(grid, lambda a: abs(a - (x, y))))

    def create_dots(self):
        #  Creates dots.
        for index, l in enumerate(self.grid):
            self.t.up()
            self.t.goto(l[0], l[1])
            self.t.dot()
            self.t.write(index)
        self.t.up()
        self.t.goto(-20, -20)
        self.t.down()
        for i in [[-20, -20], [((self.ROWN - 1)* self.GAP) + 20, -20], [((self.ROWN - 1) * self.GAP) + 20, ((self.COLN - 1) * self.GAP) + 20], [-20, ((self.COLN - 1) * self.GAP) + 20], [-20, -20]]:
            self.t.goto(i)    
        
        self.t.up()
        

        #  Changes from black to user turn colors.
        t.color(self.colors[self.turn])
            # if (index + 1) % 10 == 0 and index != 0:
            #     t.write(int((index + 1) / 10))

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
        if index != None:
            if index <= len(self.grid) and index >= 0:
                # print(f"{index} found in grid.")

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

    def draw_line(self, x, y):
        # x, y = event.x, event.y
        self.set_Point(x, y)
        score = len(self.User_scores[self.turn])
        
        if self.point_A != None and self.point_B != None:  #  Both locations must be set.
            self.correct_points()  # Puts points in Ascending order.
            if [self.point_A, self.point_B] in self.valid_options:  # Must be a valid location. Draw lines.
                # print(True)
                self.t.up()
                self.t.goto(self.point_A)
                self.t.down()
                self.t.goto(self.point_B)
                self.t.up()

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
                            self.fill_box(x)
                            self.User_scores[self.turn].append(x)
                    
                    # print(self.colors[self.turn], len(self.User_scores[self.turn]))

                #  Info
                print(len(self.valid_options))
                self.update_hud()
                if len(self.User_scores[self.turn]) == score:  # Only starts new turn, if user score didnt increase.
                    self.new_turn()
                    
                
        #  Checks if the game is over.
        if len(self.valid_options) == 0:
            self.play = tkinter.messagebox.askyesno(message = f"Winner: {self.get_winner()}. Would you like to play again?", title="Game Over")
            if self.play == True:
                self.reset()
            else:
                turtle.bye()

t = turtle.Turtle()
turtle.tracer(0, 0)

game = Dots_and_Boxes(t)
game.main()