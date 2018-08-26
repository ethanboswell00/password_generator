#© 2018 Ethan Boswell Coding LLC

from window import Window

def main():
    main_window = Window(600, 600)
    main_window.setup_gui()

    main_window.looper()

main()
