



try:
    from rich.console import Console 
    from tkinter import messagebox
    from tkinter import Tk
    from tkinter import *
    import os
    import time
    import hashlib
    import datetime
    import getpass
    import webbrowser
    import modules.RSOD_SYS as RSOD_SYS
    from modules.SYSTEM_INFO import SysInfo
    from modules.SETTINGS import SETTINGS
    from modules.NUMBERS import NUMBERS
    import platform
    from tkinter import filedialog
    from progress.bar import IncrementalBar
    from tkinter.ttk import Combobox  
    import shlex
    import random
except ModuleNotFoundError:
    console = Console()
    console.print("[yellow][WARN]: отсуствует необходимый модуль[/yellow]")
  
console = Console()

class Info:
    username = None



logo = """
████████╗░█████╗░██████╗░██╗░░░░░██╗██╗░░██╗  ░█████╗░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║██║░██╔╝  ██╔══██╗██╔════╝
░░░██║░░░███████║██████╔╝██║░░░░░██║█████═╝░  ██║░░██║╚█████╗░
░░░██║░░░██╔══██║██╔═══╝░██║░░░░░██║██╔═██╗░  ██║░░██║░╚═══██╗
░░░██║░░░██║░░██║██║░░░░░███████╗██║██║░╚██╗  ╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░╚═╝  ░╚════╝░╚═════╝░
"""

def usermanager():
    os.system("cls||clear")
    print("————————————————————————————————————————————————————————————————————————————————————————————————")
    print("Менеджер Пользователей")
    print("————————————————————————————————————————————————————————————————————————————————————————————————")
    print("create - Создать пользователя")
    print("info - Показать информацию о пользователе")
    print("edit - Изменить пользователя")
    print("exit - Выйти из менеджера пользователей")
    print("————————————————————————————————————————————————————————————————————————————————————————————————")
    command = input("Выберите действие ")
    if command == "create":
        os.system("cls||clear")
        username = input("Придумайте имя пользователя ")
        enablepassword = None
        password = None
        os.system("cls||clear")
        enablepasswordinput = input("Включить пароль? (True/False) ")
        root = None
        if enablepasswordinput != "True" and enablepasswordinput != "False":
            os.system("cls||clear")
            console.print("[red]Неверное значение (True/False)[/]")
            time.sleep(2)
            usermanager()
        elif enablepasswordinput == "True":
            enablepassword = "True"
            os.system("cls||clear")
            passwordinput = input("Придумайте пароль")
            password = hash(passwordinput)
            os.system("cls||clear")
            passwordcheck = input("Повторите пароль ")
            if hash(passwordcheck) != password:
                os.system("cls||clear")
                console.print("[red]Пароли не совпадают[/]")
                time.sleep(2)
                usermanager()              
        elif enablepasswordinput == "False":
            enablepassword = "False"
        os.system("cls||clear")
        enablerootinput = input("Root пользователь? (True/False) ")
        if enablerootinput != "True" and enablerootinput != "False":
            os.system("cls||clear")
            console.print("[red]Неверное значение (True/False)[/]")
            time.sleep(2)
            usermanager()
        elif enablerootinput == "True":
            root = "True"             
        elif enablerootinput == "False":
            enablepassword = "True"  
        text = f"""password {password}
passwordenable {enablepassword}
root {root}"""
        with open(f"users\\{username}.tapbin", "w") as file:
            file.write(text)   
        print("Пользователь успешно создан!")
        time.sleep(1)
        usermanager() 
    elif command == "info":
        os.system("cls||clear")
        dir = os.listdir("users")
        for i in range(len(dir)):
            filename = os.path.splitext(dir[i])[0]
            print(f"{i}) {filename}")


        user_name = os.path.splitext(dir[int(input("Введите номер пользователя для получения информации "))])[0]
        user_file = f'users\\{user_name}.tapbin'
        user_info = parse_user(user_file)
        os.system("cls||clear")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        print(f"Пользователь {user_name}")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        print(f"Пароль: " + user_info["password"])
        print(f"Включить пароль: " + user_info["passwordenable"])
        print(f"Root пользователь: " + user_info["root"])
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        a = input("Enter для продолжения ")
        usermanager()
    elif command == "edit":
        os.system("cls||clear")
        dir = os.listdir("users")
        for i in range(len(dir)):
            filename = os.path.splitext(dir[i])[0]
            print(f"{i}) {filename}")


        user_name = os.path.splitext(dir[int(input("Введите номер пользователя для изменения "))])[0]
        user_file = f'users\\{user_name}.tapbin'
        user_info = parse_user(user_file)
        os.system("cls||clear")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        print(f"Пользователь {user_name}")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        print("password - Сменить пароль")
        print("passwordenable - Изменить параметр включён ли пароль (True/False)")
        print("root - Изменить параметр root ли пользователь")
        print("delete - Удалить пользователя")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        a = input("Выберите действие ")
        if a == "password":
            os.system("cls||clear")
            password_input = hash(input("Придумайте новый пароль "))
            os.system("cls||clear")
            password2_input = hash(input("Повторите пароль "))
            if password2_input != password_input:
                os.system("cls||clear")
                console.print("[red]Пароли не совпадают[/]")
                time.sleep(2)
                usermanager()  
            else:
                text = f"""password {password_input}
passwordenable {user_info['passwordenable']}
root {user_info['root']}"""
                with open(f"users\\{user_name}.tapbin", "w") as file:
                    file.write(text)   
                os.system("cls||clear")
                print("Пароль успешно изменён!")
                time.sleep(1)
                usermanager() 
        elif a == "passwordenable":
            os.system("cls||clear")
            enablepasswordinput = input("Включить пароль? (True/False) ")
            if enablepasswordinput != "True" and enablepasswordinput != "False":
                os.system("cls||clear")
                console.print("[red]Неверное значение (True/False)[/]")
                time.sleep(2)
                usermanager()
            text = f"""password {user_info['password']}
passwordenable {enablepasswordinput}
root {user_info['root']}"""
            with open(f"users\\{user_name}.tapbin", "w") as file:
                file.write(text)   
            os.system("cls||clear")
            print("Параметр успешно изменён!")
            time.sleep(1)
            usermanager() 
        elif a == "root":
            os.system("cls||clear")
            enablerootinput = input("Root ли пользователь? (True/False) ")
            if enablerootinput != "True" and enablerootinput != "False":
                os.system("cls||clear")
                console.print("[red]Неверное значение (True/False)[/]")
                time.sleep(2)
                usermanager()
            text = f"""password {user_info['password']}
passwordenable {user_info['passwordenable']}
root {enablerootinput}"""
            with open(f"users\\{user_name}.tapbin", "w") as file:
                file.write(text)   
            os.system("cls||clear")
            print("Параметр успешно изменён!")
            time.sleep(1)
            usermanager() 
    elif command == "exit":
        root_menu()
            
         
            


def intToStr(intvalue):
    if intvalue == 1:
        return str(NUMBERS.n1)
    elif intvalue == 2:
        return str(NUMBERS.n2)
    elif intvalue == 3:
        return str(NUMBERS.n3)
    elif intvalue == 4:
        return str(NUMBERS.n4)
    elif intvalue == 5:
        return str(NUMBERS.n5)
    elif intvalue == 6:
        return str(NUMBERS.n6)
    elif intvalue == 7:
        return str(NUMBERS.n7)
    elif intvalue == 8:
        return str(NUMBERS.n8)
    elif intvalue == 9:
        return str(NUMBERS.n9)




def notepad():
    def chenge_theme(theme):
        text_fild['bg'] = view_colors[theme]['text_bg']
        text_fild['fg'] = view_colors[theme]['text_fg']
        text_fild['insertbackground'] = view_colors[theme]['cursor']
        text_fild['selectbackground'] = view_colors[theme]['select_bg']

    def chenge_fonts(fontss):
        text_fild['font'] = fonts[fontss]['font']


    def notepad_exit():
        answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
        if answer:
            root.destroy()





    def open_file():
        file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            text_fild.delete('1.0', END)
            text_fild.insert('1.0', open(file_path, encoding='utf-8').read())


    def save_file():
        file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        f = open(file_path, 'w', encoding='utf-8')
        text = text_fild.get('1.0', END)
        f.write(text)
        f.close()




    root = Tk()
    root.title('Блокнот')
    root.geometry('600x700')

    main_menu = Menu(root)



    # Файл
    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label='Открыть', command=open_file)
    file_menu.add_command(label='Сохранить', command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label='Закрыть', command=notepad_exit)
    root.config(menu=file_menu)

    # Вид
    view_menu = Menu(main_menu, tearoff=0)
    view_menu_sub = Menu(view_menu, tearoff=0)
    font_menu_sub = Menu(view_menu, tearoff=0)
    view_menu_sub.add_command(label='Тёмная', command=lambda: chenge_theme('dark'))
    view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
    view_menu.add_cascade(label='Тема', menu=view_menu_sub)

    font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
    font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
    font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
    view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
    root.config(menu=view_menu)

    # Добавление списков меню
    main_menu.add_cascade(label='Файл', menu=file_menu)
    main_menu.add_cascade(label='Вид', menu=view_menu)
    root.config(menu=main_menu)

    f_text = Frame(root)
    f_text.pack(fill=BOTH, expand=1)

    view_colors = {
        'dark': {
            'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
        },
        'light': {
            'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
        }
    }

    fonts = {
        'Arial': {
            'font':'Arial 14 bold'
        },
        'CSMS': {
            'font': ('Comic Sans MS', 14, 'bold')
        },
        'TNR': {
            'font': ('Times New Roman', 14, 'bold')
        }
    }



    text_fild = Text(f_text,
                    bg='black',
                    fg='lime',
                    padx=10,
                    pady=10,
                    wrap=WORD,
                    insertbackground='brown',
                    selectbackground='#8D917A',
                    spacing3=10,
                    width=30,
                    font='Arial 14 bold'
                    )
    text_fild.pack(expand=1, fill=BOTH, side=LEFT)

    scroll = Scrollbar(f_text, command=text_fild.yview)
    scroll.pack(side=LEFT, fill=Y)
    text_fild.config(yscrollcommand=scroll.set)



    print("Запуск блокнота...")
    time.sleep(3)
    root.mainloop()



