import sys
import os
import customtkinter

class Router:
  def __init__(self) -> None:
    """
    Initializes the Router object.

    Attributes:
      current_page (CTkFrame or None): Stores the current visible page/frame.
    """
    self.current_page = None

  def clear_window(self) -> None:
    """
    Hides the currently displayed page from the window if one exists.

    This is typically called before navigating to a new view to remove
    the old one from the interface.

    Returns: None
    """
    if self.current_page:
      self.current_page.pack_forget()

  def navigate(self, view_class):
    """
    Navigates to a new view by replacing the current frame with a new one.

    Args:
      view_class (class): The class representing the new view to display.
      It must have a method called `lunch_view(frame)`.
    
    Returns: None
    """
    self.clear_window()

    Configrations.window.configure(cursor="watch")
    Configrations.window.update()

    frame = customtkinter.CTkFrame(Configrations.window)
    view_instance = view_class()

    Configrations.window.configure(cursor="")
    Configrations.window.update()

    view_instance.lunch_view(frame)

    self.current_page = frame
    self.current_page.pack(fill="both", expand=True)

class Configrations:
  window = None

  def __init__(self) -> None:
    """
    Initializes the configuration object for the application.

    Attributes:
      BaseURL (str): The base URL used for API requests.
      router (Router): An instance of the Router class to manage views.
      token (str): A string to store the user's authentication token.
    """
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

  def set_window(self, window: customtkinter.CTk) -> None:
    """
    Sets the application's main window reference.

    Args:
      window: The main application window (typically a Tkinter or CTk instance).
    
    Returns: None
    """
    try:
      Configrations.window = window
    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass

  def get_base_url(self):
    """
    Retrieves the base URL used for backend API communication.

    Returns:
      str: The base URL string.
    """
    try:
      return self.BaseURL
    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass
