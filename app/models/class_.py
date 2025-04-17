import sys
import os
import app.config.configrations as Configrations

from CTkMessagebox import CTkMessagebox

class Class:
  def __init__(self, classID, SubjectArea, CatalogNBR, AcademicCareer, Course, OfferingNBR, StartTime, EndTime, Section, Component, Campus, InstructorID, InstructorType):
    self.ClassID = classID
    self.SubjectArea = SubjectArea
    self.CatalogNBR = CatalogNBR
    self.AcademicCareer = AcademicCareer
    self.Course = Course
    self.OfferingNBR = OfferingNBR
    self.StartTime = StartTime
    self.EndTime = EndTime
    self.Section = Section
    self.Component = Component
    self.Campus = Campus
    self.InstructorID = InstructorID
    self.InstructorType = InstructorType

    self.config  = Configrations.Configrations()

    self.Students = []

  def ValidateClassData(self):
    try:
      if not self.ClassID:
        title = "Missing Entry"
        message = "please enter classe ID"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.SubjectArea:
        title = "Missing Entry"
        message = "please enter class subject"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.CatalogNBR or not self.CatalogNBR.isdigit():
        title = "Missing Entry"
        message = "please enter class catalog number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.AcademicCareer:
        title = "Missing Entry"
        message = "please enter class academic career"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.Course:
        title = "Missing Entry"
        message = "please select class course"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.OfferingNBR or not self.OfferingNBR.isdigit():
        title = "Missing Entry"
        message = "please enter class offering number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.StartTime:
        title = "Missing Entry"
        message = "please enter class start time"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.EndTime:
        title = "Missing Entry"
        message = "please enter class end time"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.Section:
        title = "Missing Entry"
        message = "please enter class section"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.Component:
        title = "Missing Entry"
        message = "please enter class component"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.Campus:
        title = "Missing Entry"
        message = "please enter class campus"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.InstructorID:
        title = "Missing Entry"
        message = "please select instructor"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.InstructorType:
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
