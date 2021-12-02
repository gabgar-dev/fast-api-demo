from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get ("/about") 
def about():
    return {"Data": "About"}