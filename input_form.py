from parameters import Parameter
from typing import Any

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

  def get_json_repr(self):
    return {
      "parameters": [
        param.get_json_repr() for param in self.parameters
      ]
    }
