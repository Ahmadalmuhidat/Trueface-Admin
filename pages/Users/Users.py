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


            DeleteButton = customtkinter.CTkButton(self.UsersTableFrame)
            DeleteButton.grid(
                row=row,
                column=len(Users_data),
                sticky="nsew",
                padx=10,
                pady=5
            )
            DeleteButton.configure(
                text="Delete",
                fg_color="red",
                command=lambda rid=UsersID: self.DeleteUser(rid),
            )
            self.UsersLabels.append(DeleteButton)

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
  
  def DeleteUser(self, UserID):
    try:
      self.removeUser(UserID)
      self.refresh()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)  
  
  def SubmitNewUser(self):
    try:
      UserID = self.UserIDEntry.get()
      UserName = self.UserFullNameEntry.get()
      UserEmail = self.UserEmailEntry.get()
      UserPassword = self.UserPasswordEntry.get()
      UserRole = self.UserRoleEntry.get()

      self.insertUser(
        UserID,
        UserName,
        UserEmail,
        UserPassword,
        UserRole
      )

      self.UserIDEntry.delete(
        0,
        customtkinter.END
      )
      self.UserFullNameEntry.delete(
        0,
        customtkinter.END
      )
      self.UserEmailEntry.delete(
        0,
        customtkinter.END
      )
      self.UserPasswordEntry.delete(
        0,
        customtkinter.END
      )

      self.refresh()

    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)
      print(exc_obj)

  def addUser(self):
    try:
      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()

      self.PopWindow.geometry("490x400")
      self.PopWindow.resizable(False, False)

      self.PopWindow.title("Add New User")

      UserIDLabel = customtkinter.CTkLabel(self.PopWindow)
      UserIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=15
      )
      UserIDLabel.configure(text="User ID:")

      self.UserIDEntry = customtkinter.CTkEntry(self.PopWindow)
      self.UserIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=15
      )
      self.UserIDEntry.configure(width=350)

      UserFullNameLabel = customtkinter.CTkLabel(self.PopWindow)
      UserFullNameLabel.grid(
        row=1, 
        column=0,
        padx=10,
        pady=15
      )
      UserFullNameLabel.configure(text="First Name:")

      self.UserFullNameEntry = customtkinter.CTkEntry(self.PopWindow)
      self.UserFullNameEntry.grid(
        row=1,
        column=1,
        padx=10,
        pady=15
      )
      self.UserFullNameEntry.configure(width=350)

      UserEmailLabel = customtkinter.CTkLabel(self.PopWindow)
      UserEmailLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=15
      )
      UserEmailLabel.configure(text="Email:")

      self.UserEmailEntry = customtkinter.CTkEntry(self.PopWindow)
      self.UserEmailEntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=15
      )
      self.UserEmailEntry.configure(width=350)

      UserPasswordLabel = customtkinter.CTkLabel(self.PopWindow)
      UserPasswordLabel.grid(
        row=3,
        column=0,
        padx=10,
        pady=15
      )
      UserPasswordLabel.configure(text="Password:")

      self.UserPasswordEntry = customtkinter.CTkEntry(self.PopWindow)
      self.UserPasswordEntry.grid(
        row=3,
        column=1,
        padx=10,
        pady=15
      )
      self.UserPasswordEntry.configure(width=350, show="*")

      UserRoleLabel = customtkinter.CTkLabel(self.PopWindow)
      UserRoleLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=15
      )
      UserRoleLabel.configure(text="Role:")

      self.UserRoleEntry = customtkinter.CTkComboBox(self.PopWindow)
      self.UserRoleEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=15
      )
      self.UserRoleEntry.configure(
        values=[
          "admin",
          "teacher"
        ],
        width=350
      )
      self.UserRoleEntry.set("teacher")

      SaveButton = customtkinter.CTkButton(self.PopWindow)
      SaveButton.grid(
        row=7,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=15
      )
      SaveButton.configure(
        text="Save User",
        command=self.SubmitNewUser,
        width=350
        )

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

      InsertButton = customtkinter.CTkButton(SearchBarFrame)
      InsertButton.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=10,
        padx=5
      )
      InsertButton.configure(
        command=self.addUser,
        width=100,
        text="New User"
      )

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
        fill="both",
        expand=True
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