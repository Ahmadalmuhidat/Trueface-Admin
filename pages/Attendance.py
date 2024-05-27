import sys
import os
import customtkinter

from datetime import timedelta
from DatabaseManager import DatabaseManager

class Attendance(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.AttendanceLabels = []
      self.headers = [
        "Student ID",
        "First Name",
        "Middle Name",
        "Last Name",
        "Class Subject",
        "Attendance Time"
      ]

      self.getAttendance()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def parseTimedelta(self, time):
    hours, minutes = map(int, time.split(':'))
    return timedelta(
      hours=hours,
      minutes=minutes
    )

  def displayAttendanceTable(self):
    try:
      for label in self.AttendanceLabels:
        label.destroy()

      if len(self.Attendance) > 0:
        for row, Attendance in enumerate(self.Attendance, start=1):
          StudentID, StudentFirstName, StudentMiddleName, StudentLastName, ClassSubjectArea, AttendanceTime = Attendance
          AttendanceData = [
            StudentID,
            StudentFirstName,
            StudentMiddleName,
            StudentLastName,
            ClassSubjectArea,
            AttendanceTime
          ]

          for col, data in enumerate(AttendanceData):
            DataLabel = customtkinter.CTkLabel(self.AttendanceTableFrame)
            DataLabel.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            DataLabel.configure(
              text=data,
              padx=10,
              pady=5
            )
            self.AttendanceLabels.append(DataLabel)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def refresh(self):
    try:
      self.getAttendance()
      self.displayAttendanceTable()

      self.ResultsCount.configure(
        text="Results: " + str(len(self.Attendance))
      )

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def search(self, term):
    try:
      self.searchAttendance(term)

      self.ResultsCount.configure(
        text="Results: " + str(len(self.Attendance))
      )

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def create(self, parent):
    try:
      SearchBarFrame = customtkinter.CTkFrame(parent)
      SearchBarFrame.pack(
        fill="x",
        expand=False
      )
      SearchBarFrame.configure(bg_color="transparent")

      # SearchButton = customtkinter.CTkButton(SearchBarFrame)
      # SearchButton.grid(
      #   row=0,
      #   column=0,
      #   sticky="nsew",
      #   pady=10,
      #   padx=5
      # )
      # SearchButton.configure(
      #   command=lambda: self.search(SearchBar.get()),
      #   text="Search"
      # )

      # SearchBar = customtkinter.CTkEntry(SearchBarFrame)
      # SearchBar.grid(
      #   row=0,
      #   column=1,
      #   sticky="nsew",
      #   pady=10
      # )
      # SearchBar.configure(
      #   width=400,
      #   placeholder_text="Search by Student ID or Class Subject..."
      # )

      RefreshButton = customtkinter.CTkButton(SearchBarFrame)
      RefreshButton.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=10,
        padx=5
      )
      RefreshButton.configure(
        command=self.refresh,
        width=100,
        text="Refresh"
      )

      self.ResultsCount = customtkinter.CTkLabel(SearchBarFrame)
      self.ResultsCount.grid(
        row=0,
        column=3,
        padx=10,
        pady=5
      )
      self.ResultsCount.configure(
        text="Results: " + str(len(self.Attendance))
      )

      self.AttendanceTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.AttendanceTableFrame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(self.AttendanceTableFrame)
        HeaderLabel.grid(
          row=0,
          column=col,
          sticky="nsew"
        )
        HeaderLabel.configure(
          text=header,
          padx=10,
          pady=10  
        )

      for col in range(len(self.headers)):
        self.AttendanceTableFrame.columnconfigure(
          col,
          weight=1
        )

      self.displayAttendanceTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)