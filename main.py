import os
import sys
import customtkinter
import threading

from Configrations import Configrations

import Views.Students.Students as Students
import Views.Classes.Classes as Classes
import Views.Courses.Courses as Courses
import Views.Users.Users as Users
import Login as Login

class Router:
  CurrentWindow = None
  CurrentFrame = None
  
  def setWindow(self, window):
    Router.CurrentWindow = window

  def navigate(self, ViewObject):
    try:
      if Router.CurrentFrame:
        Router.CurrentFrame.pack_forget()

      Router.CurrentFrame = customtkinter.CTkFrame(Router.CurrentWindow)
      ViewObject().LunchGUI(Router.CurrentFrame)
      Router.CurrentFrame.pack(
        fill=customtkinter.BOTH,
        expand=True
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

class Main():
  def __init__(self):
    try:
      super().__init__()

      self.config = Configrations()
      self.router = Router()

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
        command = lambda: self.router.navigate(Students.Students),
        text = "Students"
      )
      StudentsButton.pack(side=customtkinter.LEFT)

      ClassesButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda: self.router.navigate(Classes.Classes),
        text="Classes"
      )
      ClassesButton.pack(side=customtkinter.LEFT)

      CoursesButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda: self.router.navigate(Courses.Courses),
        text="Courses"
      )
      CoursesButton.pack(side=customtkinter.LEFT)

      UsersButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda: self.router.navigate(Users.Users),
        text="Users"
      )
      UsersButton.pack(side=customtkinter.LEFT)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def OnClosing(self):
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
      width = self.window.winfo_screenwidth()
      height = self.window.winfo_screenheight()
      self.window.geometry("%dx%d" % (width, height))
      self.window.title("TrueFace Admin")
      # self.window.iconbitmap("logo.ico")
      self.window.protocol("WM_DELETE_WINDOW", self.OnClosing)

      self.router.setWindow(self.window)
      self.Navbar(self.window)

      self.router.navigate(Students.Students)

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
