from fastapi import FastAPI

app = FastAPI(title="Antonmazur API")

@app.get("/")
async def root():
    return {"message": "Antonmazur FastAPI Project"}

@app.get("/health")
async def health():
    return {"status": "ok"}
