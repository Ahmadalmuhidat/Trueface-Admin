import sys
import os
import customtkinter

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

      self.getAbsence()

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
        for row, Student in enumerate(self.Absence, start=1):
          StudentID, \
          StudentFirstName, \
          StudentMiddleName, \
          StudentLastName = Student

          AbsenceData = [
            StudentID,
            StudentFirstName,
            StudentMiddleName,
            StudentLastName
          ]

          for col, data in enumerate(AbsenceData):
            DataLabel = customtkinter.CTkLabel(self.AbsenceTableFrame)
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
            self.AbsenceLabels.append(DataLabel)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def refresh(self):
    try:
      self.getAbsence()
      self.displayAbsenceTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def search(self, term):
    try:
      self.searchAbsence(term)

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
      #   placeholder_text="Search by Student ID..."
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

      self.AbsenceTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.AbsenceTableFrame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(self.AbsenceTableFrame)
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
        self.AbsenceTableFrame.columnconfigure(col, weight=1)
      
      self.displayAbsenceTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)