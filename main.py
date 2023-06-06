import uvicorn
from fastapi import FastAPI
from app import app, Base, engine
from apscheduler.schedulers.background import BackgroundScheduler
from app.controllers.recommend import scheduler


if __name__ == '__main__':
    task = BackgroundScheduler()
    job = task.add_job(scheduler, 'interval', minutes=1)
    task.start()

    Base.metadata.create_all(engine)
    uvicorn.run("main:app", port=3031, host='185.119.58.234', reload=True)
    
