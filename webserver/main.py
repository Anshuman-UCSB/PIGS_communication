import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/land")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
	os.system("uvicorn main:app --reload")