import sys
import os
import customtkinter

from DatabaseManager import DatabaseManager
from CTkMessagebox import CTkMessagebox

class Courses(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.CoursesLabels = []
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

  def DisplayCoursessTable(self):
    try:
      for label in self.CoursesLabels:
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

          CoursesData = [
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

          for col, data in enumerate(CoursesData):
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
            self.CoursesLabels.append(DataLabel)

            DeleteButton = customtkinter.CTkButton(
              self.CoursesTableFrame,
                text = "Delete",
                fg_color = "red",
                command = lambda cid = CourseID: self.delete(cid)
              )
            DeleteButton.grid(
                row = row,
                column = len(CoursesData),
                sticky = "nsew",
                padx = 10,
                pady= 5
            )
            self.CoursesLabels.append(DeleteButton)

      self.ResultsCount.configure(text="Results: " + str(len(DatabaseManager.Courses)))

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def refresh(self):
    try:
      self.GetCourses()
      self.DisplayCoursessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def ValidateCourseData(
      self,
      CourseID,
      CourseTitle,
      CourseCredit,
      CourseMaximumUnits,
      CourseLongTitle,
      CourseOfferingNBR,
      CourseAcademicGroup,
      CourseSubjectArea,
      CourseCatalogNBR,
      CourseCampus,
      CourseAcademicOrganization,
      CourseComponent
    ):
    try:
      if not CourseID:
        title = "Missing Entry"
        message = "please enter course ID"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseTitle:
        title = "Missing Entry"
        message = "please enter course title"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseCredit or not CourseCredit.isdigit():
        title = "Missing Entry"
        message = "please enter course credit number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseMaximumUnits or not CourseMaximumUnits.isdigit():
        title = "Missing Entry"
        message = "please enter course maximum units number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseLongTitle:
        title = "Missing Entry"
        message = "please enter course long title"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseOfferingNBR or not CourseOfferingNBR.isdigit():
        title = "Missing Entry"
        message = "please enter course offering number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseAcademicGroup:
        title = "Missing Entry"
        message = "please enter course academic group"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseSubjectArea:
        title = "Missing Entry"
        message = "please enter course subject area"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseCatalogNBR or not CourseCatalogNBR.isdigit():
        title = "Missing Entry"
        message = "please enter course catalog number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseCampus:
        title = "Missing Entry"
        message = "please enter course campus"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseAcademicOrganization:
        title = "Missing Entry"
        message = "please enter course academic organization"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CourseComponent:
        title = "Missing Entry"
        message = "please enter course component"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False

      return True

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def SaveCourse(self):
    try:
      if self.ValidateCourseData(
        self.CourseIDEntry.get(),
        self.CourseTitleEntry.get(),
        self.CourseCreditEntry.get(),
        self.CourseMaximumUnitsEntry.get(),
        self.CourseLongTitleEntry.get(),
        self.CourseOfferingNBREntry.get(),
        self.CourseAcademicGroupEntry.get(),
        self.CourseSubjectAreaEntry.get(),
        self.CourseCatalogNBREntry.get(),
        self.CourseCampusEntry.get(),
        self.CourseAcademicOrganizationEntry.get(),
        self.CourseComponentEntry.get()
      ):
        self.InsertCourse(
          self.CourseIDEntry.get(),
          self.CourseTitleEntry.get(),
          self.CourseCreditEntry.get(),
          self.CourseMaximumUnitsEntry.get(),
          self.CourseLongTitleEntry.get(),
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
        self.CourseLongTitleEntry.delete(
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
      title = "Conformation"
      message = "Are you sure you want to delete the course"
      icon = "question"
      conformation = CTkMessagebox(
        title = title,
        message = message,
        icon = icon,
        option_1 = "yes",
        option_2 = "cancel" 
      )

      if conformation.get() == "yes":
        self.RemoveCourse(term)
        self.GetCourses()
        self.DisplayCoursessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def search(self, term):
    try:
      self.SearchCourses(term)
      self.DisplayCoursessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def addCourses(self):
    try:
      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()

      self.PopWindow.geometry("535x510")
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

      self.CourseLongTitleEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseLongTitleEntry.grid(
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
        command=self.SaveCourse,
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

      self.DisplayCoursessTable()


    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)