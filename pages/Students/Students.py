import sys
import os
import customtkinter
import datetime
import tkinter

from PIL import Image
from DatabaseManager import DatabaseManager
from CTkMessagebox import CTkMessagebox
from .Modals import StudentClasses

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
      self.checkLicenseStatus()
      self.getStudents()
      self.getClassesForSelection()

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
          StudentID, \
          StudentFirstName, \
          StudentMiddleName, \
          StudentLastName, \
          StudentGender, \
          StudentCreateDate = Students

          Students_data = [
            StudentID,
            StudentFirstName,
            StudentMiddleName,
            StudentLastName,
            StudentGender,
            StudentCreateDate
          ]

          for col, data in enumerate(Students_data):
            DataLabel = customtkinter.CTkLabel(self.StudentsTableFrame)
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

            self.StudentsLabels.append(DataLabel)

          ProfileButton = customtkinter.CTkButton(self.StudentsTableFrame)
          ProfileButton.grid(
            row=row,
            column=6,
            padx=10,
            pady=5,
            sticky="nsew"
          )
          ProfileButton.configure(
            text="Profile",
            command=lambda StudentID=StudentID: StudentClasses.StudentClassesPopWindow(
              StudentID,
              self.ClassesForSelection,
              self.insertClassStudentRelation,
              self.getClassesStudentRelation,
              self.RemoveClassesStudentRelation
            )
          )
          self.StudentsLabels.append(ProfileButton)

      self.ResultsCount.configure(text="Results: " + str(len(self.Students)))

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def refresh(self):
    try:
      self.getStudents()
      self.getClassesForSelection()
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

  def validateStudentsData(
      self,
      StudentID,
      FirstName,
      MiddleName,
      LastName,
      Gender,
      ImagePath
    ):
    try:
      if not StudentID:
        title = "Missing Entry"
        message = "please enter Students ID"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not FirstName:
        title = "Missing Entry"
        message = "please enter Students first name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not FirstName:
        title = "Missing Entry"
        message = "please enter Students first name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not MiddleName:
        title = "Missing Entry"
        message = "please enter Students middle name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not LastName:
        title = "Missing Entry"
        message = "please enter Students last name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not Gender:
        title = "Missing Entry"
        message = "please enter Students Gender"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False 
      elif not ImagePath:
        title = "Missing Entry"
        message = "please select Students image"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not os.path.exists(ImagePath):
        title = "Inavlid Path"
        message = "the selected path is not valid"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not self.checkFaceInImage(ImagePath):
        title = "Face Not Found"
        message = "the uploaded image contains no face"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif self.checkDuplicatedID(StudentID):
        title = "Duplicated ID"
        message = "the entered id has been already assigned to another Student"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False

      return True

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(exc_obj)
        pass

  def saveStudent(self):
    try:
      StudentID = self.StudentIDEntry.get()
      FirstName = self.StudentFirstNameEntry.get()
      MiddleName = self.StudentMiddleNameEntry.get()
      LastName = self.StudentLastNameEntry.get()
      Gender = self.StudentGenderEntry.get()
      TodayDate = datetime.date.today()

      if self.validateStudentsData(
        StudentID,
        FirstName,
        MiddleName,
        LastName,
        Gender,
        self.ImagePath
      ):
        self.insertStudent(
          StudentID = StudentID,
          FirstName = FirstName,
          MiddleName = MiddleName,
          LastName = LastName,
          Gender = Gender,
          ImagePath =  self.ImagePath,
          TodayDate = TodayDate
        )

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
      self.PopWindow.resizable(False, False)

      self.PopWindow.title("Add New Student")

      StudentIDLabel = customtkinter.CTkLabel(self.PopWindow)
      StudentIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=15
      )
      StudentIDLabel.configure(text="Student ID:")

      self.StudentIDEntry = customtkinter.CTkEntry(self.PopWindow)
      self.StudentIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=15
      )
      self.StudentIDEntry.configure(width=350)

      StudentFirstNameLabel = customtkinter.CTkLabel(self.PopWindow)
      StudentFirstNameLabel.grid(
        row=1, 
        column=0,
        padx=10,
        pady=15
      )
      StudentFirstNameLabel.configure(text="First Name:")

      self.StudentFirstNameEntry = customtkinter.CTkEntry(self.PopWindow)
      self.StudentFirstNameEntry.grid(
        row=1,
        column=1,
        padx=10,
        pady=15
      )
      self.StudentFirstNameEntry.configure(width=350)

      StudentMiddleNameLabel = customtkinter.CTkLabel(self.PopWindow)
      StudentMiddleNameLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=15
      )
      StudentMiddleNameLabel.configure(text="Middle Name:")

      self.StudentMiddleNameEntry = customtkinter.CTkEntry(self.PopWindow)
      self.StudentMiddleNameEntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=15
      )
      self.StudentMiddleNameEntry.configure(width=350)

      StudentLastNameLabel = customtkinter.CTkLabel(self.PopWindow)
      StudentLastNameLabel.grid(
        row=3,
        column=0,
        padx=10,
        pady=15
      )
      StudentLastNameLabel.configure(text="Last Name:")

      self.StudentLastNameEntry = customtkinter.CTkEntry(self.PopWindow)
      self.StudentLastNameEntry.grid(
        row=3,
        column=1,
        padx=10,
        pady=15
      )
      self.StudentLastNameEntry.configure(width=350)

      StudentGenderLabel = customtkinter.CTkLabel(self.PopWindow)
      StudentGenderLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=15
      )
      StudentGenderLabel.configure(text="Gender:")

      self.StudentGenderEntry = customtkinter.CTkComboBox(self.PopWindow)
      self.StudentGenderEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=15
      )
      self.StudentGenderEntry.configure(
        values=[
          "Male",
          "Female"
        ],
        width=350
      )
      self.StudentGenderEntry.set("Male")

      self.StudentImageEntry = customtkinter.CTkEntry(self.PopWindow)
      self.StudentImageEntry.grid(
        row=5,
        column=1,
        padx=10,
        pady=15
      )
      self.StudentImageEntry.configure(width=350)

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

      SaveButton = customtkinter.CTkButton(self.PopWindow)
      SaveButton.grid(
        row=7,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=15
      )
      SaveButton.configure(
        text="Save Students",
        command=self.saveStudent,
        width=350
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

      SearchButton = customtkinter.CTkButton(SearchBarFrame)
      SearchButton.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=10,
        padx=5
      )
      SearchButton.configure(
        command=lambda: self.searchStudents(SearchBar.get()),
        text="Search"
      )

      SearchBar = customtkinter.CTkEntry(SearchBarFrame)
      SearchBar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )
      SearchBar.configure(
        width=400,
        placeholder_text="Search for Students..."
      )

      DeleteButton = customtkinter.CTkButton(SearchBarFrame)
      DeleteButton.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=10,
        padx=5
      )
      DeleteButton.configure(
        command=lambda: self.deleteStudent(DeleteBar.get()),
        width=100,
        text="Delete"
      )

      DeleteBar = customtkinter.CTkEntry(SearchBarFrame)
      DeleteBar.grid(
        row=0,
        column=3,
        sticky="nsew",
        pady=10
      )
      DeleteBar.configure(
        width=100,
        placeholder_text="ID", 
      )

      RefreshButton = customtkinter.CTkButton(SearchBarFrame)
      RefreshButton.grid(
        row=0,
        column=4,
        sticky="nsew",
        pady=10,
        padx=5
      )
      RefreshButton.configure(
        command=self.refresh,
        width=100,
        text="Refresh"
      )

      AddStudentButton = customtkinter.CTkButton(SearchBarFrame)
      AddStudentButton.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )
      AddStudentButton.configure(
        command=self.addStudent,
        width=100,
        text="Add Student"
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
        HeaderLabel = customtkinter.CTkLabel(self.StudentsTableFrame)
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
        self.StudentsTableFrame.columnconfigure(col, weight=1)

      self.displayStudentsTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)