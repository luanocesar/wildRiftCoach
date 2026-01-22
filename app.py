import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import llm as llm

app = FastAPI()

class Prompt(BaseModel):
    championName: str

@app.post("/llm")
async def promptToLlm(prompt : Prompt | None = None):
    if not prompt.championName or len(prompt.championName.strip()) == 0:
        return {"response": "Por favor, informe o nome de um campeão."}
        
    answer = await llm.run_llm(prompt.championName)
    return {"response": answer}

try:
    app.mount("/", StaticFiles(directory="frontend/wildriftcoach_fe/dist", html=True), name="static")
    print("Server is Up")
except Exception as e:
    print(e)