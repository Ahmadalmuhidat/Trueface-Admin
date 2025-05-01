import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.models import class_
from app.core.GlobalData import GlobalData

def get_classes() -> list:
  """
  Fetches all class data from the backend and populates GlobalData.get_classes().

  This function sends a GET request to the `/admin/get_classes` endpoint and, 
  if successful, maps the returned data into Class objects and stores them 
  in the `GlobalData.get_classes()` list.

  If the request fails or an error occurs, a message box is shown to inform the user.

	Returns:
	 list: A list of classes objects.
  """
  try:
    response = requests.get(GlobalData.config.get_base_url() + "/admin/get_classes").content
    response = json.loads(response.decode('utf-8'))

    if response.get("status_code") == 200:
      GlobalData.get_classes() = [
        class_.Class(
          data['ID'],
          data['SubjectArea'],
          data['CatalogNBR'],
          data['AcademicCareer'],
          data['Course'], 
          data['OfferingNBR'], 
          data['StartTime'],
          data['EndTime'], 
          data['Section'], 
          data['Component'], 
          data['Campus'], 
          data['Instructor'], 
          data['InstructorType']
        ) for data in response.get("data")
      ]
    else:
      title = "Error"
      message = response.get("error")
      icon = "cancel"
      CTkMessagebox(
        title=title,
        message=message if message else "Something went wrong while getting the classes",
        icon=icon
      )

  except Exception as e:
    ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
    FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
    print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
    print(ExceptionObject)
    pass

def add_class(class_object: class_) -> None:
  """
  Sends a POST request to insert a new class into the system.

  Args:
    class_object (Class): An object containing all the required class information.

  Returns:
    dict or None:
      - Returns the response data if the class was inserted successfully.
      - If insertion fails, displays an error message using CTkMessagebox and returns None.
  """
  try:
    data = {
      "class_id": class_object.class_id,
      "subject": class_object.subject_area,
      "catalog_nbr": class_object.catalog_nbr,
      "academic_career": class_object.academic_career,
      "course": class_object.Course,
      "offering_nbr": class_object.offering_nbr,
      "start_time": class_object.start_time,
      "end_time": class_object.end_time,
      "section": class_object.section,
      "component": class_object.component,
      "campus": class_object.campus,
      "instructor_id": class_object.instructor_id,
      "instructor_type": class_object.instructor_type
    }

    response = requests.post(
      GlobalData.config.get_base_url() + "/admin/insert_class",
      data=data
    ).content
    response = json.loads(response.decode('utf-8'))

    if response.get("status_code") == 200:
      return response.get("data")
    else:
      title = "Error"
      message = response.get("error")
      icon = "cancel"
      CTkMessagebox(
        title=title,
        message=message if message else "Something went wrong while inserting the class",
        icon=icon
      )

  except Exception as e:
    ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
    FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
    print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
    print(ExceptionObject)
    pass

def remove_class(class_id: str, refresh_table_function: function) -> None:
	"""
	Sends a POST request to remove a class based on its ID after user confirmation.

	Args:
		class_id (str): The ID of the class to be removed.
		refresh_table_function (function): A callback function to refresh the UI table after deletion.

	Returns: None
  """
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
			data = {
				"class_id": class_id
			}
			response = requests.post(
				GlobalData.config.get_base_url() + "/admin/remove_class",
				data = data
			).content
			response = json.loads(response.decode('utf-8'))

			if response.get("status_code") == 200:
				if response.get("data"):
					title = "Success"
					message = "Class has been deleted"
					icon = "check"
					CTkMessagebox(title=title, message=message,icon=icon)
					refresh_table_function()
			else:
				title = "Error"
				message = response.get("error")
				icon = "cancel"
				CTkMessagebox(
					title = title,
					message = message if message else "Something went wrong while removing the class",
					icon = icon
				)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def search_class(class_id: str) -> list:
	"""
	Searches for a class by its ID and updates the global class list with the result.

	Args:
		class_id (str): The ID of the class to search for.

	Returns:
	  list: A list of classes objects representing the search results.
	"""
	try:
		data = {
			"class_id": class_id
		}
		response = requests.get(
			GlobalData.config.get_base_url() + "/admin/search_class",
			params = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.get_classes() =  [
				class_.Class(
					data['ID'],
					data['SubjectArea'],
					data['CatalogNBR'],
					data['AcademicCareer'],
					data['Course'], 
					data['OfferingNBR'], 
					data['StartTime'],
					data['EndTime'], 
					data['Section'], 
					data['Component'], 
					data['Campus'], 
					data['Instructor'], 
					data['InstructorType']
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while searching in classes",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def get_student_classes(student_id: str) -> None:
	"""
	Retrieves the list of classes associated with a specific student.

	Args:
		student_id (str): The unique identifier of the student.

	Returns:
		list: A list of RelationClass objects representing the student's class schedule,
		Returns None if an error occurs or the API request fails.
	"""
	try:
		data = {
			"student_id": student_id
		}
		response = requests.get(
			GlobalData.config.get_base_url() + "/admin/get_classes_student_relation",
			params = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			return [
				class_.RelationClass(
					relation_id = data['Relation'],
					class_id = data['Class'],
					SubjectArea = data['SubjectArea'],
					StartTime = data['StartTime'],
					EndTime = data['EndTime'],
					day = data['Day']
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while getting classes for the student",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def remove_student_from_class(relation_id: str) -> None:
	"""
	Removes the relationship between a student and a class using the relation ID.

	Args:
		relation_id (str): The unique identifier for the student-class relation.

	Returns: None
	"""
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
			data = {
				"relation_id": relation_id
			}
			response = requests.post(
				GlobalData.config.get_base_url() + "/admin/remove_class_student_relation",
				data = data
			).content
			response = json.loads(response.decode('utf-8'))

			if response.get("status_code") == 200:
				if response.get("data"):
					title = "Class has been removed"
					message = "Class has been removed successfully"
					icon = "check"
					CTkMessagebox(
						title = title,
						message = message,
						icon = icon
					)
			else:
				title = "Error"
				message = response.get("error")
				icon = "cancel"
				CTkMessagebox(
					title = title,
					message = message if message else "Something went wrong while removing the class",
					icon = icon
				)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def remove_student_from_all_classes(relation_id: str) -> None:
	"""
	Removes all class associations for a given student using their relation ID.

	Args:
		relation_id (str): The unique identifier for the student whose class relations should be cleared.

	Returns: None
	"""
	try:
		data = {
			"ID": relation_id
		}
		response = requests.post(
			GlobalData.config.get_base_url() + "/admin/clear_class_student_relation",
			data = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			if response.get("data"):
				title = "Classes has been cleared"
				message = "Class has been cleared successfully"
				icon = "check"
				CTkMessagebox(
					title = title,
					message = message,
					icon = icon
				)
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while clearing the classes",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def get_classes_for_selection() -> list:
	"""
	Retrieves a list of classes for selection purposes (e.g., dropdowns or lists in the UI).

	Returns:
		List of classes  if successful, otherwise None.
	"""
	try:
		response = requests.get(
			GlobalData.config.get_base_url() + "/admin/get_classes_for_selection"
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			return [
				class_.Class(
					class_id = data['ID'],
					subject_area = data['SubjectArea'],
					start_time = data['StartTime'],
					end_time = data['EndTime'],
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while getting classes",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def add_student_to_class(relation_id: str, student_id: str, class_id: str, class_day: str) -> None:
	"""
	Associates a student with a class on a specific day by sending data to the backend API.

	Args:
		relation_id (str): Unique identifier for the student-class relationship.
		student_id (str): ID of the student being added.
		class_id (str): ID of the class to assign the student to.
		class_day (str): Day of the week the class occurs.

	Returns: None
	"""
	try:
		data = {
			"relation_id": relation_id,
			"student_id": student_id,
			"class_id": class_id,
			"day": class_day
		}
		response = requests.post(
			GlobalData.config.get_base_url() + "/admin/insert_class_student_relation",
			data = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			title="Success"
			message="New class has been added"
			icon="check"
			CTkMessagebox(
				title = title,
				message = message,
				icon = icon
			)
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while inserting the class",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass
