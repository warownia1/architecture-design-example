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

  def parse_request_data(self, formdata: MultiDict[str]):
    """ Parses data coming from the http request """
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

  def parse_request_data(self, formdata):
    return int(formdata.get(self.name))


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

  def parse_request_data(self, formdata):
    return formdata.get(self.name)


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

  def parse_request_data(self, formdata):
    return formdata.get(self.name)
