from fastapi import FastAPI
app= FastAPI()

@app.get("/home")
def home():
    return {"message": "Welcome Home"}

@app.get("/login")
def login():
    return {"message": "Welcome to Login"}

