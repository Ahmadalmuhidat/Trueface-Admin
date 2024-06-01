import os
import sys
import customtkinter
import uuid

def addClassPage(
    PopWindow,
    ClassesForSelection,
    StudentID,
    insertClassStudentRelation
  ):
  try:
    class_id_title_map = {
      f"{x[1]} {x[2]}-{x[3]}": x[0] for x in ClassesForSelection
    }

    for widget in PopWindow.winfo_children():
      if widget not in (Navbar,):
        widget.pack_forget()
  
    ClassLabel = customtkinter.CTkLabel(PopWindow)
    ClassLabel.pack(
      padx=10,
      pady=10
    )
    ClassLabel.configure(text="Select Class:")

    ClassEntry = customtkinter.CTkComboBox(PopWindow)
    ClassEntry.pack(
      padx=10,
      pady=10
    )
    ClassEntry.configure(
      values = [f"{x[1]} {x[2]}-{x[3]}" for x in ClassesForSelection],
      width=350
    )
    ClassEntry.set("None")

    DayLabel = customtkinter.CTkLabel(PopWindow)
    DayLabel.pack(
      padx=10,
      pady=10
    )
    DayLabel.configure(text="Select Day:")

    DayEntry = customtkinter.CTkComboBox(PopWindow)
    DayEntry.pack(
      padx=10,
      pady=10
    )
    DayEntry.configure(
      values=[
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
      ],
      width=350
    )

    SaveButton = customtkinter.CTkButton(PopWindow)
    SaveButton.pack(
      padx=10,
      pady=5
    )
    SaveButton.configure(
      text="Save Class",
      command = lambda: insertClassStudentRelation(
        uuid.uuid4(),
        StudentID,
        class_id_title_map[ClassEntry.get()],
        DayEntry.get()
      )
    )

  except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print(exc_obj)

def displayClassesPage(
    pop_window,
    classes
  ):
  try:
    ClassessLabels = []
    headers = [
      "Classe ID",
      "Subject",
      "Start Time",	
      "End Time",
      "Day"
    ]

    for widget in pop_window.winfo_children():
      if widget not in (Navbar,):
        widget.pack_forget()

    for label in ClassessLabels:
      label.destroy()

    ClassessTableFrame = customtkinter.CTkScrollableFrame(pop_window)
    ClassessTableFrame.pack(
      fill="x",
      expand=False
    )

    for col, header in enumerate(headers):
      HeaderLabel = customtkinter.CTkLabel(ClassessTableFrame)
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

    for col in range(len(headers)):
      ClassessTableFrame.columnconfigure(col, weight=1)

    if len(classes) > 0:
      for row, Class in enumerate(classes, start=1):
        ClasseID, \
        ClassSubjectArea, \
        ClasseSessionStartTime, \
        ClasseSessionEndTime, \
        ClassDay = Class          

        Classess_data = [
          ClasseID,
          ClassSubjectArea,
          ClasseSessionStartTime,	
          ClasseSessionEndTime,
          ClassDay
        ]
        for col, data in enumerate(Classess_data):
          DataLabel = customtkinter.CTkLabel(ClassessTableFrame)
          DataLabel.grid(row=row, column=col, sticky="nsew")
          DataLabel.configure(
            text=data,
            padx=10,
            pady=5
          )
          ClassessLabels.append(DataLabel)

  except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print(exc_obj)

def StudentClassesPopWindow(
    StudentID,
    ClassesForSelection,
    insertClassStudentRelation,
    getClassesStudentRelation
  ):
  try:
    PopWindow = customtkinter.CTkToplevel()
    PopWindow.grab_set()

    PopWindow.geometry("700x600")
    PopWindow.resizable(False, False)

    PopWindow.title("Classes")

    global Navbar

    Navbar = customtkinter.CTkFrame(PopWindow)
    Navbar.pack(fill=customtkinter.X)

    AddClassButton = customtkinter.CTkButton(
      Navbar,
      corner_radius=0,
      text="Add Class",
      command = lambda: addClassPage(
        PopWindow,
        ClassesForSelection,
        StudentID,
        insertClassStudentRelation
      )
    )
    AddClassButton.pack(side=customtkinter.LEFT)

    ClassesButton = customtkinter.CTkButton(
      Navbar,
      corner_radius=0,
      text="Classes",
      command=lambda: displayClassesPage(
        PopWindow,
        getClassesStudentRelation(StudentID)
      )
    )
    ClassesButton.pack(side=customtkinter.LEFT)

    addClassPage(
      PopWindow,
      ClassesForSelection,
      StudentID,
      insertClassStudentRelation
    )

  except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print(exc_obj)