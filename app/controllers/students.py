import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.models import student
from app.core.GlobalData import GlobalData

def get_students():
	try:
		response = requests.get(GlobalData.config.get_base_url() + "/admin/get_all_students").content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.students = [
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

def add_student(student_object):
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

def remove_student(student_id, refresh_table_function: None):
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

def search_student(student_id):
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
			GlobalData.students = [
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
