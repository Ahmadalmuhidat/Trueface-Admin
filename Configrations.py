import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox

class Configrations:
  def __init__(self) -> None:
    try:
      # self.BaseURL = "https://trueface-demo-api-ddgsfvefgmfhb9aa.uaenorth-01.azurewebsites.net/"
      self.BaseURL = "http://192.168.0.4:8000"
      self.License_API = "https://trueface-license-api-cqh8fphkcccthfe7.uaenorth-01.azurewebsites.net/check_license"
      self.ActivationKey = "1234"

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def getActivationKey(self):
    try:
      return self.ActivationKey

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def getBaseURL(self):
    try:
      return self.BaseURL

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def getLicense_API(self):
    try:
      return self.License_API

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def CheckLicenseStatus(self):
    try:
      data = {
        "License": self.getActivationKey()
      }
      response = requests.get(
        self.config.getLicense_API(),
        params = data
      ).content
      response = json.loads(response.decode('utf-8'))

      if response.get("status_code") != 200:
        title = "Error"
        message = response.get("error")
        icon = "cancel"
        WarningMessage = CTkMessagebox(
          title = title,
          message = message if message else "Something went wrong while checking license status",
          icon = icon,
          option_1 = "ok"
        )

        if WarningMessage.get() == "ok":
          sys.exit(0)
        else:
          sys.exit(0)
      else:
        return True

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass