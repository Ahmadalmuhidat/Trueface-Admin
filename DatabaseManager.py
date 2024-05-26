import sys
import os
import mysql.connector
import shutil
import face_recognition
import pickle
import numpy
import json
import re

from Configrations import Configrations
from CTkMessagebox import CTkMessagebox

class DatabaseManager(Configrations):
  cursor = None
  db = None
  Courses = []

  def __init__(self) -> None:
    try:
      self.Students = []
      self.Attendance = []
      self.Absence = []
      self.History = []
      self.Classes = []
      self.Users = []

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
      DatabaseManager.cursor.execute(query, data)
      result = DatabaseManager.cursor.fetchall()

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

  def connect(self):
    try:
      DatabaseManager.db = pymysql.connect(
        host = self.Host,
        user = self.User,
        password = self.User,
        database = self.Database
      )

      DatabaseManager.cursor = DatabaseManager.db.cursor()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

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

      DatabaseManager.cursor.execute(query)
      self.Users = DatabaseManager.cursor.fetchall()

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
        UserPassword
      FROM Users
      WHERE UserEmail=%s
      '''

      DatabaseManager.cursor.execute(query, data)
      User = DatabaseManager.cursor.fetchall()

      if len(User) == 1:
        if str(User[0][1]) == str(password):
          return User[0][0]
        else:
          CTkMessagebox(title="Info", message="Incorrect password")
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

      DatabaseManager.cursor.execute(query, data)
      self.Classes = DatabaseManager.cursor.fetchall()

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
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

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
      DatabaseManager.cursor.execute(query, data)
      self.Users = DatabaseManager.cursor.fetchall()

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
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.Courses = DatabaseManager.cursor.fetchall()

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
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

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
      DatabaseManager.cursor.execute(query, data)
      result = DatabaseManager.cursor.fetchall()

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

  def connect(self):
    try:
      DatabaseManager.db = mysql.connector.connect(
        host = self.Host,
        user = self.User,
        password = self.User,
        database = self.Database
      )

      DatabaseManager.cursor = DatabaseManager.db.cursor()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
  
  def checkCustomerLicenseStatus(self):
    try:
      data = (self.ActivationKey,)
      query = "SELECT LicenseActive FROM Licenses WHERE LicenseActivationKey=%s"
      DatabaseManager.cursor.execute(query, data)
      CustomerLicenseStatus = DatabaseManager.cursor.fetchall()

      if len(CustomerLicenseStatus) > 0:
        if CustomerLicenseStatus[0][0] == "inactive":
          title="License not active"
          message="Please Renew your License"
          icon="cancel"
          msg = CTkMessagebox(title=title, message=message,icon=icon, option_1="ok")
          response = msg.get()

          if response=="ok":
            sys.exit(0)     
      else:
          title="License not found"
          message="The Activation Key is not valid, please contact the technical team"
          icon="cancel"
          msg = CTkMessagebox(title=title, message=message,icon=icon, option_1="ok")
          response = msg.get()

          if response == "ok":
            sys.exit(0)     

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
      DatabaseManager.cursor.execute(query)
      self.Classes = DatabaseManager.cursor.fetchall()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getCourses(self):
    try:
      query = "SELECT * FROM Courses"
      DatabaseManager.cursor.execute(query)
      DatabaseManager.Courses = DatabaseManager.cursor.fetchall()

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

      query = "INSERT INTO Courses VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()


    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass 

  def insertClass(self, ID, subject, CNBR, AC, CID, ONBR, ST, ET, section, component, campus, instructorID, IT):
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
      query = "INSERT INTO Classes VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass 

  def getAttendanceHistoryByDate(self, date):
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

        data = (WorkingHourStart, date)
        query = '''
          SELECT
            AttendanceStudent,
            AttendanceDate,
            AttendanceTime
          AND
            TIME(AttendanceTime) > %s
          WHERE
            AttendanceDate = %s
          '''
        DatabaseManager.cursor.execute(query, data)
        self.History = DatabaseManager.cursor.fetchall()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass
  
  def getAbsenceHistoryByDate(self, date):
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
        data = [date]
        query = '''
          SELECT
            StudentFullName
          FROM
            Students
          WHERE
            StudentFullName
          NOT IN
            (
            SELECT
              Attendance.AttendanceStudent
            FROM
              Attendance
            WHERE
              DATE(Attendance.AttendanceDate) = %s
            )
          '''
        DatabaseManager.cursor.execute(query, data)
        self.History = DatabaseManager.cursor.fetchall()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getAttendance(self):
    try:
      query = '''
        SELECT 
          Students.StudentID, 
          Students.StudentFirstName, 
          Students.StudentMiddleName, 
          Students.StudentLastName, 
          Classes.ClassSubjectArea, 
          Attendance.AttendanceTime
        FROM 
          Attendance
        LEFT JOIN 
          Students
        ON 
          Students.StudentID = Attendance.AttendanceStudentID
        LEFT JOIN 
          Classes
        ON
          Attendance.AttendanceClassID = Classes.ClasseID
        WHERE 
          Attendance.AttendanceDate = CURDATE();
      '''
      DatabaseManager.cursor.execute(query)
      self.Attendance = DatabaseManager.cursor.fetchall()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getAbsence(self):
    try:
      query = '''
        SELECT
          StudentID,
          StudentFirstName,
          StudentMiddleName,
          StudentLastName
        FROM
          Students
        WHERE
          StudentID
        NOT IN 
          (
          SELECT
            Attendance.AttendanceStudentID
          FROM
            Attendance
          WHERE
            DATE(Attendance.AttendanceDate) = CURDATE()
          )
        '''
      DatabaseManager.cursor.execute(query)
      self.Absence = DatabaseManager.cursor.fetchall()

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

  def validateStudentsData(self, ID, FN, MN, LN, Gender, ImagePath):
    try:
      if not ID:
        title = "Missing Entry"
        message = "please enter Students ID"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not FN:
        title = "Missing Entry"
        message = "please enter Students first name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not FN:
        title = "Missing Entry"
        message = "please enter Students first name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not MN:
        title = "Missing Entry"
        message = "please enter Students middle name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not LN:
        title = "Missing Entry"
        message = "please enter Students last name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not Gender:
        title = "Missing Entry"
        message = "please enter Students Gender"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False 
      elif not ImagePath:
        title = "Missing Entry"
        message = "please select Students image"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not os.path.exists(ImagePath):
        title = "Inavlid Path"
        message = "the selected path is not valid"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not self.checkFaceInImage(ImagePath):
        title = "Face Not Found"
        message = "the uploaded image contains no face"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif self.checkDuplicatedID(ID):
        title = "Duplicated ID"
        message = "the entered id has been already assigned to another Student"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False

      return True

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
      # DestinationPath = self.storeStudentImage(data["ID"], data["ImagePath"])
      FaceID = self.getFaceEncoding(data["ImagePath"])

      # if self.checkExistence(DestinationPath):
      #   pass
      # else:
      data = (
        data["ID"],
        data["FN"],
        data["MN"],
        data["LN"],
        data["Gender"],
        FaceID,
        data["TodayDate"]
      )

      query = "INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s)"
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def removeStudentImage(self, term):
    try:
      if os.path.exists("Students") and os.path.isdir("Students"):
        for filename in os.listdir("Students"):
          if filename.lower().startswith(term + "."):
            os.remove(os.path.join("Students", filename))

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def storeStudentImage(self, id, path):
    try:
      image_filename = os.path.basename(path).split(".")
      image_filename = id + "." + image_filename[1]
      destination_path = os.path.join("Students", image_filename)
      shutil.copyfile(path, destination_path)

      return destination_path

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def removeStudent(self, term):
    try:
      data = (term,)

      query = "DELETE FROM Students WHERE StudentID = %s"
      DatabaseManager.cursor.execute(query, data)
      DatabaseManager.db.commit()
      # self.removeStudentImage(term)

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass

  def getStudents(self):
    try:
      query = "SELECT * FROM Students"
      DatabaseManager.cursor.execute(query)
      self.Students = DatabaseManager.cursor.fetchall()

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
      DatabaseManager.cursor.execute(query, data)
      self.Students = DatabaseManager.cursor.fetchall()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass