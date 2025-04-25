import sys
import os
import customtkinter

from main import Main
from app.controllers.auth import login
from app.core.GlobalData import GlobalData

class Login():
  def __init__(self):
    try:
      super().__init__()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def login(self):
    result = login(
      self.EmailEntry.get(),
      self.PasswordEntry.get()
    )
    if result:
      GlobalData.config.token = result
      self.window.destroy()
      Main().start_program()

  def create(self):
    try:
      self.window = customtkinter.CTk()
      self.window.geometry("400x170")
      self.window.iconbitmap("logo.ico")
      self.window.resizable(
        width=0,
        height=0
      )

      self.window.title("Login To TrueFace")

      ContentFrame = customtkinter.CTkFrame(self.window)
      ContentFrame.pack(
        padx=20,
        pady=20
      )

      Emaillabel = customtkinter.CTkLabel(
        ContentFrame,
        text="Email:"
      )
      Emaillabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
      )

      self.EmailEntry = customtkinter.CTkEntry(
        ContentFrame,
        width=250
      )
      self.EmailEntry.grid(
        row=0,
        column=1,
        padx=10
      )

      Passwordlabel = customtkinter.CTkLabel(
        ContentFrame,
        text="Password:"
      )
      Passwordlabel.grid(
        row=1,
        column=0,
        padx=10,
      )

      self.PasswordEntry = customtkinter.CTkEntry(
        ContentFrame,
        width=250,
        show="*"
      )
      self.PasswordEntry.grid(
        row=1,
        column=1,
        padx=10,
      )

      save_button = customtkinter.CTkButton(
        ContentFrame,
        text="Login",
        command=self.login
      )
      save_button.grid(
        row=6,
        columnspan=2,
        padx=10,
        pady=10,
        sticky="nsew",
      )

      self.window.mainloop()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)