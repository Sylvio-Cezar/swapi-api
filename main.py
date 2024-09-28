from fastapi import FastAPI;
from routes import status, character
import uvicorn;

app = FastAPI();

app.include_router(status.router);
app.include_router(character.router);

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000);