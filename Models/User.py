import sys
import os
import requests
import json

from CTkMessagebox import CTkMessagebox
import Configrations

class User:
  def __init__(self, ID, name, email, role):
    self.ID = ID
    self.name = name
    self.email = email
    self.role = role

    self.config = Configrations.Configrations()
  
  def Remove(self, RefreshTableFunction: None):
    title = "Conformation"
    message = "Are you sure you want to delete the user"
    icon = "question"
    conformation = CTkMessagebox(
      title = title,
      message = message,
      icon = icon,
      option_1 = "yes",
      option_2 = "cancel" 
    )

    if conformation.get() == "yes":
      data = {
        "UserID": self.ID,
      }

      response = requests.post(
        self.config.getBaseURL() + "/admin/remove_user",
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
        message = response.get("error")
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while removing the user",
          icon = icon
        )

      RefreshTableFunction()

  def Add(self):
    try:
      data = {
        "UserID": self.ID,
        "UserName": self.name,
        "UserEmail": self.email,
        "UserPassword": "1234",
        "UserRole": self.role
      }

      response = requests.post(
        self.config.getBaseURL() + "/admin/insert_user",
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") == 200:
        title="Success"
        message="New user has been added"
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
          message = message if message else "Something went wrong while inserting the user",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def ValidateUserData(self):
    try:
      if not self.ID:
        title = "Missing Entry"
        message = "please enter user ID"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.name:
        title = "Missing Entry"
        message = "please enter user name"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.email:
        title = "Missing Entry"
        message = "please enter user email"
        icon = "cancel"
        CTkMessagebox(
          title = title,
          message = message,
          icon = icon
        )  
        return False
      if not self.role:
        title = "Missing Entry"
        message = "please enter user role"
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