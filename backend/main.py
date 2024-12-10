from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import PRODUCTION

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Allow React app
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

if PRODUCTION:
    url = "https://react-front-end-m6xa.onrender.com"
else:
    url = "http://localhost:3000"

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        url,  # Frontend deployed on Render
    ],
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
    allow_credentials=True,  # Allow cookies or authorization headers
)

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}
