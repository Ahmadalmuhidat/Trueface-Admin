import os
import sys
import customtkinter
import threading

import pages.Students.Students as Students
import pages.Classes.Classes as Classes
import pages.Courses.Courses as Courses
import pages.Attendance.Attendance as Attendance
import pages.Users.Users as Users

class UserInterface():
  def __init__(self):
    try:
      super().__init__()

      self.CurrentPage = None
      self.pages = {}

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
        command = lambda: self.showPage("Students"),
        text = "Students"
      )
      StudentsButton.pack(side=customtkinter.LEFT)

      ClassesButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda: self.showPage("Classes"),
        text="Classes"
      )
      ClassesButton.pack(side=customtkinter.LEFT)

      CoursesButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda: self.showPage("Courses"),
        text="Courses"
      )
      CoursesButton.pack(side=customtkinter.LEFT)

      AttendanceButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda: self.showPage("Attendance"),
        text="Attendance"
      )
      AttendanceButton.pack(side=customtkinter.LEFT)

      UsersButton = customtkinter.CTkButton(
        navbar,
        corner_radius=0,
        command=lambda: self.showPage("Users"),
        text="Users"
      )
      UsersButton.pack(side=customtkinter.LEFT)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def showPage(self, name):
    try:
      if self.CurrentPage:
        self.CurrentPage.pack_forget()

      self.CurrentPage = self.pages[name]
      self.CurrentPage.pack(
        fill=customtkinter.BOTH,
        expand=True
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def createPage(self, window, name):
    try:
      page = customtkinter.CTkFrame(window)
      self.pages[name] = page

      if name == "Students":
        Students.Students().create(page)
      elif name == "Classes":
        Classes.Classes().create(page)
      elif name == "Courses":
        Courses.Courses().create(page)
      elif name == "Attendance":
        Attendance.Attendance().create(page)
      elif name == "Users":
        Users.Users().create(page)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def onClosing(self):
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

  def startTheProgram(self):
    try:
      customtkinter.set_appearance_mode("dark")

      self.window = customtkinter.CTk()

      width= self.window.winfo_screenwidth()
      height= self.window.winfo_screenheight()
      self.window.geometry("%dx%d" % (width, height))

      self.window.protocol("WM_DELETE_WINDOW", self.onClosing)

      self.window.title("TrueFace Admin")
      self.window.iconbitmap("logo.ico")

      self.Navbar(self.window)
      self.createPage(self.window, "Students")
      self.createPage(self.window, "Classes")
      self.createPage(self.window, "Courses")
      self.createPage(self.window, "Attendance")
      self.createPage(self.window, "Users")

      self.showPage("Students")

      self.window.mainloop()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  UserInterface().startTheProgram()