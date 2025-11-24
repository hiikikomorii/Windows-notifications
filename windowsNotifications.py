import ctypes
from colorama import Fore, init, Style
import os
import time
import threading

init(autoreset=True)


def logo():
    ascii_art = """
                                                                ▀██▀  ▀██▀  ██      ▀██  ▀██                         █▀▀██▀▀█                 ▀██         
                                                                 ██    ██  ▄▄▄    ▄▄ ██   ██    ▄▄▄   ▄▄▄ ▄▄▄ ▄▄▄       ██      ▄▄▄     ▄▄▄    ██   ▄▄▄▄  
                                                                 ██▀▀▀▀██   ██  ▄▀  ▀██   ██  ▄█  ▀█▄  ██  ██  █        ██    ▄█  ▀█▄ ▄█  ▀█▄  ██  ██▄ ▀  
                                                                 ██    ██   ██  █▄   ██   ██  ██   ██   ███ ███         ██    ██   ██ ██   ██  ██  ▄ ▀█▄▄ 
                                                                ▄██▄  ▄██▄ ▄██▄ ▀█▄▄▀██▄ ▄██▄  ▀█▄▄█▀    █   █         ▄██▄    ▀█▄▄█▀  ▀█▄▄█▀ ▄██▄ █▀▄▄█▀
    """
    def print_cyan_to_darkblue(asciii_art):
        lines = asciii_art.split("\n")
        total_lines = len(lines)

        for i, line in enumerate(lines):
            g = int(255 - (i / max(total_lines - 1, 1)) * 255)
            b = int(255 - (i / max(total_lines - 1, 1)) * (255 - 139))
            print(f"\033[38;2;0;{g};{b}m{line}\033[0m")

    print_cyan_to_darkblue(ascii_art)

def logo_text():
    print(f"""
                                                                                                       {Fore.CYAN}1{Fore.RESET} - {Fore.LIGHTCYAN_EX}Create   {Fore.CYAN}2{Fore.RESET} - {Fore.LIGHTCYAN_EX}help

                                                                                                              {Fore.RED}3{Fore.RESET} - {Fore.LIGHTRED_EX}Exit{Fore.RESET}

            """)

def clear_cmd():
    os.system('cls')
    time.sleep(0.02)
    logo()
    logo_text()

def exit_cmd():
    exit()

def help_info():
    print(f"""{Style.BRIGHT}
[title][icon][text]
пример: {Fore.BLUE}window {Fore.RED}error {Fore.GREEN}hidlowtext
доступные иконки:
{Fore.RED}error
{Fore.BLUE}info
{Fore.YELLOW}warning
{Fore.LIGHTBLUE_EX}question\n
чтобы выйти из меню создания введите '{Fore.RED}exit{Fore.RESET}'
""")
    input(f"{Fore.BLUE}> ")
    clear_cmd()
    time.sleep(0.05)
    logo()
    logo_text()

def show_messagebox(text, title, icon):
    ctypes.windll.user32.MessageBoxW(0, text, title, icon)

def create_notify():
    notify_icons = {
        "info": 0x40,  # Информация
        "warning": 0x30,  # Внимание
        "error": 0x10,  # Ошибка
        "question": 0x20  # Вопрос
    }

    while True:
        usercreate = input("enter the data:")
        parts = usercreate.split(maxsplit=2)

        if not parts:
            print(f"{Fore.YELLOW}введите что-то\n")
            continue

        if len(parts) > 3:
            print("неправильный тип данных, попробуйте снова\n")

        if usercreate == "exit":
            clear_cmd()
            time.sleep(0.05)
            logo()
            logo_text()
            break


        try:
            title = parts[0]
            icon_type = parts[1].lower()
            text = parts[2]

            icon_code = notify_icons.get(icon_type)

            print(f"{Fore.BLUE}{Style.BRIGHT}[CTYPES]{Style.NORMAL} {Fore.GREEN}Notification was shown{Style.RESET_ALL}\n")
            threading.Thread(target=show_messagebox, args=(text, title, icon_code)).start()

        except Exception:
            print(f"{Fore.RED}Введите правильный тип данных\n")

def main_menu():
    commands = {
        "clear": clear_cmd,
        "1": create_notify,
        "2": help_info,
        "3": exit_cmd,
        "exit": exit_cmd
    }

    while True:
        cmd = input(f"{Fore.BLUE}choice number: {Style.RESET_ALL}").strip()
        if not cmd:
            pass
        if cmd:
            try:
                commands[cmd]()
            except Exception:
                print(f"{Fore.RED}[ERROR] {Fore.LIGHTRED_EX}номер функции не найден")
        else:
            pass


if __name__ == '__main__':
    logo()
    logo_text()
    main_menu()