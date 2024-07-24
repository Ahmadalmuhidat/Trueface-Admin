import sys
import os
import customtkinter
import json
import threading

from DatabaseManager import DatabaseManager

class Settings(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.getSettings()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def refreshSettings(self):
    try:
      with open('configrations.json', 'r') as file:
        Settings = json.load(file)
        Settings['Database']['host'] = self.HostEntry.get()
        Settings['Database']['user'] = self.UserEntry.get()
        Settings['Database']['password'] = self.PasswordEntry.get()
        Settings['Database']['database'] = self.DatabaseEntry.get()
        Settings['Activation_Key'] = self.ActivationKeyEntry.get()

      with open('configrations.json', 'w') as file:
        json.dump(Settings, file, indent=2)

      self.getSettings()

      self.HostEntry.configure(placeholder_text= self.Host)
      self.UserEntry.configure(placeholder_text= self.User)
      self.PasswordEntry.configure(placeholder_text= self.Password)
      self.DatabaseEntry.configure(placeholder_text= self.Database)
      self.ActivationKeyEntry.configure(placeholder_text= self.ActivationKey)

      threading.Thread(target=self.checkLicenseStatus).start()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)
 
  def create(self, parent):
    try:
      ContentFrame = customtkinter.CTkFrame(parent)
      ContentFrame.pack(
        padx=20,
        pady=20
      )

      Hostlabel = customtkinter.CTkLabel(ContentFrame)
      Hostlabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
      )
      Hostlabel.configure( text="Host:")

      self.HostEntry = customtkinter.CTkEntry(ContentFrame)
      self.HostEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
      )
      self.HostEntry.configure(width=400)
      self.HostEntry.insert(
        0,
        self.Host
      )

      Userlabel = customtkinter.CTkLabel(ContentFrame)
      Userlabel.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
      )
      Userlabel.configure(text="User:")

      self.UserEntry = customtkinter.CTkEntry(ContentFrame)
      self.UserEntry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
      )
      self.UserEntry.configure(width=400)
      self.UserEntry.insert(
        0,
        self.User
      )

      Passwordlabel = customtkinter.CTkLabel(ContentFrame)
      Passwordlabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=10
      )
      Passwordlabel.configure(text="Password:")

      self.PasswordEntry = customtkinter.CTkEntry(ContentFrame)
      self.PasswordEntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
      )
      self.PasswordEntry.configure(width=400)
      self.PasswordEntry.insert(
        0,
        self.Password
      )

      Databaselabel = customtkinter.CTkLabel(ContentFrame)
      Databaselabel.grid(
        row=3,
        column=0,
        padx=10,
        pady=10
      )
      Databaselabel.configure(text="Database:")

      self.DatabaseEntry = customtkinter.CTkEntry(ContentFrame)
      self.DatabaseEntry.grid(
        row=3,
        column=1,
        padx=10,
        pady=10
      )
      self.DatabaseEntry.configure(width=400)
      self.DatabaseEntry.insert(
        0,
        self.Database
      )

      ActivationKeylabel = customtkinter.CTkLabel(ContentFrame)
      ActivationKeylabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=10
      )
      ActivationKeylabel.configure(text="Activation Key:")

      self.ActivationKeyEntry = customtkinter.CTkEntry(ContentFrame)
      self.ActivationKeyEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=10
      )
      self.ActivationKeyEntry.configure(width=400)
      self.ActivationKeyEntry.insert(
        0,
        self.ActivationKey
      )

      save_button = customtkinter.CTkButton(ContentFrame)
      save_button.grid(
        row=5,
        columnspan=2,
        padx=10,
        pady=10,
        sticky="nsew",
      )
      save_button.configure(
        text="Refresh Settings",
        command=self.refreshSettings
      )

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)