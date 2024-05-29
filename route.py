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


@app.get("/")
async def from_clean(q: str):
    print(q)
    result = clean_grem(q)
    logging.info(f"clean_grem result: {result}")
    return result 

