from fastapi import FastAPI, Depends, HTTPException, Security, status
from pydantic import BaseModel, ValidationError
from server import emotion_analyzer

app = FastAPI()
emotion_analyzer = emotion_analyzer.EmotionFromText()

@app.get("/analyze/{text}")
async def analyze(text: str):
    return {"text": text,
            "dominant_emotion": emotion_analyzer.predict_emotion(text),
            "emotions": emotion_analyzer.predict_emotions(text),
            }