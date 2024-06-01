import sys
import os
import customtkinter
import json
import pandas

from datetime import timedelta
from DatabaseManager import DatabaseManager
from CTkMessagebox import CTkMessagebox

class History(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.HistoryLabels = []
      self.HeadersLabels = []
      self.AttendanceHeaders = [
        "Student",
        "Date",
        "Attend Time",
      ]

      self.AbsenceHeaders = [
        "Student Name",
        "Date"
      ]

      with open('configrations.json', 'r') as file:
        self.WorkingHourAbsence = self.parseTimedelta(
          json.load(file)['Working_Hours']['absence']
        )

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def parseTimedelta(self, time):
    hours, minutes = map(int, time.split(':'))
    return timedelta(hours=hours, minutes=minutes)
  
  def generateReport(self):
    try:
      searchMode = self.combobox.get()

      if len(self.History) > 0:
        if searchMode == "Absence":
          self.generateAbsenceReportByDate()
        elif searchMode == "Attendance":
          self.generateAttendanceReportByDate()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def generateAttendanceReportByDate(self):
      try:
        updated_history = []
        date = self.date_entry.get()

        for item in self.History:
          AttendTime = str(item[2]).split(":")
          AttendUpdatedTime = f"{AttendTime[0]}:{AttendTime[1]}:{AttendTime[2]}"

          updated_history.append((item[0], item[1], AttendUpdatedTime))

        results = pandas.DataFrame(
          updated_history, columns=[
          'Student Name',
          'Date',
          'Attend Time'
          ]
        )

        DownloadsFolder = os.path.join(os.path.expanduser("~"), "Downloads")
        FileName = date + "_Attendance.xlsx"
        FilePath = os.path.join(DownloadsFolder, FileName)
        results.to_excel(FilePath, index=False)

        title="Generate complete"
        message="you can find the report in {}".format(DownloadsFolder)
        icon="check"
        CTkMessagebox(title=title, message=message,icon=icon)

        updated_history.clear()

      except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(exc_obj)

  def generateAbsenceReportByDate(self):
    try:
      updated_history = []
      date = self.date_entry.get()

      for item in self.History:
        updated_history.append((item[0], date))

      results = pandas.DataFrame(updated_history, columns=['Student Name', 'Date'])

      DownloadsFolder = os.path.join(os.path.expanduser("~"), "Downloads")        
      FileName = date + "_Absence.xlsx"
      FilePath = os.path.join(DownloadsFolder, FileName)
      results.to_excel(FilePath, index=False)

      title="Generate complete"
      message="you can find the report in {}".format(DownloadsFolder)
      icon="check"
      CTkMessagebox(title=title, message=message,icon=icon)

      updated_history.clear()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def search(self, date):
    try:
      searchMode = self.combobox.get()
      
      if searchMode == "Attendance":
        self.getAttendanceHistoryByDate(date)
        self.displayAttendanceHistoryTable()
      elif searchMode == "Absence":
        self.getAbsenceHistoryByDate(date)
        self.displayAbsenceHistoryTable()

      self.ResultsCount.configure(text="Results: " + str(len(self.History)))
    
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def clearHeaders(self):
    try:
      for label in self.HistoryLabels:
        label.destroy()
 
      for label in self.HeadersLabels:
        label.destroy()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def setHeaders(self, arg):
    try:
        if arg == "Absence":
          for col, header in enumerate(self.AbsenceHeaders):
            HeaderLabel = customtkinter.CTkLabel(self.HistoryTableFrame)
            HeaderLabel.grid(row=0, column=col, sticky="nsew")
            HeaderLabel.configure(text=header, padx=10, pady=5)
            
            self.HeadersLabels.append(HeaderLabel)

          for col in range(len(self.AbsenceHeaders)):
            self.HistoryTableFrame.columnconfigure(col, weight=1)
        else:
          for col, header in enumerate(self.AttendanceHeaders):
            HeaderLabel = customtkinter.CTkLabel(self.HistoryTableFrame, text=header, padx=10, pady=5)
            HeaderLabel.grid(row=0, column=col, sticky="nsew")
            self.HeadersLabels.append(HeaderLabel)

          for col in range(len(self.AttendanceHeaders)):
            self.HistoryTableFrame.columnconfigure(col, weight=1)          

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def displayAbsenceHistoryTable(self):
    try:
      self.clearHeaders()
      self.setHeaders("Absence")

      date = self.date_entry.get()

      if len(self.History) > 0:
        for row, log in enumerate(self.History, start=1):
          history_Student_name= log
          history_data = [
            history_Student_name,
            date
          ]

          for col, data in enumerate(history_data):
            DataLabel = customtkinter.CTkLabel(self.HistoryTableFrame)
            DataLabel.grid(row=row, column=col, sticky="nsew")
            DataLabel.configure(
              text=data,
              padx=10,
              pady=5
            )
            self.HistoryLabels.append(DataLabel)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def displayAttendanceHistoryTable(self):
    try:
      self.clearHeaders()
      self.setHeaders("Attendance")

      if len(self.History) > 0:
        for row, log in enumerate(self.History, start=1):
          history_Student, history_date, history_attend_time, = log
          history_data = [
            history_Student,
            history_date,
            history_attend_time,
          ]

          for col, data in enumerate(history_data):
            if history_attend_time < self.WorkingHourAbsence:
              DataLabel = customtkinter.CTkLabel(self.HistoryTableFrame, text=data, padx=10, pady=5)
              DataLabel.grid(row=row, column=col, sticky="nsew")
              self.HistoryLabels.append(DataLabel)
            else:
              DataLabel = customtkinter.CTkLabel(self.HistoryTableFrame, text=data, padx=10, pady=5, text_color="red")
              DataLabel.grid(row=row, column=col, sticky="nsew")
              self.HistoryLabels.append(DataLabel)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)  

  def create(self, parent):
    try:
      search_bar_frame = customtkinter.CTkFrame(parent, bg_color="transparent")
      search_bar_frame.pack(fill="x", expand=False)

      search_button = customtkinter.CTkButton(search_bar_frame, text="Search")
      search_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=5)
      search_button.configure(command=lambda: self.search(self.date_entry.get()))

      self.date_entry = customtkinter.CTkEntry(search_bar_frame)
      self.date_entry.grid(row=0, column=1, sticky="nsew", pady=10)
      self.date_entry.configure(width=400, placeholder_text="YYYY-MM-DD")

      self.combobox = customtkinter.CTkComboBox(master=search_bar_frame, values=["Attendance", "Absence"])
      self.combobox.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
      self.combobox.set("Attendance")

      lectures = customtkinter.CTkComboBox(master=search_bar_frame, values=self.Classes)
      lectures.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
      lectures.set(self.Classes[0])

      generate_report_button = customtkinter.CTkButton(search_bar_frame, text="Generate Report")
      generate_report_button.grid(row=0, column=3, sticky="nsew", pady=10, padx=5)
      generate_report_button.configure(command=self.generateReport)

      self.ResultsCount = customtkinter.CTkLabel(search_bar_frame, text="Results: 0")
      self.ResultsCount.grid(row=0, column=4, padx=10, pady=10)
      
      self.HistoryTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.HistoryTableFrame.pack(fill="both", expand=True)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)