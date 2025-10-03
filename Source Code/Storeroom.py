import turtle as tr
import math
import tkinter as tk
from PIL import Image, ImageGrab
import os


class AStar:
    number_of_tries = 0

    def __init__(self):
        self.x = None
        self.y = None
        AStar.number_of_tries += 1
        self.Try = str(AStar.number_of_tries)
        self.t_mane = 0
        self.out = None
        self.mavane = None
        self.end = None
        self.start = None
        self.base = 50
        self.other_coordinates = None
        self.hScore = None
        self.get_inf()

        self.root = tk.Tk()
        canvas = tk.Canvas(self.root, width=500, height=500)
        canvas.pack()
        self.screen = tr.RawTurtle(canvas)

    def get_inf(self):  # get information with manual errors
        self.other_coordinates = list()
        message = "طول و عرض انبار را به متر و با فاصله وارد کنيد"
        while True:
            try:
                x, y = map(int, tr.textinput("طول و عرض انبار", message).split())
                if (x <= 0) or (x > 250) or (y <= 0) or (y > 250): raise OverflowError
                self.x, self.y = x, y
                break

            except OverflowError:
                message = "!لطفا اعداد مجاز برای طول و عرض انبار وارد کنید\n.توجه کنید که طول و عرض انبار، عددی مثبت و " \
                          "کوچکتر مساوی 250 است\nطول و عرض انبار را به متر و با فاصله وارد کنيد "
                continue

            except:
                message = "!مشکلی در ذخیره اطلاعات پیش آمد! لطفا اطلاعات را دوباره و با فرمت درست وارد کنید\nطول و " \
                          "عرض انبار را به متر و با فاصله وارد کنيد "
                continue

        self.base = min(min(50, 500 // self.x), min(50, 500 // self.y))

        message = "مختصات نقطه شروع را با فاصله وارد کنيد"
        self.start = AStar.get_handled_coordinate("نقطه شروع", message, self.x, self.y)
        self.other_coordinates.append(self.start)

        message = "مختصات نقطه پایان را با فاصله وارد کنيد"
        self.end = AStar.get_handled_coordinate("نقطه پایان", message, self.x, self.y, self.other_coordinates)
        self.other_coordinates.append(self.end)

        message = "تعداد موانع را وارد کنيد\nتوجه کنید که ابعاد هر مانع، یک متر در یک متر است"
        while True:
            try:
                mane = int(tr.numinput("تعداد موانع", message))
                if mane > self.x * self.y: raise OverflowError
                self.t_mane = mane
                break

            except:
                message = "!لطفا تعداد موانعی که در انبار وجود دارند را وارد کنید\nتعداد موانع را وارد کنيد\nتوجه " \
                          "کنید که ابعاد هر مانع، یک متر در یک متر است "
                continue

        self.mavane = list()

        for i in range(1, self.t_mane + 1):
            message = f"مختصات مانع {i} را وارد کنید"
            self.mavane.append(
                AStar.get_handled_coordinate(
                    "مختصات مانع", message, self.x, self.y, self.other_coordinates
                )
            )
            self.other_coordinates.append(self.mavane[-1])

    def make_path(self):
        print("Find path...")
        self.hScore = []
        for i in range(1, self.y + 1):
            self.hScore.append([])
            for j in range(1, self.x + 1):
                self.hScore[-1].append(AStar.make_hScore(j, i, self.end[0], self.end[1]))
        self.out = self.a_star()

    def print_path(self):
        path = self.out
        self.print_anbar()

        if len(path) == 0:
            print("No path defind!!!")
            self.screen.pencolor("red")
            self.screen.write("راهي وجود ندارد", font=("B Nazanin", 30, "bold"))

        else:
            print("You can see the path in turtle")

            self.screen.pencolor("green")

            x2 = path[0][0]
            y2 = path[0][1]
            self.screen.pendown()
            self.screen.pensize(4 * self.base // 50)

            self.screen.speed(6)
            for i in path[1:]:  # Check the next vertices
                changeY = i[1] - y2
                y2 += changeY
                changeX = i[0] - x2
                x2 += changeX
                # x2 and y2 are Coordinates of the vertex

                if (changeY != 0) and (changeX != 0):  # We should move diagonal
                    go = math.sqrt(2) * self.base
                    if (changeY > 0) and (changeX > 0):  # Up Right
                        self.screen.rt(45)
                        self.screen.fd(go)
                        self.screen.lt(45)

                    elif (changeY > 0) and (changeX < 0):  # Up Left
                        self.screen.lt(45)
                        self.screen.fd(go)
                        self.screen.rt(45)

                    elif (changeY < 0) and (changeX > 0):  # Down Right
                        self.screen.rt(135)
                        self.screen.fd(go)
                        self.screen.lt(135)

                    else:  # Down Left
                        self.screen.lt(135)
                        self.screen.fd(go)
                        self.screen.rt(135)

                else:  # We should move horizontal or vertical
                    self.screen.fd(self.base * changeY)
                    self.screen.rt(90)
                    self.screen.fd(self.base * changeX)
                    self.screen.lt(90)

        self.screen.ht()
        x0 = self.root.winfo_rootx()
        y0 = self.root.winfo_rooty()
        x1 = x0 + self.root.winfo_width()
        y1 = y0 + self.root.winfo_height()
        path = os.getcwd() + "\\Storeroom manager software results"
        path += "\\Storeroom\\"
        file_name = "try" + self.Try + ".png"
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(path + file_name)  # save the result

    @staticmethod
    def check_coordinate(x, y, storeroom_x, storeroom_y):
        if (x > storeroom_x) or (x <= 0) or (y > storeroom_y) or (y <= 0):
            raise OverflowError

    @staticmethod
    def get_handled_coordinate(title, message, storeroom_x, storeroom_y, others=None):  # get and handle a coordinate
        if others is None:
            others = list()

        new_message = message  # others list is for other coordinates
        while True:
            try:
                x, y = map(int, tr.textinput(title, new_message).split())
                if (x, y) in others: raise LookupError
                AStar.check_coordinate(x, y, storeroom_x, storeroom_y)
                return x, y

            except OverflowError:
                new_message = "!لطفا مختصات موجود در انبار را وارد کنید\n" + message
                continue

            except LookupError:
                new_message = "!این مختصات قبلا برای کار دیگری استفاده شده است\n" + message
                continue

            except:
                new_message = "!مشکلی در ذخیره اطلاعات پیش آمد! لطفا اطلاعات را دوباره و با فرمت درست وارد کنید\n" + message
                continue

    def fill(self, base):  # Fill the obstacles in the storeroom
        self.screen.begin_fill()
        for i in range(4):
            self.screen.lt(90)
            self.screen.fd(base)
        self.screen.end_fill()

    def print_anbar(self):
        self.screen.speed(0)
        x = self.x * self.base
        y = self.y * self.base

        self.screen.penup()
        self.screen.bk(x / 2)
        self.screen.lt(90)
        self.screen.bk(y / 2)

        self.screen.pendown()
        for i in range(2):
            self.screen.fd(y)
            self.screen.rt(90)
            self.screen.fd(x)
            self.screen.rt(90)  # Draw the base of the storeroom

        for i in range(y // self.base // 2):
            self.screen.fd(self.base)
            self.screen.rt(90)
            self.screen.fd(x)
            self.screen.lt(90)
            self.screen.fd(self.base)
            self.screen.lt(90)
            self.screen.fd(x)
            self.screen.rt(90)  # Draw horizontal lines

        if y // self.base % 2 == 1:
            self.screen.fd(self.base)

        self.screen.rt(90)

        for i in range(x // self.base // 2):
            self.screen.fd(self.base)
            self.screen.rt(90)
            self.screen.fd(y)
            self.screen.lt(90)
            self.screen.fd(self.base)
            self.screen.lt(90)
            self.screen.fd(y)
            self.screen.rt(90)  # Draw vertical lines

        if x // self.base % 2 == 1:
            self.screen.fd(self.base)

        self.screen.penup()

        self.screen.bk(x)
        self.screen.lt(90)
        self.screen.bk(y)

        x2 = 0
        y2 = 0
        self.screen.fillcolor("gray")  # Draw obstacles in gray
        for i in self.mavane:
            self.screen.fd(self.base * (i[1] - y2))
            y2 += i[1] - y2
            self.screen.rt(90)
            self.screen.fd(self.base * (i[0] - x2))
            x2 += i[0] - x2
            self.screen.lt(90)
            self.fill(self.base)

        self.screen.fd(self.base * ((self.y // self.base) - y2))
        self.screen.rt(90)
        self.screen.fd(self.base * ((self.x // self.base) - x2))

        self.screen.bk(((self.x // self.base) - self.start[0]) * self.base + self.base / 2)
        self.screen.lt(90)
        self.screen.bk(
            ((self.y // self.base) - self.start[1]) * self.base + self.base / 2)  # Go to the start coordinate

    @staticmethod
    def make_hScore(startx, starty, endx, endy):  # Calculate with "Diagonal Distance"
        return max(abs(startx - endx), abs(starty - endy))  # It's hioristic

    @staticmethod
    def reconstruct_path(cameFrom, current):
        total_path = [(current[1], current[2])]

        '''cameFrom = {
                goal : neighbor1,
                neighbor1 : neighbor2,
                neighbor3 : neighbor4,
                neighbor2 : start
                }'''

        keys = cameFrom.keys()
        while True:
            if current not in keys: break
            current = cameFrom[current]
            total_path.append((current[1], current[2]))
        return total_path[::-1]

    def a_star(self):
        startx, starty = self.start[0], self.start[1]
        endx, endy = self.end[0], self.end[1]

        closeset = set()
        openset = set()
        openset.add((self.hScore[starty - 1][startx - 1], startx, starty))

        cameFrom = dict()

        gScore = []
        for i in range(self.y):
            gScore.append([])
            for j in range(self.x):
                if (i == starty - 1) and (j == startx - 1):
                    gScore[-1].append(0)
                else:
                    gScore[-1].append(float('inf'))

        fScore = []  # f() = g()+h()
        for i in range(self.y):
            fScore.append([])
            for j in range(self.x):
                if (i == starty - 1) and (j == startx - 1):
                    fScore[-1].append(self.hScore[starty - 1][startx - 1])
                else:
                    fScore[-1].append(float('inf'))

        while len(openset) != 0:
            current = min(openset)
            # current = (h, x, y) (And also each member in openset and closeset)

            if (current[1] == endx) and (current[2] == endy):
                return AStar.reconstruct_path(cameFrom, current)

            openset.remove(current)
            closeset.add(current)

            neighbors_current = [(current[1] - 1, current[2] + 1), (current[1], current[2] + 1),
                                 (current[1] + 1, current[2] + 1), (current[1] - 1, current[2]),
                                 (current[1] + 1, current[2]), (current[1] - 1, current[2] - 1),
                                 (current[1], current[2] - 1), (current[1] + 1, current[2] + 1)]
            # 0 0 0
            # 0 1 0
            # 0 0 0
            # 1 --> current    0 --> neighbor
            # neighbor = (x, y)

            for neighbor in neighbors_current:
                if (neighbor[0] > self.x) or (neighbor[1] > self.y) or (neighbor[0] < 1) or (neighbor[1] < 1): continue
                if neighbor in self.mavane: continue
                if (self.hScore[neighbor[1] - 1][neighbor[0] - 1], neighbor[0], neighbor[1]) in closeset: continue

                tentative_gScore = gScore[current[2] - 1][current[1] - 1] + 1
                # This "1" is distance between neighbor from currnet

                if not ((self.hScore[neighbor[1] - 1][neighbor[0] - 1], neighbor[0], neighbor[1]) in openset):
                    openset.add((self.hScore[neighbor[1] - 1][neighbor[0] - 1], neighbor[0], neighbor[1]))

                elif tentative_gScore >= gScore[neighbor[1] - 1][neighbor[0] - 1]:
                    continue

                cameFrom[(self.hScore[neighbor[1] - 1][neighbor[0] - 1], neighbor[0], neighbor[1])] = current
                gScore[neighbor[1] - 1][neighbor[0] - 1] = tentative_gScore
                fScore[neighbor[1] - 1][neighbor[0] - 1] = gScore[neighbor[1] - 1][neighbor[0] - 1] + \
                                                           self.hScore[neighbor[1] - 1][neighbor[0] - 1]
        return ()

    @staticmethod
    def show_storeroom(astar_obj):
        path = "Storeroom manager software results\\Storeroom"
        file_name = "try" + astar_obj.Try + ".png"
        path += "\\" + file_name

        img = Image.open(path)
        img.show()
        del img
