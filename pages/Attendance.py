import sys
import os
import customtkinter
import time

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
    return timedelta(hours=hours, minutes=minutes)

  def displayAttendanceTable(self):
    try:
      for label in self.AttendanceLabels:
        label.destroy()

      if len(self.Attendance) > 0:
        for row, log in enumerate(self.Attendance, start=1):
          StudentID, StudentFirstName, StudentMiddleName, StudentLastName, ClassSubjectArea, AttendanceTime = log
          attendance_data = [
            StudentID,
            StudentFirstName,
            StudentMiddleName,
            StudentLastName,
            ClassSubjectArea,
            AttendanceTime
          ]

          for col, data in enumerate(attendance_data):
            data_label = customtkinter.CTkLabel(self.attendance_table_frame, text=data, padx=10, pady=5)
            data_label.grid(row=row, column=col, sticky="nsew")
            self.AttendanceLabels.append(data_label)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def refresh(self):
    try:
      self.getAttendance()
      self.displayAttendanceTable()

      self.results_count.configure(text="Results: " + str(len(self.Attendance)))

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def search(self, term):
    try:
      self.searchAttendance(term)

      self.results_count.configure(text="Results: " + str(len(self.Attendance)))

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def create(self, parent):
    try:
      search_bar_frame = customtkinter.CTkFrame(
        parent,
        bg_color="transparent"
      )
      search_bar_frame.pack(
        fill="x",
        expand=False
      )

      search_button = customtkinter.CTkButton(
        search_bar_frame,
        text="Search"
      )
      search_button.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=10,
        padx=5
      )
      search_button.configure(command=lambda: self.search(search_bar.get()))

      search_bar = customtkinter.CTkEntry(search_bar_frame)
      search_bar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )
      search_bar.configure(
        width=400,
        placeholder_text="Search by Student ID or Class Subject..."
      )

      refresh_button = customtkinter.CTkButton(
        search_bar_frame,
        width=100,
        text="Refresh"
      )
      refresh_button.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=10,
        padx=5
      )
      refresh_button.configure(command=self.refresh)

      self.results_count = customtkinter.CTkLabel(search_bar_frame)
      self.results_count.grid(
        row=0,
        column=3,
        padx=10,
        pady=5
      )
      self.results_count.configure(
        text="Results: " + str(len(self.Students))
      )

      self.attendance_table_frame = customtkinter.CTkScrollableFrame(parent)
      self.attendance_table_frame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        header_label = customtkinter.CTkLabel(
          self.attendance_table_frame,
          text=header,
          padx=10,
          pady=10
        )
        header_label.grid(
          row=0,
          column=col,
          sticky="nsew"
        )

      for col in range(len(self.headers)):
        self.attendance_table_frame.columnconfigure(
          col,
          weight=1
        )

      self.displayAttendanceTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)