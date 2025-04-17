import sys
import os
import customtkinter
import tkinter

from PIL import Image
from app.core.GlobalData import GlobalData
from .Modals import StudentClasses
from app.models import student
from app.controllers.students import GetStudents, SearchStudent, AddStudent, RemoveStudent
from app.controllers.classes import InsertClassStudentRelation, GetClassesForSelection, GetClassesStudentRelation, RemoveClassesStudentRelation, ClearClassesStudentRelation

class Students():
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

      GetStudents()
      GetClassesForSelection()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  # def AddClassInputWindow(self, ID):
  #   try:
  #     class_id_title_map = {
  #       f"{x[1]} {x[2]}-{x[3]}": x[0] for x in self.ClassesForSelection
  #     }

  #     for widget in self.PopWindow.winfo_children():
  #       if widget not in (Navbar,):
  #         widget.pack_forget()

  #     ClassLabel = customtkinter.CTkLabel(
  #       self.PopWindow,
  #       text="Select Class:"
  #     )
  #     ClassLabel.pack(
  #       padx=10,
  #       pady=10
  #     )

  #     ClassEntry = customtkinter.CTkComboBox(
  #       self.PopWindow,
  #       values=[f"{x[1]} {x[2]}-{x[3]}" for x in self.ClassesForSelection],
  #       width=350
  #     )
  #     ClassEntry.pack(
  #       padx=10,
  #       pady=10
  #     )
  #     ClassEntry.set("None")

  #     DayLabel = customtkinter.CTkLabel(
  #       self.PopWindow,
  #       text="Select Day:"
  #     )
  #     DayLabel.pack(
  #       padx=10,
  #       pady=10
  #     )

  #     DayEntry = customtkinter.CTkComboBox(
  #       self.PopWindow,
  #       values=[
  #         "Sunday",
  #         "Monday",
  #         "Tuesday",
  #         "Wednesday",
  #         "Thursday",
  #         "Friday",
  #         "Saturday"
  #       ],
  #       width=350
  #     )
  #     DayEntry.pack(
  #       padx=10,
  #       pady=10
  #     )
  #     DayEntry.set("None")

  #     SaveButton = customtkinter.CTkButton(
  #       self.PopWindow,
  #       text="Save Class",
  #       command=lambda: self.InsertClassStudentRelation(
  #         str(uuid.uuid4()),
  #         ID,
  #         class_id_title_map[ClassEntry.get()],
  #         DayEntry.get()
  #       )
  #     )
  #     SaveButton.pack(
  #       padx=10,
  #       pady=5
  #     )

  #   except Exception as e:
  #     ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
  #     FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
  #     print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
  #     print(ExceptionObject)

  def search(self, term):
    try:
      SearchStudent(term)
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

      if len(GlobalData.students) > 0:
        for row, student in enumerate(GlobalData.students, start=1):
          Students_data = [
            student.student_id,
            student.first_name,
            student.middle_name,
            student.last_name,
            student.gender,
            student.create_date
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
            # command=lambda ID=student.student_id: StudentClasses.StudentClassesPopWindow(
            #   ID,
            #   self.ClassesForSelection,
            #   InsertClassStudentRelation,
            #   GetClassesStudentRelation,
            #   RemoveClassesStudentRelation,
            #   ClearClassesStudentRelation
            # )
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
              command = lambda: RemoveStudent(student.student_id, self.RefreshStudentsTable)
            )
          DeleteButton.grid(
            row = row,
            column = 7,
            sticky = "nsew",
            padx = 10,
            pady= 5
          )
          self.StudentsLabels.append(DeleteButton)

      self.ResultsCount.configure(text="Results: " + str(len(GlobalData.students)))

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def RefreshStudentsTable(self):
    try:
      GetStudents()
      GetClassesForSelection()
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
      ID = self.StudentIDEntry.get()
      FirstName = self.StudentFirstNameEntry.get()
      MiddleName = self.StudentMiddleNameEntry.get()
      LastName = self.StudentLastNameEntry.get()
      Gender = self.StudentGenderEntry.get()
      CreateDate = ""

      NewStudent = student.Student(ID, FirstName, MiddleName, LastName, Gender, CreateDate, self.StudentImage)
      NewStudent.ValidateStudentsData()
      AddStudent(NewStudent)

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
        command=lambda: self.search(SearchBar.get()),
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
