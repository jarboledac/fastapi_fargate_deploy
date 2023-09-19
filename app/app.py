from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="./app/static"), name="static")


@app.get("/")
def home():
    with open("app/templates/portada.html") as file:
        content = file.read()
        return HTMLResponse(content=content)

@app.get("/saludo")
def home(name: str):
    return HTMLResponse(f"<h1>Hola {name}, estás desplegando tu app !!</h1>")