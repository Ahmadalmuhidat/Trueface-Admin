import sys
import os
import face_recognition
import pickle
import numpy
import json
import requests

from Configrations import Configrations
from CTkMessagebox import CTkMessagebox

class DatabaseManager(Configrations):
  cursor = None
  db = None
  Courses = []

  def __init__(self) -> None:
    try:
      self.BaseURL = "http://localhost:3000"
      self.Students = []
      self.Attendance = []
      self.Classes = []
      self.ClassesForSelection = []
      self.Users = []

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getClassesStudentRelation(self, StudentID):
    try:
      data = {
        "StudentID": StudentID
      }
      response = requests.get(
        self.BaseURL + "/get_classes_for_selection",
        data
      ).content
      response_str = response.decode('utf-8')

      return json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def RemoveClassesStudentRelation(self, RelationID):
    try:
      data = {
        "RelationID": RelationID
      }
      response = requests.delete(self.BaseURL + "/remove_classes_student_relation", data).content
      response_str = response.decode('utf-8')

      title = "Relation has been Deleted"
      message = "Class has been removed successfully"
      icon = "check"
      CTkMessagebox(title=title, message=message, icon=icon)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getClassesForSelection(self):
    try:
      response = requests.get(self.BaseURL + "/get_classes_for_selection").content
      response_str = response.decode('utf-8')

      self.ClassesForSelection = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def removeUser(
      self,
      UserID,
    ):
    try:
      data = {
        "UserID": UserID,
      }

      response = requests.delete(self.BaseURL + "/remove_user", data).content
      response_str = response.decode('utf-8')

      title="Success"
      message="User has been removed"
      icon="check"
      CTkMessagebox(title=title, message=message,icon=icon)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def insertUser(
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

      response = requests.post(self.BaseURL + "/insert_user", data).content
      response_str = response.decode('utf-8')

      self.Students = json.loads(response_str)

      title="Success"
      message="New user has been added"
      icon="check"
      CTkMessagebox(title=title, message=message,icon=icon)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def insertClassStudentRelation(
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
      response = requests.post(self.BaseURL + "/get_classes_for_selection", data).content
      response_str = response.decode('utf-8')

      if response_str == True:
        title="Success"
        message="New class has been added"
        icon="check"
        CTkMessagebox(title=title, message=message,icon=icon)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getUsers(self):
    try:
      response = requests.get(self.BaseURL + "/get_users").content
      response_str = response.decode('utf-8')
      self.Users = json.loads(response_str)

    except Exception as e: 
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def checkUser(self, email, password):
    try:
      data = {
        "email": email,
        "password": password
      }

      response = requests.get(self.BaseURL + "/check_user", data).content
      response_str = response.decode('utf-8')

      return json.loads(response_str)
      
    except Exception as e: 
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def SearchClasse(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.get(self.BaseURL + "/search_classe", data).content
      response_str = response.decode('utf-8')

      self.Classes = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def RemoveClasse(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.delete(self.BaseURL + "/remove_classe", data).content
      response_str = response.decode('utf-8')

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def searchUsers(self, term):
    try:
      data = {
        "term": term
      }

      response = requests.get(self.BaseURL + "/search_user", data).content
      response_str = response.decode('utf-8')

      self.Users = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def searchCourses(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.get(self.BaseURL + "/search_courses", data).content
      response_str = response.decode('utf-8')

      DatabaseManager.Courses = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def deleteCourses(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.delete(self.BaseURL + "/remove_course", data).content
      response_str = response.decode('utf-8')

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def checkDuplicatedID(self, id):
    try:
      data = {
        "StudentID": id
      }
      response = requests.post(self.BaseURL + "/check_duplicated_id", data).content
      response_str = response.decode('utf-8')

      return json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass
  
  def checkLicenseStatus(self):
    try:
      data = (self.ActivationKey,)
      query = '''
        SELECT
          LicenseActive
        FROM
          Licenses
        WHERE
          LicenseActivationKey = %s
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      CustomerLicenseStatus = DatabaseManager.cursor.fetchall()

      if len(CustomerLicenseStatus) > 0:
        if CustomerLicenseStatus[0][0] == 0:
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
      else:
          title="License not found"
          message="The Activation Key is not valid, please contact the technical team"
          icon="cancel"
          msg = CTkMessagebox(
            title=title,
            message=message,
            icon=icon,
            option_1="ok"
          )
          response = msg.get()

          if response == "ok":
            sys.exit(0)     

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getClasses(self):
    try:
      response = requests.get(self.BaseURL + "/get_classes").content
      response_str = response.decode('utf-8')

      self.Classes = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getCourses(self):
    try:
      response = requests.get(self.BaseURL + "/get_courses").content
      response_str = response.decode('utf-8')

      DatabaseManager.Courses = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass  
  
  def insertCourse(
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

      response = requests.get(self.BaseURL + "/insert_course", data).content
      response_str = response.decode('utf-8')

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass 

  def insertClass(
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

      response = requests.get(self.BaseURL + "/insert_class", data).content
      response_str = response.decode('utf-8')

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass 

  def getFaceEncoding(self, path):
    try:
      load_stored_image = face_recognition.load_image_file(path)
      stored_face_encoding = numpy.array(face_recognition.face_encodings(load_stored_image)[0])
      return pickle.dumps(stored_face_encoding)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def checkFaceInImage(self, path):
    try:
      load_stored_image = face_recognition.load_image_file(path)
      FaceFound = face_recognition.face_locations(load_stored_image)

      if FaceFound:
        return True
      else:
        return False

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def insertStudent(self, **data):
    try:
      FaceEncoding = self.getFaceEncoding(data["ImagePath"])
      data = {
        "StudentID": data["StudentID"],
        'FirstName': data["FirstName"],
        "MiddleName": data["MiddleName"],
        "LastName": data["LastName"],
        "Gender": data["Gender"],
        "FaceEncoding": FaceEncoding,
        "TodayDate": data["TodayDate"]
      }

      response = requests.get(self.BaseURL + "/insert_student", data).content
      response_str = response.decode('utf-8')

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def removeStudent(self, term):
    try:
      data = {
        "term": term
      }
      response = requests.delete(self.BaseURL + "/remove_student", data).content
      response_str = response.decode('utf-8')

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getStudents(self):
    try:
      response = requests.get(self.BaseURL + "/get_students").content
      response_str = response.decode('utf-8')

      self.Students = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def searchStudent(self, term):
    try:
      data = {
        "term": str(term)
      }

      response = requests.get(self.BaseURL + "/search_student", data).content
      response_str = response.decode('utf-8')
      self.Students = json.loads(response_str)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass