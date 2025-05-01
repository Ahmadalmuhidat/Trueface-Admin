from app.config.configrations import Configrations

class GlobalData():
  courses = []
  classes = []
  users = []
  students = []

  config = Configrations()

  def get_courses(self):
    return GlobalData.courses

  def get_classes(self):
    return GlobalData.classes
  
  def get_users(self):
    return GlobalData.users

  def get_students(self):
    return GlobalData.students