import sys
import os
import customtkinter

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
        for row, User in enumerate(self.Users, start=1):
          UsersID, \
          UserName, \
          UsesEmail, \
          UserRole = User
          Users_data = [
            UsersID,
            UserName,
            UsesEmail,
            UserRole
          ]

          for col, data in enumerate(Users_data):
            DataLabel = customtkinter.CTkLabel(self.UsersTableFrame)
            DataLabel.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            DataLabel.configure(
              text=data,
              padx=10,
              pady=5
            )
            self.UsersLabels.append(DataLabel)

      self.ResultsCount.configure(
        text="Results: " + str(len(self.Users))
      )

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
      SearchBarFrame = customtkinter.CTkFrame(parent)
      SearchBarFrame.pack(
        fill="x",
        expand=False
      )
      SearchBarFrame.configure(bg_color="transparent")

      SearchButton = customtkinter.CTkButton(SearchBarFrame)
      SearchButton.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=10,
        padx=5
      )
      SearchButton.configure(
        command=lambda: self.search(SearchBar.get()),
        text="Search"
      )

      SearchBar = customtkinter.CTkEntry(SearchBarFrame)
      SearchBar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )
      SearchBar.configure(
        width=400,
        placeholder_text="Search for Users..."
      )

      # delete_button = customtkinter.CTkButton(
      #   SearchBarFrame,
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

      # DeleteBar = customtkinter.CTkEntry(SearchBarFrame)
      # DeleteBar.grid(
      #   row=0,
      #   column=3,
      #   sticky="nsew",
      #   pady=10
      # )
      # DeleteBar.configure(
      #   width=100,
      #   placeholder_text="ID",
      # )

      RefreshButton = customtkinter.CTkButton(SearchBarFrame)
      RefreshButton.grid(
        row=0,
        column=4,
        sticky="nsew",
        pady=10,
        padx=5
      )
      RefreshButton.configure(
        command=self.refresh,
        width=100,
        text="Refresh"
      )

      # AddUsersButton = customtkinter.CTkButton(SearchBarFrame)
      # AddUsersButton.grid(
      #   row=0,
      #   column=5,
      #   sticky="nsew",
      #   pady=10,
      #   padx=5
      # )
      # AddUsersButton.configure(
      #   command=self.addUsers,
      #   width=100,
      #   text="Add Users"
      # )

      self.ResultsCount = customtkinter.CTkLabel(SearchBarFrame)
      self.ResultsCount.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.UsersTableFrame = customtkinter.CTkScrollableFrame(parent)
      self.UsersTableFrame.pack(
        fill="x",
        expand=False
      )

      for col, header in enumerate(self.headers):
        HeaderLabel = customtkinter.CTkLabel(self.UsersTableFrame)
        HeaderLabel.grid(
          row=0,
          column=col,
          sticky="nsew"
        )
        HeaderLabel.configure(
          text=header,
          padx=10,
          pady=10
        )
  
      for col in range(len(self.headers)):
        self.UsersTableFrame.columnconfigure(col, weight=1)

      self.displayUsersTable()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)