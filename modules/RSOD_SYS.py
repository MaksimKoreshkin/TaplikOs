import os
import time
import platform
from rich.console import Console 
console = Console(highlight=False)

def RSOD_RESTORATION_OR_NO2():
    print("---------------------------------------------------------")
    print("Что вы хотите сделать?")
    print("---------------------------------------------------------")
    print("exit - выйти")
    print("res - выполнить востоновление")
    print("---------------------------------------------------------")
    command = input()
    if command == "exit":
        exit()
    elif command == "res":
        print("Запуск системы востоновления...")   
        time.sleep(2)
        print("Востоновление...")
        with open('bottest.tapbin', 'a') as f:
            f.write('GfDfdODWFFCFDDVFFfGGO00%1')
        print("Востоновление завершено. Пожалуйста перезапустите taplik.")
        a = input()
        
def RSOD_RESTORATION_OR_NO():
    print("---------------------------------------------------------")
    print("Что вы хотите сделать?")
    print("---------------------------------------------------------")
    print("exit - выйти")
    print("res - выполнить востоновление")
    print("---------------------------------------------------------")
    command = input()
    if command == "exit":
        exit()
    elif command == "res":
        print("Запуск системы востоновления...")   
        time.sleep(2) 
        bottest_problem = "no"
        print("Поиск проблем...")
        file_bottest = open("bottest.tapbin")
        if file_bottest.read() != "GfDfdODWFFCFDDVFFfGGO00%121" or "GfDfdODWFFCFDDVFFfGGO00%1":
            bottest_problem = "yes"
        if bottest_problem == "yes":
            print("Обнаружена проблема с файлом bottest.txt")  
            print("Восстановление...") 
            with open('bottest.tapbin', 'wb'):
                pass
            test=open('bottest.tapbin', 'a')
            test.write('GfDfdODWFFCFDDVFFfGGO00%1')
            test.close() 
            time.sleep(2)
            print("Восстановление завершено, пожалуйста перезапустите taplik")
            a = input()
def RSOD(STOP, damaged_file, color, RES_OR_NO, RES_TYPE2):
    os.system("cls||clear")
    if platform.system() == "Windows":
        if color == "RED":
            os.system("color 40")
            os.system("title taplik_os - RSOD")
            console.print("[white]SYSTEM CRASHED[/white]", justify="center")  
            console.print("[white]Произошла ошибка и вы больше не можете пользоваться taplik_os :([/white]", justify="center")
            console.print("[white]Damaged files:[/white]", justify="center")
            console.print("[white]" + damaged_file + "[/white]", justify="center")
            console.print("[white]STOP_CODE: " + STOP + "[/white]", justify="center")        
        elif color == "BLUE":
            os.system("color 90")
            os.system("title taplik_os - BSOD")
            console.print("[red]SYSTEM CRASHED[/red]", justify="center")  
            console.print("[red]Произошла ошибка и вы больше не можете пользоваться taplik_os :([/red]", justify="center")
            console.print("[red]Damaged files:[/red]", justify="center")
            console.print("[red]" + damaged_file + "[/red]", justify="center")
            console.print("[red]STOP_CODE: " + STOP + "[/red]", justify="center") 
        elif color == "MAGIC":
            console.print("[white]SYSTEM CRASHED[/white]", justify="center")  
            console.print("[white]Произошла ошибка и вы больше не можете пользоваться taplik_os :([/white]", justify="center")
            console.print("[white]Damaged files:[/white]", justify="center")
            console.print("[white]" + damaged_file + "[/white]", justify="center")
            console.print("[white]STOP_CODE: " + STOP + "[/white]", justify="center") 
            while True:
                os.system("color 40")  
                os.system("title taplik_os - RSOD")  
                time.sleep(0.4)
                os.system("color 90")
                os.system("title taplik_os - BSOD")
                time.sleep(0.4)
                os.system("color 20") 
                os.system("title taplik_os - GSOD")
                time.sleep(0.4)
        else:
            os.system("color 40")
            os.system("title taplik_os - RSOD")
            console.print("[white]SYSTEM CRASHED[/white]", justify="center")  
            console.print("[white]Произошла ошибка и вы больше не можете пользоваться taplik_os :([/white]", justify="center")
            console.print("[white]Damaged files:[/white]", justify="center")
            console.print("[white]" + damaged_file + "[/white]", justify="center")
            console.print("[white]STOP_CODE: " + STOP + "[/white]", justify="center")   
    else:
        console.print("[white]SYSTEM CRASHED[/white]", justify="center")  
        console.print("[white]Произошла ошибка и вы больше не можете пользоваться taplik_os :([/white]", justify="center")
        console.print("[white]Damaged files:[/white]", justify="center")
        console.print("[white]" + damaged_file + "[/white]", justify="center")
        console.print("[white]STOP_CODE: " + STOP + "[/white]", justify="center") 
    if RES_OR_NO == "NO":
        a = input()
    elif RES_OR_NO == "YES": 
        if RES_TYPE2 == "YES":  
            RSOD_RESTORATION_OR_NO2()
        elif RES_TYPE2 == "NO":
            RSOD_RESTORATION_OR_NO()    

def test():
    print("[RSOD_SYS]: Yes")