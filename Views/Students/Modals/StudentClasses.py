import os
import sys
import customtkinter
import uuid

from CTkMessagebox import CTkMessagebox

def AddClassInputWindow(
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

    ClassLabel = customtkinter.CTkLabel(
      PopWindow,
      text="Select Class:"
    )
    ClassLabel.pack(
      padx=10,
      pady=10
    )

    ClassEntry = customtkinter.CTkComboBox(
      PopWindow,
      values=[f"{x[1]} {x[2]}-{x[3]}" for x in ClassesForSelection],
      width=350
    )
    ClassEntry.pack(
      padx=10,
      pady=10
    )
    ClassEntry.set("None")

    DayLabel = customtkinter.CTkLabel(
      PopWindow,
      text="Select Day:"
    )
    DayLabel.pack(
      padx=10,
      pady=10
    )

    DayEntry = customtkinter.CTkComboBox(
      PopWindow,
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
    DayEntry.pack(
      padx=10,
      pady=10
    )
    DayEntry.set("None")

    SaveButton = customtkinter.CTkButton(
      PopWindow,
      text="Save Class",
      command=lambda: insertClassStudentRelation(
        str(uuid.uuid4()),
        StudentID,
        class_id_title_map[ClassEntry.get()],
        DayEntry.get()
      )
    )
    SaveButton.pack(
      padx=10,
      pady=5
    )

  except Exception as e:
    ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
    FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
    print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
    print(ExceptionObject)

def displayClassesPage(
  pop_window,
  StudentID,
  GetClassesStudentRelation,
  RemoveClassesStudentRelation,
  ClearClassesStudentRelation
):
  try:
    for widget in pop_window.winfo_children():
      if widget not in (Navbar,):
        widget.pack_forget()

    classes = GetClassesStudentRelation(StudentID)
    ClassessLabels = []
    headers = [
      "Classe ID",
      "Subject",
      "Start Time",    
      "End Time",
      "Day"
    ]

    SearchBarFrame = customtkinter.CTkFrame(
      pop_window,
      bg_color="transparent"
    )
    SearchBarFrame.pack(
      fill="x",
      expand=False
    )

    SearchButton = customtkinter.CTkButton(
      SearchBarFrame,
      command=lambda: ClearClassesStudentRelation(StudentID),
      text="Clear"
    )
    SearchButton.grid(
      row=0,
      column=0,
      sticky="nsew",
      pady=10,
      padx=5
    )
    
    ClassessTableFrame = customtkinter.CTkScrollableFrame(pop_window)
    ClassessTableFrame.pack(
      fill = "both",
      expand = True
    )

    for col, header in enumerate(headers):
        HeaderLabel = customtkinter.CTkLabel(
          ClassessTableFrame,
          text=header,
          padx=10,
          pady=10
        )
        HeaderLabel.grid(
          row=0,
          column=col,
          sticky="nsew"
        )

    for col in range(len(headers)):
      ClassessTableFrame.columnconfigure(col, weight=1)

    def RemoveRelation(rid):
      try:
        title = "Conformation"
        message = "Are you sure you want to delete the class"
        icon = "question"
        conformation = CTkMessagebox(
          title = title,
          message = message,
          icon = icon,
          option_1 = "yes",
          option_2 = "cancel" 
        )

        if conformation.get() == "yes":
          RemoveClassesStudentRelation(rid)
          nonlocal classes
          classes = GetClassesStudentRelation(StudentID)
          DisplayTable()

      except Exception as e:
        ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
        FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
        print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
        print(ExceptionObject)
  
    def DisplayTable():
      try:
        for label in ClassessLabels:
          label.destroy()

        if len(classes) > 0:
          for row, Class in enumerate(classes, start=1):
            RelationID, \
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
              DataLabel = customtkinter.CTkLabel(
                ClassessTableFrame,
                text=data,
                padx=10,
                pady=5
              )
              DataLabel.grid(
                row=row,
                column=col,
                sticky="nsew"
              )
              ClassessLabels.append(DataLabel)

            DeleteButton = customtkinter.CTkButton(
              ClassessTableFrame,
              text="Remove",
              fg_color="red",
              command=lambda rid=RelationID: RemoveRelation(rid)
            )
            DeleteButton.grid(
              row=row,
              column=len(Classess_data),
              sticky="nsew",
              padx=10,
              pady=5
            )
            ClassessLabels.append(DeleteButton)

      except Exception as e:
        ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
        FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
        print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
        print(ExceptionObject)

    DisplayTable()
  except Exception as e:
    ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
    FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
    print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
    print(ExceptionObject)

def StudentClassesPopWindow(
  StudentID,
  ClassesForSelection,
  insertClassStudentRelation,
  GetClassesStudentRelation,
  RemoveClassesStudentRelation,
  ClearClassesStudentRelation
):
  try:
    PopWindow = customtkinter.CTkToplevel()
    PopWindow.grab_set()

    PopWindow.geometry("700x500")
    PopWindow.resizable(False, False)
    PopWindow.title("Classes")

    global Navbar

    Navbar = customtkinter.CTkFrame(PopWindow)
    Navbar.pack(fill = customtkinter.X)

    AddClassButton = customtkinter.CTkButton(
      Navbar,
      corner_radius=0,
      text="Add Class",
      command=lambda: AddClassInputWindow(
        PopWindow,
        ClassesForSelection,
        StudentID,
        insertClassStudentRelation
      )
    )
    AddClassButton.pack(side=customtkinter.LEFT)

    ClassesButton = customtkinter.CTkButton(
        Navbar,
        corner_radius = 0,
        text = "Classes",
        command = lambda: displayClassesPage(
          PopWindow,
          StudentID,
          GetClassesStudentRelation,
          RemoveClassesStudentRelation,
          ClearClassesStudentRelation
        )
    )
    ClassesButton.pack(side=customtkinter.LEFT)

    AddClassInputWindow(
      PopWindow,
      ClassesForSelection,
      StudentID,
      insertClassStudentRelation
    )

  except Exception as e:
    ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
    FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
    print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
    print(ExceptionObject)
