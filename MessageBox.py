import tkinter as tk
import random

AutoCount = 0
Classes = []

class MessageBox:

    def __init__(self, master, Title, Description, Unit):

        Classes.append(self)

        self.Count = Unit

        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title(Title)
        self.master.geometry(f"200x100+{random.randint(100, self.master.winfo_screenwidth() - 100)}+{random.randint(100, self.master.winfo_screenheight() - 100)}")
        self.master.resizable(False, False)

        self.text = tk.Label(self.frame, text=Title)
        self.text.pack()

        self.text = tk.Label(self.frame, text=Description, height=3)
        self.text.pack()

        self.button1 = tk.Button(self.frame, text = 'Ok', width = 25, height=2, command= lambda: [self.CheckForAns()])
        self.button1.pack()

        self.frame.pack()

        self.master.configure(bg='White')
        self.master.overrideredirect(1)
        self.master.protocol("WM_DELETE_WINDOW", lambda x : [print("lol not that ez")])
        self.master.mainloop()

    def CheckForAns(self):
        global AutoCount
        if self.Count == AutoCount:
            AutoCount += 1
            self.master.configure(bg='GREEN')
            if AutoCount >= len(Classes):
                raise SystemExit("you win")
        else:
            AutoCount = 0
            for _Class in Classes:
                _Class.master.configure(bg='White')
            print("you screwed up!")


if __name__ == "__main__":
    box = MessageBox(tk.Toplevel(), "Less go", "brr", 0)
