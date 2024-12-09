from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve React static files
app.mount("/", StaticFiles(directory="frontend-build", html=True), name="static")

@app.get("/api/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}
