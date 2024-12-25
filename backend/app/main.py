import sys
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Pixel"}

if __name__ == "__main__":
    print(sys.path)
    uvicorn.run(app, host="0.0.0.0", port=8001)
