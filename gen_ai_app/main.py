from fastapi import FastAPI, Depends
from dto import HypothesisSuggestionRequest, HypothesisSuggestionResponse
from suggestion import SuggestionEngine


app = FastAPI()

@app.post("/suggestion")
async def suggest_hypothesis(rq: HypothesisSuggestionRequest) -> list[HypothesisSuggestionResponse]:
    engine = SuggestionEngine()
    response = engine.suggest(rq.product_context)
    print(response)
    return response
