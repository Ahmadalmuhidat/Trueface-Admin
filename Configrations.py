import sys
import os
import json

class Configrations:
  def __init__(self) -> None:
    try:
      self.Host = None
      self.User = None
      self.Password = None
      self.Database = None
      self.ActivationKey = None

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass
  
  def getSettings(self):
    try:
      # path = os.path.join(
      #   os.environ.get(
      #     "_MEIPASS2",
      #      os.path.abspath(".")
      #   ),
      #   "Configrations.py"
      # )

      # with open(path, 'r') as file:
      #   Settings = json.load(file)
      #   self.Host = Settings['Database']['host']
      #   self.User = Settings['Database']['user']
      #   self.Password = Settings['Database']['password']
      #   self.Database = Settings['Database']['database']
      #   self.ActivationKey = Settings['Activation_Key']

      self.Host = "34.83.216.163"
      self.User = "root"
      self.Password = "root"
      self.Database = "TimeWizeAI"
      self.ActivationKey = "123"

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
      pass