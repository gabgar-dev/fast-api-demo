from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "Lars"}


@app.get ("/about") 
def about():
    return {"Data": "About"}