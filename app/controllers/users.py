import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.models import user
from app.core.GlobalData import GlobalData

def get_users():
	try:
		response = requests.get(GlobalData.config.get_base_url() + "/admin/get_users").content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.users = [
				user.User(
					data['ID'],
					data['Name'],
					data['Email'],
					data['Role'], 
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while getting the users",
				icon = icon
			)

	except Exception as e: 
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)

def add_user(user_object):
	try:
		data = {
			"user_id": user_object.user_id,
			"name": user_object.name,
			"email": user_object.email,
			"password": "1234",
			"role": user_object.role
		}

		response = requests.post(
			GlobalData.config.get_base_url() + "/admin/insert_user",
			data = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			title="Success"
			message="New user has been added"
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
				message = message if message else "Something went wrong while inserting the user",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def remove_user(user_id, refresh_table_function: None):
	title = "Conformation"
	message = "Are you sure you want to delete the user"
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
			"user_id": user_id,
		}

		response = requests.post(
			GlobalData.config.get_base_url() + "/admin/remove_user",
			data = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			title="Success"
			message="User has been removed"
			icon="check"
			CTkMessagebox(title=title, message=message,icon=icon)
			refresh_table_function()
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while removing the user",
				icon = icon
			)

def search_user(user_id):
	try:
		data = {
			"user_id": user_id
		}

		response = requests.get(
			GlobalData.config.get_base_url() + "/admin/search_user",
			params = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.users = [
				user.User(
					data['ID'],
					data['Name'],
					data['Email'],
					data['Role'], 
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while searching in users",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass
