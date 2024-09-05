from fastapi import FastAPI
import uvicorn

from routes import init_routes

app = FastAPI()

init_routes(app)

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)