def parse_meta(meta_file):
    meta = open(meta_file, "r", encoding="UTF-8").read()
    allowed = ["color", "stop", "damaged"]
    lines = meta.splitlines()
    result = {}
    for line in lines:
        splited = shlex.split(line)
        if len(splited) != 2:
            raise Exception(f"Invalid {meta_file}: invalid line {line!r}")
        if splited[0] in allowed:
            result[splited[0]] = splited[1] 
        else:
            raise Exception(f"Invalid {meta_file}: {splited[0]} not allowed")
    return result


def parse_user(user_file):
    meta = open(user_file, "r", encoding="UTF-8").read()
    allowed = ["password", "passwordenable", "root"]
    lines = meta.splitlines()
    result = {}
    for line in lines:
        splited = shlex.split(line)
        if len(splited) != 2:
            raise Exception(f"Invalid {user_file}: invalid line {line!r}")
        if splited[0] in allowed:
            result[splited[0]] = splited[1] 
        else:
            raise Exception(f"Invalid {user_file}: {splited[0]} not allowed")
    return result



def callFakeBsod(stop, damaged_file, color):
    RSOD_SYS.RSOD(STOP=stop, damaged_file=damaged_file, color=color, RES_OR_NO="NO", RES_TYPE2="NO")

def fakersod():
    window = Tk()  
    window.title("RSOD Generator")  
    window.geometry('400x250')  
    combo = Combobox(window)  
    combo['values'] = ("RED", "BLUE", "MAGIC")  
    combo.current(0)  # установите вариант по умолчанию  
    combo.grid(column=0, row=0)  
    combo.place(y=50, x=0)
    lbl = Label(window, text="Тип")  
    lbl.grid(column=0, row=0)  
    lbl.place(y=27, x=0)
    lbl2 = Label(window, text="Стоп код")  
    lbl2.grid(column=0, row=0)  
    lbl2.place(y=27, x=200)
    txt = Entry(window, width=20)  
    txt.grid(column=1, row=0)  
    txt.place(y=50, x=200)
    lbl3 = Label(window, text="Damaged files")  
    lbl3.grid(column=0, row=0)  
    lbl3.place(y=90, x=0)
    txt2 = Entry(window, width=20)  
    txt2.grid(column=1, row=0) 
    txt2.place(y=110, x=0)
    def clicked():
        callFakeBsod(stop=txt.get(), damaged_file=txt2.get(), color=combo.get())
    def open_file():
        filepath = filedialog.askopenfilename(initialfile="save.tapbin", filetypes =[('Taplik Files', '*.tapbin')])
        if filepath != "":
            result = parse_meta(filepath)
            colorvalue = result["color"]
            if colorvalue == "RED":
                combo.current(0)
            elif colorvalue == "BLUE":
                combo.current(1)
            elif colorvalue == "MAGIC":
                combo.current(2)
            else:
                combo.current(0)
            txt.delete(0, END)
            txt2.delete(0, END)
            txt.insert(0, result["stop"])
            txt2.insert(0, result["damaged"])
    def save_file():
        if combo.get() != "" and txt.get() != "" and txt2.get() != "":
            filepath = filedialog.asksaveasfilename(initialfile="save.tapbin", filetypes =[('Taplik Files', '*.tapbin')])
            if filepath != "":
                text = f"""color {combo.get()}
stop {txt.get()}
damaged {txt2.get()}"""
                with open(filepath, "w") as file:
                    file.write(text)
        else:
            messagebox.showerror(title="Ошибка", message="Невозможно сохранить пустую строку")
    btn = Button(window, text="Запустить RSOD", command=clicked, height=1, width=15)  
    btn.grid(column=2, row=0)  
    btn.place(y=110, x=200)
    menu = Menu(window)  
    new_item = Menu(menu, tearoff=0)  
    new_item.add_command(label='Сохранить', command=save_file)  
    new_item.add_command(label='Открыть', command=open_file)  
    menu.add_cascade(label='Файл', menu=new_item)  
    window.config(menu=menu)  
    window.mainloop()



def loadingScreen():
    if platform.system() == "Windows":
        os.system("color 90")
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        mylist2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        time.sleep(5)
        os.system("color 07")
        print(" ")
        bar = IncrementalBar(color = "blue",message = 'Импорт библиотек' , max = len(mylist),)

        for item in mylist:
            bar.next()
            time.sleep(0.4)

        bar.finish()

        bar2 = IncrementalBar(color = "blue",message = 'Загрузка TaplikOs' , max = len(mylist2),)

        for item2 in mylist2:
            bar2.next()
            time.sleep(0.4)

        bar2.finish()
    else:
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        mylist2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        print(" ")
        bar = IncrementalBar(color = "blue",message = 'Импорт библиотек' , max = len(mylist),)

        for item in mylist:
            bar.next()
            time.sleep(0.4)

        bar.finish()

        bar2 = IncrementalBar(color = "blue",message = 'Загрузка TaplikOs' , max = len(mylist2),)

        for item2 in mylist2:
            bar2.next()
            time.sleep(0.4)

        bar2.finish()
if SETTINGS.enableLogo == True:
    loadingScreen()


def crash():
    if platform.system() == "Windows":
        os.system("color 90")
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        print("")
        console.print("[white]Поиск проблем[/]", justify="center")
        time.sleep(3)
        bootsettings()
    else:
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        print("")
        console.print("[white]Поиск проблем[/]")
        time.sleep(3)
        bootsettings()

def credits():
    os.system("cls||clear")
    time.sleep(3)
    if platform.system() == "Windows":
        os.system("color 90")
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        print("")
        console.print("[white]Разработчики Taplik[/white]", justify="center")
        console.print("[white]Машина#2046 - Главный разработчик Taplik[/white]", justify="center")
        console.print("[white]Благодарности[/white]", justify="center")
        console.print("[white]DarkSlipe#0543[/white]", justify="center")
        console.print("[white]hopTech#5355[/white]", justify="center")
        console.print("[white]Kotaz#4769[/white]", justify="center")
        console.print("[white]Машина#2046 (возрадил Taplik XD)[/white]", justify="center")
        console.input("[white]Enter для закрытия меню[/]")
        os.system("color 07")
        os.system("cls||clear")
        time.sleep(3)
    else:
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        print("")
        console.print("[white]Разработчики Taplik[/white]", justify="center")
        console.print("[white]Машина#2046 - Главный разработчик Taplik[/white]", justify="center")
        console.print("[white]Благодарности[/white]", justify="center")
        console.print("[white]DarkSlipe#0543[/white]", justify="center")
        console.print("[white]hopTech#5355[/white]", justify="center")
        console.print("[white]Kotaz#4769[/white]", justify="center")
        console.print("[white]Машина#2046 (возрадил Taplik XD)[/white]", justify="center")      
        console.input("[white]Enter для закрытия меню[/]")
        os.system("cls||clear")
        time.sleep(3)


def bootsettings():
    os.system("cls||clear")
    time.sleep(3)
    if platform.system() == "Windows":
        os.system("color 90")
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        print("")
        console.print("[white]Выберите действие[/white]", justify="center")
        console.print("[white]1) Запустить Shiza Taplik[/white]", justify="center")
        console.print("[white]2) Переустановить Taplik[/white]", justify="center")
        console.print("[white]3) Закрыть окно настроек загрузки[/white]", justify="center")
        vibor = console.input("[white]>[/]")
        if vibor == "2)":
            os.system("cls||clear")
            os.system("color 07")
            time.sleep(3)
            os.remove("installed.tapbin")
            sys_crash_or_no()
        elif vibor == "1)":
            os.system("cls||clear")
            os.system("color 07")
            time.sleep(3)
            shiza()
        elif vibor == "3)":
            os.system("cls||clear")
            os.system("color 07")
            time.sleep(3)
        else:
            os.system("cls||clear")
            os.system("color 07")
            time.sleep(3)
    else:
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        print("")
        console.print("[white]Выберите действие[/white]", justify="center")
        console.print("[white]1) Запустить Shiza Taplik[/white]", justify="center")
        console.print("[white]2) Закрыть окно настроек загрузки[/white]", justify="center")
        vibor = console.input("[white]>[/]")
        if vibor == "2)":
            os.system("cls||clear")
            time.sleep(3)
        elif vibor == "1)":
            os.system("cls||clear")
            time.sleep(3)
            shiza()
        else:
            os.system("cls||clear")
            time.sleep(3)

def fakeinstall(text, inttime):
    if platform.system() == "Windows":
        time.sleep(3)
        os.system("color 90")
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        time.sleep(3)
        print(" ")
        console.print(text, justify="center")
        time.sleep(inttime)
        os.system("cls||clear")
        os.system("color 07")
        time.sleep(3)
    else:
        time.sleep(3)
        console.print("[white]" + logo + "[/white]", justify="center")
        console.print("[white]Made by CraftBox[/white]", justify="center")
        time.sleep(3)
        print(" ")
        console.print(text, justify="center")
        time.sleep(inttime)
        os.system("cls||clear")
        time.sleep(3)
def sysinfo():
    console.print("[bright_cyan]———————————————————————————————————————————————————————————[/bright_cyan]")
    console.print("[bright_cyan]Имя системы: [/bright_cyan]" + "[green1]" + SysInfo.osname + "[/green1]")
    console.print("[bright_cyan]Версия системы: [/bright_cyan]" + "[green1]" + SysInfo.version + "[/green1]")
    console.print("[bright_cyan]Описание системы: [/bright_cyan]" + "[green1]" + SysInfo.opisanie + "[/green1]")
    console.print("[bright_cyan]Статус системы: [/bright_cyan]" + "[green1]" + SysInfo.status + "[/green1]")
    console.print("[bright_cyan]———————————————————————————————————————————————————————————[/bright_cyan]")


                      
def tc_file(adc2, message):
    with open(adc2, 'a') as f:
        f.write(message) 

