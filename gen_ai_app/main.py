from fastapi import FastAPI, Depends, HTTPException
from dto import HypothesisSuggestionRequest, HypothesisSuggestionResponse
from suggestion import SuggestionEngine
from exceptions import LlmResponseNotSerializableIntoArrayOfDictError

app = FastAPI()

@app.post("/suggestion")
async def suggest_hypothesis(rq: HypothesisSuggestionRequest, engine: SuggestionEngine = Depends(SuggestionEngine)) -> list[HypothesisSuggestionResponse]:
    try:
        response = engine.suggest(rq.product_context)
        return response
    except LlmResponseNotSerializableIntoArrayOfDictError as e:
        raise HTTPException(status_code=501, detail=e.message)
    
