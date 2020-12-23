import tkinter as tk
from tkinter import messagebox
from instapy import InstaPy


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.title_label = tk.Label(self, text='liking by a feed')
        self.title_label.pack()

        #login field
        self.loginInsta_label = tk.Label(self, text="Enter your Insta login:",
                                         background="purple1")
        self.loginInsta_label.pack()

        loginInsta = tk.StringVar()

        self.loginInsta_entry = tk.Entry(self, textvariable=loginInsta)
        self.loginInsta_entry.pack()

        #password field
        self.passwordInsta_label = tk.Label(self, text="Enter your Insta password:",
                                       background="SlateBlue3")
        self.passwordInsta_label.pack()
        passwordInsta = tk.StringVar()
        self.passwordInsta_entry = tk.Entry(self, textvariable=passwordInsta)
        self.passwordInsta_entry.pack()



        #start button
        def startBot():
            messagebox.showinfo("Starting liking by a feed)", loginInsta.get() + " " + passwordInsta.get())
            session = InstaPy(username=loginInsta.get(),
                              password=passwordInsta.get(),
                              headless_browser=False).login()
            session.set_user_interact(amount=3,
                                      randomize=True,
                                      percentage=100,
                                      media='Photo')
            session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)
            session.login()

        self.start_button = tk.Button(self, text="Start",
                                 command=startBot,
                                 background="cyan2")
        self.start_button.pack()

        self.pack()

