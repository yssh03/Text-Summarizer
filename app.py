import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from main import data_ingestion_stage, data_validation_stage, data_transformation_stage, model_trainer_stage, model_evaluation_stage
from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Text(BaseModel):
    text: str


@app.get("/", tags=["authentication"])
def welcome():
    return RedirectResponse(url="/docs")


@app.get("/train", tags=["model"])
async def training():
    try:
        await data_ingestion_stage()
        await data_validation_stage()
        await data_transformation_stage()
        await model_trainer_stage()
        await model_evaluation_stage()
        return JSONResponse("Training successful !!")
    except Exception as e:
        return JSONResponse(f"Error: {e}")


@app.post("/predict/", tags=["model"])
async def predict(text: Text):
    try:
        print(text.text)
        predict = PredictionPipeline()
        output = predict.prediction(text.text)
        return JSONResponse({"summary": output})
    except Exception as e:
        return JSONResponse(f"Error: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)
