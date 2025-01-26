from tkinter import messagebox
from tkinter import *
import gui
import os
import csv

#def teacherlogin(username, password):
 #   if username == "user" and password == "password":
  #      print("PRG: login opt success")
   #     return True
    #else:
     #   return False

#    def navigate_to_panel(self, role):
 #       if role == "teacher":
  #          teacher_panel = TeacherPanel()
   #         self.win.destroy()
    #    elif role == "student":
     #       #student_panel = StudentPanel()
      #      print("student panel not implemented yet")
       #     self.win.destroy()

#get entered username and get entered password
#check username validation, if matches a username, return true then check password validation, if return true,
# then return true to login proces in gui 
# if return false, send false to gui & create error message corrosponding to the problem


def teacher_login_validation(username,password): #finds teachers username and checks to see if they match
    #print("HELLO >>", os.getcwd())
    
    with open("..\\data\\teacher_data.txt","r") as teacherdata:
        line = teacherdata.readline()
        found = False
        while line != "" and not found:
            line = line.replace("\n","")
            record = line.split(",")
            if username == record[0] and password == record[1]:
                found = True
                messagebox.showinfo("success","words")
            line = teacherdata.readline()

        if found == False:
            messagebox.showerror("Login Error","There was a problem logging in.\nPlease check entries and try again.")



