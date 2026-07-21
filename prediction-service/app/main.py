# prediction-service/app/main.py
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="EcoFlinkScheduler Prediction Service",
    version="0.1.0",
)


class PredictionRequest(BaseModel):
    recent_load: list[float]


class PredictionResponse(BaseModel):
    predicted_load: float
    model: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    # Simple baseline predictor: use the average of recent observations.
    if not payload.recent_load:
        return PredictionResponse(predicted_load=0.0, model="mean-baseline")

    predicted = sum(payload.recent_load) / len(payload.recent_load)
    return PredictionResponse(predicted_load=predicted, model="mean-baseline")
