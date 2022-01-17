from abc import ABC, abstractmethod


class Parameter(ABC):
  name: str

  @abstractmethod
  def validate(self, value: Any):
    """ Validate value or throw ValidationError """
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


class StringParameter(Parameter):
  minlength: int
  maxlength: int
  default: str
  required: bool

  def __init__(self, name, minlength, maxlength, required, default):
    ...

  def validate(self, value: Any):
    ...


class ChoiceParameter(Parameter):
  choices: list[str]
  default: str
  required: bool

  def __init__(self, name, choices, required, default):
    ...

  def validate(self, value: Any):
    ...