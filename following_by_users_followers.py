import tkinter as tk
from tkinter import messagebox
from instapy import InstaPy


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.title_label = tk.Label(self, text='following by a users followers')
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

        #friend1 field
        self.friend1_label = tk.Label(self, text="Enter friend1:",
                                 background="tomato")
        self.friend1_label.pack()
        friend1 = tk.StringVar()
        self.friend1_entry = tk.Entry(self, textvariable=friend1)
        self.friend1_entry.pack()

        # friend2 field
        self.friend2_label = tk.Label(self, text="Enter friend2:",
                                      background="tomato")
        self.friend2_label.pack()
        friend2 = tk.StringVar()
        self.friend2_entry = tk.Entry(self, textvariable=friend2)
        self.friend2_entry.pack()

        # friend3 field
        self.friend3_label = tk.Label(self, text="Enter friend3:",
                                      background="tomato")
        self.friend3_label.pack()
        friend3 = tk.StringVar()
        self.friend3_entry = tk.Entry(self, textvariable=friend3)
        self.friend3_entry.pack()

        #start button
        def startBot():
            messagebox.showinfo("Starting following by a users followers:)", loginInsta.get() + " " + passwordInsta.get())
            session = InstaPy(username=loginInsta.get(),
                              password=passwordInsta.get(),
                              headless_browser=False).login()
            session.set_user_interact(amount=3,
                                      randomize=True,
                                      percentage=100,
                                      media='Photo')
            session.follow_user_followers([friend1.get(), friend2.get(), friend3.get()],
                                          amount=50,
                                          interact=True)
            session.login()

        self.start_button = tk.Button(self, text="Start",
                                 command=startBot,
                                 background="cyan2")
        self.start_button.pack()

        self.pack()

