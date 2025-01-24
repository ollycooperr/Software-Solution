from tkinter import *
import init

class loginoptions:
    def __init__(self):
        self.win = Tk()
        self.win.title("Login Options")
        self.win.geometry("1920x1080")
        self.win.configure(bg="#6495ed")
        self.lbl_title = Label(text="Edusoft Math Quiz",font=("Comic Sans MS",72,"bold"),fg="#ffffff",bg="#6495ed")
        self.lbl_title.pack(pady=30)
        self.btn_teacher = Button(self.win,text="Teacher",font=("Calibri",40,"bold"),fg="#ffffff",width=10,bg="#191970",command=self.t_option)
        self.btn_teacher.pack(pady=30)
        self.btn_student = Button(self.win,text="Student",font=("Calibri",40,"bold"),fg="#ffffff",width=10,bg="#191970")
        self.btn_student.pack()

        self.win.mainloop()

    def t_option(self):
        self.win.destroy()
        init.teacherlogin()
        
if __name__ == "__main__":
    loginoptions()

def teacher_login_panel():
    win = Tk()  
    win.title("Teacher login panel")
    win.geometry("1920x1080")
    win.configure(bg="#6495ed")
    win.lbl_title = Label(win,text="Teacher Login",font=("Calibri",60,"bold"),fg="#ffffff",bg="#6495ed")
    win.lbl_title.pack()
    win.lbl_username = Label(win,text="Enter Username: ",font=("Calibri",30,"bold"),fg="#191970",bg="#6495ed")
    win.lbl_username.pack()
    win.ent_username = Entry(win,width=40)
    win.ent_username.pack()

    win.lbl_password = Label(win,text="Enter Password: ",font=("Calibri",30,"bold"),fg="#191970",bg="#6495ed")
    win.ent_password = Entry(win,width=40)
    win.lbl_password.pack()
    win.ent_password.pack()

    win.btn_login = Button(win,text="Confirm Login",font=("Calibri",20,"bold"),fg="#ffffff",bg="#191970",width=20)
    win.btn_login.pack(pady=10)
    win.btn_goback = Button(win,text="Go Back",font=("Calibri",20,"bold"),fg="#ffffff",bg="#191970",width=20)
    win.btn_goback.pack()

    




    win.mainloop()