def hash(inp):
    return hashlib.sha512(inp.encode("utf-8")).hexdigest()
class User:
    def __init__(self, name, password="", abobus="", root=""):
        self.name = name
        self.password = password
        self.abobus = abobus
        self.root = root
users: User = [User("taplik", abobus=False, root=False), User("root", password="b17da26d23dd4d2e05d94a69e8fcd4a45243a74f2036ee3247acb1ff74642a51d38151923c1fdd9f37e96d06c96ca2a3f3eb32076d3acefef03ab1cf588d4209", root=True)]

def fetch_user(usr):
    for u in users:
        if u.name == usr:
            return u

def input_commands():
    user = getpass.getuser()
    a = input(f"{user}, Введи команду или menu для вывода всех команд: ")
    if a == "menu":
        menu()
    if a == "Calc":
        class Main(Frame):
            def __init__(self, root):
                super(Main, self).__init__(root)
                self.build()
            def build(self):
                self.formula = "0"
                self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
                self.lbl.place(x=11, y=50)

                btns = [
                    "C", "DEL", "*", "=",
                    "1", "2", "3", "/",
                    "4", "5", "6", "+",
                    "7", "8", "9", "-",
                    "(", "0", ")", "X^2"
                ]
                x = 10
                y = 140
                for bt in btns:
                    com = lambda x=bt: self.logicalc(x)
                    Button(text=bt, bg="#FFF",
                        font=("Times New Roman", 15),
                        command=com).place(x=x, y=y,
                                            width=115,
                                            height=79)
                    x += 117
                    if x > 400:
                        x = 10
                        y += 81
            def logicalc(self, operation):
                if operation == "C":
                    self.formula = ""
                elif operation == "DEL":
                    self.formula = self.formula[0:-1]
                elif operation == "X^2":
                    self.formula = str((eval(self.formula))**2)
                elif operation == "=":
                    self.formula = str(eval(self.formula))
                else:
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation
                self.update()
            def update(self):
                if self.formula == "":
                    self.formula = "0"
                self.lbl.configure(text=self.formula)
        if __name__ == '__main__':
            root = Tk()
            root["bg"] = "#000"
            root.geometry("485x550+200+200")
            root.title("Калькулятор")
            root.resizable(False, False)
            app = Main(root)
            app.pack()
            root.mainloop()
        input_commands()
    elif a == "exit":
        os.system("cls||clear")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        print("Вы действительно хотите выйти? Y/N")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        abcabc = input()
        if abcabc == "Y":
            exit()
        elif abcabc == "N":
            input_commands()
        else:
            print("Вариант не найден", abcabc)
            window = Tk()
            window.withdraw()
            messagebox.showerror("Ошибка", "Вариант не найден")
            input_commands()     
    elif a == "gener":
        os.system("cls||clear")
        aa = int(input("От: "))
        aa2 = int(input("До: "))
        cc = random.randint(aa, aa2)    
        print(cc)
        input_commands()
    elif a == "server":
        os.system("cls||clear")
        print("https://discord.gg/tjnNZGVR") 
        input_commands()
    elif a == "time":
        os.system("cls||clear")
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        print(current_time)
        input_commands()
    elif a == "date":
        os.system("cls||clear")
        current_date = datetime.date.today()
        print(current_date)
        input_commands()
    elif a == "feedback":
        os.system("cls||clear")
        print("Этой команды не существует :(")
        input_commands()
    elif a == "open":
        os.system("cls||clear")
        open = input("Введите URL сайта который хотите открыть ") 
        webbrowser.open(open)    
        input_commands()
    elif a == "meme":
        os.system("cls||clear")
        def meme():
            a = input("Введите шутку или menu для выхода в главное меню ")
            if a == "menu":
                menu()
            else:    
                import random
                random2 = random.randint(1,5)
                if random2 == 2:
                    print("Хахах не могу перестать смеяться")
                    input_commands()
                elif random2 == 3:
                    print("ХахахаАХАХАХАаХ хорошая шутка!")
                    input_commands()
                elif random2 == 4:
                    print("Хех")
                    input_commands()
                    
                elif random2 == 5:
                    print("Хорошая шутка!") 
                    input_commands()
                elif random2 == 1:
                    print("Не смешно")
                    input_commands()
                else:
                    print("Ошибка")
                    input_commands()             
        meme() 
    elif a == "usc":
        os.system("cls||clear")
        def usc():
            import getpass
            import random
            print(getpass.getuser(), "Оскарбляет программу")
            random3 = random.randint(1,5)
            if random3 == 1:
                print("Программа: каждый может оскорбить программу :(")
                input_commands()
            elif random3 == 2:
                print("Программа: :(")
                input_commands()
            elif random3 == 3:
                print("Программа: простите")
                input_commands()
            elif random3 == 4:
                print("Программа: простите меня пожалуйста")
                input_commands()
            elif random3 == 5:
                print("Программа: я больше так не буду")  
                input_commands()
        usc()
    elif a == "error":
        os.system("cls||clear")
        print("Напишите нам ошибку на почту maximkoreshkin@yandex.ru") 
        input_commands()   
    elif a == "hack":
        os.system("cls||clear")
        os.system("color a")
        input_commands()
    elif a == "gtn":
        os.system("cls||clear")
        def gnt():
            import random
            print("————————————————————————————————————————————————————————————————————————————————————————————————")
            print("Выберите уровень или menu для выхода")
            print("————————————————————————————————————————————————————————————————————————————————————————————————")
            print("лёгкий - будет загадано число от 0 до 5")
            print("сложный - будет загадано число от 0 до 20")
            print("хард - будет загадано число от 0 до 40")
            print("невозможный - будет загадано число от 0 до 100")
            print("————————————————————————————————————————————————————————————————————————————————————————————————")
            ot = input()
            if ot == "лёгкий":
                random4 = random.randint(0,5)
                def game(random4, pop2):
                    if pop2 == False:
                        print("было загадано число от 0 до 5")
                    elif pop2 == True:
                        pass    
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet)
                        game(random4=random4, pop2=True) 
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")  
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:            
                            menu()
                game(random4=random4, pop2=False)  
            elif ot == "сложный":
                random4 = random.randint(0,20)
                def game2(random4, pop2):
                    if pop2 == False:
                        print("Было загадано число от 0 до 20")
                    elif pop2 == True:
                        pass
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game2(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet) 
                        game2(random4=random4, pop2=True)   
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:
                            menu()  
                game2(random4=random4, pop2=False)                 
            elif ot == "хард":
                random4 = random.randint(0,40)
                def game3(random4, pop2):
                    if pop2 == False:
                        print("Было загадано число от 0 до 40")
                    elif pop2 == True:
                        pass
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game3(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet) 
                        game3(random4=random4, pop2=True)   
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:
                            menu()  
                game3(random4=random4, pop2=False)  
            elif ot == "невозможный":
                random4 = random.randint(0,100)
                def game4(random4, pop2):
                    if pop2 == False:
                        print("Было загадано число от 0 до 100")
                    elif pop2 == True:
                        pass
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game4(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet) 
                        game4(random4=random4, pop2=True)   
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:
                            menu()  
                game4(random4=random4, pop2=False)  
            else:
                menu()    
        gnt()
    elif a == "block":
        login()        
    elif a == "play":
        os.startfile("modules\\MusicPlayer\\start.bat")
        input_commands()
    elif a == "paint":
        os.startfile("modules\\Paint\\start.bat")
        input_commands()
    elif a == "translate":
        os.startfile("modules\\Translate\\start.bat")
        input_commands()
    elif a == "sysinfo":
        os.system("cls||clear")
        sysinfo()
        input_commands()
    elif a == "notepad":
        os.system("cls||clear")
        notepad()
        input_commands()
    elif a == "credits":
        credits()
        menu()
    else:
        console.print("[red]ERR: Команда не найдена[/red]")
        window = Tk()
        window.withdraw()
        messagebox.showerror("Ошибка", "Команда не найдена")
        time.sleep(2)
        input_commands()    
def root_input_commands():
    user = getpass.getuser()
    a = input(f"{user}, Введи команду или menu для вывода всех команд: ")
    if a == "menu":
        root_menu()
    if a == "Calc":
        class Main(Frame):
            def __init__(self, root):
                super(Main, self).__init__(root)
                self.build()
            def build(self):
                self.formula = "0"
                self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
                self.lbl.place(x=11, y=50)

                btns = [
                    "C", "DEL", "*", "=",
                    "1", "2", "3", "/",
                    "4", "5", "6", "+",
                    "7", "8", "9", "-",
                    "(", "0", ")", "X^2"
                ]
                x = 10
                y = 140
                for bt in btns:
                    com = lambda x=bt: self.logicalc(x)
                    Button(text=bt, bg="#FFF",
                        font=("Times New Roman", 15),
                        command=com).place(x=x, y=y,
                                            width=115,
                                            height=79)
                    x += 117
                    if x > 400:
                        x = 10
                        y += 81
            def logicalc(self, operation):
                if operation == "C":
                    self.formula = ""
                elif operation == "DEL":
                    self.formula = self.formula[0:-1]
                elif operation == "X^2":
                    self.formula = str((eval(self.formula))**2)
                elif operation == "=":
                    self.formula = str(eval(self.formula))
                else:
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation
                self.update()
            def update(self):
                if self.formula == "":
                    self.formula = "0"
                self.lbl.configure(text=self.formula)
        if __name__ == '__main__':
            root = Tk()
            root["bg"] = "#000"
            root.geometry("485x550+200+200")
            root.title("Калькулятор")
            root.resizable(False, False)
            app = Main(root)
            app.pack()
            root.mainloop()
        root_input_commands()
    elif a == "exit":
        os.system("cls||clear")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        print("Вы действительно хотите выйти? Y/N")
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        abcabc = input()
        if abcabc == "Y":
            exit()
        elif abcabc == "N":
            input_commands()
        else:
            print("Неверный вариант (Y/N) ", abcabc)
            window = Tk()
            window.withdraw()
            messagebox.showerror("Ошибка", "Неверный вариант (Y/N)")
            input_commands()     
    elif a == "gener":
        os.system("cls||clear")
        import random
        aa = int(input("От: "))
        aa2 = int(input("До: "))
        cc = random.randint(aa, aa2)    
        print(cc)
        root_input_commands()
    elif a == "server":
        os.system("cls||clear")
        print("Такой команды нет :(") 
        root_input_commands()
    elif a == "time":
        os.system("cls||clear")
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        print(current_time)
        root_input_commands()
    elif a == "date":
        os.system("cls||clear")
        current_date = datetime.date.today()
        print(current_date)
        root_input_commands()
    elif a == "Tslist_windows":
        os.system("cls||clear")
        os.system("tasklist")
        root_input_commands()
    elif a == "open":
        os.system("cls||clear")
        open = input("Введите URL сайта который хотите открыть ") 
        webbrowser.open(open)    
        root_input_commands()
    elif a == "cmd":
        os.system("cls||clear")
        command = input("Введите команду ")
        os.system(command)
        time.sleep(4)
        menu()
    elif a == "meme":
        os.system("cls||clear")
        def meme():
            a = input("Введите шутку или menu для выхода в главное меню ")
            if a == "menu":
                root_menu()
            else:    
                import random
                random2 = random.randint(1,5)
                if random2 == 2:
                    print("Хахах не могу перестать смеяться")
                    root_input_commands()
                elif random2 == 3:
                    print("ХахахаАХАХАХАаХ хорошая шутка!")
                    root_input_commands()
                elif random2 == 4:
                    print("Хех")
                    root_input_commands()
                    
                elif random2 == 5:
                    print("Хорошая шутка!") 
                    root_input_commands()
                elif random2 == 1:
                    print("Не смешно")
                    root_input_commands()
                else:
                    print("Ошибка")
                    root_input_commands()             
        meme() 
    elif a == "usc":
        os.system("cls||clear")
        def usc():
            import getpass
            import random
            print(getpass.getuser(), "Оскарбляет программу")
            random3 = random.randint(1,5)
            if random3 == 1:
                print("Программа: каждый может оскорбить программу :(")
                root_input_commands()
            elif random3 == 2:
                print("Программа: :(")
                root_input_commands()
            elif random3 == 3:
                print("Программа: простите")
                root_input_commands()
            elif random3 == 4:
                print("Программа: простите меня пожалуйста")
                root_input_commands()
            elif random3 == 5:
                print("Программа: я больше так не буду")  
                root_input_commands()
        usc()
    elif a == "error":
        os.system("cls||clear")
        print("Напишите нам ошибку на почту maximkoreshkin@yandex.ru") 
        root_input_commands()   
    elif a == "hack":
        os.system("color a")
        root_input_commands()
    elif a == "gtn":
        os.system("cls||clear")
        def gnt():
            import random
            print("————————————————————————————————————————————————————————————————————————————————————————————————")
            print("Выберите уровень или menu для выхода")
            print("————————————————————————————————————————————————————————————————————————————————————————————————")
            print("лёгкий - будет загадано число от 0 до 5")
            print("сложный - будет загадано число от 0 до 20")
            print("хард - будет загадано число от 0 до 40")
            print("невозможный - будет загадано число от 0 до 100")
            print("————————————————————————————————————————————————————————————————————————————————————————————————")
            ot = input()
            if ot == "лёгкий":
                random4 = random.randint(0,5)
                def game(random4, pop2):
                    if pop2 == False:
                        print("было загадано число от 0 до 5")
                    elif pop2 == True:
                        pass    
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet)
                        game(random4=random4, pop2=True) 
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")  
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            root_menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:            
                            root_menu()
                game(random4=random4, pop2=False)  
            elif ot == "сложный":
                random4 = random.randint(0,20)
                def game2(random4, pop2):
                    if pop2 == False:
                        print("Было загадано число от 0 до 20")
                    elif pop2 == True:
                        pass
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game2(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet) 
                        game2(random4=random4, pop2=True)   
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            root_menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:
                            root_menu()  
                game2(random4=random4, pop2=False)                 
            elif ot == "хард":
                random4 = random.randint(0,40)
                def game3(random4, pop2):
                    if pop2 == False:
                        print("Было загадано число от 0 до 40")
                    elif pop2 == True:
                        pass
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game3(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet) 
                        game3(random4=random4, pop2=True)   
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            root_menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:
                            root_menu()  
                game3(random4=random4, pop2=False)  
            elif ot == "невозможный":
                random4 = random.randint(0,100)
                def game4(random4, pop2):
                    if pop2 == False:
                        print("Было загадано число от 0 до 100")
                    elif pop2 == True:
                        pass
                    otvet = int(input())
                    if otvet < random4:
                        print("Неверно, было загадано число которое больше", otvet)
                        game4(random4=random4, pop2=True)
                    elif otvet > random4:
                        print("Неверно, было загадано число которое меньше", otvet) 
                        game4(random4=random4, pop2=True)   
                    elif otvet == random4:
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        print("Поздравляю! Вы выйграли! вы хотите продолжить играть или вернуться в меню?")
                        print("————————————————————————————————————————————————————————————————————————————————————————————————") 
                        print("menu - вернуться в меню")
                        print("game - играть сново") 
                        print("————————————————————————————————————————————————————————————————————————————————————————————————")
                        game_or_menu = input()
                        if game_or_menu == "menu":
                            root_menu()
                        elif game_or_menu == "game":
                            gnt()
                        else:
                            root_menu()  
                game4(random4=random4, pop2=False)    
            else:
                root_menu()  
        gnt()
    elif a == "block":
        login()        
    elif a == "tc":
        os.system("cls||clear")
        adc = input("Введите путь к файлу или /m чтобы перейти в папку с данной oc ")
        if adc == "/m":
            adc2 = input("Введите имя файла который хотите изменить не забудьте про расширение! ")
            if adc2 == "bottest.tapbin":
                RSOD_SYS.RSOD(STOP="ATTEMPT_TO_CHANGE_A_FILE_BOTTEST.TAPBIN", damaged_file="No damaged files.", color="RED", RES_OR_NO="NO", RES_TYPE2="NO")
                time.sleep(2)
                exit()
            elif adc2 == "os.py":
                time.sleep(5)
                RSOD_SYS.RSOD(STOP="ATTEMPT_TO_CHANGE_A_FILE_OS.PY", damaged_file="No damaged files.", color="MAGIC", RES_OR_NO="NO", RES_TYPE2="NO")
            else:
                message = input("Введите что добавить к файлу ")
                tc_file(adc2=adc2, message=message)
        else:
            os.system("cd {adc}")
            adc2 = input("Введите имя файла который хотите изменить не забудьте про расширение! ")
            if adc2 == "bottest.tapbin":
                RSOD_SYS.RSOD(STOP="ATTEMPT_TO_CHANGE_A_FILE_BOTTEST.TAPBIN", damaged_file="No damaged files.", color="RED", RES_OR_NO="NO", RES_TYPE2="NO")
                time.sleep(2)
                exit()
            elif adc2 == "os.py":
                time.sleep(5)
                RSOD_SYS.RSOD(STOP="ATTEMPT_TO_CHANGE_A_FILE_OS.PY", damaged_file="No damaged files.", color="MAGIC", RES_OR_NO="NO", RES_TYPE2="NO")
            else:
                message = input("Введите что добавить к файлу ")
                tc_file(adc2=adc2, message=message)
    elif a == "play":
        os.startfile("modules\\MusicPlayer\\start.bat")
        input_commands()
    elif a == "paint":
        os.startfile("modules\\Paint\\start.bat")
        input_commands()
    elif a == "translate":
        os.startfile("modules\\Translate\\start.bat")
        root_input_commands()
    elif a == "python_terminal":
        os.system("cls||clear")
        def python_terminal():
            command = input(">>>")
            if command == "exit()":
                root_input_commands()
            else:
                print(exec(command))
                python_terminal()
        if SETTINGS.enablePythonTerminal == False:
            logging.info("Python терминал отключен в настройках")
            print("Python терминал отключен в настройках!")
        else:
            python_terminal()
    elif a == "sysinfo":
        os.system("cls||clear")
        sysinfo()
        root_input_commands()
    elif a == "fakersod":
        fakersod()
    elif a == "notepad":
        os.system("cls||clear")
        notepad()
        input_commands()
    elif a == "credits":
        credits()
        root_menu()
    elif a == "boot":
        bootsettings()
        root_menu()
    elif a == "usermanager":
        usermanager()
    else:
        console.print("[red]ERR: Команда не найдена[/red]")
        window = Tk()
        window.withdraw()
        messagebox.showerror("Ошибка", "Команда не найдена.")
        time.sleep(2)
        root_input_commands()  
