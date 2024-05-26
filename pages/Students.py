import sys
import os
import customtkinter
import datetime
import tkinter

from PIL import Image
from DatabaseManager import DatabaseManager

class Students(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.StudentsLabels = []
      self.headers = [
        "Student ID",
        "First Name",
        "Middle Name",
        "Last Name",
        "Gender",
        "Create Date",
      ]

      self.getSettings()
      self.connect()
      # self.checkCustomerLicenseStatus()
      self.getStudents()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def searchStudents(self, term):
    try:
      self.searchStudent(term)
      self.displayStudentsTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def deleteStudent(self, term):
    try:
      self.removeStudent(term)
      self.getStudents()
      self.displayStudentsTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def displayStudentsTable(self):
    try:
      for label in self.StudentsLabels:
        label.destroy()

      if len(self.Students) > 0:
        for row, Students in enumerate(self.Students, start=1):
          StudentID, StudentFirstName, StudentMiddleName, StudentLastName, StudentGender, StudentFaceID, StudentCreateDate = Students
          Students_data = [
            StudentID,
            StudentFirstName,
            StudentMiddleName,
            StudentLastName,
            StudentGender,
            StudentCreateDate
          ]

          for col, data in enumerate(Students_data):
            data_label = customtkinter.CTkLabel(
              self.Students_table_frame,
              text=data,
              padx=10,
              pady=5
            )
            data_label.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            self.StudentsLabels.append(data_label)

      self.results_count.configure(text="Results: " + str(len(self.Students)))

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def refresh(self):
    try:
      self.getStudents()
      self.displayStudentsTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def uploadImage(self):
    try:
      FilePath = tkinter.filedialog.askopenfilename()

      if FilePath:
        image = Image.open(FilePath)
        image.thumbnail((150, 150))
        self.ImagePath = FilePath
        self.StudentImageEntry.delete(0, customtkinter.END)
        self.StudentImageEntry.insert(0, FilePath)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def saveStudent(self):
    try:
      ID = self.StudentIDEntry.get()
      FN = self.StudentFirstNameEntry.get()
      MN = self.StudentMiddleNameEntry.get()
      LN = self.StudentLastNameEntry.get()
      Gender = self.StudentGenderEntry.get()
      TodayDate = datetime.date.today()

      if self.validateStudentsData(ID, FN, MN, LN, Gender, self.ImagePath):
        self.insertStudent(
          ID = ID,
          FN = FN,
          MN = MN,
          LN = LN,
          Gender = Gender,
          ImagePath =  self.ImagePath,
          TodayDate = TodayDate
        )

        self.StudentIDEntry.delete(0, customtkinter.END)
        self.StudentFirstNameEntry.delete(0, customtkinter.END)
        self.StudentMiddleNameEntry.delete(0, customtkinter.END)
        self.StudentLastNameEntry.delete(0, customtkinter.END)
        self.StudentImageEntry.delete(0, customtkinter.END)

        self.refresh()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def addStudent(self):
    try:
      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()
      self.PopWindow.geometry("490x400")
      self.PopWindow.title("Add New Student")
      self.PopWindow.resizable(False, False)

      StudentIDLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Student ID:"
      )
      StudentIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=15
      )
      self.StudentIDEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.StudentIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=15
      )

      StudentFirstNameLabel = customtkinter.CTkLabel(
        self.PopWindow, 
        text="First Name:"
      )
      StudentFirstNameLabel.grid(
        row=1, 
        column=0,
        padx=10,
        pady=15
      )
      self.StudentFirstNameEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.StudentFirstNameEntry.grid(
        row=1,
        column=1,
        padx=10,
        pady=15
      )

      StudentMiddleNameLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Middle Name:"
      )
      StudentMiddleNameLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=15
      )
      self.StudentMiddleNameEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.StudentMiddleNameEntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=15
      )

      StudentLastNameLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="last Name:"
      )
      StudentLastNameLabel.grid(
        row=3,
        column=0,
        padx=10,
        pady=15
      )
      self.StudentLastNameEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.StudentLastNameEntry.grid(
        row=3,
        column=1,
        padx=10,
        pady=15
      )

      StudentGenderLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Gender:"
      )
      StudentGenderLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=15
      )
      self.StudentGenderEntry = customtkinter.CTkComboBox(
        self.PopWindow,
        values=["Male", "Female"],
        width=350
      )
      self.StudentGenderEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=15
      )
      self.StudentGenderEntry.set("Male")

      self.StudentImageEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.StudentImageEntry.grid(
        row=5,
        column=1,
        padx=10,
        pady=15
      )

      UploadButton = customtkinter.CTkButton(self.PopWindow)
      UploadButton.grid(
        row=5,
        column=0,
        padx=10,
        pady=15
      )
      UploadButton.configure(
        text="Upload Image", 
        width=30,
        height=30,
        command=self.uploadImage
      )

      SaveButton = customtkinter.CTkButton(
        self.PopWindow,
        width=350
      )
      SaveButton.grid(
        row=7,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=15
      )
      SaveButton.configure(
        text="Save Students",
        command=self.saveStudent
        )

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
      search_button.configure(command=lambda: self.searchStudents(search_bar.get()))

      search_bar = customtkinter.CTkEntry(search_bar_frame)
      search_bar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )
      search_bar.configure(
        width=400,
        placeholder_text="Search for Students..."
      )

      delete_button = customtkinter.CTkButton(
        search_bar_frame,
        width=100,
        text="Delete"
      )
      delete_button.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=10,
        padx=5
      )
      delete_button.configure(command=lambda: self.deleteStudent(delete_bar.get()))

      delete_bar = customtkinter.CTkEntry(
        search_bar_frame,
        width=100,
        placeholder_text="ID",
        
      )
      delete_bar.grid(
        row=0,
        column=3,
        sticky="nsew",
        pady=10
      )

      refresh_button = customtkinter.CTkButton(
        search_bar_frame,
        width=100,
        text="Refresh"
      )
      refresh_button.grid(
        row=0,
        column=4,
        sticky="nsew",
        pady=10,
        padx=5
      )
      refresh_button.configure(command=self.refresh)

      add_Student_button = customtkinter.CTkButton(
        search_bar_frame,
        width=100,
        text="Add Student"
      )
      add_Student_button.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )
      add_Student_button.configure(command=self.addStudent)

      self.results_count = customtkinter.CTkLabel(search_bar_frame)
      self.results_count.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.Students_table_frame = customtkinter.CTkFrame(parent)
      self.Students_table_frame.pack(
        fill="x",
        expand=False
      )

      for col, header in enumerate(self.headers):
        header_label = customtkinter.CTkLabel(
          self.Students_table_frame,
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
        self.Students_table_frame.columnconfigure(col, weight=1)

      self.displayStudentsTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)