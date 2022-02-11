from os import system
from time import sleep


def exec():
    while True:
        system('python3 -m unittest tests.Wallpaper.PaperTest')
        sleep(60 * 30)


if __name__ == '__main__':
    exec()
