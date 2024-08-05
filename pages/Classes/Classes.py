import sys
import os
import customtkinter

from DatabaseManager import DatabaseManager
from CTkMessagebox import CTkMessagebox

class Classes(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.ClassessLabels = []
      self.headers = [
        "Classe ID",
        "Subject",
        "Catalog NBR",	
        "Academic Career",	
        "Course ID",	
        "Course Offering NBR",	
        "Start Time",	
        "End Time",	
        "Section",	
        "Component",	
        "Campus",	
        "Instructor ID",	
        "Instructor Type"
      ]

      self.GetClasses()
      self.GetCourses()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def DisplayClassessTable(self):
    try:
      for label in self.ClassessLabels:
        label.destroy()

      if len(self.Classes) > 0:
        for row, Class in enumerate(self.Classes, start=1):
          ClasseID, \
          ClassSubjectArea, \
          ClasseCatalogNBR, \
          ClasseAcademicCareer, \
          ClasseCourseID, \
          ClasseCourseOfferingNBR, \
          ClasseSessionStartTime, \
          ClasseSessionEndTime, \
          ClasseSection, \
          ClasseComponent, \
          ClasseCampus, \
          ClasseInstructorID, \
          ClasseInstructorType, \
          CourseTitle = Class          

          ClassessData = [
            ClasseID,
            ClassSubjectArea,
            ClasseCatalogNBR,	
            ClasseAcademicCareer,	
            CourseTitle,	
            ClasseCourseOfferingNBR,	
            ClasseSessionStartTime,	
            ClasseSessionEndTime,	
            ClasseSection,	
            ClasseComponent,	
            ClasseCampus,	
            ClasseInstructorID,	
            ClasseInstructorType
          ]

          for col, data in enumerate(ClassessData):
            DataLabel = customtkinter.CTkLabel(
              self.ClassessTableFrame,
              text = data,
              padx = 10,
              pady = 5
            )
            DataLabel.grid(
              row = row,
              column = col,
              sticky = "nsew"
            )
            self.ClassessLabels.append(DataLabel)

            DeleteButton = customtkinter.CTkButton(
              self.ClassessTableFrame,
                text = "Delete",
                fg_color = "red",
                command = lambda cid = ClasseID: self.delete(cid),
              )
            DeleteButton.grid(
                row = row,
                column = len(ClassessData),
                sticky = "nsew",
                padx = 10,
                pady= 5
            )
            self.ClassessLabels.append(DeleteButton)

      self.ResultsCount.configure(
        text="Results: " + str(len(self.Classes))
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def refresh(self):
    try:
      self.GetClasses()
      self.DisplayClassessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def ValidateClassData(
      self,
      ClasseID,
      Subject,
      CatalogNBR,
      AcademicCareer,
      ClassesCourse,
      OfferingNBR,
      StartTime,
      EndTime,
      Section,
      Component,
      Campus,
      InstructorID,
      InstructorType
    ):
    try:
      if not ClasseID:
        title = "Missing Entry"
        message = "please enter classe ID"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not Subject:
        title = "Missing Entry"
        message = "please enter class subject"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not CatalogNBR or not CatalogNBR.isdigit():
        title = "Missing Entry"
        message = "please enter class catalog number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not AcademicCareer:
        title = "Missing Entry"
        message = "please enter class academic career"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not ClassesCourse:
        title = "Missing Entry"
        message = "please select classes course"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not OfferingNBR or not OfferingNBR.isdigit():
        title = "Missing Entry"
        message = "please enter class offering number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not StartTime:
        title = "Missing Entry"
        message = "please enter class start time"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not EndTime:
        title = "Missing Entry"
        message = "please enter class end time"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not Section:
        title = "Missing Entry"
        message = "please enter class section"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not Component:
        title = "Missing Entry"
        message = "please enter class component"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not Campus:
        title = "Missing Entry"
        message = "please enter class campus"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not InstructorID:
        title = "Missing Entry"
        message = "please select instructor"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not InstructorType:
        title = "Missing Entry"
        message = "please enter instructor type"
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

  def SaveClasses(self):
    try:
      if self.ValidateClassData(
        self.ClasseIDEntry.get(),
        self.SubjectEntry.get(),
        self.CatalogNBREntry.get(),
        self.AcademicCareerEntry.get(),
        self.course_id_title_map[self.ClassesCourseEntry.get()],
        self.OfferingNBREntry.get(),
        self.StartTimeEntry.get(),
        self.EndTimeEntry.get(),
        self.SectionEntry.get(),
        self.ComponentEntry.get(),
        self.CampusEntry.get(),
        self.InstructorIDEntry.get(),
        self.InstructorTypeEntry.get()     
      ):
        self.InsertClass(
          self.ClasseIDEntry.get(),
          self.SubjectEntry.get(),
          self.CatalogNBREntry.get(),
          self.AcademicCareerEntry.get(),
          self.course_id_title_map[self.ClassesCourseEntry.get()],
          self.OfferingNBREntry.get(),
          self.StartTimeEntry.get(),
          self.EndTimeEntry.get(),
          self.SectionEntry.get(),
          self.ComponentEntry.get(),
          self.CampusEntry.get(),
          self.InstructorIDEntry.get(),
          self.InstructorTypeEntry.get()
        )
        
        self.ClasseIDEntry.delete(
          0,
          customtkinter.END
        )
        self.SubjectEntry.delete(
          0,
          customtkinter.END
        )
        self.CatalogNBREntry.delete(
          0,
          customtkinter.END
        )
        self.AcademicCareerEntry.delete(
          0,
          customtkinter.END
        )
        self.OfferingNBREntry.delete(
          0,
          customtkinter.END
        )
        self.StartTimeEntry.delete(
          0,
          customtkinter.END
        )
        self.EndTimeEntry.delete(
          0,
          customtkinter.END
        )
        self.SectionEntry.delete(
          0,
          customtkinter.END
        )
        self.ComponentEntry.delete(
          0,
          customtkinter.END
        )
        self.CampusEntry.delete(
          0,
          customtkinter.END
        )
        self.InstructorIDEntry.delete(
          0,
          customtkinter.END
        )
        self.InstructorTypeEntry.delete(
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
      message = "Are you sure you want to delete the class"
      icon = "question"
      conformation = CTkMessagebox(
        title = title,
        message = message,
        icon = icon,
        option_1 = "yes",
        option_2 = "cancel" 
      )

      if conformation.get() == "yes":
        self.RemoveClass(term)
        self.GetClasses()
        self.DisplayClassessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def search(self, term):
    try:
      self.SearchClass(term)
      self.DisplayClassessTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def AddClasses(self):
    try:
      self.course_id_title_map = {x[1]: x[0] for x in DatabaseManager.Courses}

      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()

      self.PopWindow.geometry("520x550")
      self.PopWindow.resizable(False, False)

      self.PopWindow.title("Add New Class")

      ClasseIDLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Class ID:"
      )
      ClasseIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=5
      )

      self.ClasseIDEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.ClasseIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=5
      )

      SubjectLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Subject:"
      )
      SubjectLabel.grid(
        row=1,
        column=0,
        padx=10,
        pady=5
      )

      self.SubjectEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.SubjectEntry.grid(
        row=1,
        column=1,
        padx=10,
        pady=5
      )

      CatalogNBRLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Catalog NBR:"
      )
      CatalogNBRLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=5
      )

      self.CatalogNBREntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CatalogNBREntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=5
      )

      AcademicCareerLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Academic Career:"
      )
      AcademicCareerLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=5
      )

      self.AcademicCareerEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.AcademicCareerEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=5
      )

      OfferingNBRLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Course Offering NBR:"
      )
      OfferingNBRLabel.grid(
        row=5,
        column=0,
        padx=10,
        pady=5
      )

      self.OfferingNBREntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.OfferingNBREntry.grid(
        row=5,
        column=1,
        padx=10,
        pady=5
      )

      StartTimeLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Start Time:"
      )
      StartTimeLabel.grid(
        row=6,
        column=0,
        padx=10,
        pady=5
      )

      self.StartTimeEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.StartTimeEntry.grid(
        row=6,
        column=1,
        padx=10,
        pady=5
      )

      EndTimeLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="End Time:"
      )
      EndTimeLabel.grid(
        row=7,
        column=0,
        padx=10,
        pady=5
      )

      self.EndTimeEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.EndTimeEntry.grid(
        row=7,
        column=1,
        padx=10,
        pady=5
      )

      SectionLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Section:"
      )
      SectionLabel.grid(
        row=8,
        column=0,
        padx=10,
        pady=5
      )

      self.SectionEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.SectionEntry.grid(
        row=8,
        column=1,
        padx=10,
        pady=5
      )

      ComponentLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Component:"
      )
      ComponentLabel.grid(
        row=9,
        column=0,
        padx=10,
        pady=5
      )

      self.ComponentEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.ComponentEntry.grid(
        row=9,
        column=1,
        padx=10,
        pady=5
      )

      CampusLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Campus:"
      )
      CampusLabel.grid(
        row=10,
        column=0,
        padx=10,
        pady=5
      )

      self.CampusEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.CampusEntry.grid(
        row=10,
        column=1,
        padx=10,
        pady=5
      )

      InstructorIDLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Instructor ID:"
      )
      InstructorIDLabel.grid(
        row=11,
        column=0,
        padx=10,
        pady=5
      )

      self.InstructorIDEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.InstructorIDEntry.grid(
        row=11,
        column=1,
        padx=10,
        pady=5
      )

      InstructorTypeLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Instructor Type:"
      )
      InstructorTypeLabel.grid(
        row=12,
        column=0,
        padx=10,
        pady=5
      )

      self.InstructorTypeEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.InstructorTypeEntry.grid(
        row=12,
        column=1,
        padx=10,
        pady=5
      )

      ClassesCourseLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Course:"
      )
      ClassesCourseLabel.grid(
        row=13,
        column=0,
        padx=10,
        pady=5
      )

      self.ClassesCourseEntry = customtkinter.CTkComboBox(
        self.PopWindow,
        values=[x[1] for x in DatabaseManager.Courses],
        width=350
      )
      self.ClassesCourseEntry.grid(
        row=13,
        column=1,
        padx=10,
        pady=5
      )
      self.ClassesCourseEntry.set(DatabaseManager.Courses[0][1])

      SaveButton = customtkinter.CTkButton(
        self.PopWindow,
        text="Save Class",
        command=self.SaveClasses
      )
      SaveButton.grid(
        row=14,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=5
      )

    except Exception as e:
      ExceptionType,ExceptionObject,ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType,FileName,ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def create(self,parent):
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
        placeholder_text="Search for Classes..."
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

      AddClassesButton = customtkinter.CTkButton(
        SearchBarFrame,
        command=self.AddClasses,
        width=100,
        text="Add Class"
      )
      AddClassesButton.grid(
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

      self.ClassessTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.ClassessTableFrame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(
          self.ClassessTableFrame,
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
        self.ClassessTableFrame.columnconfigure(col, weight=1)

      self.DisplayClassessTable()


    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)