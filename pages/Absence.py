import sys
import os
import customtkinter
import threading
import time

from DatabaseManager import DatabaseManager

class Absence(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.AbsenceLabels = []
      self.headers = [
        "Student ID",
        "First Name",
        "Middle Name",
        "Last Name",
      ]

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def displayAbsenceTable(self):
    try:
      for label in self.AbsenceLabels:
        label.destroy()

      if len(self.Absence) > 0:
        for row, log in enumerate(self.Absence, start=1):
          StudentID, StudentFirstName, StudentMiddleName, StudentLastName = log
          absence_data = [
            StudentID,
            StudentFirstName,
            StudentMiddleName,
            StudentLastName
          ]

          for col, data in enumerate(absence_data):
            data_label = customtkinter.CTkLabel(
              self.absence_table_frame,
              text=data,
              padx=10,
              pady=5
            )
            data_label.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            self.AbsenceLabels.append(data_label)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def refresh(self):
    try:
      while True:
        self.getAbsence()
        self.displayAbsenceTable()
        time.sleep(5)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def create(self, parent):
    try:
      self.absence_table_frame = customtkinter.CTkScrollableFrame(parent)
      self.absence_table_frame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        header_label = customtkinter.CTkLabel(
          self.absence_table_frame,
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
        self.absence_table_frame.columnconfigure(col, weight=1)
      
      threading.Thread(target=self.refresh).start()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)