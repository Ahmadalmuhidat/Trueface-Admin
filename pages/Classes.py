import sys
import os
import customtkinter

from DatabaseManager import DatabaseManager

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

      self.getClasses()
      self.getCourses()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def displayClassessTable(self):
    try:
      for label in self.ClassessLabels:
        label.destroy()

      if len(self.Classes) > 0:
        for row, Classes in enumerate(self.Classes, start=1):
          ClasseID, ClassSubjectArea, ClasseCatalogNBR,	ClasseAcademicCareer, ClasseCourseID,	ClasseCourseOfferingNBR,	ClasseSessionStartTime,	ClasseSessionEndTime,	ClasseSection,	ClasseComponent,	ClasseCampus,	ClasseInstructorID,	ClasseInstructorType, CourseTitle = Classes          
          Classess_data = [
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

          for col, data in enumerate(Classess_data):
            DataLabel = customtkinter.CTkLabel(self.ClassessTableFrame)
            DataLabel.grid(row=row, column=col, sticky="nsew")
            DataLabel.configure(
              text=data,
              padx=10,
              pady=5
            )
            self.ClassessLabels.append(DataLabel)

      self.ResultsCount.configure(
        text="Results: " + str(len(self.Classes))
      )

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def refresh(self):
    try:
      self.getClasses()
      self.displayClassessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def saveClasses(self):
    try:
      self.insertClass(
        ID = self.ClasseIDEntry.get(),
        subject = self.SubjectEntry.get(),
        CNBR = self.CatalogNBREntry.get(),
        AC = self.AcademicCareerEntry.get(),
        CID = self.course_id_title_map[self.ClassesCourseEntry.get()],
        ONBR = self.OfferingNBREntry.get(),
        ST = self.StartTimeEntry.get(),
        ET = self.EndTimeEntry.get(),
        section = self.SectionEntry.get(),
        component = self.ComponentEntry.get(),
        campus = self.CampusEntry.get(),
        instructorID = self.InstructorIDEntry.get(),
        IT = self.InstructorTypeEntry.get()
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
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def delete(self, term):
    try:
      self.deleteClasse(term)
      self.getClasses()
      self.displayClassessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def search(self, term):
    try:
      self.searchClasse(term)
      self.displayClassessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def addClasses(self):
    try:
      self.course_id_title_map = {x[1]: x[0] for x in DatabaseManager.Courses}

      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()

      self.PopWindow.geometry("515x550")
      self.PopWindow.resizable(False, False)

      self.PopWindow.title("Add New Class")

      ClasseIDLabel = customtkinter.CTkLabel(self.PopWindow)
      ClasseIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=5
      )
      ClasseIDLabel.configure(text="Class ID:")

      self.ClasseIDEntry = customtkinter.CTkEntry(self.PopWindow)
      self.ClasseIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=5
      )
      self.ClasseIDEntry.configure(width=350)

      SubjectLabel = customtkinter.CTkLabel(self.PopWindow)
      SubjectLabel.grid(
        row=1,
        column=0,
        padx=10,
        pady=5
      )
      SubjectLabel.configure(text="Subject:")

      self.SubjectEntry = customtkinter.CTkEntry(self.PopWindow)
      self.SubjectEntry.grid(
        row=1,
        column=1,
        padx=10,
        pady=5
      )
      self.SubjectEntry.configure(width=350)

      CatalogNBRLabel = customtkinter.CTkLabel(self.PopWindow)
      CatalogNBRLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=5
      )
      CatalogNBRLabel.configure(text="Catalog NBR:")

      self.CatalogNBREntry = customtkinter.CTkEntry(self.PopWindow)
      self.CatalogNBREntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=5
      )
      self.CatalogNBREntry.configure(width=350)

      AcademicCareerLabel = customtkinter.CTkLabel(self.PopWindow)
      AcademicCareerLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=5
      )
      AcademicCareerLabel.configure(text="Academic Career:")

      self.AcademicCareerEntry = customtkinter.CTkEntry(self.PopWindow)
      self.AcademicCareerEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=5
      )
      self.AcademicCareerEntry.configure(width=350)

      OfferingNBRLabel = customtkinter.CTkLabel(self.PopWindow)
      OfferingNBRLabel.grid(
        row=5,
        column=0,
        padx=10,
        pady=5
      )
      OfferingNBRLabel.configure(text="Course Offering NBR:")

      self.OfferingNBREntry = customtkinter.CTkEntry(self.PopWindow)
      self.OfferingNBREntry.grid(
        row=5,
        column=1,
        padx=10,
        pady=5
      )
      self.OfferingNBREntry.configure(width=350)

      StartTimeLabel = customtkinter.CTkLabel(self.PopWindow)
      StartTimeLabel.grid(
        row=6,
        column=0,
        padx=10,
        pady=5
      )
      StartTimeLabel.configure(text="Start Time:")

      self.StartTimeEntry = customtkinter.CTkEntry(self.PopWindow)
      self.StartTimeEntry.grid(
        row=6,
        column=1,
        padx=10,
        pady=5
      )
      self.StartTimeEntry.configure(width=350)

      EndTimeLabel = customtkinter.CTkLabel(self.PopWindow)
      EndTimeLabel.grid(
        row=7,
        column=0,
        padx=10,
        pady=5
      )
      EndTimeLabel.configure(text="End Time:")

      self.EndTimeEntry = customtkinter.CTkEntry(self.PopWindow)
      self.EndTimeEntry.grid(
        row=7,
        column=1,
        padx=10,
        pady=5
      )
      self.EndTimeEntry.configure(width=350)

      SectionLabel = customtkinter.CTkLabel(self.PopWindow)
      SectionLabel.grid(
        row=8,
        column=0,
        padx=10,
        pady=5
      )
      SectionLabel.configure(text="Section:")

      self.SectionEntry = customtkinter.CTkEntry(self.PopWindow)
      self.SectionEntry.grid(
        row=8,
        column=1,
        padx=10,
        pady=5
      )
      self.SectionEntry.configure(width=350)

      ComponentLabel = customtkinter.CTkLabel(self.PopWindow)
      ComponentLabel.grid(
        row=9,
        column=0,
        padx=10,
        pady=5
      )
      ComponentLabel.configure(text="Component:")

      self.ComponentEntry = customtkinter.CTkEntry(self.PopWindow)
      self.ComponentEntry.grid(
        row=9,
        column=1,
        padx=10,
        pady=5
      )
      self.ComponentEntry.configure(width=350)

      CampusLabel = customtkinter.CTkLabel(self.PopWindow)
      CampusLabel.grid(
        row=10,
        column=0,
        padx=10,
        pady=5
      )
      CampusLabel.configure(text="Campus:")

      self.CampusEntry = customtkinter.CTkEntry(self.PopWindow)
      self.CampusEntry.grid(
        row=10,
        column=1,
        padx=10,
        pady=5
      )
      self.CampusEntry.configure(width=350)

      InstructorIDLabel = customtkinter.CTkLabel(self.PopWindow)
      InstructorIDLabel.grid(
        row=11,
        column=0,
        padx=10,
        pady=5
      )
      InstructorIDLabel.configure(text="Instructor ID:")

      self.InstructorIDEntry = customtkinter.CTkEntry(self.PopWindow)
      self.InstructorIDEntry.grid(
        row=11,
        column=1,
        padx=10,
        pady=5
      )
      self.InstructorIDEntry.configure(width=350)

      InstructorTypeLabel = customtkinter.CTkLabel(self.PopWindow)
      InstructorTypeLabel.grid(
        row=12,
        column=0,
        padx=10,
        pady=5
      )
      InstructorTypeLabel.configure(text="Instructor Type:")

      self.InstructorTypeEntry = customtkinter.CTkEntry(self.PopWindow)
      self.InstructorTypeEntry.grid(
        row=12,
        column=1,
        padx=10,
        pady=5
      )
      self.InstructorTypeEntry.configure(width=350)

      ClassesCourseLabel = customtkinter.CTkLabel(self.PopWindow)
      ClassesCourseLabel.grid(
        row=13,
        column=0,
        padx=10,
        pady=5
      )
      ClassesCourseLabel.configure(text="Course:")

      self.ClassesCourseEntry = customtkinter.CTkComboBox(self.PopWindow)
      self.ClassesCourseEntry.grid(
        row=13,
        column=1,
        padx=10,
        pady=5
      )
      self.ClassesCourseEntry.configure(
        values=[x[1] for x in DatabaseManager.Courses],
        width=350
      )
      self.ClassesCourseEntry.set(DatabaseManager.Courses[0][1])

      SaveButton = customtkinter.CTkButton(self.PopWindow)
      SaveButton.grid(
        row=14,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=5
      )
      SaveButton.configure(
        text="Save Class",
        command=self.saveClasses
      )

    except Exception as e:
      exc_type,exc_obj,exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type,fname,exc_tb.tb_lineno)
      print(exc_obj)

  def create(self,parent):
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
        placeholder_text="Search for Classes..."
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

      AddClassesButton = customtkinter.CTkButton(SearchBarFrame)
      AddClassesButton.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )
      AddClassesButton.configure(
        command=self.addClasses,
        width=100,
        text="Add Class"
      )

      self.ResultsCount = customtkinter.CTkLabel(SearchBarFrame)
      self.ResultsCount.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.ClassessTableFrame = customtkinter.CTkFrame(parent)
      self.ClassessTableFrame.pack(
        fill="x",
        expand=False
      )

      for col,header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(self.ClassessTableFrame)
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
        self.ClassessTableFrame.columnconfigure(col,weight=1)

      self.displayClassessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)