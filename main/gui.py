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
        print ("b")
        self.win.destroy()
        init.teacherlogin()
        
if __name__ == "__main__":
    loginoptions()

def teacher_login_panel():
    win = Tk()  
    win.title("Teacher login panel")
    win.geometry("1920x1080")
    win.configure(bg="#6495ed")
    win.lbl_title = Label(text="Teacher Login",font=("Calibri",60,"bold"),fg="#ffffff",bg="#6495ed")
    win.lbl_title.pack(pady=30)


    win.mainloop()