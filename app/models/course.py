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
