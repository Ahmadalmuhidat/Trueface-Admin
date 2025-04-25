import sys
import os
import app.config.configrations as Configrations

from CTkMessagebox import CTkMessagebox

class User:
  def __init__(self, user_id, name, email, role):
    self.user_id = user_id
    self.name = name
    self.email = email
    self.role = role

    self.config = Configrations.Configrations()

  def validate_user_data(self):
    try:
      if not self.user_id:
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