def shiza_input_commands():
    a = input("ш̴̨̡̡͔͎̲̥̺̳͚̮̤͈̰̹͈͎͇͎̞̲̭̦̳͙̲͍̙̤̗͍̎̓̄̆̈́͑̉͆͐͛́̅͝ͅͅӧ̴̱͎̘̬̜̩̩̬͚̳͓̲̼̣́͗́́͌̉́͊̎̂͊͗͌̃̊̏͑̔̀̈̓̓̀̀̈̔̚͘͘̕̕̚͝ ̴̡̧̙̯͔̜̗̖̝̦͙̪̫̘͈̣̯͈̦͚̞̹̪͉̹͚̰̘̤̫̱̹̙̱̊̾̊̾̉̏̄̄̔̈͂̂̈̌̐̓̉͝т̴̢̢̨̛̖̘̥̤͎̺̩̪͇̣̠̗͚͉̣̹͉̱͖͈̦͇͎̜̝̜͈̞̣͔̯͍̘̜͉̎̎̂͒̂́̀̓̒͌͆̆̃̈́̈́̍̈́͆̅͑͊̑͋̋̄̌̂̓́̈̊̒̑̓́̀̆̄̚͘̚͜͜͠͝ͅͅу̷̡͔̦̲̣͉̼͛̈́́̒̾̀͂̈́͗̄̈́͂͌̈̉̄̀́͗̊̒̓͑̈́̓̎͛̔̊̓̈́̅͛̑͒́̃͒͘̕͝͠͝т̴̢̨̨̧̡̨̡̗̲̫̺̞̭̱͚͚̲͎̙̜̟̻͙͇͖̺̻͈̮̩͕̳̩͓̆͐͂̽̔̇͛̚͠͝͝͠͝ͅ ̷̢̧̢̡̨̢̡̼̪̯̬̗͙̰͔̼͇͖̭̞͇̯̻̱̮͍̤͈̱̦̰͍̼͈̪̗͔̦̜̣͇͇̞͖̦̜̘̖̽͒̔п̶̡̮̞̟̻̼͔̣̩̼̫̖͙̙̩̲̝͂͜ͅи̵̨̡̺̫̳̞̹͕̗̣̳̱͙̗͓̼̱̪̖̠̟̣̟͖̰̗̪̬̲̑̉̾̔̊̍̅̔̆̀̈́͑͜͜ͅс̸̛̛̞̼̫̏̿̉̇̐̃̈́̉̐̔̆̋͗̀̔̾̿̓͆̒̏͌̿̌̊̍͆̈̈́̆̚͘͝͝͝а̸̨̨̧̨̢̢̛̻̯̺͉̬̝̼̬͚̼͙̺͔͕͚̪̯͈̰̜̩̘̮͍̠͓̙̬̘̫̼͕̗͕̞̣̼͙̻̙̇͗̈́̌̐̔́̐̈́́̌͌͌̇̿͑̾̀̉̾͊̑͂͐̈́̽͂̈́̂̚̚̕͜͝͝͝ͅт̵̢̨̧̡̺̗̲͇͒́͐͂̄̅͂̉͗̂̀̀̄̕ь̵̢̻̜̹̞͈̱̠̙̤͍̭̫̱͚͈̣̟͈̮̬̰̲̫̘͕͈̦̗̳̤̭̬̟̱̪̘̫̖̓̎͒̃͒̅͋̅̉͌̿̂ͅ?̶̛̹̰̭̻͉̭̽̑̔͆̀̈́̒̀́̄̕̚͠  ")
    if a == "menu":
        shiza()
    if a == "exit":
        print("аААА НИИТИ ТИ ПРАСНУЛЬСЯЯЯ")
        print("ААААААААААААААААААААААААААААААА ИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИПТААААААААА")
        time.sleep(3)
    else:
        console.print("[red]ERR: Штука не найдена ъъъъъъъъъъъъъъ[/red]")
        window = Tk()
        window.withdraw()
        messagebox.showerror("ашипка", "шо тут писать?")
        time.sleep(2)
        input_commands()      
def root_menu():
    os.system("cls||clear")
    os_name = SysInfo.osname + " " + SysInfo.version
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print(f"{os_name}", justify="center")
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("Пользователь windows/linux:" + "[green] " + getpass.getuser() + "[/]", justify="center" )
    console.print("Пользователь taplik:" + "[green] " + Info.username + "[/]", justify="center")
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("[bright_cyan]--------------------------  [/bright_cyan]", justify="center")
    console.print("[bright_cyan]| " +     "T | A | P | L | I | K. " + "|[/bright_cyan]", justify="center")
    console.print('[bright_cyan]--------------------------[/bright_cyan]', justify="center")
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("[white][bold]Команды:[/][/]", justify="center")
    console.print("[spring_green3]Calc[/] - Калькулятор", justify="center")
    console.print("[spring_green3]gener[/] - Генерация рандомного числа", justify="center")
    console.print("[spring_green3]time[/] - Текущее время", justify="center")
    console.print("[spring_green3]date[/] - Текущаяя дата", justify="center")
    console.print("[spring_green3]Tslist_windows[/] - Все процессы", justify="center")
    console.print("[spring_green3]open[/] - Открыть сайт по URL адресу", justify="center")
    console.print("[spring_green3]cmd[/] - Выполнить команду linux/windows", justify="center")
    console.print("[spring_green3]meme[/] - Пошутить программе", justify="center")
    console.print("[spring_green3]usc[/] - Оскорбить программу", justify="center")
    console.print("[spring_green3]exit[/] - Выйти из taplik", justify="center")
    console.print("[spring_green3]hack[/] - Включить режим хакера", justify="center")
    console.print("[spring_green3]gtn[/] - Игра угадай число", justify="center")
    console.print("[spring_green3]block[/] - Заблокировать", justify="center")
    console.print("[spring_green3]play[/] - Аудио плеер", justify="center")
    console.print("[spring_green3]error[/] - Сообщить об ошибке", justify="center")      
    console.print("[spring_green3]tc[/] - Добавить к тестовому документу...", justify="center")      
    console.print("[spring_green3]sysinfo[/] - Информация о системе", justify="center")           
    console.print("[spring_green3]notepad[/] - Блокнот", justify="center")     
    console.print("[spring_green3]fakersod[/] - RSOD генератор", justify="center") 
    console.print("[spring_green3]credits[/] - Разработчики", justify="center")      
    console.print("[spring_green3]boot[/] - Настройки загрузки", justify="center")   
    console.print("[spring_green3]paint[/] - Программа для рисования", justify="center")    
    console.print("[spring_green3]translate[/] - Переводчик", justify="center")                                  
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("Taplik все права защищены", justify="center") 
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    root_input_commands()
def menu():
    os.system("cls||clear")
    os_name = SysInfo.osname + " " + SysInfo.version
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print(f"{os_name}", justify="center")
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("Пользователь windows/linux:" + "[green] " + getpass.getuser() + "[/]", justify="center" )
    console.print("Пользователь taplik:" + "[green] " + Info.username + "[/]", justify="center" )
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("[bright_cyan]--------------------------  [/bright_cyan]", justify="center")
    console.print("[bright_cyan]| " +     "T | A | P | L | I | K. " + "|[/bright_cyan]", justify="center")
    console.print('[bright_cyan]--------------------------[/bright_cyan]', justify="center")
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("[white]Команды:[/]", justify="center")
    console.print("[spring_green3]Calc[/] - Калькулятор", justify="center")
    console.print("[spring_green3]gener[/] - Генерация рандомного числа", justify="center")
    console.print("[spring_green3]time[/] - Текущее время ", justify="center")
    console.print("[spring_green3]date[/] - Текущаяя дата", justify="center")
    console.print("[spring_green3]open[/] - Открыть сайт по URL адресу", justify="center")
    console.print("[spring_green3]meme[/] - Пошутить программе", justify="center")
    console.print("[spring_green3]usc[/] - Оскорбить программу", justify="center")
    console.print("[spring_green3]exit[/] - Выйти из taplik", justify="center")
    console.print("[spring_green3]hack[/] - Включить режим хакера", justify="center")
    console.print("[spring_green3]gtn[/] - Игра угадай число", justify="center")
    console.print("[spring_green3]block[/] - Заблокировать", justify="center")
    console.print("[spring_green3]play[/] - Аудио плеер", justify="center")
    console.print("[spring_green3]error[/] - Сообщить об ошибке", justify="center")                 
    console.print("[spring_green3]sysinfo[/] - Информация о системе", justify="center") 
    console.print("[spring_green3]notepad[/] - Блокнот", justify="center")      
    console.print("[spring_green3]translate[/] - Переводчик", justify="center")                                     
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    console.print("Taplik все права защищены", justify="center") 
    console.print("[bright_cyan]————————————————————————————————————————————————————————————————————————————————————————————————[/bright_cyan]", justify="center")
    input_commands()
