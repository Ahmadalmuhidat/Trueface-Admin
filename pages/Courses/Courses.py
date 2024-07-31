import sys
import os
import customtkinter

from DatabaseManager import DatabaseManager

class Courses(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.CoursessLabels = []
      self.headers = [
        "Course ID",
        "Course Title",
        "Course Credit",
        "Maximum Units",
        "Long Course Title",
        "Offering NBR",
        "Academic Group",
        "Subject Area",
        "Catalog NBR",
        "Campus",
        "Academic Organizatio",
        "Component"
      ]

      self.GetCourses()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def displayCoursessTable(self):
    try:
      for label in self.CoursessLabels:
        label.destroy()

      if len(DatabaseManager.Courses) > 0:
        for row, Courses in enumerate(DatabaseManager.Courses, start = 1):
          CourseID, \
          CourseTitle, \
          CourseCredit, \
          CourseMaximumUnits, \
          CourseLongCourseTitle, \
          CourseOfferingNBR, \
          CourseAcademicGroup, \
          CourseSubjectArea, \
          CourseCatalogNBR, \
          CourseCampus, \
          CourseAcademicOrganizatio, \
          CourseComponent = Courses

          Coursess_data = [
            CourseID,
            CourseTitle,
            CourseCredit,
            CourseMaximumUnits,
            CourseLongCourseTitle,
            CourseOfferingNBR,
            CourseAcademicGroup,
            CourseSubjectArea,
            CourseCatalogNBR,
            CourseCampus,
            CourseAcademicOrganizatio,
            CourseComponent
          ]

          for col, data in enumerate(Coursess_data):
            DataLabel = customtkinter.CTkLabel(
            self.CoursesTableFrame,
             text=data,
              padx=10,
              pady=5
            )
            DataLabel.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            self.CoursessLabels.append(DataLabel)

      self.ResultsCount.configure(text="Results: " + str(len(DatabaseManager.Courses)))

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def refresh(self):
    try:
      self.GetCourses()
      self.displayCoursessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def saveCourse(self):
    try:
      self.InsertCourse(
        self.CourseIDEntry.get(),
        self.CourseTitleEntry.get(),
        self.CourseCreditEntry.get(),
        self.CourseMaximumUnitsEntry.get(),
        self.CourseLongCourseTitleEntry.get(),
        self.CourseOfferingNBREntry.get(),
        self.CourseAcademicGroupEntry.get(),
        self.CourseSubjectAreaEntry.get(),
        self.CourseCatalogNBREntry.get(),
        self.CourseCampusEntry.get(),
        self.CourseAcademicOrganizationEntry.get(),
        self.CourseComponentEntry.get()
      )

      self.CourseIDEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseTitleEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseCreditEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseMaximumUnitsEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseLongCourseTitleEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseOfferingNBREntry.delete(
        0,
        customtkinter.END
      )
      self.CourseAcademicGroupEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseSubjectAreaEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseCatalogNBREntry.delete(
        0,
        customtkinter.END
      )
      self.CourseCampusEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseAcademicOrganizationEntry.delete(
        0,
        customtkinter.END
      )
      self.CourseComponentEntry.delete(
        0,
        customtkinter.END
      )

      self.refresh()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def delete(self, term):
    try:
      self.DeleteCourses(term)
      self.GetCourses()
      self.displayCoursessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def search(self, term):
    try:
      self.SearchCourses(term)
      self.displayCoursessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def addCourses(self):
    try:
      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()

      self.PopWindow.geometry("525x510")
      self.PopWindow.resizable(False, False)

      self.PopWindow.title("Add New Course")

      CourseIDLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Course ID:"
      )
      CourseIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseIDEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=5
      )

      CourseTitleLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Title:"
      )
      CourseTitleLabel.grid(
        row=1, 
        column=0,
        padx=10,
        pady=5
      )

      self.CourseTitleEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseTitleEntry.grid(
        row=1, 
        column=1, 
        padx=10, 
        pady=5
      )

      CourseCreditLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Credit:"
      )
      CourseCreditLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseCreditEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseCreditEntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=5
      )

      CourseMaximumUnitsLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Maximum Units:"
      )
      CourseMaximumUnitsLabel.grid(
        row=3,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseMaximumUnitsEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseMaximumUnitsEntry.grid(
        row=3,
        column=1,
        padx=10,
        pady=5
      )

      CourseLongCourseTitleLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Long Course Title:"
      )
      CourseLongCourseTitleLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseLongCourseTitleEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseLongCourseTitleEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=5
      )

      CourseOfferingNBRLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Offering NBR:"
      )
      CourseOfferingNBRLabel.grid(
        row=5,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseOfferingNBREntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseOfferingNBREntry.grid(
        row=5,
        column=1,
        padx=10,
        pady=5
      )

      CourseAcademicGroupLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Academic Group:"
      )
      CourseAcademicGroupLabel.grid(
        row=6,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseAcademicGroupEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseAcademicGroupEntry.grid(
        row=6,
        column=1,
        padx=10,
        pady=5
      )

      CourseSubjectAreaLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Subject Area:"
      )
      CourseSubjectAreaLabel.grid(
        row=7,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseSubjectAreaEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseSubjectAreaEntry.grid(
        row=7,
        column=1,
        padx=10,
        pady=5
      )

      CourseCatalogNBRLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Catalog NBR:"
      )
      CourseCatalogNBRLabel.grid(
        row=8,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseCatalogNBREntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseCatalogNBREntry.grid(
        row=8,
        column=1,
        padx=10,
        pady=5
      )

      CourseCampusLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Campus:"
      )
      CourseCampusLabel.grid(
        row=9,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseCampusEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseCampusEntry.grid(
        row=9,
        column=1,
        padx=10,
        pady=5
      )

      CourseAcademicOrganizationLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Academic Organization:"
      )
      CourseAcademicOrganizationLabel.grid(
        row=10,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseAcademicOrganizationEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseAcademicOrganizationEntry.grid(
        row=10,
        column=1,
        padx=10,
        pady=5
      )

      CourseComponentLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Component:"
      )
      CourseComponentLabel.grid(
        row=11,
        column=0,
        padx=10,
        pady=5
      )

      self.CourseComponentEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseComponentEntry.grid(
        row=11,
        column=1,
        padx=10,
        pady=5
      )

      SaveButton = customtkinter.CTkButton(
        self.PopWindow,
        text="Save Course",
        command=self.saveCourse,
        width=350
      )
      SaveButton.grid(
        row=12,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=5
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
        placeholder_text="Search for Courses..."
      )
      SearchBar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )

      DeleteButton = customtkinter.CTkButton(
        SearchBarFrame,
        command=lambda: self.delete(DeleteBar.get()),
        width=100,
        text="Delete"
      )
      DeleteButton.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=10,
        padx=5
      )

      DeleteBar = customtkinter.CTkEntry(
        SearchBarFrame,
        width=100,
        placeholder_text="ID"
      )
      DeleteBar.grid(
        row=0,
        column=3,
        sticky="nsew",
        pady=10
      )

      RefreshButton = customtkinter.CTkButton(
        SearchBarFrame,
        command=self.refresh,
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

      AddCoursesButton = customtkinter.CTkButton(
        SearchBarFrame,
        command=self.addCourses,
        width=100,
        text="Add Course"
      )
      AddCoursesButton.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )

      self.ResultsCount = customtkinter.CTkLabel(
        SearchBarFrame
      )
      self.ResultsCount.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.CoursesTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.CoursesTableFrame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
          HeaderLabel = customtkinter.CTkLabel(
            self.CoursesTableFrame,
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
        self.CoursesTableFrame.columnconfigure(col, weight=1)

      self.displayCoursessTable()


    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)