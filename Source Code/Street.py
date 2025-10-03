import turtle as tr
from igraph import *
from PIL import Image
import sys

sys.setrecursionlimit(10 ** 6)


class DFS:
    number_of_tries = 0

    def __init__(self):
        self.goal = None
        self.weight = None
        self.path = None
        self.start = None
        self.edges = None
        self.number_of_edges = None
        self.graph = dict()
        # graph { ras mabda : {ras maghsad : vazn} }
        self.number_of_nodes = None
        self.get_inf()
        DFS.number_of_tries += 1
        self.Try = str(DFS.number_of_tries)

        edges_igraph = []
        for mabda in self.graph.keys():
            for maghsad in self.graph[mabda].keys():
                edges_igraph.append((mabda - 1, maghsad - 1))
        self.g = Graph(vertex_attrs={"label": list(self.graph.keys())}, edges=edges_igraph, directed=True)

    def get_inf(self):
        message = "تعداد راس های گراف را وارد کنید"
        while True:
            try:
                ras = int(tr.numinput("تعداد راس", message))
                if ras <= 0:
                    raise Exception()
                self.number_of_nodes = ras
                break

            except:
                message = "!مشکلی در ذخیره سازی اطلاعات پیش آمد\nلطفا دوباره وارد کنید\nتوجه کنید که تعداد راس ها، عددی " \
                          "صحیح و مثبت است\nتعداد راس های گراف را وارد کنید "
                continue

        for i in range(1, self.number_of_nodes + 1):
            self.graph[i] = dict()

        tr.textinput("اطلاعيه",
                     "(((: راس ها به صورت عدد ذخيره شده اند. براي ادامه، در باکس زير هرچه دل تنگتان مي گويد بنويسيد")

        message = "تعداد یال های گراف را وارد کنید"
        while True:
            try:
                yal = int(tr.numinput("تعداد یال", message))
                if yal <= 0:
                    raise Exception()
                if yal > self.number_of_nodes * (self.number_of_nodes - 1):
                    raise OverflowError()
                self.number_of_edges = yal
                break

            except OverflowError:
                message = "!این تعداد یال وجود ندارد\nتعداد یال های گراف را وارد کنید"
                continue

            except:
                message = "!مشکلی در ذخیره سازی اطلاعات پیش آمد\nلطفا دوباره وارد کنید\nتوجه کنید که تعداد یال ها، " \
                          "عددی " \
                          "صحیح و مثبت است\nتعداد یال های گراف را وارد کنید "
                continue

        self.edges = []
        for _ in range(self.number_of_edges):
            message = "مشخصات يال را با فاصله وارد کنيد\nتوجه کنيد که يال جهت دار و " \
                      "وزن دار " \
                      "است\nابتدا نقطه مبدا سپس نقطه مقصد و سپس وزن يال را وارد " \
                      "کنيد\n:مثال\n1 2 3\nيال از نقطه 1 به نقطه 2 با وزن 3"
            while True:
                try:
                    s, g, v = map(int, tr.textinput("مشخصات يال", message).split())  # start, goal, value
                    if [s, g] in self.edges:
                        raise LookupError()

                    if (s < 1) or (s > self.number_of_nodes) or (g < 1) or (g > self.number_of_nodes):
                        raise OverflowError()

                    self.edges.append([s, g])
                    self.graph[s][g] = v
                    break

                except OverflowError:
                    message = "!لطفا مقدار معتبر برای راس های شروع و پایان وارد کنید\n" \
                              "توجه کنید که راس ها به صورت اعداد صحیح ذخیره شده و از عدد 1 شروع می شوند\n" \
                              "مشخصات يال را با فاصله وارد کنيد\nتوجه کنيد که يال جهت دار و " \
                              "وزن دار " \
                              "است\nابتدا نقطه مبدا سپس نقطه مقصد و سپس وزن يال را وارد " \
                              "کنيد\n:مثال\n1 2 3\nيال از نقطه 1 به نقطه 2 با وزن 3"
                    continue

                except LookupError:
                    message = "این یال تکراری است! لطفا یک یال جدید وارد کنید\n" \
                              "مشخصات يال را با فاصله وارد کنيد\nتوجه کنيد که يال جهت دار و " \
                              "وزن دار " \
                              "است\nابتدا نقطه مبدا سپس نقطه مقصد و سپس وزن يال را وارد " \
                              "کنيد\n:مثال\n1 2 3\nيال از نقطه 1 به نقطه 2 با وزن 3"
                    continue

                except:
                    message = "مشکلی در ذخیره سازی اطلاعات پیش آمد! لطفا دوباره وارد کنید\n" \
                              "مشخصات يال را با فاصله وارد کنيد\nتوجه کنيد که يال جهت دار و " \
                              "وزن دار " \
                              "است\nابتدا نقطه مبدا سپس نقطه مقصد و سپس وزن يال را وارد " \
                              "کنيد\n:مثال\n1 2 3\nيال از نقطه 1 به نقطه 2 با وزن 3"
                    continue

        message = "شماره راس شروع را وارد کنيد"
        while True:
            try:
                s = int(tr.numinput("راس شروع", message))
                if (s < 1) or (s > self.number_of_nodes):
                    raise OverflowError()
                self.start = s
                break

            except OverflowError:
                message = "لطفا مقدار معتبر وارد کنید\n" \
                          "توجه کنید که شماره راس ها، اعدادی سحیح هستند و از 1 شروع می شوند\nشماره راس شروع را وارد " \
                          "کنید "
                continue

            except:
                message = "!مشکلی در ذخیره سازی اطلاعات به وجود آمد\nلطفا دوباره وارد کنید\n" \
                          "توجه کنید که شماره راس ها، اعدادی سحیح هستند و از 1 شروع می شوند\nشماره راس شروع را وارد " \
                          "کنید "
                continue

        message = "شماره راس هدف را وارد کنيد"
        while True:
            try:
                g = int(tr.numinput("راس هدف", message))
                if (g < 1) or (g > self.number_of_nodes):
                    raise OverflowError()
                self.goal = g
                break

            except OverflowError:
                message = "لطفا مقدار معتبر وارد کنید\n" \
                          "توجه کنید که شماره راس ها، اعدادی سحیح هستند و از 1 شروع می شوند\nشماره راس هدف را وارد کنید"
                continue

            except:
                message = "!مشکلی در ذخیره سازی اطلاعات به وجود آمد\nلطفا دوباره وارد کنید\n" \
                          "توجه کنید که شماره راس ها، اعدادی سحیح هستند و از 1 شروع می شوند\nشماره راس هدف را وارد کنید"
                continue

    def make_and_print_path(self):
        self.path = []  # The best path till now
        self.weight = float('inf')  # The weight of the best path

        self.plot_base_graph()
        print("Find path...")
        self.DFS([self.start], self.start)

        if len(self.path) == 0:
            print("No path defind!!!")
            layout = self.g.layout("tree")
            self.g.vs["color"] = "white"
            self.g.vs.select(self.start - 1)["color"] = "#5df449"
            self.g.vs.select(self.goal - 1)["color"] = "red"

            self.g.vs.select(self.start - 1)["shape"] = "triangle-up"
            self.g.vs.select(self.goal - 1)["shape"] = "triangle-down"

            plot(self.g, "file.png", layout=layout)

            img = Image.open("file.png")
            path = os.getcwd() + "\\Storeroom manager software results\\Street\\"  # The address of the file
            file_name = "answer_graph.png"

            folder_name = "Try" + self.Try
            path += folder_name

            img.save(path + "\\" + file_name)
            img.show()
            os.remove("file.png")

        else:
            self.print_graph()
            print("This is a symbolic way and the length of the edges is not real.")
            print(
                "But you can see the answer graph(again without the real length of the edges!) near the source code "
                "in folder \"Storeroom manager software result\" and \"Street\" as\"answer_graph\"")
            tr.textinput("گراف جواب",
                         ".مشاهده مي کنيد، يک گراف نمادين است و طول يال ها واقعي نيست. همچنين فقط نقاطي که در مسير "
                         "هستند نمايش داده شده اندturtle گرافي که در محيط\n.اما شما مي توانيد بعد از وارد کردن هر چه "
                         "دل تنگتان مي گويد در باکس زير، گراف کامل جواب را مشاهده کنيد\n.ذخيره شده است answer_graph و "
                         "با نام Storeroom manager software result در Street اين گراف در کنار فايل منبع برنامه در "
                         "پوشه\n!توجه کنيد که در گراف کامل جواب هم "
                         "طول يال ها واقعي نيست")
            self.plot_answer_graph()

    def plot_base_graph(self):  # Draw a general shape of graph
        layout = self.g.layout("tree")
        plot(self.g, "file.png", layout=layout)  # Save a temporary PNG file

        img = Image.open("file.png")
        path = os.getcwd() + "\\Storeroom manager software results\\Street\\"  # The address of the file
        file_name = "base_graph.png"

        folder_name = "Try" + self.Try
        path += folder_name
        os.mkdir(path)

        img.save(path + "\\" + file_name)
        img.show()
        os.remove("file.png")
        print(
            "Graph which you see as a picture, has been saved near the source code in folder \"Storeroom manager "
            "software results\" and \"Street\" as "
            "\"base_graph\".")
        print("It is a general shape of the graph")
        tr.textinput("!ذخيره تصوير",
                     "عکسی که مشاهده می کنید، در پوشه \nStoreroom manager software results در Street"
                     "\nbase_graph و با نام\n"
                     ".ذخیره شده است"
                     "\n((:براي ادامه و ديدن مسير تشخيص داده شده، در باکس زير، هرچه دل تنگتان مي گويد وارد کنيد")

    def plot_answer_graph(self):  # Draw the path in a complete graph
        self.g.vs["color"] = "white"
        path = [x - 1 for x in self.path.copy()]

        self.g.vs.select(path[0])["color"] = "#5df449"
        self.g.vs.select(path[1:-1])["color"] = "#075dc6"
        self.g.vs.select(path[-1])["color"] = "red"

        self.g.vs.select(path[0])["shape"] = "triangle-down"
        self.g.vs.select(path[1:-1])["shape"] = "rectangle"
        self.g.vs.select(path[-1])["shape"] = "triangle-up"

        for i in range(len(self.path) - 1):
            start = self.path[i] - 1
            end = self.path[i + 1] - 1

            green_edges = self.g.es.select(_source_in=[start], _target_in=[end])
            green_edges["color"] = "#15870d"
            green_edges["width"] = 4

        layout = self.g.layout("tree")
        plot(self.g, "file.png", layout=layout)  # Save a temporary PNG file

        img = Image.open("file.png")
        path = os.getcwd() + "\\Storeroom manager software results\\Street\\"  # The address of the file
        file_name = "answer_graph.png"

        folder_name = "Try" + self.Try
        path += folder_name

        img.save(path + "\\" + file_name)
        img.show()
        os.remove("file.png")

    def find_weight(self, path):  # find the weight of a path
        out = 0
        for i in range(len(path) - 1):
            out += self.graph[path[i]][path[i + 1]]
        return out

    def DFS(self, path_current, current):  # DFS routing path

        if current == self.goal:
            weight_current = self.find_weight(path_current)
            if weight_current < self.weight:
                self.path = path_current
                self.weight = weight_current
            return

        if len(self.graph[current]) == 0:
            return

        for neighbor in self.graph[current]:
            if neighbor in path_current: continue
            self.DFS(path_current + [neighbor], neighbor)

    def print_graph(self):  # Draw the path
        base = 50
        for i in self.path[:-1]:
            tr.pencolor("black")
            tr.pensize(20)
            tr.fd(1)
            tr.bk(1)

            tr.pensize(5)
            tr.pencolor("blue")
            tr.write(i, font=("Arial", 27, "bold"))
            tr.pencolor("green")
            tr.fd(base)
            tr.rt(90)
            base += 25

        tr.pencolor("black")
        tr.pensize(20)
        tr.fd(1)
        tr.bk(1)

        tr.pensize(5)
        tr.pencolor("blue")
        tr.write(self.path[-1], font=("Arial", 27, "bold"))
        tr.pencolor("red")

        return ()

    @staticmethod
    def show_graph(dfs_obj, file_name):
        path = os.getcwd() + "\\Storeroom manager software results\\Street"  # The address of the file
        folder_name = "Try" + dfs_obj.Try
        path += "\\" + folder_name + "\\" + file_name

        img = Image.open(path)
        img.show()
        del img
