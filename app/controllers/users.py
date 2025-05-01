import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.models import user
from app.core.GlobalData import GlobalData

def get_users() -> list:
	"""
	Retrieves the list of users from the backend API and stores them in the GlobalData object.

	This function sends a GET request to the backend API to fetch all users in the system. If the request is successful, the list of users in `GlobalData` is updated with the user data returned by the API. If the request fails, an error message is displayed.

	Returns:
		list: The list of users objects objects representing all the students.
	"""
	try:
		response = requests.get(GlobalData.config.get_base_url() + "/admin/get_users").content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.get_users() = [
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

def add_user(user_object: user) -> None:
	"""
	Adds a new user to the backend system.

	This function sends a POST request to the backend API to insert a new user into the system. It takes a `user_object` containing the user's information, including user ID, name, email, password, and role. Upon success, a confirmation message is shown, otherwise, an error message is displayed.

	Args:
		user_object (user): An instance of the `user` class containing the user's details.

	Returns: None
  """
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

def remove_user(user_id: str, refresh_table_function: function) -> None:
	"""
	Removes a user from the backend system after confirming the deletion.

	This function first prompts the user for confirmation to delete the selected user. If confirmed, it sends a POST request to the backend API to remove the user. Upon success, a success message is displayed, and the table is refreshed. If an error occurs, an error message is shown.

	Args:
		user_id (str): The unique identifier of the user to be deleted.
		refresh_table_function (function): A function that is called to refresh the user list (typically to update the displayed data in the UI) after the user has been removed.

	Returns: None
	"""
	try:
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

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass

def search_user(user_id: str) -> list:
	"""
	Searches for a user in the backend system based on the provided user ID.

	This function sends a GET request to the backend API with the provided user ID as a query parameter. If the user is found, it updates the global list `GlobalData.get_users()` with the user's details. If the user is not found or an error occurs, an error message is displayed.

	Parameters:
		user_id (str): The unique identifier of the user to be searched for.

	Returns:
		list: A list of `user.User` objects populated with the data of the found users.
	"""
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
			GlobalData.get_users() = [
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
