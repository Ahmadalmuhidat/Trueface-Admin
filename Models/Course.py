import sys
import os
import requests
import json

from CTkMessagebox import CTkMessagebox
import Configrations

class Course:
  def __init__(self, ID, title, credit, MaximumUnits, LongCourseTitle, OfferingNBR, AcademicGroup, SubjectArea, CatalogNBR, campus, AcademicOrganization, component):
    self.ID = ID
    self.title = title
    self.credit = credit
    self.MaximumUnits = MaximumUnits
    self.LongCourseTitle = LongCourseTitle
    self.OfferingNBR = OfferingNBR
    self.AcademicGroup = AcademicGroup
    self.SubjectArea = SubjectArea
    self.CatalogNBR = CatalogNBR
    self.campus = campus
    self.AcademicOrganization = AcademicOrganization
    self.component = component

    self.config  = Configrations.Configrations()
  
  def Add(self):
    try:
      data = {
        "ID": self.ID,
        "title": self.title,
        "credit": self.credit,
        "MaximumUnits": self.MaximumUnits,
        "LongCourseTitle": self.LongCourseTitle,
        "OfferingNBR": self.OfferingNBR,
        "AcademicGroup": self.AcademicGroup,
        "SubjectArea": self.SubjectArea,
        "CatalogNBR": self.CatalogNBR,
        "campus": self.campus,
        "AcademicOrganization": self.AcademicOrganization,
        "component": self.component
      }

      response = requests.post(
        self.config.getBaseURL() + "/admin/insert_course",
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
          message = message if message else "Something went wrong while inserting the course",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass 

  def Remove(self, RefreshTableFunction: None):
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
        data = {
          "CourseID": self.ID
        }
        response = requests.post(
          self.config.getBaseURL() + "/admin/remove_course",
          params = data
        ).content
        response = json.loads(response.decode('utf-8'))

        if response.get("status_code") == 200:
          if response.get("data"):
            title = "Success"
            message = "Course has been deleted"
            icon = "check"
            CTkMessagebox(
              title = title,
              message = message if message else "Something went wrong while removing the course",
              icon = icon
            )
        else:
          title = "Error"
          message = response.get("error")
          icon = "cancel"
          CTkMessagebox(
            title = title,
            message = message if message else "Something went wrong while removing the course",
            icon = icon
          )
      
      RefreshTableFunction()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def ValidateCourseData(self):
    try:
      if not self.ID:
        title = "Missing Entry"
        message = "please enter course ID"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.title:
        title = "Missing Entry"
        message = "please enter course title"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.credit or not self.credit.isdigit():
        title = "Missing Entry"
        message = "please enter course credit number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.MaximumUnits or not self.MaximumUnits.isdigit():
        title = "Missing Entry"
        message = "please enter course maximum units number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.title:
        title = "Missing Entry"
        message = "please enter course long title"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.OfferingNBR or not self.OfferingNBR.isdigit():
        title = "Missing Entry"
        message = "please enter course offering number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.AcademicGroup:
        title = "Missing Entry"
        message = "please enter course academic group"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.SubjectArea:
        title = "Missing Entry"
        message = "please enter course subject area"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.CatalogNBR or not self.CatalogNBR.isdigit():
        title = "Missing Entry"
        message = "please enter course catalog number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.campus:
        title = "Missing Entry"
        message = "please enter course campus"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.AcademicOrganization:
        title = "Missing Entry"
        message = "please enter course academic organization"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.component:
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

