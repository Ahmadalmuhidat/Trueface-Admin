import os
import sys
import customtkinter
import threading

import pages.Students as Students
import pages.Classes as Classes
import pages.Courses as Courses
import pages.Attendance as Attendance
import pages.Absence as Absence
import pages.Users as Users
import pages.History as History
import pages.Settings as Settings

class UserInterface():
  def __init__(self):
    try:
      super().__init__()

      self.CurrentPage = None
      self.pages = {}

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def Navbar(self, window):
    try:
      navbar = customtkinter.CTkFrame(window)
      navbar.pack(fill=customtkinter.X)

      StudentsButton = customtkinter.CTkButton(navbar, text="Students")
      StudentsButton.configure(corner_radius=0, command=lambda: self.showPage("Students"))
      StudentsButton.pack(side=customtkinter.LEFT)

      ClassesButton = customtkinter.CTkButton(navbar, text="Classes")
      ClassesButton.configure(corner_radius=0, command=lambda: self.showPage("Classes"))
      ClassesButton.pack(side=customtkinter.LEFT)

      CoursesButton = customtkinter.CTkButton(navbar, text="Courses")
      CoursesButton.configure(corner_radius=0, command=lambda: self.showPage("Courses"))
      CoursesButton.pack(side=customtkinter.LEFT)

      AttendanceButton = customtkinter.CTkButton(navbar, text="Attendance")
      AttendanceButton.configure(corner_radius=0, command=lambda: self.showPage("Attendance"))
      AttendanceButton.pack(side=customtkinter.LEFT)

      AbsenceButton = customtkinter.CTkButton(navbar, text="Absence")
      AbsenceButton.configure(corner_radius=0, command=lambda: self.showPage("Absence"))
      AbsenceButton.pack(side=customtkinter.LEFT)

      UsersButton = customtkinter.CTkButton(navbar, text="Users")
      UsersButton.configure(corner_radius=0, command=lambda: self.showPage("Users"))
      UsersButton.pack(side=customtkinter.LEFT)

      # HistoryButton = customtkinter.CTkButton(navbar, text="History")
      # HistoryButton.configure(corner_radius=0, command=lambda: self.showPage("History"))
      # HistoryButton.pack(side=customtkinter.LEFT)

      SettingsButton = customtkinter.CTkButton(navbar, text="Settings")
      SettingsButton.configure(corner_radius=0, command=lambda: self.showPage("Settings"))
      SettingsButton.pack(side=customtkinter.LEFT)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def showPage(self, name):
    try:
      if self.CurrentPage:
        self.CurrentPage.pack_forget()

      self.CurrentPage = self.pages[name]
      self.CurrentPage.pack(fill=customtkinter.BOTH, expand=True)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

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
      elif name == "Absence":
        Absence.Absence().create(page)
      elif name == "Users":
        Users.Users().create(page)
      elif name == "History":
        History.History().create(page)
      elif name == "Settings":
        Settings.Settings().create(page)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def onClosing(self):
    try:
      self.window.destroy()

      threadsToTerminate = [thread for thread in threading.enumerate() if thread.ident != threading.get_ident()]

      for thread in threadsToTerminate:
        if thread.is_alive():
          thread.join(timeout=1)
      
      print("Done Closing")

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(exc_obj)
    finally:
        sys.exit(0)

  def startTheProgram(self):
    try:
      self.window = customtkinter.CTk()

      width= self.window.winfo_screenwidth()
      height= self.window.winfo_screenheight()
      self.window.geometry("%dx%d" % (width, height))

      self.window.title("TimeWizeAI Admin")

      self.window.protocol("WM_DELETE_WINDOW", self.onClosing)

      self.Navbar(self.window)
      self.createPage(self.window, "Students")
      self.createPage(self.window, "Classes")
      self.createPage(self.window, "Courses")
      self.createPage(self.window, "Attendance")
      self.createPage(self.window, "Absence")
      self.createPage(self.window, "Users")
      # self.createPage(self.window, "History")
      # self.createPage(self.window, "Settings")

      self.showPage("Students")

      self.window.mainloop()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  UserInterface().startTheProgram()