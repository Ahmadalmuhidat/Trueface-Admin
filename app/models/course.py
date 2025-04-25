import sys
import os
import app.config.configrations as Configrations

from CTkMessagebox import CTkMessagebox

class Course:
  def __init__(
    self, course_id, title, credit, maximum_units, long_course_title, offering_nbr,
    academic_group, subject_area, catalog_nbr, campus, academic_organization, component
  ):
    self.course_id = course_id
    self.title = title
    self.credit = credit
    self.maximum_units = maximum_units
    self.long_course_title = long_course_title
    self.offering_nbr = offering_nbr
    self.academic_group = academic_group
    self.subject_area = subject_area
    self.catalog_nbr = catalog_nbr
    self.campus = campus
    self.academic_organization = academic_organization
    self.component = component

    self.config  = Configrations.Configrations() 

  def ValidateCourseData(self):
    try:
      if not self.course_id:
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
      if not self.maximum_units or not self.maximum_units.isdigit():
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
      if not self.offering_nbr or not self.offering_nbr.isdigit():
        title = "Missing Entry"
        message = "please enter course offering number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.academic_group:
        title = "Missing Entry"
        message = "please enter course academic group"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.subject_area:
        title = "Missing Entry"
        message = "please enter course subject area"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.catalog_nbr or not self.catalog_nbr.isdigit():
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
      if not self.academic_organization:
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

