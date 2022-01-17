from abc import ABC, abstractmethod


class Parameter(ABC):
  name: str

  @abstractmethod
  def validate(self, value: Any):
    """ Validate value or throw ValidationError """
    ...

  def get_json_repr(self):
    """ Returns json representation of the field """
    ...


class NumberParameter(Parameter):
  min: float
  max: float
  default: float
  required: bool

  def __init__(self, name, min, max, required, default):
    ...

  def validate(self. value: Any):
    ...

  def get_json_repr(self):
    ...


class StringParameter(Parameter):
  minlength: int
  maxlength: int
  default: str
  required: bool

  def __init__(self, name, minlength, maxlength, required, default):
    ...

  def validate(self, value: Any):
    ...

  def get_json_repr(self):
    ...


class ChoiceParameter(Parameter):
  choices: list[str]
  default: str
  required: bool

  def __init__(self, name, choices, required, default):
    ...

  def validate(self, value: Any):
    ...

  def get_json_repr(self):
    ...
