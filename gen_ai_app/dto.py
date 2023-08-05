from pydantic import BaseModel

class HypothesisSuggestionRequest(BaseModel):
    product_context: str    

class HypothesisSuggestionResponse(BaseModel):
    hypothesis: str