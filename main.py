import tkinter as tk

class atmCec(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('1024x600')
        tk.Tk.wm_title(self, 'Attendance Monitoring System CeC')
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, DashPage, ManagePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        headerColorlabel = tk.Label(self, bg='#1B1464', height=5, width=600)
        headerColorlabel.place(relx=.0,rely=.0)

        headerColorUnderlabel = tk.Label(self, bg='#F7941D', height=1, width=600)
        headerColorUnderlabel.place(relx=.0,rely=.144)

        headerCenterLabel = tk.Label(self, text='Cristal e-College', fg='#FFFFFF', bg='#1B1464')
        headerCenterLabel.config(font='TkHeadingFont, 50')
        headerCenterLabel.place(relx=.325,rely=.025)

        headingCenterlabel = tk.Label(self, text='Please scan your rfid')
        headingCenterlabel.config(font='TkHeadingFont, 80')
        headingCenterlabel.place(relx=.15,rely=.4)

        footerColorlabel = tk.Label(self, bg='#1B1464', height=5, width=600)
        footerColorlabel.place(relx=.0,rely=.856)

        button = tk.Button(self, text="Visit Page 1", bg='#1B1464',
                            command=lambda: controller.show_frame(DashPage))
        button.place(relx=.0,rely=.3)

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(ManagePage))
        button2.place(relx=.0,rely=.2)


class DashPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        headerColorlabel = tk.Label(self, bg='#1B1464', height=5, width=600)
        headerColorlabel.place(relx=.0,rely=.0)

        headerColorUnderlabel = tk.Label(self, bg='#F7941D', height=1, width=600)
        headerColorUnderlabel.place(relx=.0,rely=.144) 

        footerColorlabel = tk.Label(self, bg='#1B1464', height=5, width=600)
        footerColorlabel.place(relx=.0,rely=.856)


        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(relx=.0,rely=.4)

        button_dash = tk.Button(self, text="Dashboard", height='3', width='10',
                            command=lambda: controller.show_frame(DashPage))
        button_dash.place(relx=.2,rely=.025)

        button_manage = tk.Button(self, text="Manage \nAccounts", height='3', width='10',
                            command=lambda: controller.show_frame(ManagePage))
        button_manage.place(relx=.325,rely=.025)

        button_fines = tk.Button(self, text="Student \nFines", height='3', width='10',
                            command=lambda: controller.show_frame())
        button_fines.place(relx=.45,rely=.025)

        button_archive = tk.Button(self, text="Archive \nEvents", height='3', width='10',
                            command=lambda: controller.show_frame())
        button_archive.place(relx=.575,rely=.025)


class ManagePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        headerColorlabel = tk.Label(self, bg='#1B1464', height=5, width=600)
        headerColorlabel.place(relx=.0,rely=.0)

        headerColorUnderlabel = tk.Label(self, bg='#F7941D', height=1, width=600)
        headerColorUnderlabel.place(relx=.0,rely=.144) 

        footerColorlabel = tk.Label(self, bg='#1B1464', height=5, width=600)
        footerColorlabel.place(relx=.0,rely=.856)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(relx=.0,rely=.4)

        button_dash = tk.Button(self, text="Dashboard", height='3', width='10',
                            command=lambda: controller.show_frame(DashPage))
        button_dash.place(relx=.2,rely=.025)

        button_manage = tk.Button(self, text="Manage \nAccounts", height='3', width='10',
                            command=lambda: controller.show_frame(ManagePage))
        button_manage.place(relx=.325,rely=.025)

        button_fines = tk.Button(self, text="Student \nFines", height='3', width='10',
                            command=lambda: controller.show_frame())
        button_fines.place(relx=.45,rely=.025)

        button_archive = tk.Button(self, text="Archive \nEvents", height='3', width='10',
                            command=lambda: controller.show_frame())
        button_archive.place(relx=.575,rely=.025)
        

if __name__ == '__main__':
    app = atmCec()
    app.mainloop()