import sys
import os
import requests
import json
import numpy
import face_recognition
import pickle
import app.config.configrations as Configrations

from CTkMessagebox import CTkMessagebox

class Student:
  def __init__(self, student_id, first_name, middle_name, last_name, gender, create_date, picture = None):
    self.student_id = student_id
    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.gender = gender
    self.create_date = create_date
    self.picture = picture

    self.config  = Configrations.Configrations()

    self.classes = []

  def check_duplicated_id(self):
    try:
      data = {
        "student_id": self.student_id
      }
      response = requests.get(
        self.config.get_base_url() + "/admin/check_duplicated_id",
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
          message = message if message else "Something went wrong while checking duplicated IDs",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass
  
  def get_face_encode(self):
    try:
      load_stored_image = face_recognition.load_image_file(self.picture)
      return pickle.dumps(numpy.array(
        face_recognition.face_encodings(load_stored_image)[0])
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def check_face_in_image(self):
    try:
      load_stored_image = face_recognition.load_image_file(self.picture)
      face_found = face_recognition.face_locations(load_stored_image)

      if face_found:
        return True
      else:
        return False

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def validate_students_data(self):
    try:
      if not self.student_id:
        title = "Missing Entry"
        message = "please enter Students ID"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not self.first_name:
        title = "Missing Entry"
        message = "please enter Students first name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not self.middle_name:
        title = "Missing Entry"
        message = "please enter Students middle name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not self.last_name:
        title = "Missing Entry"
        message = "please enter Students last name"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not self.gender:
        title = "Missing Entry"
        message = "please enter Students Gender"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False 
      elif not self.picture:
        title = "Missing Entry"
        message = "please select Students image"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not os.path.exists(self.picture):
        title = "Inavlid Path"
        message = "the selected path is not valid"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif not self.check_face_in_image():
        title = "Face Not Found"
        message = "the uploaded image does not contain face"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif self.check_duplicated_id():
        title = "Duplicated ID"
        message = "the entered id has been already assigned to another Student"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False

      return True

    except Exception as e:
        ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
        FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
        print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
        print(ExceptionObject)
        pass