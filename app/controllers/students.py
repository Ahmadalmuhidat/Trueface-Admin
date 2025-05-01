import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.models import student
from app.core.GlobalData import GlobalData

def get_students() -> list:
	"""
	Retrieves a list of all students from the backend API and stores them in the GlobalData object.

	This function sends a GET request to the backend API to fetch all student data. If successful, the student details are retrieved and stored in the `GlobalData.get_students()` list. If there is an error or the request fails, an error message is displayed.

	Args:
		None

	Returns:
		list: A list of `student.Student` objects representing all the students.
	"""
	try:
		response = requests.get(GlobalData.config.get_base_url() + "/admin/get_all_students").content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.get_students() = [
				student.Student(
					data['ID'],
					data['FirstName'],
					data['MiddleName'],
					data['LastName'], 
					data['Gender'],
					data['CreateDate']
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while getting the students",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def add_student(student_object: student) -> None:
	"""
	Adds a new student to the system by sending the student data to the backend API.

	This function constructs the student data from the provided `student_object` and sends a POST request to the backend API to insert the student into the system. If the request is successful, the newly added student data is returned. If there is an error, an error message is displayed.

	Args:
		student_object (student): An instance of the `student.Student` class containing the student's details.

	Returns: None
	"""
	try:
		data = {
			"student_id": student_object.student_id,
			"first_name": student_object.first_name,
			"middle_name": student_object.middle_name,
			"last_name": student_object.last_name,
			"gender": student_object.gender,
			"face_encode": student_object.face_encode
		}

		response = requests.post(
			GlobalData.config.get_base_url() + "/admin/insert_student",
			data = data,
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			return response.get("data")
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while inserting the student",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def remove_student(student_id: str, refresh_table_function: function) -> None:
	"""
	Removes a student from the system by sending the student ID to the backend API.

	This function sends a POST request to the backend API to delete a student based on the provided `student_id`. If the request is successful, a success message is displayed and the table is refreshed by calling the `refresh_table_function`. In case of an error, an error message is shown.

	Args:
		student_id (str): The ID of the student to be removed.
		refresh_table_function (function): A function to refresh the table view after the student is removed.

	Returns: None
	"""
	try:
		data = {
			"student_id": student_id
		}
		response = requests.post(
			GlobalData.config.get_base_url() + "/admin/remove_student", 
			data = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			if response.get("data"):
				title = "Relation has been deleted"
				message = "Class has been removed successfully"
				icon = "check"
				CTkMessagebox(title=title, message=message,icon=icon)
				refresh_table_function()
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while removing the student",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def search_student(student_id: str) -> list:
	"""
	Searches for a student by their ID in the system and updates the list of students.

	This function sends a GET request to the backend API to search for a student based on the provided `student_id`. If the request is successful, the list of students in `GlobalData` is updated with the student data returned by the API. In case of an error, an error message is displayed.

	Args:
		student_id (str): The ID of the student to be searched.

	Returns:
		list: The list of students objects representing the search results.
	"""
	try:
		data = {
			"student_id": str(student_id)
		}
		response = requests.get(
			GlobalData.config.get_base_url() + "/admin/search_student",
			params = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.get_students() = [
				student.Student(
					data['ID'],
					data['FirstName'],
					data['MiddleName'],
					data['LastName'], 
					data['Gender'],
					data['CreateDate']
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while searching in students",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass
