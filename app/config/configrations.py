import sys
import os
import customtkinter

class Router:
  def __init__(self):
    self.current_page = None
    self.cached_frames = {}

  def ClearWindow(self):
    if self.current_page:
      self.current_page.pack_forget()

  def navigate(self, view_class, window):
    self.ClearWindow()

    if view_class not in self.cached_frames:
      frame = customtkinter.CTkFrame(window)
      view_instance = view_class()
      view_instance.LunchGUI(frame)
      self.cached_frames[view_class] = frame
    else:
      frame = self.cached_frames[view_class]

    self.current_page = frame
    self.current_page.pack(fill="both", expand=True)

class Configrations:
  def __init__(self) -> None:
    try:
      self.BaseURL = "http://localhost:8000"
      self.router = Router()
      self.token = ""

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