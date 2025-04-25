import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.core.GlobalData import GlobalData

def login(email, password):
	try:
		data = {
			"email": email,
			"password": password
		}

		response = requests.get(
			GlobalData.config.get_base_url() + "/admin/check_user",
			params = data
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
				message = message if message else "Something went wrong while checking user info",
				icon = icon
			)

	except Exception as e: 
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)