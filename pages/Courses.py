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
        for row, Courses in enumerate(DatabaseManager.Courses, start=1):
          CourseID, CourseTitle, CourseCredit, CourseMaximumUnits, CourseLongCourseTitle,	CourseOfferingNBR, CourseAcademicGroup,	CourseSubjectArea, CourseCatalogNBR, CourseCampus, CourseAcademicOrganizatio, CourseComponent = Courses
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
            data_label = customtkinter.CTkLabel(
              self.Coursess_table_frame,
              text=data,
              padx=10, 
              pady=5
            )
            data_label.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            self.CoursessLabels.append(data_label)

      self.results_count.configure(text="Results: " + str(len(DatabaseManager.Courses)))

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

      self.CourseIDEntry.delete(0, customtkinter.END)
      self.CourseTitleEntry.delete(0, customtkinter.END)
      self.CourseCreditEntry.delete(0, customtkinter.END)
      self.CourseMaximumUnitsEntry.delete(0, customtkinter.END)
      self.CourseLongCourseTitleEntry.delete(0, customtkinter.END)
      self.CourseOfferingNBREntry.delete(0, customtkinter.END)
      self.CourseAcademicGroupEntry.delete(0, customtkinter.END)
      self.CourseSubjectAreaEntry.delete(0, customtkinter.END)
      self.CourseCatalogNBREntry.delete(0, customtkinter.END)
      self.CourseCampusEntry.delete(0, customtkinter.END)
      self.CourseAcademicOrganizationEntry.delete(0, customtkinter.END)
      self.CourseComponentEntry.delete(0, customtkinter.END)

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
      self.PopWindow = customtkinter.CTk()
      self.PopWindow.geometry("525x750")
      self.PopWindow.title("Add New Course")
      self.PopWindow.resizable(False, False)

      CourseIDLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Course ID:"
      )
      CourseIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=15
      )
      self.CourseIDEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=15
      )

      CourseTitleLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Title:"
      )
      CourseTitleLabel.grid(
        row=1, 
        column=0,
        padx=10,
        pady=15
      )
      self.CourseTitleEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CourseTitleEntry.grid(
        row=1, 
        column=1, 
        padx=10, 
        pady=15
      )

      CourseCreditLabel = customtkinter.CTkLabel(self.PopWindow, text="Credit:")
      CourseCreditLabel.grid(row=2, column=0, padx=10, pady=15)
      self.CourseCreditEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseCreditEntry.grid(row=2, column=1, padx=10, pady=15)

      CourseMaximumUnitsLabel = customtkinter.CTkLabel(self.PopWindow, text="Maximum Units:")
      CourseMaximumUnitsLabel.grid(row=3, column=0, padx=10, pady=15)
      self.CourseMaximumUnitsEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseMaximumUnitsEntry.grid(row=3, column=1, padx=10, pady=15)

      CourseLongCourseTitleLabel = customtkinter.CTkLabel(self.PopWindow, text="Long Course Title:")
      CourseLongCourseTitleLabel.grid(row=4, column=0, padx=10, pady=15)
      self.CourseLongCourseTitleEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseLongCourseTitleEntry.grid(row=4, column=1, padx=10, pady=15)

      CourseOfferingNBRLabel = customtkinter.CTkLabel(self.PopWindow, text="Offering NBR:")
      CourseOfferingNBRLabel.grid(row=5, column=0, padx=10, pady=15)
      self.CourseOfferingNBREntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseOfferingNBREntry.grid(row=5, column=1, padx=10, pady=15)

      CourseAcademicGroupLabel = customtkinter.CTkLabel(self.PopWindow, text="Academic Group:")
      CourseAcademicGroupLabel.grid(row=6, column=0, padx=10, pady=15)
      self.CourseAcademicGroupEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseAcademicGroupEntry.grid(row=6, column=1, padx=10, pady=15)

      CourseSubjectAreaLabel = customtkinter.CTkLabel(self.PopWindow, text="Subject Area:")
      CourseSubjectAreaLabel.grid(row=7, column=0, padx=10, pady=15)
      self.CourseSubjectAreaEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseSubjectAreaEntry.grid(row=7, column=1, padx=10, pady=15)

      CourseCatalogNBRLabel = customtkinter.CTkLabel(self.PopWindow, text="Catalog NBR:")
      CourseCatalogNBRLabel.grid(row=8, column=0, padx=10, pady=15)
      self.CourseCatalogNBREntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseCatalogNBREntry.grid(row=8, column=1, padx=10, pady=15)

      CourseCampusLabel = customtkinter.CTkLabel(self.PopWindow, text="Campus:")
      CourseCampusLabel.grid(row=9, column=0, padx=10, pady=15)
      self.CourseCampusEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseCampusEntry.grid(row=9, column=1, padx=10, pady=15)

      CourseAcademicOrganizationLabel = customtkinter.CTkLabel(self.PopWindow, text="Academic Organization:")
      CourseAcademicOrganizationLabel.grid(row=10, column=0, padx=10, pady=15)
      self.CourseAcademicOrganizationEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseAcademicOrganizationEntry.grid(row=10, column=1, padx=10, pady=15)

      CourseComponentLabel = customtkinter.CTkLabel(self.PopWindow, text="Component:")
      CourseComponentLabel.grid(row=11, column=0, padx=10, pady=15)
      self.CourseComponentEntry = customtkinter.CTkEntry(self.PopWindow, width=350)
      self.CourseComponentEntry.grid(row=11, column=1, padx=10, pady=15)

      SaveButton = customtkinter.CTkButton(self.PopWindow, width=350)
      SaveButton.grid(row=12, columnspan=2, sticky="nsew", padx=10, pady=15)
      SaveButton.configure(text="Save Course", command=self.saveCourse)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def create(self, parent):
    try:
      search_bar_frame = customtkinter.CTkFrame(parent, bg_color="transparent")
      search_bar_frame.pack(fill="x", expand=False)

      search_button = customtkinter.CTkButton(search_bar_frame, text="Search")
      search_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=5)
      search_button.configure(command=lambda: self.search(search_bar.get()))

      search_bar = customtkinter.CTkEntry(search_bar_frame)
      search_bar.grid(row=0, column=1, sticky="nsew", pady=10)
      search_bar.configure(width=400, placeholder_text="Search for Courses...")

      delete_button = customtkinter.CTkButton(search_bar_frame, width=100, text="Delete")
      delete_button.grid(row=0, column=2, sticky="nsew", pady=10, padx=5)
      delete_button.configure(command=lambda: self.delete(delete_bar.get()))

      delete_bar = customtkinter.CTkEntry(search_bar_frame, width=100, placeholder_text="ID")
      delete_bar.grid(row=0, column=3, sticky="nsew", pady=10)

      reset_button = customtkinter.CTkButton(search_bar_frame, width=100, text="Refresh")
      reset_button.grid(row=0, column=4, sticky="nsew", pady=10, padx=5)
      reset_button.configure(command=self.refresh)

      add_Courses_button = customtkinter.CTkButton(search_bar_frame, width=100, text="Add Course")
      add_Courses_button.grid(row=0, column=5, sticky="nsew", pady=10, padx=5)
      add_Courses_button.configure(command=self.addCourses)

      self.results_count = customtkinter.CTkLabel(search_bar_frame)
      self.results_count.grid(row=0, column=6, padx=10, pady=5)

      self.Coursess_table_frame = customtkinter.CTkFrame(parent)
      self.Coursess_table_frame.pack(fill="x", expand=False)

      for col, header in enumerate(self.headers):
        header_label = customtkinter.CTkLabel(self.Coursess_table_frame, text=header, padx=10, pady=10)
        header_label.grid(row=0, column=col, sticky="nsew")
  
      for col in range(len(self.headers)):
        self.Coursess_table_frame.columnconfigure(col, weight=1)

      self.displayCoursessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)