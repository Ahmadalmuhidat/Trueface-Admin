import sys
import os
import customtkinter
import pandas

from datetime import timedelta
from DatabaseManager import DatabaseManager
from CTkMessagebox import CTkMessagebox

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

      self.GetClasses()

      self.ClassesMap = {
        f"{x[1]} {x[6]}-{x[7]}": x[0] for x in self.Classes
      }

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
  
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
          StudentID, \
          StudentFirstName, \
          StudentMiddleName, \
          StudentLastName, \
          ClassSubjectArea, \
          AttendanceTime = Attendance

          AttendanceData = [
            StudentID,
            StudentFirstName,
            StudentMiddleName,
            StudentLastName,
            ClassSubjectArea,
            AttendanceTime
          ]

          for col, data in enumerate(AttendanceData):
            DataLabel = customtkinter.CTkLabel(
              self.AttendanceTableFrame,
              text=data,
              padx=10,
              pady=5
            )
            DataLabel.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            self.AttendanceLabels.append(DataLabel)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def GenerateReport(self):
    try:
      report = pandas.DataFrame(
        self.Attendance,
        columns=self.headers
      )

      DownloadsFolder = os.path.join(os.path.expanduser("~"), "Downloads")
      FileName = "Attendance Report.xlsx"
      FilePath = os.path.join(DownloadsFolder, FileName)
      report.to_excel(FilePath, index=False)

      title = "Generate complete"
      message = "you can find the report in {}".format(DownloadsFolder)
      icon = "check"
      CTkMessagebox(
        title = title,
        message = message,
        icon = icon
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
  
  def search(self):
    try:
      self.GetAttendanceByDate(
        self.ClassesMap[self.SubjectEntry.get()],
        self.DateEntry.get()
      )

      self.displayAttendanceTable()

      self.ResultsCount.configure(
        text="Results: " + str(len(self.Attendance))
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def create(self, parent):
    try:
      SearchBarFrame = customtkinter.CTkFrame(
        parent,
        bg_color = "transparent"
      )
      SearchBarFrame.pack(
        fill = "x",
        expand = False
      )

      SearchButton = customtkinter.CTkButton(
        SearchBarFrame,
        command = self.search,
        text = "Search"
      )
      SearchButton.grid(
        row = 0,
        column = 0,
        sticky = "nsew",
        pady = 10,
        padx = 5
      )

      self.DateEntry = customtkinter.CTkEntry(
        SearchBarFrame,
        width = 400,
        placeholder_text = "YYYY-MM-DD"
      )
      self.DateEntry.grid(
        row = 0,
        column = 1,
        sticky = "nsew",
        pady = 10
      )

      self.SubjectEntry = customtkinter.CTkComboBox(
        SearchBarFrame, 
        values = [f"{x[1]} {x[6]}-{x[7]}" for x in self.Classes],
        width = 400
      )
      self.SubjectEntry.grid(
        row = 0,
        column = 2,
        sticky = "nsew",
        pady = 10,
        padx = 5
      )

      GenerateReportButton = customtkinter.CTkButton(
        SearchBarFrame,
        command = self.GenerateReport,
        text = "Generate Report"
      )
      GenerateReportButton.grid(
        row = 0,
        column = 3,
        sticky = "nsew",
        pady = 10,
        padx = 5
      )

      self.ResultsCount = customtkinter.CTkLabel(
        SearchBarFrame,
        text="Results: " + str(len(self.Attendance))
      )
      self.ResultsCount.grid(
        row = 0,
        column = 4,
        padx = 10,
        pady = 5
      )

      self.AttendanceTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.AttendanceTableFrame.pack(
        fill = "both",
        expand = True
      )

      for col, header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(
          self.AttendanceTableFrame,
          text = header,
          padx = 10,
          pady = 10
        )
        HeaderLabel.grid(
          row = 0,
          column = col,
          sticky = "nsew"
        )

      for col in range(len(self.headers)):
        self.AttendanceTableFrame.columnconfigure(
          col,
          weight=1
        )

      self.displayAttendanceTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)