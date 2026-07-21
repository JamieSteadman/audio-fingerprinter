from fastapi import FastAPI

app = FastAPI(title="Audio Fingerprinter API")

@app.get("/")
def read_root():
    return {"status": "Backend is running!"}