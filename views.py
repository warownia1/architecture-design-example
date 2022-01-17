from abc import ABC, abstractmethod
from .input_form import *
from .parameters import *


class JSONParameterView(ABC):
  @abstractmethod
  def get_json_repr(self):
    ...


class JSONNumberParameterView(JSONParameterView):
  parameter: NumberParameter

  def __init__(self, parameter: NumberParameter):
    ...

  def get_json_repr(self):
    ...


class JSONStringParameterView(JSONParameterView):
  parameter: StringParameter

  def __init__(self, parameter: StringParameter):
    ...

  def get_json_repr(self):
    ...


class JSONChoiceParameterView(JSONParameterView):
  parameter: ChoiceParameter

  def __init__(self, parameter: ChoiceParameter):
    ...

  def get_json_repr(self):
    ...


class JSONFormView:
  form: InputForm

  def __init__(self, form: InputForm):
    ...

  def get_json_repr(self):
    params_repr = []
    for param in self.form.parameters:
      # parameter "casting" must be performed in each case
      if isinstance(param, NumberParameter):
        view = JSONNumberParameterView(param)
      elif isinstance(param, StringParameter):
        view = JSONStringParameterView(param)
      elif isinstance(param, ChoiceParameter):
        view = JSONChoiceParameterView(param)
      else:
        # what if new parameter type is added?
        raise TypeError
      params_repr.append(view.get_json_repr())
    return {
      "parameters": params_repr
    }
