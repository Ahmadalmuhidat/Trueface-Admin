import os
import sys
import customtkinter
import threading

import pages.Students.Students as Students
import pages.Classes.Classes as Classes
import pages.Courses.Courses as Courses
import pages.Attendance.Attendance as Attendance
import pages.Absence.Absence as Absence
import pages.Users.Users as Users
import pages.History.History as History
import pages.Settings.Settings as Settings

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

      StudentsButton = customtkinter.CTkButton(navbar)
      StudentsButton.configure(
        corner_radius=0,
        command=lambda: self.showPage("Students"),
        text="Students"
      )
      StudentsButton.pack(side=customtkinter.LEFT)

      ClassesButton = customtkinter.CTkButton(navbar)
      ClassesButton.configure(
        corner_radius=0,
        command=lambda: self.showPage("Classes"),
        text="Classes"
      )
      ClassesButton.pack(side=customtkinter.LEFT)

      CoursesButton = customtkinter.CTkButton(navbar)
      CoursesButton.configure(
        corner_radius=0,
        command=lambda: self.showPage("Courses"),
        text="Courses"
      )
      CoursesButton.pack(side=customtkinter.LEFT)

      AttendanceButton = customtkinter.CTkButton(navbar)
      AttendanceButton.configure(
        corner_radius=0,
        command=lambda: self.showPage("Attendance"),
        text="Attendance"
      )
      AttendanceButton.pack(side=customtkinter.LEFT)

      AbsenceButton = customtkinter.CTkButton(navbar)
      AbsenceButton.configure(
        corner_radius=0,
        command=lambda: self.showPage("Absence"),
        text="Absence"
      )
      AbsenceButton.pack(side=customtkinter.LEFT)

      UsersButton = customtkinter.CTkButton(navbar)
      UsersButton.configure(
        corner_radius=0,
        command=lambda: self.showPage("Users"),
        text="Users"
      )
      UsersButton.pack(side=customtkinter.LEFT)

      # HistoryButton = customtkinter.CTkButton(navbar)
      # HistoryButton.configure(
      #   corner_radius=0,
      #   command=lambda: self.showPage("History"),
      #   text="History"
      # )
      # HistoryButton.pack(side=customtkinter.LEFT)

      # SettingsButton = customtkinter.CTkButton(navbar)
      # SettingsButton.configure(
      #   corner_radius=0,
      #   command=lambda: self.showPage("Settings"),
      #   text="Settings"
      # )
      # SettingsButton.pack(side=customtkinter.LEFT)

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
      self.CurrentPage.pack(
        fill=customtkinter.BOTH,
        expand=True
      )

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

      threadsToTerminate = [
        thread for thread in 
          threading.enumerate() if
            thread.ident != threading.get_ident()
      ]

      for thread in threadsToTerminate:
        if thread.is_alive():
          thread.join(timeout=1)

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

      # self.window.after(
      #   100,
      #   lambda: self.window.attributes('-alpha', 0.85)
      # )

      self.window.protocol("WM_DELETE_WINDOW", self.onClosing)

      self.window.title("TimeWizeAI Admin")

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