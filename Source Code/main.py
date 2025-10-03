from Storeroom import *
from Street import *
import shutil
import os
import turtle as tr

print("Welcome!")
new_path = os.getcwd() + "\\Storeroom manager software results"
# The path of the folder "Storeroom manager software results"

if os.path.exists(new_path):
    shutil.rmtree(new_path)  # Remove the folder "Storeroom manager software results" if it exists
os.makedirs(new_path)
os.makedirs(new_path + "\\Storeroom")
os.makedirs(new_path + "\\Street")

Storeroom_tries = []
Street_tries = []
while True:
    tr.reset()
    tr.title("صفحه اصلي")
    ghabeliat = tr.textinput("کدام قابليت",
                             "کدام قابليت نرم افزار را مي خواهيد؟"
                             "\nstoreroom --> براي مسيريابي در انبار"
                             "\nstreet --> برای مسیریابی در خیابان"
                             "\nprevious tries --> برای مشاهده تلاش های قبلی نرم افزار در مسیر یابی"
                             "\nabout us --> درباره ما"
                             "\nexit --> خروج")
    while (ghabeliat != "storeroom") and (ghabeliat != "street") and (ghabeliat != "exit") and \
            (ghabeliat != "about us") and (ghabeliat != "previous tries"):
        ghabeliat = tr.textinput("کدام قابليت",
                                 "کدام قابليت نرم افزار را مي خواهيد؟"
                                 "\nstoreroom --> براي مسير يابي در انبار"
                                 "\nstreet --> برای مسیر یابی در خیابان"
                                 "\nprevious tries --> برای مشاهده تلاش های قبلی نرم افزار در مسیر یابی"
                                 "\nabout us --> درباره ما"
                                 "\nexit --> خروج")

    if ghabeliat == "exit":
        tr.ht()
        print("Thanks for using this app. You can email us and say your comments")
        print("mahsan.ms1386@gmail.com")
        print("fatimamostafavi85@gmail.com")
        print("We are Mahsan Mohammadzade and Fatemeh Mostafavi from Farzanegan1 middle school")
        tr.write(
            "!ممنونیم که از نرم افزار ما استفاده می کنید! شما می توانید در ایمیل، با ما در تماس باشید"
            "\nmahsan.ms1386@gmail.com\nfatimamostafavi85@gmail.com\n"
            "مهسان محمدزاده و فاطمه مصطفوی از دبیرستان فرزانگان 1 تهران دوره اول",
            font=("Arial", 10, "bold"), align="center")
        print()
        print()
        input("Press Enter to exit.")
        sys.exit()

    if ghabeliat == "about us":
        tr.ht()
        print("Programmers: Mahsan Mohammadzade-Fateme Mostafavi")
        print("From Farzanegan 1 middle school")
        print("mahsan.ms1386@gmail.com")
        print("fatimamostafavi85@gmail.com")
        tr.write(
            "برنامه نویسان: مهسان محمدزاده-فاطمه مصطفوی\n"
            "(= از دبیرستان فرزانگان 1 تهران دوره اول"
            "\nmahsan.ms1386@gmail.com\nfatimamostafavi85@gmail.com",
            font=("Arial", 10, "bold"), align="center")
        tr.textinput("درباره ما", "")

    elif ghabeliat == "storeroom":
        tr.title("انبار")
        storeroom = AStar()
        storeroom.make_path()
        storeroom.print_path()
        Storeroom_tries.append(storeroom)

    elif ghabeliat == "street":
        tr.title("خيابان")
        street = DFS()
        street.make_and_print_path()
        Street_tries.append(street)

    elif ghabeliat == "previous tries":
        print("You're in \"previous tries\" part.")
        print()
        if (DFS.number_of_tries == 0) and (AStar.number_of_tries == 0):  # There's no results yet!
            tr.textinput("", "!هنوز هیچ تلاشی انجام نشده است")
            print("___________________")
            print()
            continue

        while True:
            part = tr.textinput("کدام بخش", "تلاش های قبلی کدام بخش را می خواهید؟"
                                            "\nstoreroom --> برای مشاهده تلاش های مسیریابی در انبار"
                                            "\nstreet --> برای مشاهده تلاش های مسیریابی در خیابان"
                                            "\nexit --> خروج از این بخش")
            while (part != "storeroom") and (part != "street") and (part != "exit"):
                part = tr.textinput("کدام بخش", "تلاش های قبلی کدام بخش را می خواهید؟"
                                                "\nstoreroom --> برای مشاهده تلاش های مسیریابی در انبار"
                                                "\nstreet --> برای مشاهده تلاش های مسیریابی در خیابان"
                                                "\nexit --> خروج از این بخش")

            if part == "exit":
                break

            if part == "storeroom":
                if AStar.number_of_tries == 0:  # There's no results for storeroom yet!
                    tr.textinput("", "!هنوز هیچ تلاشی در بخش مسیریابی در انبار انجام نشده است")
                    continue

                if AStar.number_of_tries == 1:  # There's just one result.
                    AStar.show_storeroom(Storeroom_tries[0])
                    print("You can see your request as a picture.")
                    print("***")
                    print()
                    tr.textinput("نتیجه درخواست", ".می توانید نتیجه درخواست خود را به صورت یک عکس ببینید")
                    continue

                num = int(tr.numinput("شماره تلاش", "شماره تلاش را وارد کنید"))
                while (num <= 0) or (num > AStar.number_of_tries):
                    num = int(tr.numinput("شماره تلاش", "!این شماره وجود ندارد\nلطفا دوباره وارد کنید\nشماره تلاش را "
                                                        "وارد "
                                                        "کنید"))
                AStar.show_storeroom(Storeroom_tries[num - 1])

            elif part == "street":
                if DFS.number_of_tries == 0:  # There's no results for street yet!
                    tr.textinput("", "!هنوز هیچ تلاشی در بخش مسیریابی در خیابان انجام نشده است")
                    continue

                if DFS.number_of_tries == 1:  # There's just one result.
                    num = 1
                    mode = tr.textinput("حالت تلاش", "کدام حالت تلاش " + str(num) + " ام را می خواهید؟"
                                                                                    "\nbase --> برای شکل کلی گراف "
                                                                                    "بدون مسیر "
                                                                                    "\nanswer --> برای گراف با مسیر")
                    while (mode != "base") and (mode != "answer"):
                        mode = tr.textinput("حالت تلاش", "کدام حالت تلاش " + str(num) + " ام را می خواهید؟"
                                                                                        "\nbase --> برای شکل کلی گراف "
                                                                                        "بدون مسیر "
                                                                                        "\nanswer --> برای گراف با مسیر"
                                            )
                    DFS.show_graph(Street_tries[0], "base_graph.png" if mode == "base" else "answer_graph.png")
                    print("You can see your request as a picture.")
                    print("***")
                    print()
                    tr.textinput("نتیجه درخواست", ".می توانید نتیجه درخواست خود را به صورت یک عکس ببینید")
                    continue

                num = int(tr.numinput("شماره تلاش", "شماره تلاش را وارد کنید"))
                while (num <= 0) or (num > DFS.number_of_tries):
                    num = int(tr.numinput("شماره تلاش", "!این شماره وجود ندارد\nلطفا دوباره وارد کنید\nشماره تلاش را "
                                                        "وارد "
                                                        "کنید"))

                mode = tr.textinput("حالت تلاش", "کدام حالت تلاش " + str(num) + " ام را می خواهید؟"
                                                                                "\nbase --> برای شکل کلی گراف بدون مسیر"
                                                                                "\nanswer --> برای گراف با مسیر")
                while (mode != "base") and (mode != "answer"):
                    mode = tr.textinput("حالت تلاش", "کدام حالت تلاش " + str(num) + " ام را می خواهید؟"
                                                                                    "\nbase --> برای شکل کلی گراف "
                                                                                    "بدون مسیر "
                                                                                    "\nanswer --> برای گراف با مسیر")
                DFS.show_graph(Street_tries[num - 1], "base_graph.png" if mode == "base" else "answer_graph.png")

            print("You can see your request as a picture.")
            print("***")
            print()
            tr.textinput("نتیجه درخواست", ".می توانید نتیجه درخواست خود را به صورت یک عکس ببینید")

    print("___________________")
    print()
