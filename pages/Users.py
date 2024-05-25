import customtkinter
import sys
import os
import datetime
import tkinter

from PIL import Image
from DatabaseManager import DatabaseManager

class Users(DatabaseManager):
  def __init__(self):
    try:
      super().__init__()

      self.UsersLabels = []
      self.headers = [
        "Users ID",
        "User Name",
        "User Email",
        "User Role",
      ]

      self.getUsers()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def search(self, term):
    try:
      self.searchUsers(term)
      self.displayUsersTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def displayUsersTable(self):
    try:
      for label in self.UsersLabels:
        label.destroy()

      if len(self.Users) > 0:
        for row, Users in enumerate(self.Users, start=1):
          UsersID, UserName, UsesEmail, UserRole = Users
          Users_data = [
            UsersID,
            UserName,
            UsesEmail,
            UserRole
          ]

          for col, data in enumerate(Users_data):
            data_label = customtkinter.CTkLabel(
              self.Users_table_frame,
              text=data,
              padx=10,
              pady=5
            )
            data_label.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            self.UsersLabels.append(data_label)

      self.results_count.configure(text="Results: " + str(len(self.Users)))

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def refresh(self):
    try:
      self.getUsers()
      self.displayUsersTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def create(self, parent):
    try:
      search_bar_frame = customtkinter.CTkFrame(
        parent,
        bg_color="transparent"
      )
      search_bar_frame.pack(
        fill="x",
        expand=False
      )

      search_button = customtkinter.CTkButton(
        search_bar_frame,
        text="Search"
      )
      search_button.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=10,
        padx=5
      )
      search_button.configure(command=lambda: self.search(search_bar.get()))

      search_bar = customtkinter.CTkEntry(search_bar_frame)
      search_bar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )
      search_bar.configure(
        width=400,
        placeholder_text="Search for Users..."
      )

      # delete_button = customtkinter.CTkButton(
      #   search_bar_frame,
      #   width=100,
      #   text="Delete"
      # )
      # delete_button.grid(
      #   row=0,
      #   column=2,
      #   sticky="nsew",
      #   pady=10,
      #   padx=5
      # )
      # delete_button.configure(command=lambda: self.deleteUsers(delete_bar.get()))

      # delete_bar = customtkinter.CTkEntry(
      #   search_bar_frame,
      #   width=100,
      #   placeholder_text="ID",
      # )
      # delete_bar.grid(
      #   row=0,
      #   column=3,
      #   sticky="nsew",
      #   pady=10
      # )

      refresh_button = customtkinter.CTkButton(
        search_bar_frame,
        width=100,
        text="Refresh"
      )
      refresh_button.grid(
        row=0,
        column=4,
        sticky="nsew",
        pady=10,
        padx=5
      )
      refresh_button.configure(command=self.refresh)

      # add_Users_button = customtkinter.CTkButton(
      #   search_bar_frame,
      #   width=100,
      #   text="Add Users"
      # )
      # add_Users_button.grid(
      #   row=0,
      #   column=5,
      #   sticky="nsew",
      #   pady=10,
      #   padx=5
      # )
      # add_Users_button.configure(command=self.addUsers)

      self.results_count = customtkinter.CTkLabel(search_bar_frame)
      self.results_count.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.Users_table_frame = customtkinter.CTkFrame(parent)
      self.Users_table_frame.pack(
        fill="x",
        expand=False
      )

      for col, header in enumerate(self.headers):
        header_label = customtkinter.CTkLabel(
          self.Users_table_frame,
          text=header,
          padx=10,
          pady=10
        )
        header_label.grid(
          row=0,
          column=col,
          sticky="nsew"
        )
  
      for col in range(len(self.headers)):
        self.Users_table_frame.columnconfigure(col, weight=1)

      self.displayUsersTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)