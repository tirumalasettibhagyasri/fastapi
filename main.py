from fastapi import FastAPI

app = FastAPI(title="Bhagya Sri API")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name")
def read_name():
    return {"name": "Bhagya Sri"}

@app.get("/batch")
def read_batch():
    return {"batch": "Batch 55B"}