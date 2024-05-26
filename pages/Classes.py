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
            data_label = customtkinter.CTkLabel(self.Classess_table_frame, text=data, padx=10, pady=5)
            data_label.grid(row=row, column=col, sticky="nsew")
            self.ClassessLabels.append(data_label)

      self.results_count.configure(text="Results: " + str(len(self.Classes)))

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
      
      self.ClasseIDEntry.delete(0, customtkinter.END)
      self.SubjectEntry.delete(0, customtkinter.END)
      self.CatalogNBREntry.delete(0, customtkinter.END)
      self.AcademicCareerEntry.delete(0, customtkinter.END)
      self.OfferingNBREntry.delete(0, customtkinter.END)
      self.StartTimeEntry.delete(0, customtkinter.END)
      self.EndTimeEntry.delete(0, customtkinter.END)
      self.SectionEntry.delete(0, customtkinter.END)
      self.ComponentEntry.delete(0, customtkinter.END)
      self.CampusEntry.delete(0, customtkinter.END)
      self.InstructorIDEntry.delete(0, customtkinter.END)
      self.InstructorTypeEntry.delete(0, customtkinter.END)

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
      self.PopWindow.title("Add New Class")
      self.PopWindow.resizable(False, False)

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
        pady=5)
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
      search_button.configure(command=lambda: self.search(search_bar.get()))

      search_bar = customtkinter.CTkEntry(search_bar_frame)
      search_bar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )
      search_bar.configure(
        width=400,
        placeholder_text="Search for Classes..."
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
      delete_button.configure(command=lambda: self.delete(delete_bar.get()))

      delete_bar = customtkinter.CTkEntry(
        search_bar_frame,
        width=100,
        placeholder_text="ID"
      )
      delete_bar.grid(
        row=0,
        column=3,
        sticky="nsew",
        pady=10
      )

      reset_button = customtkinter.CTkButton(
        search_bar_frame,
        width=100,
        text="Refresh"
      )
      reset_button.grid(
        row=0,
        column=4,
        sticky="nsew",
        pady=10,
        padx=5
      )
      reset_button.configure(command=self.refresh)

      add_Classes_button = customtkinter.CTkButton(
        search_bar_frame,
        width=100,
        text="Add Class"
      )
      add_Classes_button.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )
      add_Classes_button.configure(command=self.addClasses)

      self.results_count = customtkinter.CTkLabel(search_bar_frame)
      self.results_count.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.Classess_table_frame = customtkinter.CTkFrame(parent)
      self.Classess_table_frame.pack(
        fill="x",
        expand=False
      )

      for col,header in enumerate(self.headers):
        header_label = customtkinter.CTkLabel(
          self.Classess_table_frame,
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
        self.Classess_table_frame.columnconfigure(col,weight=1)

      self.displayClassessTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)