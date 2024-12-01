from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck() -> dict[str, str]:
    return {
        "status": "OK"}
