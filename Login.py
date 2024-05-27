import sys
import os
import customtkinter

from UserInterface import UserInterface
from DatabaseManager import DatabaseManager

class Login(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.getSettings()
      self.connect()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def login(self):
    result = self.checkUser(
      self.EmailEntry.get(),
      self.PasswordEntry.get()
    )

    if result:
      self.window.destroy()
      UserInterface().startTheProgram()

  def create(self):
    try:
      self.window = customtkinter.CTk()
      self.window.geometry("400x350")
      self.window.resizable(
        width=0,
        height=0
      )

      self.window.title("Login To TimeWizeAI")

      ContentFrame = customtkinter.CTkFrame(self.window)
      ContentFrame.pack(
        padx=20,
        pady=20
      )

      Emaillabel = customtkinter.CTkLabel(ContentFrame)
      Emaillabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
      )
      Emaillabel.configure(text="Email:")

      self.EmailEntry = customtkinter.CTkEntry(ContentFrame)
      self.EmailEntry.grid(
        row=0,
        column=1,
        padx=10
      )
      self.EmailEntry.configure(width=250)

      Passwordlabel = customtkinter.CTkLabel(ContentFrame)
      Passwordlabel.grid(
        row=1,
        column=0,
        padx=10,
      )
      Passwordlabel.configure(text="Password:")

      self.PasswordEntry = customtkinter.CTkEntry(ContentFrame)
      self.PasswordEntry.grid(
        row=1,
        column=1,
        padx=10,
      )
      self.PasswordEntry.configure(width=250)

      save_button = customtkinter.CTkButton(ContentFrame)
      save_button.grid(
        row=6,
        columnspan=2,
        padx=10,
        pady=10,
        sticky="nsew",
      )
      save_button.configure(
        text="Login",
        command=self.login
      )

      self.window.mainloop()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

if __name__ ==  "__main__":
  login = Login().create()