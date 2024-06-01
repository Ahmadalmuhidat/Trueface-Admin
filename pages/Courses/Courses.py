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

      self.getCourses()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

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
            DataLabel = customtkinter.CTkLabel(self.CoursessTableFrame)
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
            self.CoursessLabels.append(DataLabel)

      self.ResultsCount.configure(text="Results: " + str(len(DatabaseManager.Courses)))

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def refresh(self):
    try:
      self.getCourses()
      self.displayCoursessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def saveCourse(self):
    try:
      self.insertCourse(
        ID = self.CourseIDEntry.get(),
        title = self.CourseTitleEntry.get(),
        credit = self.CourseCreditEntry.get(),
        MaximumUnits = self.CourseMaximumUnitsEntry.get(),
        LongCourseTitle = self.CourseLongCourseTitleEntry.get(),
        OfferingNBR = self.CourseOfferingNBREntry.get(),
        AcademicGroup  = self.CourseAcademicGroupEntry.get(),
        SubjectArea = self.CourseSubjectAreaEntry.get(),
        CatalogNBR = self.CourseCatalogNBREntry.get(),
        campus = self.CourseCampusEntry.get(),
        AcademicOrganization = self.CourseAcademicOrganizationEntry.get(),
        component = self.CourseComponentEntry.get()
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
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def delete(self, term):
    try:
      self.deleteCourses(term)
      self.getCourses()
      self.displayCoursessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def search(self, term):
    try:
      self.searchCourses(term)
      self.displayCoursessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def addCourses(self):
    try:
      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()

      self.PopWindow.geometry("525x510")
      self.PopWindow.resizable(False, False)

      self.PopWindow.title("Add New Course")

      CourseIDLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=5
      )
      CourseIDLabel.configure(text="Course ID:")

      self.CourseIDEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseIDEntry.configure(width=350)

      CourseTitleLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseTitleLabel.grid(
        row=1, 
        column=0,
        padx=10,
        pady=5
      )
      CourseTitleLabel.configure(text="Title:")

      self.CourseTitleEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseTitleEntry.grid(
        row=1, 
        column=1, 
        padx=10, 
        pady=5
      )
      self.CourseTitleEntry.configure(width=350)

      CourseCreditLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseCreditLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=5
      )
      CourseCreditLabel.configure(text="Credit:")

      self.CourseCreditEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseCreditEntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseCreditEntry.configure(width=350)

      CourseMaximumUnitsLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseMaximumUnitsLabel.grid(
        row=3,
        column=0,
        padx=10,
        pady=5
      )
      CourseMaximumUnitsLabel.configure(text="Maximum Units:")

      self.CourseMaximumUnitsEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseMaximumUnitsEntry.grid(
        row=3,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseMaximumUnitsEntry.configure(width=350)

      CourseLongCourseTitleLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseLongCourseTitleLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=5
      )
      CourseLongCourseTitleLabel.configure(text="Long Course Title:")

      self.CourseLongCourseTitleEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseLongCourseTitleEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseLongCourseTitleEntry.configure(width=350)

      CourseOfferingNBRLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseOfferingNBRLabel.grid(
        row=5,
        column=0,
        padx=10,
        pady=5
      )
      CourseOfferingNBRLabel.configure(text="Offering NBR:")

      self.CourseOfferingNBREntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseOfferingNBREntry.grid(
        row=5,
        column=1,
        padx=10,
        pady=5)
      self.CourseOfferingNBREntry.configure(width=350)

      CourseAcademicGroupLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseAcademicGroupLabel.grid(
        row=6,
        column=0,
        padx=10,
        pady=5
      )
      CourseAcademicGroupLabel.configure(text="Academic Group:")
      
      self.CourseAcademicGroupEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseAcademicGroupEntry.grid(
        row=6,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseAcademicGroupEntry.configure(width=350)

      CourseSubjectAreaLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseSubjectAreaLabel.grid(
        row=7,
        column=0,
        padx=10,
        pady=5
      )
      CourseSubjectAreaLabel.configure(text="Subject Area:")
      
      self.CourseSubjectAreaEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseSubjectAreaEntry.grid(
        row=7,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseSubjectAreaEntry.configure(width=350)

      CourseCatalogNBRLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseCatalogNBRLabel.grid(
        row=8,
        column=0,
        padx=10,
        pady=5
      )
      CourseCatalogNBRLabel.configure(text="Catalog NBR:")
      
      self.CourseCatalogNBREntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseCatalogNBREntry.grid(
        row=8,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseCatalogNBREntry.configure(width=350)

      CourseCampusLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseCampusLabel.grid(
        row=9,
        column=0,
        padx=10,
        pady=5
      )
      CourseCampusLabel.configure(text="Campus:")

      self.CourseCampusEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseCampusEntry.grid(
        row=9,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseCampusEntry.configure(width=350)

      CourseAcademicOrganizationLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseAcademicOrganizationLabel.grid(
        row=10,
        column=0,
        padx=10,
        pady=5
      )
      CourseAcademicOrganizationLabel.configure(text="Academic Organization:")

      self.CourseAcademicOrganizationEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseAcademicOrganizationEntry.grid(
        row=10,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseAcademicOrganizationEntry.configure(width=350)

      CourseComponentLabel = customtkinter.CTkLabel(self.PopWindow)
      CourseComponentLabel.grid(
        row=11,
        column=0,
        padx=10,
        pady=5
      )
      CourseComponentLabel.configure(text="Component:")

      self.CourseComponentEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CourseComponentEntry.grid(
        row=11,
        column=1,
        padx=10,
        pady=5
      )
      self.CourseComponentEntry.configure(width=350)

      SaveButton = customtkinter.CTkButton(self.PopWindow)
      SaveButton.grid(
        row=12,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=5
      )
      SaveButton.configure(
        text="Save Course",
        command=self.saveCourse,
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
        command=lambda: self.search(SearchBar.get()),
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
        placeholder_text="Search for Courses..."
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
        command=lambda: self.delete(DeleteBar.get()),
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
        placeholder_text="ID"
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

      AddCoursesButton = customtkinter.CTkButton(SearchBarFrame)
      AddCoursesButton.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )
      AddCoursesButton.configure(
        command=self.addCourses,
        width=100,
        text="Add Course"
      )

      self.ResultsCount = customtkinter.CTkLabel(SearchBarFrame)
      self.ResultsCount.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.CoursessTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.CoursessTableFrame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(self.CoursessTableFrame)
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
        self.CoursessTableFrame.columnconfigure(col, weight=1)

      self.displayCoursessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)