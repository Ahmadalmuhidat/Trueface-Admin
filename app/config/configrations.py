class Configrations:
  # static
  window = None
  token = None

  def __init__(self) -> None:
    # private
    self._base_url = "http://localhost:8000"

  @classmethod
  def loading_cursor_on(cls):
    cls.get_window().configure(cursor="watch")
    cls.get_window().update()

  @classmethod
  def loading_cursor_off(cls):
    cls.get_window().configure(cursor="")
    cls.get_window().update()

  @classmethod
  def set_window(cls, window):
    cls.window = window

  @classmethod
  def get_window(cls):
    return cls.window

  @classmethod
  def set_token(cls, token):
    cls.token = token

  @classmethod
  def get_token(cls):
    return cls.token

  def get_base_url(self):
    return self._base_url