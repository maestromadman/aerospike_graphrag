from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from clean import clean_grem

# create fastapi instance called "app"
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

# HTTP request; how you communicate with path
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/")
async def from_clean():
    result = clean_grem()
    logging.info(f"clean_grem result: {result}")
    return result