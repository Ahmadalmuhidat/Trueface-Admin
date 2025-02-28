import sys
import os
import customtkinter
import tkinter

from PIL import Image
from DatabaseManager import DatabaseManager
from .Modals import StudentClasses
from Models import Student

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

      self.GetStudents()
      self.GetClassesForSelection()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def SearchStudents(self, term):
    try:
      self.SearchStudent(term)
      self.DisplayStudentsTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def DisplayStudentsTable(self):
    try:
      for label in self.StudentsLabels:
        label.destroy()

      if len(self.Students) > 0:
        for row, Student in enumerate(self.Students, start=1):
          Students_data = [
            Student.ID,
            Student.first_name,
            Student.middle_name,
            Student.last_name,
            Student.gender,
            Student.create_date
          ]

          for col, data in enumerate(Students_data):
            DataLabel = customtkinter.CTkLabel(
              self.StudentsTableFrame,
              text=data,
              padx=10,
              pady=5
            )
            DataLabel.grid(
              row=row,
              column=col,
              sticky="nsew"
            )

            self.StudentsLabels.append(DataLabel)

          ProfileButton = customtkinter.CTkButton(
            self.StudentsTableFrame,
            text="Profile",
            command=lambda StudentID=Student.ID: StudentClasses.StudentClassesPopWindow(
              StudentID,
              self.ClassesForSelection,
              self.InsertClassStudentRelation,
              self.GetClassesStudentRelation,
              self.RemoveClassesStudentRelation,
              self.ClearClassesStudentRelation
            )
          )
          ProfileButton.grid(
            row=row,
            column=6,
            padx=10,
            pady=5,
            sticky="nsew"
          )
          self.StudentsLabels.append(ProfileButton)

          DeleteButton = customtkinter.CTkButton(
            self.StudentsTableFrame,
              text = "Delete",
              fg_color = "red",
              command = lambda: Student.Remove(self.RefreshStudentsTable)
            )
          DeleteButton.grid(
            row = row,
            column = 7,
            sticky = "nsew",
            padx = 10,
            pady= 5
          )
          self.StudentsLabels.append(DeleteButton)

      self.ResultsCount.configure(text="Results: " + str(len(self.Students)))

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def RefreshStudentsTable(self):
    try:
      self.GetStudents()
      self.GetClassesForSelection()
      self.DisplayStudentsTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def UploadImage(self):
    try:
      FilePath = tkinter.filedialog.askopenfilename()

      if FilePath:
        image = Image.open(FilePath)
        image.thumbnail((150, 150))
        self.StudentImage = FilePath
        self.StudentImageEntry.delete(0, customtkinter.END)
        self.StudentImageEntry.insert(0, FilePath)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def SubmitNewStudent(self):
    try:
      StudentID = self.StudentIDEntry.get()
      FirstName = self.StudentFirstNameEntry.get()
      MiddleName = self.StudentMiddleNameEntry.get()
      LastName = self.StudentLastNameEntry.get()
      Gender = self.StudentGenderEntry.get()
      CreateDate = ""

      NewStudent = Student.Student(StudentID, FirstName, MiddleName, LastName, Gender, CreateDate, self.StudentImage)
      NewStudent.ValidateStudentsData()
      NewStudent.Add()

      self.StudentIDEntry.delete(
        0,
        customtkinter.END
      )
      self.StudentFirstNameEntry.delete(
        0,
        customtkinter.END
      )
      self.StudentMiddleNameEntry.delete(
        0,
        customtkinter.END
      )
      self.StudentLastNameEntry.delete(
        0,
        customtkinter.END
      )
      self.StudentImageEntry.delete(
        0,
        customtkinter.END
      )

      self.RefreshStudentsTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def AddStudentInputWindow(self):
    try:
      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()
      self.PopWindow.geometry("490x410")
      self.PopWindow.resizable(False, False)
      self.PopWindow.title("Add New Student")

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
        text="Last Name:"
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

      UploadButton = customtkinter.CTkButton(
        self.PopWindow,
        text="Upload Image",
        width=30,
        height=30,
        command=self.UploadImage
      )
      UploadButton.grid(
        row=5,
        column=0,
        padx=10,
        pady=15
      )

      SaveButton = customtkinter.CTkButton(
        self.PopWindow,
        text="Save Students",
        command=self.SubmitNewStudent,
        width=350
      )
      SaveButton.grid(
        row=7,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=15
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def LunchGUI(self, parent):
    try:
      SearchBarFrame = customtkinter.CTkFrame(
        parent,
        bg_color="transparent"
      )
      SearchBarFrame.pack(
        fill="x",
        expand=False
      )

      SearchButton = customtkinter.CTkButton(
        SearchBarFrame,
        command=lambda: self.SearchStudents(SearchBar.get()),
        text="Search"
      )
      SearchButton.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=10,
        padx=5
      )

      SearchBar = customtkinter.CTkEntry(
        SearchBarFrame,
        width=400,
        placeholder_text="Search for Students..."
      )
      SearchBar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )

      RefreshButton = customtkinter.CTkButton(
        SearchBarFrame,
        command=self.RefreshStudentsTable,
        width=100,
        text="Refresh"
      )
      RefreshButton.grid(
        row=0,
        column=4,
        sticky="nsew",
        pady=10,
        padx=5
      )

      AddStudentButton = customtkinter.CTkButton(
        SearchBarFrame,
        command=self.AddStudentInputWindow,
        width=100,
        text="Add Student"
      )
      AddStudentButton.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )

      self.ResultsCount = customtkinter.CTkLabel(SearchBarFrame)
      self.ResultsCount.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.StudentsTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.StudentsTableFrame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(
          self.StudentsTableFrame,
          text=header,
          padx=10,
          pady=10
        )
        HeaderLabel.grid(
          row=0,
          column=col,
          sticky="nsew"
        )

      for col in range(len(self.headers)):
        self.StudentsTableFrame.columnconfigure(col, weight=1)

      self.DisplayStudentsTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