def shiza():
    os.system("cls||clear")
    console.print("[bright_cyan]——————————————---—[/]", justify="center")
    console.print("АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА ЁПТА")
    console.print("[bright_cyan]—————————————----------——————————————[/]", justify="center")
    console.print("ЧОООООООООООООООООООООООООООООООООООООО", justify="center" )
    console.print("Ч̷̧͎̤͖̜̖̩̲͙͚͍͎̺̰͕̪̩͙͔̘̬̱̬̅̈́͂̀̀̿̇̄̔̽̒̅͛͊̚͜͠͝͠͝͠ͅЁ̶̧̝͈̠̼̣͕̎̈̒͑̈́̂̅͗͑̑̈̒̓́̍̌͂̄͂̇͂̽̆̀͂̚͘͝ ̴̛̺̦̪͈̲̭̓̈̎̏̓̈́̋̀̋̔̈́̓͌̏̐̈́̓̈́̂͊̑̍̋̓̓̃̂̄͘̕͜͝͠З̷̡̨̣̖̫̞̹͖̜͕̜̤͚̘̜̻̮̻̫͕͙̣̝̖̣̩̱̿̓̒̍̍̇̕͜͠ͅА̸̡̡̨̨̠̬͎̩̟̯͔̲̪̘͚͕̜͎̭̖̯̼͕̭̰̭͕͇̰͈̞͓̺̝̭̼͖̥͓̹͚͚̙͎̫̰̂́̆́̆͊̈̒͗̏̍͗̊͑̾̂́̆́͌̓͗̊̌̓̆̄̈̕̕͝͠ͅА̷̖̭͈̝̘̬͙̦͖͍͎̦̘̑̄́͌̌̔̌͂͘А̴̨̡̨̡̨̢̺̗̞̻̝͖̭̬̣͇̟̹͖̙͎͍̟̱͕̝̞̠̼̹̥̩̘̬̮͓̤̲͓͙͇͆̍͐̀̈́̎͌̀̋̅̀͂̚͜А̵̡̢̻̯̞̹̻̫̗̣̤̩͓͙͍̠̻̤͎͉̹͔͍͕̠̫̞̝̭͕̱̘͔̻̓А̵̢̛̛͚̹̯͔͉̺̠̟̯̥̥̏͐̊͗̐̔͒͛͒́̈͐̅͛̔͗̌͆̂͌͐͊͊̽͑̈́͌́̋̌͌̚͘͝͝ͅА̵͓̌͌́̒̈́̃̕͠А̵̧̛̼̩͍̦̼̥̺̝̜̺͕͎̱̪̖̱̯̺͈̣́̈́͐̃̈́͒̓̐͛͗͊̒̈́̽̆͋̈̅͌͒̓̈́̆͒͛̇͊̈͒̓̚͜͜͝ͅͅА̸̢̛̛͇̼̱̺̰̯̘̥̱̎̃̈́͆̂̓̀̒̓̃̂̀̓͒̿́͛̓̌́̈̅̓̎̆̌͐̅̌̈̒̀̇́̎̏̌͘̚͘͠͝ͅА̸̡̡͇̩̙͖͍̙̻̺͇̻̯̲̜̗̥̳͙̓̄̽̂̌̃̅̂̐͐̆͒̓͐̕А̶̧̨̰̟̬̹̣̳͈̙̬͓͓̦̗̦̰̬̫̖͎͚̮͇͍̜̙̳̖̘̖̲̤̮̫̭̦̣̼̤̠͚̮̦̗͙̾̀̈́̅̔̊̄̽͋̈͌͑́̅͌̋͜͜͜͝А̸̛̛̳̩̘̣̯̻̰̙̣͎͉̳̗̠͌͗̈́̄̒͊̿͂͊̉́͒̽̈̃͐͛̅̏̄̄̂̄͐̈̈́̀̒͐́͌̒̊͊̄̈̂̇̕͘̕͘͝А̶̨͙̞͎̻̳̳̯͚̫̱͖̟̂̅̉̌́̊̄̈́̊̋͗̆̄̑̆͆̆̉͊̓̃̀͆̔̀̿̓̃̒̐̕̚͝͠͠͠͝ͅͅА̷̛̖̜̪̃̒͆̎͗̈́̎̐̽͆̔͌͂̑͊̌̎̔͆̆͋̒̔͒͐͑̂͊̈̏̉̀͗̏͂̾͛͛̋̈̈́̚̚͘̚͘͘͜͝А̵̧̢̡̨̛̛̤̮͕̫̣̲͇̬̰̟̳̖̼̦͉͎͍̪̬̼͍̱̩̲̮͈̲̝̤͈͈͎͙̝̩͙͇͍̩̤̹͙͐̌̊̅̾̿̽̅̊͛̈́͑̌̑̑̔̐̇̓͛̓̐̓͑͐͂̌̋̃̅͊̊̀̐͂̐̐͌̾̉̿̅̏͘͘͘͘͜ͅА̶̨̢̧̨͎̰̯̝̲͔̺͓̥̻̼̂͜А̶̧̨̡̧͇̼̰̟͚͙̺̣͎͈̞̘̼̭̤͚͇̰̲̟̪̗̣̝͎̼̠͇̭̞͉̫̹͎̳̤̪̹͖̠̽͐͊̉̌̔̇͛̄̓͛̍̆̈́̂̿͛̑̋̉̈́̈́̍͆̇͛̿́͊̄͆̎̇͘̚͘͘̚͜͜͜͜͝͝А̴̨̧̢̢̧̙̰̭̲̻̣̫̠̥̰̳͍̲̼̰̘̫̜̗̱͙͇̣̗͖͙͖̙͇̪͙̣̫͚̅͑̏̾̓̊ͅА̴͇̠̹̻̙̻̥̅̅̋́̆̽́̿͋͊͗̌̆̓̆̊̊̇̅͒͆̌̈́͋̋̍̎̚̕͘̚͝А̴̨̢̡̛̭̰͇̪̻͔̫̳̜̗̯͉̺̩̗̳͙̦̹͓͍͉̺̮͉͍̋̇̏̌̃̐̈͗͑̏̈̈́̉̆̾̉̍̍́̓̒̌̎̎͌̄͛̓́͆͒͐́̇͋͐̂̐̓̑̿̚͘͜͝͝͝͠͠ͅА̷̝̞̱͉͊̇̓̃̀̄̏͑̿̓̈̊̓͑̍͛̃̾͊͘̕ͅА̵̡̢͓͚̤̣̰̗͕̪̱̱̼̠͎̬̬͖̤̭̩̞̏̊̄̍̔͋̍͒͋̂̃̉̾͐̎̈́͂̆́͐̏͑͂̾̎͑̾̒̕͜͝͝А̴̢̢̢̡̰͔͎̜̦̼̳̺͖͙̟̲͎͚̮̖̞̠͓̠̻̭͉̮̠̦̐̎́̈́̓̒̂͛́̑̈́̾́̽̊̌͒͗̈́̌̈̔̄̐̅̓̑̓͌̾̂͒̌̍͘̚̕͘А̷̡̢̛̛̙͓̖̭̘͔͔̜̙̰̮̯̲͔̯̫̝̞̥̠͚͈̹̜̖͚̦͖̿͂̑̈́͐͂͐̂͐̑̀͐̂̊̊̀̍̊͊̿͋̉̌̀͂̋̋̃̊̒̓̎̇̔̋͜͝", justify="center" )
    console.print("[bright_cyan]—————————————————----------——————————————————————————————[/]", justify="center")
    console.print("[bright_cyan]--------------------------  [/]", justify="center")
    console.print("[bright_cyan]Ч̷̧͎̤͖̜̖̩̲͙͚͍͎̺̰͕̪̩͙͔̘̬̱̬̅̈́͂̀̀̿̇̄̔̽̒̅͛͊̚͜͠͝͠͝͠ͅЁ̶̧̝͈̠̼̣͕̎̈̒͑̈́̂̅͗͑̑̈̒̓́̍̌͂̄͂̇͂̽̆̀͂̚͘͝ ̴̛̺̦̪͈̲̭̓̈̎̏̓̈́̋̀̋̔̈́̓͌̏̐̈́̓̈́̂͊̑̍̋̓̓̃̂̄͘̕͜͝͠З̷̡̨̣̖̫̞̹͖̜͕̜̤͚̘̜̻̮̻̫͕͙̣̝̖̣̩̱̿̓̒̍̍̇̕͜͠ͅА̸̡̡̨̨̠̬͎̩̟̯͔̲̪̘͚͕̜͎̭̖̯̼͕̭̰̭͕͇̰͈̞͓̺̝̭̼͖̥͓̹͚͚̙͎̫̰̂́̆́̆͊̈̒͗̏̍͗̊͑̾̂́̆́͌̓͗̊̌̓̆̄̈̕̕͝͠ͅА̷̖̭͈̝̘̬͙̦͖͍͎̦̘̑̄́͌̌̔̌͂͘А̴̨̡̨̡̨̢̺̗̞̻̝͖̭̬̣͇̟̹͖̙͎͍̟̱͕̝̞̠̼̹̥̩̘̬̮͓̤̲͓͙͇͆̍͐̀̈́̎͌̀̋̅̀͂̚͜А̵̡̢̻̯̞̹̻̫̗̣̤̩͓͙͍̠̻̤͎͉̹͔͍͕̠̫̞̝̭͕̱̘͔̻̓А̵̢̛̛͚̹̯͔͉̺̠̟̯̥̥̏͐̊͗̐̔͒͛͒́̈͐̅͛̔͗̌͆̂͌͐͊͊̽͑̈́͌́̋̌͌̚͘͝͝ͅА̵͓̌͌́̒̈́̃̕͠А̵̧̛̼̩͍̦̼̥̺̝̜̺͕͎̱̪̖̱̯̺͈̣́̈́͐̃̈́͒̓̐͛͗͊̒̈́̽̆͋̈̅͌͒̓̈́̆͒͛̇͊̈͒̓̚͜͜͝ͅͅА̸̢̛̛͇̼̱̺̰̯̘̥̱̎̃̈́͆̂̓̀̒̓̃̂̀̓͒̿́͛̓̌́̈̅̓̎̆̌͐̅̌̈̒̀̇́̎̏̌͘̚͘͠͝ͅА̸̡̡͇̩̙͖͍̙̻̺͇̻̯̲̜̗̥̳͙̓̄̽̂̌̃̅̂̐͐̆͒̓͐̕А̶̧̨̰̟̬̹̣̳͈̙̬͓͓̦̗̦̰̬̫̖͎͚̮͇͍̜̙̳̖̘̖̲̤̮̫̭̦̣̼̤̠͚̮̦̗͙̾̀̈́̅̔̊̄̽͋̈͌͑́̅͌̋͜͜͜͝А̸̛̛̳̩̘̣̯̻̰̙̣͎͉̳̗̠͌͗̈́̄̒͊̿͂͊̉́͒̽̈̃͐͛̅̏̄̄̂̄͐̈̈́̀̒͐́͌̒̊͊̄̈̂̇̕͘̕͘͝А̶̨͙̞͎̻̳̳̯͚̫̱͖̟̂̅̉̌́̊̄̈́̊̋͗̆̄̑̆͆̆̉͊̓̃̀͆̔̀̿̓̃̒̐̕̚͝͠͠͠͝ͅͅА̷̛̖̜̪̃̒͆̎͗̈́̎̐̽͆̔͌͂̑͊̌̎̔͆̆͋̒̔͒͐͑̂͊̈̏̉̀͗̏͂̾͛͛̋̈̈́̚̚͘̚͘͘͜͝А̵̧̢̡̨̛̛̤̮͕̫̣̲͇̬̰̟̳̖̼̦͉͎͍̪̬̼͍̱̩̲̮͈̲̝̤͈͈͎͙̝̩͙͇͍̩̤̹͙͐̌̊̅̾̿̽̅̊͛̈́͑̌̑̑̔̐̇̓͛̓̐̓͑͐͂̌̋̃̅͊̊̀̐͂̐̐͌̾̉̿̅̏͘͘͘͘͜ͅА̶̨̢̧̨͎̰̯̝̲͔̺͓̥̻̼̂͜А̶̧̨̡̧͇̼̰̟͚͙̺̣͎͈̞̘̼̭̤͚͇̰̲̟̪̗̣̝͎̼̠͇̭̞͉̫̹͎̳̤̪̹͖̠̽͐͊̉̌̔̇͛̄̓͛̍̆̈́̂̿͛̑̋̉̈́̈́̍͆̇͛̿́͊̄͆̎̇͘̚͘͘̚͜͜͜͜͝͝А̴̨̧̢̢̧̙̰̭̲̻̣̫̠̥̰̳͍̲̼̰̘̫̜̗̱͙͇̣̗͖͙͖̙͇̪͙̣̫͚̅͑̏̾̓̊ͅА̴͇̠̹̻̙̻̥̅̅̋́̆̽́̿͋͊͗̌̆̓̆̊̊̇̅͒͆̌̈́͋̋̍̎̚̕͘̚͝А̴̨̢̡̛̭̰͇̪̻͔̫̳̜̗̯͉̺̩̗̳͙̦̹͓͍͉̺̮͉͍̋̇̏̌̃̐̈͗͑̏̈̈́̉̆̾̉̍̍́̓̒̌̎̎͌̄͛̓́͆͒͐́̇͋͐̂̐̓̑̿̚͘͜͝͝͝͠͠ͅА̷̝̞̱͉͊̇̓̃̀̄̏͑̿̓̈̊̓͑̍͛̃̾͊͘̕ͅА̵̡̢͓͚̤̣̰̗͕̪̱̱̼̠͎̬̬͖̤̭̩̞̏̊̄̍̔͋̍͒͋̂̃̉̾͐̎̈́͂̆́͐̏͑͂̾̎͑̾̒̕͜͝͝А̴̢̢̢̡̰͔͎̜̦̼̳̺͖͙̟̲͎͚̮̖̞̠͓̠̻̭͉̮̠̦̐̎́̈́̓̒̂͛́̑̈́̾́̽̊̌͒͗̈́̌̈̔̄̐̅̓̑̓͌̾̂͒̌̍͘̚̕͘А̷̡̢̛̛̙͓̖̭̘͔͔̜̙̰̮̯̲͔̯̫̝̞̥̠͚͈̹̜̖͚̦͖̿͂̑̈́͐͂͐̂͐̑̀͐̂̊̊̀̍̊͊̿͋̉̌̀͂̋̋̃̊̒̓̎̇̔̋͜͝[/]", justify="center")
    console.print('[bright_cyan]--------------------------[/]', justify="center")
    console.print("[bright_red]——————--------------——————————-———————————[/]", justify="center")
    console.print("[white]Кто-то[/]", justify="center")
    console.print("[spring_green3]ЁПТА[/] [thistle3]- калькулятор[/]", justify="center")
    console.print("[spring_green3]ЁПТА[/] [bright_yellow]- генерация рандомного числа[/]", justify="center")
    console.print("[spring_green3]ЁПТА[/] [thistle3]- текущее время [/]", justify="center")
    console.print("[spring_green3]АНДРОИД[/] [white]- Ӥ̸̧̢̢̢̧̛̛͉̰̝̘̤̻̘̥̺͈̯̩̩͈͕͎͕̻͙̠̯̱̹͚́̃͗͌̍̆͆̍͋͗̄̓͛̃̏͊͑̓̍̐̔̆̽̍̒͊͛͌̇̿̑͊͐̍̆̏̏̎̓̈́̏͘͘̚̚͜͜͝͠͝И̵̡͖̥̣̦̝̯̙͇̖̭̪͖̩̱̣̯̹̫͔̻͍͍͈̼̺͙̣̟̭̯̟͈̘̠̯͉͔̯͙̗̬͎̹̮͖͌̈́͌̈̌̾̋̽̒͛͒̏͜͜͝ͅИ̴̖̥͍̼̼͇̽͒̾̔̈͆́̈́̆̀̄͛̓̈́̓̒̃͑̕͘͠͝͝И̵̩͈̮̪̗̰͕͍̲̳̣̬̣̙͍̝̟̦͈͔͎̝̥̼̫̖̤̮̣̱̲̰͇͔̫̦̮̺̰͐́́͜͝ͅИ̵̛̳͌͑̓͗̔͛̏̀̃̒͑̐̈́̚И̷̜̩̥͛̈̍̂̋́̈́͐̅͋̈́̿̅͒̊͋̒̎͂̀̕͝И̸̧̢̗̫̣̬̮̲̯̲̗̲̳̱̯̭̲̜͇͉̘̟̝͔̪̬̝̬̮̯̉͂͒̃͌̂̅͋́̕ͅͅͅͅИ̷̢̨̢̲̻̱̪͍̭͚̙̰̼̦͖͔̙̥̪̙̳̳̪͈͙̝͈͙̩̾̌̓̀̊͑̆̈͌̄̅̔̇͑͌̓͆̓͜͜͜͝И̴̛̮͈̪͓̱̼̌̈͆̀̍̈́̾͋̉͐̉͆̓͊̀̔̐̚͝П̵̢̡̨̨̩͈̼͓͈̻͚̩̞͇̳̘̪̳̰͇̗͈̽̈́̓͑̉͐̓͐͛́̽̾̂̈́̀̄̎̌̾̌̿̈́̔̌̓͌́͊̀̊͋͘͘̚͜͝͝Т̷̧̢̯̻͓̲̯͉̭̻͕͖̟̳̤̖̗̮͇̼̪̜̳̭͚̝̩̰̖̗̹̥̪͈̅͌̓̊̔̇̓̃̌̑̉̑̃̐͜͠ͅͅА̷̧̧̢̡͈͔̗̺̜̺͈̰̜̘̤̬̩̘̠̘̰̻̰̜̣͙͓̳̹͓̖̼͔͙͚̻̥͓̮͉̣͕̹̰̄́̅̀͑̿̄͗̈́̀͋͂̈͛̋̅̓̆̃̌̋͊̄̐͆̍̄̋̀̑̔́̄͑̒̀̑̍͒̄͘̕̚͘͜͜͠͝͝͝ͅА̵͖̮̳̐̊̍̅̇̏͆̓̀̉͊̂̂̐͒̌̈͊̔̍̍̆̄̉͊̎̎̊̏̔͛̆̔̋͋͗͋͑̚͘͠͝͝͝А̷̼̍́̽̽͌̆̿̌́̽̆̚͠А̷̡̨̡̨͎̺̣͈̞͉̯͕̜̦͕̯̩̟̹̞͔̤̮̺̩͕̪̥̦͈̬̪̺̻̥̩͚͇̱̘̝̣̳̩̮̒̍̒͑̾̽̋̋̈́͂͜͜ͅͅА̷̨̢̛̝̙̮͖̮̪͉̭͔̙̱͋͋͆̓́̑̍̀̈̉͗͛̐̓̐̉͠͝А̷͕͇̺̂́̇̿̽̂̊̀̋̐̈̃̕͝ͅ[/]", justify="center")
    console.print("[bright_red]АНДРОИД[/] [thistle3]- открыть сайт по URL адресу[/]", justify="center")
    console.print("[spring_green3]АНДРОИД[/] [white]- пошутить программе[/]", justify="center")
    console.print("[spring_green3]ДАРК[/] [bright_yellow]- оскорбить программу[/]", justify="center")
    console.print("[spring_green3]ДАРК[/] [thistle3]- включить режим хакера[/]", justify="center")
    console.print("[spring_green3]МАШИНА[/] [white]- Игра угадай число[/]", justify="center")
    console.print("[spring_green3]МАШИНА[/] [bright_yellow]- заблокировать[/]", justify="center")
    console.print("[spring_green3]Машина[/] [white]- аудио плеер[/]", justify="center")
    console.print("[bright_red]МАШИНААААААА[/] [thistle3]- сообщить об ошибке[/]", justify="center")                 
    console.print("[spring_green3]Й̵̟͉̰͋̆̌͌͗̇̽̅̍͂̆̅͝Й̴̧̫̰̫̗͈̳͓̫̯̟̲̹̦̹̩̝̞̭̥͓̖̭̪̯͓͉͕͖̖̘̖͖̭͙̟̞̟̃̃̔̓͐̈́̀̓̂̓̍̇̈͌̓̽̿̾́̚͠͠Й̸̡̛̛̬͖̟̦̱̰̤̙͎̜̣͚̺̺̙̜͉̐̾̏̔͛̑̊̋̀̀̂̎̔͆͌̀̈͗͛͋̀͌͋͂̎͌͋̍̅̀̃͘̕̕̕͝͠͝͝͠Й̶̧̨̧̢̧̡̨͍̤͕̟̣̪̲̳̠̙̙̲̞̗̖̪̫͉̠̪͉̟͙̞͉̝͖͔͙̝̜̘̈͊́͐̊̿̿̋͊͗̀̋̍̾͋͌̀̅͊́̔̈́̄̅́̌̐̃͘͜͝͠͝͝ͅͅͅͅЙ̵̨̧̨̺̜̠̥͈͓̳̺̠̻̤̹̣̼͇̩̪̖̪̹͈̟̪̲̬̺̬͉͖̪̲͕͈̤̥͈̮̬̝̻̾̐̄͑̽͌͛̈́̋̿̂͌̋̒̀̓͆̆͋͂̀͐̀͌͊̓͒͗̈̀̐̄̃͋̕̕͘̕͠͠͠͝Й̴̨̲̟̤̠͙̙̝̤̖͓̦͖̗͎̗͌̀͊̆̂͛̿́̇́̇͒̊͌͛́̀̉͜͜͜͝͝ͅЙ̷̛̛̛̦̘̙̥̰͙̩̠͍̳͖̦͙͕̩̼̮͔͛́̀͋̉̋̊̃̂̀̎̅̈́̈͐͗̏̉̂͑͆̂̐́͑̑́́̔̑͑̒̃̌͂̊̈́͘̚͘͠͠͝͝͠͝͝Й̵̛̛̠̜͙̤̜̙̹̬̤̳̻̬͔̩̬͈̼̬͔̠͖̜̫̗̯͍̲̗̭̼̉̀̀̇̈́̄͑̌͊̇̾͆͂͂̒͐͗̈́͊̾̋͒́͐́̓̌͗͑̑̂͐̊͆̍̕̕͝͝͝Й̴̡͍̜̠̏̿Й̷̡̢͉̲̦͚͇̝͔͎̣̹̳̥̥̾́͋̀̃́̒̽̄̋̔̋̕͜Й̷̧̢̯̺̹̞͕̳͔͈̼̮̹͉͖̼̯̞̥͔͎̠̪̜̯͍̞̞̙͕̱̱̰̩̫̦̟̼̩͊̽͊͊͌̆̀̔͑͜͜͝ͅЙ̵̨̢̨̢̹̖̭̫̬̰͔͇͎̯̙̫̜͍͇͍̝̖̭̲̝͎̫̘̳͇͉͔̜̘̀̔͛̿͘͘͜͜͠Й̵̛̛̤̥̦̰͔̝̻̤̗̳̠̰͚̼̓̐̆̓̀́̅̊̍̇̔̃̌̆̌̀͐͐̑̃̀̕̚̕̕͠͝ͅЙ̶̢̢̡̢̢̛̛͍͓̠̗̜̦̯͙͍͍̦̭̫̦̼̼̤̩̮͕͈͈̱̭̮̪̄̈́́͑͛̒̌̈́̃̽̅̏̏̉͐͗̒̃̈͑́̎̿́̆̽́͗͊̇͆̿̂̅̌̓͌́̀͆̀̀̚͜͝͝͝͝͝ͅЙ̸̱̙̯̝̞͙̻͓̜͈̹̯̩͕̙̫̇͋̋̇͋̒́͂́͒̾͊͒̉̀̀͛̈̀͋̑͗͊̾̿̎̍̆̈́͘̚̕̚͘͜͝͠͠͝͠͝Й̸̡̢̢̛̠̦͔̰͓̲͚͚̠͔͕̙̺̮̻̭͇̯̣̙̠̳̠͙̞̤̯͒̀͐̎̉͛͆̐̆͋́̈̀̏̒̑̈́̀́̋̃̽̋̀͒͂͆̓̄̆́̄́̎́̾̾͑̅͊̈́̇̅̾̈́̏̚̚[/] [white]- информация о системе[/]", justify="center") 
    console.print("[spring_green3]ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ[/] [thistle3]- блокнот[/]", justify="center")    
    console.print("[bright_red3]exit[/] [thistle3]- плахая каманда ваабщи[/]", justify="center")                                        
    console.print("[bright_cyan]---————[/bright_cyan]", justify="center")
    console.print("Taplik - Тапок", justify="center") 
    console.print("[bright_cyan]--[/bright_cyan]", justify="center")
    shiza_input_commands()


