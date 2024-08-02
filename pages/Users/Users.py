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

      self.GetUsers()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def search(self, term):
    try:
      self.SearchUsers(term)
      self.displayUsersTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

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
            DataLabel = customtkinter.CTkLabel(
              self.UsersTableFrame,
              text=data,
              padx=10,
              pady=5
            )
            DataLabel.grid(
              row=row,
              column=col,
              sticky="nsew"
            )
            self.UsersLabels.append(DataLabel)


            DeleteButton = customtkinter.CTkButton(
              self.UsersTableFrame,
                text="Delete",
                fg_color="red",
                command=lambda rid=UsersID: self.DeleteUser(rid)
              )
            DeleteButton.grid(
                row=row,
                column=len(Users_data),
                sticky="nsew",
                padx=10,
                pady=5
            )
            self.UsersLabels.append(DeleteButton)

      self.ResultsCount.configure(
        text="Results: " + str(len(self.Users))
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def refresh(self):
    try:
      self.GetUsers()
      self.displayUsersTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
  
  def DeleteUser(self, UserID):
    try:
      self.RemoveUser(UserID)
      self.refresh()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)  
  
  def SubmitNewUser(self):
    try:
      UserID = self.UserIDEntry.get()
      UserName = self.UserFullNameEntry.get()
      UserEmail = self.UserEmailEntry.get()
      UserPassword = self.UserPasswordEntry.get()
      UserRole = self.UserRoleEntry.get()

      self.InsertUser(
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
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def addUser(self):
    try:
      self.PopWindow = customtkinter.CTkToplevel()
      self.PopWindow.grab_set()

      self.PopWindow.geometry("460x350")
      self.PopWindow.resizable(False, False)
      self.PopWindow.title("Add New User")

      UserIDLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="User ID:"
      )
      UserIDLabel.grid(
        row=0,
        column=0,
        padx=10,
        pady=15
      )

      self.UserIDEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.UserIDEntry.grid(
        row=0,
        column=1,
        padx=10,
        pady=15
      )

      UserFullNameLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="First Name:"
      )
      UserFullNameLabel.grid(
        row=1,
        column=0,
        padx=10,
        pady=15
      )

      self.UserFullNameEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.UserFullNameEntry.grid(
        row=1,
        column=1,
        padx=10,
        pady=15
      )

      UserEmailLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Email:"
      )
      UserEmailLabel.grid(
        row=2,
        column=0,
        padx=10,
        pady=15
      )

      self.UserEmailEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350
      )
      self.UserEmailEntry.grid(
        row=2,
        column=1,
        padx=10,
        pady=15
      )

      UserPasswordLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Password:"
      )
      UserPasswordLabel.grid(
        row=3,
        column=0,
        padx=10,
        pady=15
      )

      self.UserPasswordEntry = customtkinter.CTkEntry(
        self.PopWindow,
        width=350,
        show="*"
      )
      self.UserPasswordEntry.grid(
        row=3,
        column=1,
        padx=10,
        pady=15
      )

      UserRoleLabel = customtkinter.CTkLabel(
        self.PopWindow,
        text="Role:"
      )
      UserRoleLabel.grid(
        row=4,
        column=0,
        padx=10,
        pady=15
      )

      self.UserRoleEntry = customtkinter.CTkComboBox(
        self.PopWindow,
        values=["admin", "teacher"],
        width=350
      )
      self.UserRoleEntry.grid(
        row=4,
        column=1,
        padx=10,
        pady=15
      )
      self.UserRoleEntry.set("teacher")

      SaveButton = customtkinter.CTkButton(
        self.PopWindow,
        text="Save User",
        command=self.SubmitNewUser,
        width=350
      )
      SaveButton.grid(
        row=7,
        columnspan=2,
        sticky="nsew",
        padx=10,
        pady=15
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def create(self, parent):
    try:
      SearchBarFrame = customtkinter.CTkFrame(
        parent,
        bg_color="transparent"
      )
      SearchBarFrame.pack(
        fill="x",
        expand=False
      )

      SearchButton = customtkinter.CTkButton(
        SearchBarFrame,
        text="Search",
        command=lambda: self.search(SearchBar.get())
      )
      SearchButton.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=10,
        padx=5
      )

      SearchBar = customtkinter.CTkEntry(
        SearchBarFrame,
        width=400,
        placeholder_text="Search for Users..."
      )
      SearchBar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )

      RefreshButton = customtkinter.CTkButton(
        SearchBarFrame,
        text="Refresh",
        command=self.refresh,
        width=100
      )
      RefreshButton.grid(
        row=0,
        column=4,
        sticky="nsew",
        pady=10,
        padx=5
      )

      AddUsersButton = customtkinter.CTkButton(
        SearchBarFrame,
        text="Add Users",
        command=self.addUser,
        width=100
      )
      AddUsersButton.grid(
        row=0,
        column=5,
        sticky="nsew",
        pady=10,
        padx=5
      )

      self.ResultsCount = customtkinter.CTkLabel(SearchBarFrame)
      self.ResultsCount.grid(
        row=0,
        column=6,
        padx=10,
        pady=5
      )

      self.UsersTableFrame = customtkinter.CTkScrollableFrame(
        parent
      )
      self.UsersTableFrame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
          HeaderLabel = customtkinter.CTkLabel(
            self.UsersTableFrame,
            text=header,
            padx=10,
            pady=10
          )
          HeaderLabel.grid(
            row=0,
            column=col,
            sticky="nsew"
          )

      for col in range(len(self.headers)):
          self.UsersTableFrame.columnconfigure(col, weight=1)

      self.displayUsersTable()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)