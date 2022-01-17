from parameters import Parameter
from typing import Any
from .views import JSONFormView

class InputForm:
  parameters: list[Parameter]
  formdata: dict[Any]

  def __init__(self, parameters: list[Parameter]):
    self.parameters = parameters

  def bind_data(self, formdata: dict[Any]):
    self.formdata = formdata

  def validate(self):
    for parameter in self.parameters:
      data = self.formdata.get(parameter.name)
      parameter.validate(data)

  def get_json_view(self) -> JSONFormView:
    return JSONFormView(self)

  def bind_request_data(self, formdata: MultiDict[str]):
    data = {
      param.name: param.parse_request_data(formdata)
      for param in self.parameters
    }
