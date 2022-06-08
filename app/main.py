import os
import dotenv
from fastapi import FastAPI
from routers import programs
from routers import index
from starlette.middleware.cors import CORSMiddleware

dotenv.load_dotenv()

app = FastAPI()

origins = os.getenv("CORS_ORIGIN_SERVER")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(programs.router, prefix="/programs")
app.include_router(index.router)