import sys
import os
import requests
import json

from CTkMessagebox import CTkMessagebox
import Configrations

class Class:
  def __init__(self, ID, SubjectArea, CatalogNBR, AcademicCareer, CourseID, CourseOfferingNBR, SessionStartTime, SessionEndTime, Section, Component, Campus, InstructorID, InstructorType, CourseTitle):
    self.ID = ID
    self.SubjectArea = SubjectArea
    self.CatalogNBR = CatalogNBR
    self.AcademicCareer = AcademicCareer
    self.CourseID = CourseID
    self.OfferingNBR = CourseOfferingNBR
    self.SessionStartTime = SessionStartTime
    self.SessionEndTime = SessionEndTime
    self.Section = Section
    self.Component = Component
    self.Campus = Campus
    self.InstructorID = InstructorID
    self.InstructorType = InstructorType
    self.CourseTitle = CourseTitle

    self.config  = Configrations.Configrations()

    self.Students = []
  
  def Add(self):
    try:
      data = {
        "ClassID": self.ID,
        "subject": self.SubjectArea,
        "CatalogNBR": self.CatalogNBR,
        "AcademicCareer": self.AcademicCareer,
        "CourseID": self.CourseID,
        "OfferingNBR": self.OfferingNBR,
        "StartTime": self.SessionStartTime,
        "EndTime": self.SessionEndTime,
        "section": self.Section,
        "component": self.Component,
        "campus": self.Campus,
        "instructorID": self.InstructorID,
        "InstructorType": self.InstructorType
      }

      response = requests.post(
        self.config.getBaseURL() + "/admin/insert_class",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while inserting the class",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass 

  def Remove(self, RefreshTableFunction):
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
        data = {
          "ClassID": self.ID
        }
        response = requests.post(
          self.config.getBaseURL() + "/admin/remove_class",
          params = data
        ).content
        response = json.loads(response.decode('utf-8'))

        if response.get("status_code") == 200:
          if response.get("data"):
            title = "Success"
            message = "Class has been deleted"
            icon = "check"
            CTkMessagebox(
              title = title,
              message = message,
              icon = icon
            )
        else:
          title = "Error"
          message = response.get("error")
          icon = "cancel"
          CTkMessagebox(
            title = title,
            message = message if message else "Something went wrong while removing the class",
            icon = icon
          )

      RefreshTableFunction()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def ValidateClassData(self):
    try:
      if not self.ID:
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
      if not self.CourseID:
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
      if not self.SessionStartTime:
        title = "Missing Entry"
        message = "please enter class start time"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.SessionEndTime:
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