def login():
    os.system("cls||clear")
    logging.info("Система входа запущена")
    username_input = input("Введите имя пользователя ")
    if os.path.exists(f"users\\{username_input}.tapbin"):
        user_info = parse_user(f"users\\{username_input}.tapbin")
        if user_info["passwordenable"] == "False":
            if user_info["root"] == "False":
                if SETTINGS.enableNoRootUsers == True:
                    Info.username = username_input
                    print("Добро пожаловать!")
                    time.sleep(1)
                    menu()
                else:
                    os.system("cls||clear")
                    console.print("[red]Пользователи без root прав отключены![/]")
                    time.sleep(2)
                    login()  
            else:
                if SETTINGS.enableRootUsers == True:
                    Info.username = username_input
                    print("Добро пожаловать!")
                    time.sleep(1)
                    root_menu()
                else:
                    os.system("cls||clear")
                    console.print("[red]Root пользователи отключены![/]")
                    time.sleep(2)
                    login()  
        else:
            password = None
            if SETTINGS.hidePassword == True:
                password = hash(getpass.getpass("Введите пароль "))
            else:
                password = hash(input("Введите пароль "))
            if password == user_info["password"]:
                if user_info["root"] == "False":
                    if SETTINGS.enableNoRootUsers == True:
                        Info.username = username_input
                        print("Добро пожаловать!")
                        time.sleep(1)
                        menu()
                    else:
                        os.system("cls||clear")
                        console.print("[red]Пользователи без root прав отключены![/]")
                        time.sleep(2)
                        login()  
                else:
                    if SETTINGS.enableRootUsers == True:
                        Info.username = username_input
                        print("Добро пожаловать!")
                        time.sleep(1)
                        root_menu()  
                    else:
                        os.system("cls||clear")
                        console.print("[red]Root пользователи отключены![/]")
                        time.sleep(2)
                        login()  
            else:
                os.system("cls||clear")
                console.print("[red]Неверный пароль[/]")
                time.sleep(2)
                login()           
    else:
        os.system("cls||clear")
        console.print("[red]Пользователь не найден[/]")
        time.sleep(2)
        login()
