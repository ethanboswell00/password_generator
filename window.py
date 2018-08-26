import tkinter as tk
import random

# Almost all of the code is contained within this module.
class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.title = "Password Generator"
        self.root.title(self.title)

        self.num = 0
        self.check_pressed = False
        self.password = None

        self.width = width
        self.height = height

        self.main_frame = tk.Frame(width=self.width, height=self.height, bd=1, relief=tk.SUNKEN)

        self.user_label = tk.Label(self.main_frame, text="How many characters long do you want your password to be?")

        self.user_input = tk.Entry(self.main_frame, width=25)

        self.submit_button = tk.Button(self.main_frame, text="Submit", width=25, command=self.submit_handle)

        self.output_box = tk.Text(self.main_frame, height=2, width=30)

        self.quit_button = tk.Button(self.root, text="Quit", width=25, command=self.root.destroy)

    def setup_gui(self):
        self.main_frame.pack(fill=tk.X, padx=5, pady=5)
        self.output_box.pack(side=tk.BOTTOM)
        self.submit_button.pack(side=tk.BOTTOM)
        self.quit_button.pack(side=tk.RIGHT)
        self.user_label.pack()
        self.user_input.pack()

    def submit_handle(self):
        self.check_pressed = True
        self.num = int(self.user_input.get())

        self.password = self.set_string()
        self.output_box.delete('1.0', tk.END)
        self.output_box.insert(tk.END, self.password)

    def set_string(self):
        self.password = ""

        for i in range(self.num):
            ascii_id = random.randint(33, 125)
            self.password += chr(ascii_id)

        return self.password

    def looper(self):
        self.root.mainloop()
