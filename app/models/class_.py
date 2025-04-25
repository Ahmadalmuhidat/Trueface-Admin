import sys
import os
import app.config.configrations as Configrations

from CTkMessagebox import CTkMessagebox

class Class:
  def __init__(
    self, class_id, subject_area, catalog_nbr = None, academic_career = None,
    course= None, offering_nbr = None, start_time = None, end_time = None, section = None,
    component = None, campus = None, instructor_id = None, instructor_type = None
  ):
    self.class_id = class_id
    self.subject_area = subject_area
    self.catalog_nbr = catalog_nbr
    self.academic_career = academic_career
    self.Course = course
    self.offering_nbr = offering_nbr
    self.start_time = start_time
    self.end_time = end_time
    self.section = section
    self.component = component
    self.campus = campus
    self.instructor_id = instructor_id
    self.instructor_type = instructor_type

    self.config  = Configrations.Configrations()

    self.Students = []

  def validate_class_data(self):
    try:
      if not self.class_id:
        title = "Missing Entry"
        message = "please enter classe ID"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.subject_area:
        title = "Missing Entry"
        message = "please enter class subject"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.catalog_nbr or not self.catalog_nbr.isdigit():
        title = "Missing Entry"
        message = "please enter class catalog number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.academic_career:
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
      if not self.offering_nbr or not self.offering_nbr.isdigit():
        title = "Missing Entry"
        message = "please enter class offering number"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.start_time:
        title = "Missing Entry"
        message = "please enter class start time"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.end_time:
        title = "Missing Entry"
        message = "please enter class end time"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.section:
        title = "Missing Entry"
        message = "please enter class section"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.component:
        title = "Missing Entry"
        message = "please enter class component"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.campus:
        title = "Missing Entry"
        message = "please enter class campus"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.instructor_id:
        title = "Missing Entry"
        message = "please select instructor"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.instructor_type:
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

class RelationClass(Class):
  def __init__(
    self, class_id, SubjectArea, CatalogNBR=None, AcademicCareer=None, Course=None,
    OfferingNBR=None, StartTime=None, EndTime=None, Section=None, Component=None,
    Campus=None, InstructorID=None, InstructorType=None, relation_id=None, day=None
  ):
    super().__init__(
      class_id, SubjectArea, CatalogNBR, AcademicCareer,
      Course, OfferingNBR, StartTime, EndTime, Section,
      Component, Campus, InstructorID, InstructorType
    )

    self.relation_id = relation_id
    self.day = day