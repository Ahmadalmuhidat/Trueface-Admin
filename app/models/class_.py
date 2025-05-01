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