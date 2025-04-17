import sys
import os
import json
import requests

from CTkMessagebox import CTkMessagebox
from app.models import course
from app.core.GlobalData import GlobalData

def AddCourse(course_object):
    try:
      data = {
        "course_id": course_object.ID,
        "title": course_object.title,
        "credit": course_object.credit,
        "maximum_units": course_object.MaximumUnits,
        "long_course_title": course_object.LongCourseTitle,
        "offering_nbr": course_object.OfferingNBR,
        "academic_group": course_object.AcademicGroup,
        "subject_area": course_object.SubjectArea,
        "catalog_nbr": course_object.CatalogNBR,
        "campus": course_object.campus,
        "academic_organization": course_object.AcademicOrganization,
        "component": course_object.component
      }

      response = requests.post(
        GlobalData.config.getBaseURL() + "/admin/insert_course",
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
          message = message if message else "Something went wrong while inserting the course",
          icon = icon
        )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
      pass 

def RemoveCourse(course_id, refresh_table_function: None):
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
          GlobalData.config.getBaseURL() + "/admin/remove_course",
          params = data
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

def SearchCourses(course_id):
	try:
		data = {
			"course_id": course_id
		}
		response = requests.get(
			GlobalData.config.getBaseURL() + "/admin/search_courses",
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

def GetCourses():
	try:
		response = requests.get(GlobalData.config.getBaseURL() + "/admin/get_courses").content
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
