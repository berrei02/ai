class LlmResponseNotSerializableIntoArrayOfDictError(BaseException):
    message = "Text response from LLM cannot be mapped to Array of Dict format."