def bottest():
    logging.info("Успешно запущена проверка на бота")
    bot_or_no = open("bottest.tapbin") 
    if bot_or_no.read() == "GfDfdODWFFCFDDVFFfGGO00%1":
        check1 = random.randint(1,9)
        check2 = random.randint(1,9)
        check3 = random.randint(1,9)
        check4 = random.randint(1,9)
        check5 = random.randint(1,9)
        code = str(check1) + str(check2) + str(check3) + str(check4) + str(check5)
        print(intToStr(check1) + intToStr(check2) + intToStr(check3) + intToStr(check4) + intToStr(check5))
        key = input("Введите код ")
        if key == code:
            logging.info("Введен верный код")
            with open('bottest.tapbin', 'a') as f:
                f.write('21')
            login()  
    bot_or_no2 = open("bottest.tapbin")        
    if bot_or_no2.read() == "GfDfdODWFFCFDDVFFfGGO00%121":  
        login()             
    else:
        RSOD_SYS.RSOD(STOP="DAMAGED_BOTTEST.TAPBIN", damaged_file="BOTTEST.TAPBIN", color="RED", RES_OR_NO="YES", RES_TYPE2="NO")





def sys_crash_or_no():
    logging.info("Сканирование запущено")
    if os.path.exists("installed.tapbin"):
        logging.info("Обнаружен файл installed.tapbin")
        if os.path.exists("bottest.tapbin"):
            fake_crash = random.randint(0,100)
            if fake_crash < 41:
                crash()
                logging.info("Ошибка запуска")
                exit()
            logging.info("Обнаружен файл bottest.tapbin")
            bottest()
        else:
            RSOD_SYS.RSOD(STOP="NO_FILE_BOTTEST.TAPBIN", damaged_file="bottest.tapbin", color="BLUE", RES_OR_NO="YES", RES_TYPE2="YES")
            logging.error("Файл bottest.tapbin не найден")
            logging.info("Успешно запущен BSOD")
    else:
        logging.info("Установка TaplikOs")
        print("C:/Taplik/System42/Modules/SETTINGS.py")
        time.sleep(1)
        print("C:/Taplik/System42/Modules/NUMBERS.py")
        time.sleep(1)
        print("C:/Taplik/System42/Modules/RSOD_SYS.py")
        time.sleep(1)
        print("C:/Taplik/System42/Modules/SYS_INFO.py")
        time.sleep(1)
        print("SYS_INFO.py Запускается")
        time.sleep(3)
        print("SYS_INFO.py Запущен")
        print("Выполняется проверка")
        time.sleep(1)
        sysinfo()
        print("Файл SYS_INFO.py успешно запущен и проверен")
        time.sleep(1)
        print("SETTINGS.py Запускается")
        time.sleep(3)
        print("SETTINGS.py Запущен")
        print("Выполняется проверка")
        time.sleep(1)
        print(SETTINGS.testMessage)
        print("Файл SETTINGS.py успешно запущен и проверен")
        time.sleep(1)
        print("RSOD_SYS.py Запускается")
        time.sleep(3)
        print("RSOD_SYS.py Запущен")
        print("Выполняется проверка")
        time.sleep(1)
        RSOD_SYS.test()
        print("Файл RSOD_SYS.py успешно запущен и проверен")
        time.sleep(1)
        print("NUMBERS.py Запускается")
        time.sleep(3)
        print("NUMBERS.py Запущен")
        print("Выполняется проверка")
        time.sleep(1)
        print(NUMBERS.n1 + NUMBERS.n2 + NUMBERS.n3)
        print("Файл SETTINGS.py успешно запущен и проверен")
        time.sleep(2)
        os.system("cls||clear")
        time.sleep(2)
        fakeinstall("[white]Выполняется установка TaplikOs... \n Компьютер перезагрузится несколько раз[/]", inttime=5)
        fakeinstall("[white]Копирование файлов[/]", inttime=5)
        fakeinstall("[white]Подготовка файлов для установки[/]", inttime=5)
        fakeinstall("[white]Установка компонентов[/]", inttime=5)
        random_rsod = random.randint(0,100)
        if random_rsod < 11:
            RSOD_SYS.RSOD(STOP="FAILED_SYSTEM_REBOOT", damaged_file="install.tapbin", color="RED", RES_OR_NO="NO", RES_TYPE2="NO")
            time.sleep(5)
            if platform.system() == "Windows":
                os.system("color 07")
                os.system("title taplik_os")
        os.system("cls||clear")
        fakeinstall("[white]Установка обновлений[/]", inttime=3)
        def rootuser():
            os.system("cls||clear")
            username = input("Придумайте имя root пользователю ")
            os.system("cls||clear")
            rootpassword = hash(input("Придумайте пароль root пользователю "))
            os.system("cls||clear")
            rootpassword2 = hash(input("Повторите пароль root пользователя "))
            if rootpassword2 != rootpassword:
                os.system("cls||clear")
                console.print("[red]Пароли не совпадают[/]")
                time.sleep(2)
                rootuser()
            text = f"""password {rootpassword}
passwordenable True
root True"""
            with open(f"users\\{username}.tapbin", "w") as file:
                file.write(text)  
            logging.info("Создан root пользователь")
        rootuser()  
        os.system("cls||clear")
        installed = open("installed.tapbin", "w+")
        installed.write("123")
        installed.close()
        sys_crash_or_no()


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    logging.info("Запуск сканирования системы")
    sys_crash_or_no()
