import sys
import os
import json
import requests
import face_recognition
import pickle
import numpy

from Configrations import Configrations
from CTkMessagebox import CTkMessagebox

class DatabaseManager(Configrations):
  cursor = None
  db = None
  Courses = []

  def __init__(self) -> None:
    try:
      # self.BaseURL = "https://timewizeai-api.azurewebsites.net"
      self.BaseURL = "http://192.168.1.112:8000"
      self.Students = []
      self.Attendance = []
      self.Classes = []
      self.ClassesForSelection = []
      self.Users = []
      self.token = ""

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def GetClassesStudentRelation(self, StudentID):
    try:
      data = {
        "StudentID": StudentID
      }
      response = requests.get(
        self.BaseURL + "/get_classes_student_relation",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
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
        self.BaseURL + "/remove_classes_student_relation",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        title = "Relation has been Deleted"
        message = "Class has been removed successfully"
        icon = "check"
        CTkMessagebox(title=title, message=message, icon=icon)
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
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
        self.BaseURL + "/get_classes_for_selection"
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.ClassesForSelection = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def RemoveUser(
      self,
      UserID,
    ):
    try:
      data = {
        "UserID": UserID,
      }

      response = requests.post(
        self.BaseURL + "/remove_user",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        title="Success"
        message="User has been removed"
        icon="check"
        CTkMessagebox(title=title, message=message,icon=icon)
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def InsertUser(
      self,
      UserID,
      UserName,
      UserEmail,
      UserPassword,
      UserRole
    ):
    try:
      data = {
        "UserID": UserID,
        "UserName": UserName,
        "UserEmail": UserEmail,
        "UserPassword": UserPassword,
        "UserRole": UserRole
      }

      response = requests.post(
        self.BaseURL + "/insert_user",
        params=data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        title="Success"
        message="New user has been added"
        icon="check"
        CTkMessagebox(title=title, message=message,icon=icon)
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
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
        self.BaseURL + "/insert_class_student_relation",
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
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
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
      response = requests.get(self.BaseURL + "/get_users").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Users = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e: 
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def CheckUser(self, email, password):
    try:
      data = {
        "email": email,
        "password": password
      }

      response = requests.get(
        self.BaseURL + "/check_user",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e: 
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
  
  def SearchClasse(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.get(
        self.BaseURL + "/search_classe",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Classes = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def RemoveClasse(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.post(
        self.BaseURL + "/remove_classe",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def SearchUsers(self, term):
    try:
      data = {
        "term": term
      }

      response = requests.get(
        self.BaseURL + "/search_user",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Users = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def SearchCourses(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.get(
        self.BaseURL + "/search_courses",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        DatabaseManager.Courses = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def DeleteCourses(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.post(
        self.BaseURL + "/remove_course",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def CheckDuplicatedID(self, id):
    try:
      data = {
        "StudentID": id
      }
      response = requests.get(
        self.BaseURL + "/check_duplicated_id",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass
  
  def CheckLicenseStatus(self):
    try:
      data = {
        "License": self.ActivationKey
      }
      response = requests.get(
        "https://timewizeai-license-api.azurewebsites.net/check_license",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") != 200:
          title="License not active"
          message="Please Renew your License"
          icon="cancel"
          msg = CTkMessagebox(
            title=title,
            message=message,
            icon=icon,
            option_1="ok"
          )
          response = msg.get()

          if response=="ok":
            sys.exit(0)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def GetClasses(self):
    try:
      response = requests.get(self.BaseURL + "/get_classes").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Classes = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
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
      response = requests.get(self.BaseURL + "/get_courses").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        DatabaseManager.Courses = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass  
  
  def InsertCourse(
      self,
      CourseID,
      CourseTitle,
      CourseCredit,
      CourseMaximumUnits,
      CourseLongCourseTitle,
      CourseOfferingNBR,
      CourseAcademicGroup,
      CourseSubjectArea,
      CourseCatalogNBR,
      CourseCampus,
      CourseAcademicOrganization,
      CourseComponent
      ):
    try:
      data = {
        "ID": CourseID,
        "title": CourseTitle,
        "credit": CourseCredit,
        "MaximumUnits": CourseMaximumUnits,
        "LongCourseTitle": CourseLongCourseTitle,
        "OfferingNBR": CourseOfferingNBR,
        "AcademicGroup": CourseAcademicGroup,
        "SubjectArea": CourseSubjectArea,
        "CatalogNBR": CourseCatalogNBR,
        "campus": CourseCampus,
        "AcademicOrganization": CourseAcademicOrganization,
        "component": CourseComponent
      }

      response = requests.post(
        self.BaseURL + "/insert_course",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass 

  def InsertClass(
      self,
      ClasseID,
      subject,
      CatalogNBR,
      AcademicCareer,
      CourseID,
      OfferingNBR,
      StartTime,
      EndTime,
      section,
      component,
      campus,
      InstructorID,
      InstructorType
    ):
    try:
      data = {
        "ClasseID":ClasseID ,
        "subject": subject,
        "CatalogNBR": CatalogNBR,
        "AcademicCareer": AcademicCareer,
        "CourseID": CourseID,
        "OfferingNBR": OfferingNBR,
        "StartTime": StartTime,
        "EndTime": EndTime,
        "section": section,
        "component": component,
        "campus": campus,
        "instructorID": InstructorID,
        "InstructorType": InstructorType
      }

      response = requests.post(
        self.BaseURL + "/insert_class",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass 

  def CheckFaceInImage(self, path):
    try:
      load_stored_image = face_recognition.load_image_file(path)
      FaceFound = face_recognition.face_locations(load_stored_image)

      if FaceFound:
        return True
      else:
        return False

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def InsertStudent(self, **data):
    try:
      files = {'FaceEncoding': open(data["ImagePath"], 'rb')}
      data = {
        "StudentID": data["StudentID"],
        "FirstName": data["FirstName"],
        "MiddleName": data["MiddleName"],
        "LastName": data["LastName"],
        "Gender": data["Gender"],
        "StudentImage":  open(data["ImagePath"], 'rb'),
      }

      response = requests.post(
        self.BaseURL + "/insert_student",
        params = data,
        files = files
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def RemoveStudent(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.post(
        self.BaseURL + "/remove_student", 
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        return response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def GetStudents(self):
    try:
      response = requests.get(self.BaseURL + "/get_all_students").content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Students = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
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
        "term": str(term)
      }
      response = requests.get(
        self.BaseURL + "/search_student",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        self.Students = response.get("data")
      else:
        title = "Error"
        message = response.get("Error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass