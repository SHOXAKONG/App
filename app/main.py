from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import admin, customer, auth
from app.database import engine, Base
from app import models
from app.utils import log_message

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)


app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(customer.router, prefix="/customer", tags=["Customer"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    log_message("Server is up and running", level="INFO")
    return {"message": "Welcome to NewEra Cash & Carry API!"}

