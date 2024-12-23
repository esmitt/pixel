import sys
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Pixel"}

# if __name__ == "__main__":
#     print(sys.path)
