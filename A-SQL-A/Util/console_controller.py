import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_welcome():
    large_text = [
        "██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗",
        "██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝",
        "██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ",
        "██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ",
        "╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗",
        " ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝"
    ]

    for line in large_text:
        print(line)


def print_see_you_again():
    see_you_again_text = [
        " ██████╗███████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗     █████╗  ██████╗  █████╗ ██╗███╗   ██╗",
        "██╔════╝██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔════╝ ██╔══██╗██║████╗  ██║",
        "███████╗█████╗  █████╗       ╚████╔╝ ██║   ██║██║   ██║    ███████║██║  ███╗███████║██║██╔██╗ ██║",
        "╚════██║██╔══╝  ██╔══╝        ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██║   ██║██╔══██║██║██║╚██╗██║",
        "███████║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝    ██║  ██║╚██████╔╝██║  ██║██║██║ ╚████║",
        "╚══════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝"
    ]

    for line in see_you_again_text:
        print(line)