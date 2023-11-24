from fastapi import FastAPI ,HTTPException, Depends
import requests

app = FastAPI()

# Endpoint GET
@app.get("/get")
def get():
    return {"BircleAI"}

# Endpoint POST
@app.get("/post")
def post():
    public_api = "https://api.publicapis.org/random"
    response = requests.get(public_api)
    print("Response:", response.json())
    return response.json()

# Endpoint UPDATE
@app.get("/update/{number}")

def update_number(number: int):
    squared_number = number ** 2
    return {"original number ": number,
        "squared number ": squared_number}
