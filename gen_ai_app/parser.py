import json
from langchain.schema import BaseOutputParser
from exceptions import LlmResponseNotSerializableIntoArrayOfDictError

class ArrayOfDictResponseParser(BaseOutputParser):
    """Parse the output of an LLM call to a Array of Dict (later mapped to JSON)."""

    def parse(self, text: str) -> list[dict[str, str]]:
        """Parse the output of an LLM call."""
        try:
            serialized_response = json.loads(text) 
            return serialized_response
        except json.decoder.JSONDecodeError as e:
            raise LlmResponseNotSerializableIntoArrayOfDictError(e)