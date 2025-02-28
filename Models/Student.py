import sys
import os
import requests
import json
import face_recognition

from CTkMessagebox import CTkMessagebox
import Configrations

class Student:
  def __init__(self, ID, first_name, middle_name, last_name, gender, create_date, picture):
    self.ID = ID
    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.gender = gender
    self.create_date = create_date
    self.picture = picture

    self.config  = Configrations.Configrations()

  def Add(self):
    try:
      data = {
        "StudentID": self.ID,
        "FirstName": self.first_name,
        "MiddleName": self.middle_name,
        "LastName": self.last_name,
        "Gender": self.gender
      }
      files = {'StudentImage': open(self.picture, 'rb')}

      response = requests.post(
        self.config.getBaseURL() + "/admin/insert_student",
        params = data,
        files = files
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
          message = message if message else "Something went wrong while inserting the student",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass
  
  def Remove(self, RefreshTableFunction: None):
    try:
      data = {
        "StudentID": self.ID
      }
      response = requests.post(
        self.config.getBaseURL() + "/admin/remove_student", 
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        if response.get("data"):
          title = "Relation has been deleted"
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
          message = message if message else "Something went wrong while removing the student",
          icon = icon
        )

      RefreshTableFunction()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def CheckDuplicatedID(self):
    try:
      data = {
        "StudentID": self.ID
      }
      response = requests.get(
        self.config.getBaseURL() + "/admin/check_duplicated_id",
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

  def CheckFaceInImage(self, image_path):
    try:
      load_stored_image = face_recognition.load_image_file(image_path)
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

  def ValidateStudentsData(self):
    try:
      if not self.ID:
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
      elif not self.CheckFaceInImage(self.picture):
        title = "Face Not Found"
        message = "the uploaded image does not contain face"
        icon = "cancel"
        CTkMessagebox(title=title, message=message, icon=icon)  
        return False
      elif self.CheckDuplicatedID():
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