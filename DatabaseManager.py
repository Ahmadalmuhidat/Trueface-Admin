import sys
import os
import mysql.connector
import face_recognition
import pickle
import numpy
import json
import re

from Configrations import Configrations
from CTkMessagebox import CTkMessagebox
from datetime import date

class DatabaseManager(Configrations):
  cursor = None
  db = None
  Courses = []

  def __init__(self) -> None:
    try:
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

  def connect(self):
    try:
      DatabaseManager.db = mysql.connector.connect(
        host = self.Host,
        user = self.User,
        password = self.Password,
        database = self.Database
      )

      DatabaseManager.cursor = DatabaseManager.db.cursor()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def getClassesStudentRelation(self, StudentID):
    try:
      data = (StudentID,)
      query = '''
        SELECT
          ClassStudentRelation.RelationID,
          Classes.ClasseID,
          Classes.ClassSubjectArea,
          Classes.ClasseSessionStartTime,
          Classes.ClasseSessionEndTime,
          ClassStudentRelation.ClassDay
        FROM
          Classes
        JOIN
          ClassStudentRelation
        ON
          Classes.ClasseID = ClassStudentRelation.ClassID
        WHERE
          ClassStudentRelation.StudentID = %s
        '''
      DatabaseManager.cursor = DatabaseManager.db.cursor()
      DatabaseManager.cursor.execute(query, data)

      result = DatabaseManager.cursor.fetchall()
    
      DatabaseManager.cursor.close()

      return result

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def RemoveClassesStudentRelation(self, RelationID):
    try:
      data = (RelationID,)
      query = '''
        DELETE FROM
          ClassStudentRelation
        WHERE
          RelationID = %s
        '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

      DatabaseManager.cursor.close()

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
      query = '''
        SELECT
          ClasseID,
          ClassSubjectArea,
          ClasseSessionStartTime,
          ClasseSessionEndTime
        FROM
          Classes
        '''
      DatabaseManager.cursor = DatabaseManager.db.cursor()
      DatabaseManager.cursor.execute(query)

      self.ClassesForSelection = DatabaseManager.cursor.fetchall()
    
      DatabaseManager.cursor.close()

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
      data = (
        UserID,
      )
      query = '''
        DELETE FROM
          Users
        WHERE
          UserID = %s
        '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

      DatabaseManager.cursor.close()

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
      data = (
        UserID,
        UserName,
        UserEmail,
        UserPassword,
        UserRole
      )
      query = '''
        INSERT INTO
          Users
        VALUES
          (
            %s,
            %s,
            %s,
            %s,
            %s
          )
        '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

      DatabaseManager.cursor.close()

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

  def insertClassStudentRelation(self, RelationID, StudentID, ClassID, ClassDay):
    try:
      data = (RelationID, StudentID, ClassID, ClassDay)
      query = '''
        INSERT INTO
          ClassStudentRelation
        VALUES
          (
            %s,
            %s,
            %s,
            %s
          )
        '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()
      DatabaseManager.cursor.close()

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

  def checkDuplicatedID(self, id):
    try:
      data = (id,)
      query = "SELECT StudentID FROM Students WHERE StudentID=%s"

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      result = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

      if len(result) > 0:
        return True
      else:
        return False

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getUsers(self):
    try:
      query = '''
      SELECT
        UserID,
        UserName,
        UserEmail,
        UserRole
      FROM
        Users
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query)
      self.Users = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

    except Exception as e: 
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def checkUser(self, email, password):
    try:
      data = (email,)
      query = '''
      SELECT
        UserID,
        UserPassword,
        UserRole
      FROM Users
      WHERE UserEmail=%s
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      User = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

      if len(User) == 1:
        if User[0][2] == "admin":
          if str(User[0][1]) == str(password):
            return User[0][0]
          else:
            CTkMessagebox(title="Info", message="Incorrect password")
            return False
        else:
          CTkMessagebox(title="Info", message="You are not authorized to access the admin panel")
          return False
      else:
        CTkMessagebox(title="Info", message="Email was not found")
        return False

    except Exception as e: 
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def searchClasse(self, term):
    try:
      data = (term,)
      query = '''
        SELECT
          Classes.*,
          Courses.CourseTitle
        FROM
          Classes
        LEFT JOIN
          Courses
        ON
          Courses.CourseID = Classes.ClasseCourseID
        WHERE
          ClasseID=%s
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      self.Classes = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def deleteClasse(self, term):
    try:
      data = (term,)
      query = "DELETE FROM Classes WHERE ClasseID=%s"

      DatabaseManager.cursor = DatabaseManager.db.cursor()
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()
      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def searchUsers(self, term):
    try:
      data = (term,)
      query = '''
        SELECT
          UserID,
          UserName,
          UserEmail,
          UserRole
        FROM
          Users
         WHERE
          UserID=%s
        '''
      
      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      self.Users = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def searchCourses(self, term):
    try:
      data = (term,)
      query = "SELECT * FROM Courses WHERE CourseID=%s"

      DatabaseManager.cursor = DatabaseManager.db.cursor()
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.Courses = DatabaseManager.cursor.fetchall()
      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def deleteCourses(self, term):
    try:
      data = (term,)
      query = "DELETE FROM Courses WHERE CourseID=%s"

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def checkDuplicatedID(self, id):
    try:
      data = (id,)
      query = "SELECT StudentID FROM Students WHERE StudentID=%s"

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      result = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

      if len(result) > 0:
        return True
      else:
        return False

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
      query = '''
        SELECT
          Classes.*,
          Courses.CourseTitle
        FROM
          Classes
        LEFT JOIN
          Courses
        ON
          Courses.CourseID = Classes.ClasseCourseID
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query)
      self.Classes = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getCourses(self):
    try:
      query = "SELECT * FROM Courses"

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query)
      DatabaseManager.Courses = DatabaseManager.cursor.fetchall()
      
      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass  
  
  def insertCourse(self, **data):
    try:
      data = (
        data["ID"],
        data["title"],
        data["credit"],
        data["MaximumUnits"],
        data["LongCourseTitle"],
        data["OfferingNBR"],
        data["AcademicGroup"],
        data["SubjectArea"],
        data["CatalogNBR"],
        data["campus"],
        data["AcademicOrganization"],
        data["component"]
      )

      query = '''
        INSERT INTO
          Courses
        VALUES
          (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
          )
      
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()
      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass 

  def insertClass(
      self,
      ID,
      subject,
      CNBR,
      AC,
      CID,
      ONBR,
      ST,
      ET,
      section,
      component,
      campus,
      instructorID,
      IT
    ):
    try:
      data = (
        ID ,
        subject,
        CNBR,
        AC,
        CID,
        ONBR,
        ST,
        ET,
        section,
        component,
        campus,
        instructorID,
        IT
      )
      query = '''
        INSERT INTO
          Classes
        VALUES
          (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
          )
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass 

  def getAttendanceByDate(self, date, ClassSubject):
    try:
      if not date:
        title = "Missing Entry"
        message = "please enter the date"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)

      elif not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        title = "Wrong Date Format"
        message = "the allowed date format is YYYY-MM-DD"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)

      else: 
        with open('configrations.json', 'r') as file:
          WorkingHourStart = json.load(file)['Working_Hours']['start']

        data = (date, ClassSubject)
        query = '''
          SELECT
            AttendanceStudent,
            AttendanceDate,
            AttendanceTime
          AND
            TIME(AttendanceTime) > %s
          WHERE
            AttendanceDate = %s
          AND
            AttendanceClass = %s
          '''
        
        DatabaseManager.cursor = DatabaseManager.db.cursor()

        DatabaseManager.cursor.execute(query, data)
        self.Attendance = DatabaseManager.cursor.fetchall()

        DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def checkExistence(self, ImagePath):
    try:
      load_image = face_recognition.load_image_file(ImagePath)
      image_face_encodings = face_recognition.face_encodings(load_image)
      
      for target in self.Students:        
        stored_face_encoding = target[3]
        TargetName = target[1]
        load_encoding = pickle.loads(stored_face_encoding)
        results = face_recognition.compare_faces([image_face_encodings[0]], numpy.array(load_encoding))

        if any(results):
          message = "the person in the image has been already found in the database, and his name is {}".format(TargetName)
          title = "Student is already exist"
          CTkMessagebox(title=title, message=message)
          return True

      return False
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

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
      FaceID = self.getFaceEncoding(data["ImagePath"])

      # if self.checkExistence(DestinationPath):
      #   pass
      # else:
      data = (
        data["StudentID"],
        data["FirstName"],
        data["MiddleName"],
        data["LastName"],
        data["Gender"],
        FaceID,
        data["TodayDate"]
      )

      query = '''
        INSERT INTO
          Students
        VALUES
          (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
          )
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def removeStudent(self, term):
    try:
      data = (term,)
      query = "DELETE FROM Students WHERE StudentID = %s"

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getStudents(self):
    try:
      query = '''
        SELECT
          StudentID,
          StudentFirstName,
          StudentMiddleName,
          StudentLastName,
          StudentGender,
          StudentCreateDate
        FROM
          Students
      '''

      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query)
      self.Students = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def searchStudent(self, term):
    try:
      data = (term,)
      query = "SELECT * FROM Students WHERE StudentID = %s"
      
      DatabaseManager.cursor = DatabaseManager.db.cursor()

      DatabaseManager.cursor.execute(query, data)
      self.Students = DatabaseManager.cursor.fetchall()

      DatabaseManager.cursor.close()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass