from tkinter import *
import init
class TeacherPanel:
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

        self.win.btn_login = Button(self.win,text="Confirm Login",font=("Calibri",20,"bold"),fg="#ffffff",bg="#191970",width=20)
        self.win.btn_login.pack(pady=10)
        self.win.btn_goback = Button(self.win,text="Go Back",font=("Calibri",20,"bold"),fg="#ffffff",bg="#191970",width=20,command=self.nav_to_login)
        self.win.btn_goback.pack()
    

        self.win.mainloop()

    def nav_to_login(self):
        self.win.destroy()
        self.master.deiconify()





class LoginOptions:
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
#    def navigate_to_panel(self, role):
 #       if role == "teacher":
  #          teacher_panel = TeacherPanel()
   #         self.win.destroy()
    #    elif role == "student":
     #       #student_panel = StudentPanel()
      #      print("student panel not implemented yet")
       #     self.win.destroy()
    def navigate_to_teacher(self):
        self.win.withdraw()
        TeacherPanel(self.win)

    def navigate_to_student(self):
        print("prg stu not implented") 















if __name__ == "__main__":
    app = LoginOptions()
    mainloop()

