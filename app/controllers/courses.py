import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.models import course
from app.core.GlobalData import GlobalData

def get_courses():
	try:
		response = requests.get(GlobalData.config.get_base_url() + "/admin/get_courses").content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.courses = [
				course.Course(
					data['ID'],
					data['Title'],
					data['Credit'],
					data['MaximumUnits'], 
					data['LongCourseTitle'],
					data['OfferingNBR'],
					data['AcademicGroup'], 
					data['SubjectArea'],
					data['CatalogNBR'],
					data['Campus'], 
					data['AcademicOrganization'],
					data['Component']
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while getting the courses",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass 

def add_course(course_object):
    try:
      data = {
        "course_id": course_object.course_id,
        "title": course_object.title,
        "credit": course_object.credit,
        "maximum_units": course_object.maximum_units,
        "long_course_title": course_object.long_course_title,
        "offering_nbr": course_object.offering_nbr,
        "academic_group": course_object.academic_group,
        "subject_area": course_object.subject_area,
        "catalog_nbr": course_object.catalog_nbr,
        "campus": course_object.campus,
        "academic_organization": course_object.academic_organization,
        "component": course_object.component
      }

      response = requests.post(
        GlobalData.config.get_base_url() + "/admin/insert_course",
        data = data
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
          message = message if message else "Something went wrong while inserting the course",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass 

def remove_course(course_id, refresh_table_function: None):
    try:
      title = "Conformation"
      message = "Are you sure you want to delete the course"
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
          "course_id": course_id
        }
        response = requests.post(
          GlobalData.config.get_base_url() + "/admin/remove_course",
          data = data
        ).content
        response = json.loads(response.decode('utf-8'))

        if response.get("status_code") == 200:
          if response.get("data"):
            title = "Success"
            message = "Course has been deleted"
            icon = "check"
            CTkMessagebox(title=title, message=message,icon=icon)
            refresh_table_function()
        else:
          title = "Error"
          message = response.get("error")
          icon = "cancel"
          CTkMessagebox(
            title = title,
            message = message if message else "Something went wrong while removing the course",
            icon = icon
          )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

def search_course(course_id):
	try:
		data = {
			"course_id": course_id
		}
		response = requests.get(
			GlobalData.config.get_base_url() + "/admin/search_courses",
			params = data
		).content
		response = json.loads(response.decode('utf-8'))

		if response.get("status_code") == 200:
			GlobalData.courses = [
				course.Course(
					data['ID'],
					data['Title'],
					data['Credit'],
					data['MaximumUnits'], 
					data['LongCourseTitle'],
					data['OfferingNBR'],
					data['AcademicGroup'], 
					data['SubjectArea'],
					data['CatalogNBR'],
					data['Campus'], 
					data['AcademicOrganization'],
					data['Component']
				) for data in response.get("data")
			]
		else:
			title = "Error"
			message = response.get("error")
			icon = "cancel"
			CTkMessagebox(
				title = title,
				message = message if message else "Something went wrong while searching in courses",
				icon = icon
			)

	except Exception as e:
		ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
		FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
		print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
		print(ExceptionObject)
		pass 
