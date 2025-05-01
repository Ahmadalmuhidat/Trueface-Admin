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

  def create_navbar(self):
    try:
      navbar = customtkinter.CTkFrame(self.config.window)
      navbar.pack(fill=customtkinter.X)

      students_view = customtkinter.CTkButton(
        navbar,
        corner_radius = 0,
        command = lambda: self.config.router.navigate(Students.Students),
        text = "Students"
      )
      students_view.pack(side=customtkinter.LEFT)

      classes_view = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command= lambda: self.config.router.navigate(Classes.Classes),
        text="Classes"
      )
      classes_view.pack(side=customtkinter.LEFT)

      courses_view = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command= lambda: self.config.router.navigate(Courses.Courses),
        text="Courses"
      )
      courses_view.pack(side=customtkinter.LEFT)

      users_view = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command= lambda:  self.config.router.navigate(Users.Users),
        text="Users"
      )
      users_view.pack(side=customtkinter.LEFT)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def when_app_close(self):
    try:
      self.config.window.destroy()

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

  def start_program(self):
    try:
      customtkinter.set_appearance_mode("dark")

      self.window = customtkinter.CTk()

      width = self.window.winfo_screenwidth()
      height = self.window.winfo_screenheight()
      self.window.geometry("%dx%d" % (width, height))
      self.window.title("TrueFace Admin")
      # self.window.iconbitmap("logo.ico")
      self.window.protocol("WM_DELETE_WINDOW", self.when_app_close)
      self.config.set_window(self.window)

      self.create_navbar()
      self.config.router.navigate(Students.Students)

      self.window.mainloop()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  Main().start_program()
  # Login.Login().lunch_view()
