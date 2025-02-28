import sys
import os
import json
import requests

from Configrations import Configrations
from CTkMessagebox import CTkMessagebox
from Models import Course, Student, Class, User

class DatabaseManager():
  cursor = None
  db = None
  Courses = []

  def __init__(self) -> None:
    try:
      self.config = Configrations()

      self.Users = []
      self.Students = []
      self.Classes = []
      self.ClassesForSelection = []
      self.token = ""

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  ##########
  # Users
  ##########

  def SearchUser(self, term):
    try:
      data = {
        "UserID": term
      }

      response = requests.get(
        self.config.getBaseURL() + "/admin/search_user",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Users = response.get("data")
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while searching in users",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def GetUsers(self):
    try:
      response = requests.get(self.config.getBaseURL() + "/admin/get_users").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Users = [
          User.User(
            data['UserID'],
            data['UserName'],
            data['UserEmail'],
            data['UserRole'], 
          ) for data in response.get("data")
        ]
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while getting the users",
          icon = icon
        )

    except Exception as e: 
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  # remove later
  def CheckUser(self, email, password):
    try:
      data = {
        "email": email,
        "password": password
      }

      response = requests.get(
        self.config.getBaseURL() + "/admin/check_user",
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
          message = message if message else "Something went wrong while checking user info",
          icon = icon
        )

    except Exception as e: 
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  ##############################
  # Classes Student Relation
  ##############################

  def GetClassesStudentRelation(self, StudentID):
    try:
      data = {
        "StudentID": StudentID
      }
      response = requests.get(
        self.config.getBaseURL() + "/admin/get_classes_student_relation",
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
          message = message if message else "Something went wrong while getting classes for the student",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def RemoveClassesStudentRelation(self, RelationID):
    try:
      data = {
        "RelationID": RelationID
      }
      response = requests.post(
        self.config.getBaseURL() + "/admin/remove_class_student_relation",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        if response.get("data"):
          title = "Class has been removed"
          message = "Class has been removed successfully"
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

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def ClearClassesStudentRelation(self, StudentID):
    try:
      data = {
        "StudentID": StudentID
      }
      response = requests.post(
        self.config.getBaseURL() + "/admin/clear_class_student_relation",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        if response.get("data"):
          title = "Classes has been cleared"
          message = "Class has been cleared successfully"
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
          message = message if message else "Something went wrong while clearing the classes",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def GetClassesForSelection(self):
    try:
      response = requests.get(
        self.config.getBaseURL() + "/admin/get_classes_for_selection"
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.ClassesForSelection = response.get("data")
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while getting classes",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def InsertClassStudentRelation(
      self,
      RelationID,
      StudentID,
      ClassID,
      ClassDay
    ):
    try:
      data = {
        "RelationID": RelationID,
        "StudentID": StudentID,
        "ClassID": ClassID,
        "ClassDay": ClassDay
      }
      response = requests.post(
        self.config.getBaseURL() + "/admin/insert_class_student_relation",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        title="Success"
        message="New class has been added"
        icon="check"
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
          message = message if message else "Something went wrong while inserting the class",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  ##########
  # Classes
  ##########

  def SearchClass(self, term):
    try:
      data = {
        "ClassID": term
      }
      response = requests.get(
        self.config.getBaseURL() + "/admin/search_class",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Classes = response.get("data")
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while searching in classes",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def GetClasses(self):
    try:
      response = requests.get(self.config.getBaseURL() + "/admin/get_classes").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Classes =  [
          Class.Class(
            data['ClasseID'],
            data['ClassSubjectArea'],
            data['ClasseCatalogNBR'],
            data['ClasseAcademicCareer'],
            data['ClasseCourseID'], 
            data['ClasseCourseOfferingNBR'], 
            data['ClasseSessionStartTime'],
            data['ClasseSessionEndTime'], 
            data['ClasseSection'], 
            data['ClasseComponent'], 
            data['ClasseCampus'], 
            data['ClasseInstructorID'], 
            data['ClasseInstructorType'], 
            data['CourseTitle'],
          ) for data in response.get("data")
        ]
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while getting the classes",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass
  
  ##########
  # Course
  ##########

  def SearchCourses(self, term):
    try:
      data = {
        "CourseID": term
      }
      response = requests.get(
        self.config.getBaseURL() + "/admin/search_courses",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        DatabaseManager.Courses = [
          Course(
            data['CourseID'],
            data['CourseTitle'],
            data['CourseCredit'],
            data['CourseMaximumUnits'], 
            data['CourseLongCourseTitle'],
            data['CourseOfferingNBR'],
            data['CourseAcademicGroup'], 
            data['CourseSubjectArea'],
            data['CourseCatalogNBR'],
            data['CourseCampus'], 
            data['CourseAcademicOrganization'],
            data['CourseComponent']
          ) for data in response.get("data")
        ]
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while searching in courses",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def GetCourses(self):
    try:
      response = requests.get(self.config.getBaseURL() + "/admin/get_courses").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        DatabaseManager.Courses = [
          Course.Course(
            data['CourseID'],
            data['CourseTitle'],
            data['CourseCredit'],
            data['CourseMaximumUnits'], 
            data['CourseLongCourseTitle'],
            data['CourseOfferingNBR'],
            data['CourseAcademicGroup'], 
            data['CourseSubjectArea'],
            data['CourseCatalogNBR'],
            data['CourseCampus'], 
            data['CourseAcademicOrganization'],
            data['CourseComponent']
          ) for data in response.get("data")
        ]
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while getting the courses",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass  

  ##########
  # Student
  ##########

  def GetStudents(self):
    try:
      response = requests.get(self.config.getBaseURL() + "/admin/get_all_students").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Students = DatabaseManager.Courses = [
          Student.Student(
            data['StudentID'],
            data['StudentFirstName'],
            data['StudentMiddleName'],
            data['StudentLastName'], 
            data['StudentGender'],
            data['StudentCreateDate']
          ) for data in response.get("data")
        ]
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while getting the students",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def SearchStudent(self, term):
    try:
      data = {
        "StudentID": str(term)
      }
      response = requests.get(
        self.config.getBaseURL() + "/admin/search_student",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Students = response.get("data")
      else:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while searching in students",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass
