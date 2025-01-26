from tkinter import *
from tkinter import messagebox
import init


class TeacherPanel: #TeacherPanel designed for teachers to access their panel and login
    def __init__(self,master):
        self.master = master
        self.win = Toplevel(master)  
        self.win.title("Teacher login panel")
        self.win.geometry("1920x1080")
        self.win.configure(bg="#6495ed")
        self.win.lbl_title = Label(self.win,text="Teacher Login",font=("Calibri",60,"bold"),fg="#ffffff",bg="#6495ed")
        self.win.lbl_title.pack()
        self.win.lbl_username = Label(self.win,text="Enter Username: ",font=("Calibri",30,"bold"),fg="#191970",bg="#6495ed")
        self.win.lbl_username.pack()
        self.win.ent_username = Entry(self.win,width=40)
        self.win.ent_username.pack()

        self.win.lbl_password = Label(self.win,text="Enter Password: ",font=("Calibri",30,"bold"),fg="#191970",bg="#6495ed")
        self.win.ent_password = Entry(self.win,width=40)
        self.win.lbl_password.pack()
        self.win.ent_password.pack()

        self.win.btn_login = Button(self.win,text="Confirm Login",font=("Calibri",20,"bold"),fg="#ffffff",bg="#191970",width=20,command=self.do_attempt_login)
        self.win.btn_login.pack(pady=10)
        self.win.btn_goback = Button(self.win,text="Go Back",font=("Calibri",20,"bold"),fg="#ffffff",bg="#191970",width=20,command=self.nav_to_options)
        self.win.btn_goback.pack()
    

        self.win.mainloop()

    def do_attempt_login(self):
        username = self.win.ent_username.get()
        password = self.win.ent_password.get()
        if username != "":
            pass_username = init.teacher_login_validation(username,password)
        else:
            messagebox.showerror("Username","Cannot leave username blank")
            self.win.ent_username.delete(0,END) #clear data to ensure fluidity

            


    def nav_to_options(self): #navigates to LoginOptions and closes TeacherPanel window
        self.win.destroy()
        self.master.deiconify()

class StudentPanel: #StudentPanel for students to enter their name and class to access their quizzes etc
    def __init__(self,master):
        self.master = master
        self.win = Toplevel(master)  
        self.win.title("Student Login Panel")
        self.win.geometry("1920x1080")
        self.win.configure(bg="#6495ed")
        self.win.lbl_title = Label(self.win,text="Student Login",font=("Comic Sans MS",60,"bold"),fg="#ffffff",bg="#6495ed")
        self.win.lbl_title.pack()
        self.win.lbl_username = Label(self.win,text="Enter Username: ",font=("Comic Sans MS",30,"bold"),fg="#191970",bg="#6495ed")
        self.win.lbl_username.pack()
        self.win.ent_username = Entry(self.win,width=40)
        self.win.ent_username.pack()

        self.win.lbl_tutorgroup = Label(self.win,text="Enter Password: ",font=("Comic Sans MS",30,"bold"),fg="#191970",bg="#6495ed")
        self.win.ent_tutorgroup = Entry(self.win,width=40)
        self.win.lbl_tutorgroup.pack()
        self.win.ent_tutorgroup.pack()

        self.win.btn_login = Button(self.win,text="Confirm Login",font=("Comic Sans MS",20,"bold"),fg="#ffffff",bg="#191970",width=20)
        self.win.btn_login.pack(pady=10)
        self.win.btn_goback = Button(self.win,text="Go Back",font=("Comic Sans MS",20,"bold"),fg="#ffffff",bg="#191970",width=20,command=self.nav_to_options)
        self.win.btn_goback.pack()
    

        self.win.mainloop()

    def nav_to_options(self): #navigates to the LoginOptions and closes the StudentPanel window
        self.win.destroy()
        self.master.deiconify()


class LoginOptions: #LoginOptions is the main GUI showing student or teacher options on startup
    def __init__(self):
        self.win = Tk()
        self.win.title("Login Options")
        self.win.geometry("1920x1080")
        self.win.configure(bg="#6495ed")
        self.lbl_title = Label(text="Edusoft Math Quiz",font=("Comic Sans MS",72,"bold"),fg="#ffffff",bg="#6495ed")
        self.lbl_title.pack(pady=30)
        self.btn_teacher = Button(self.win,text="Teacher",font=("Calibri",40,"bold"),fg="#ffffff",width=10,bg="#191970",command=self.navigate_to_teacher)
        self.btn_teacher.pack(pady=30)
        self.btn_student = Button(self.win,text="Student",font=("Calibri",40,"bold"),fg="#ffffff",width=10,bg="#191970",command=self.navigate_to_student)
        self.btn_student.pack()
    
        self.win.mainloop()

    def navigate_to_teacher(self): #Navigates to teacher login panel
        self.win.withdraw()
        TeacherPanel(self.win)

    def navigate_to_student(self): #navigates to student login panel
        self.win.withdraw()
        StudentPanel(self.win)

#start the program at LoginOptions
if __name__ == "__main__":
    app = LoginOptions()
