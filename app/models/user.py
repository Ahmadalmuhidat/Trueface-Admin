import sys
import os
import app.config.configrations as Configrations

from CTkMessagebox import CTkMessagebox

class User:
  def __init__(self, user_id, name, email, role):
    self.user_id = user_id
    self.name = name
    self.email = email
    self.role = role

    self.config = Configrations.Configrations()