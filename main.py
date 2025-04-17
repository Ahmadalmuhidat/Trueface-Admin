import os
import sys
import customtkinter
import threading

from app.config.configrations import Configrations

import app.views.students.students as Students
import app.views.classes.classes as Classes
import app.views.courses.courses as Courses
import app.views.users.users as Users
import app.views.login.login as Login

class Main():
  def __init__(self):
    try:
      super().__init__()

      self.config = Configrations()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def Navbar(self, window):
    try:
      navbar = customtkinter.CTkFrame(window)
      navbar.pack(fill=customtkinter.X)

      StudentsButton = customtkinter.CTkButton(
        navbar,
        corner_radius = 0,
        command = lambda: self.config.router.navigate(Students.Students, self.window),
        text = "Students"
      )
      StudentsButton.pack(side=customtkinter.LEFT)

      ClassesButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda:  self.config.router.navigate(Classes.Classes, self.window),
        text="Classes"
      )
      ClassesButton.pack(side=customtkinter.LEFT)

      CoursesButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda:  self.config.router.navigate(Courses.Courses, self.window),
        text="Courses"
      )
      CoursesButton.pack(side=customtkinter.LEFT)

      UsersButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda:  self.config.router.navigate(Users.Users, self.window),
        text="Users"
      )
      UsersButton.pack(side=customtkinter.LEFT)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def WhenAppClose(self):
    try:
      self.window.destroy()

      threadsToTerminate = [
        thread for thread in 
          threading.enumerate() if
            thread.ident != threading.get_ident()
      ]

      for thread in threadsToTerminate:
        if thread.is_alive():
          thread.join(timeout=1)

    except Exception as e:
        ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
        FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
        print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
        print(ExceptionObject)
    finally:
        sys.exit(0)

  def StartTheProgram(self):
    try:
      customtkinter.set_appearance_mode("dark")

      self.window = customtkinter.CTk()
      width= self.window.winfo_screenwidth()
      height= self.window.winfo_screenheight()
      self.window.geometry("%dx%d" % (width, height))
      self.window.title("TrueFace Admin")
      # self.window.iconbitmap("logo.ico")

      self.window.protocol("WM_DELETE_WINDOW", self.WhenAppClose)

      self.Navbar(self.window)
      self.config.router.navigate(Students.Students, self.window)

      self.window.mainloop()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  Main().StartTheProgram()
  # login = Login.Login().create()
