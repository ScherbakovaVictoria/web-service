import uvicorn
from fastapi import FastAPI
from app import app, Base, engine


if __name__=="__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("main:app", port=8080, host='localhost', reload=True)
    
