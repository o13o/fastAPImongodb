from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mount static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# Sample products
products = [
    {
        "id": 1,
        "name": "Yellow Designer Dress",
        "price": 2499,
        "image": "/static/images/yellow_dress.jpg"
    },
    {
        "id": 2,
        "name": "White Formal Shirt",
        "price": 1299,
        "image": "/static/images/white_shirt.jpg"
    },
    {
        "id": 3,
        "name": "Blue Denim Jeans",
        "price": 1899,
        "image": "/static/images/blue_jeans.jpg"
    },
    {
        "id": 4,
        "name": "Red Ethnic Dress",
        "price": 2999,
        "image": "/static/images/red_dress.jpg"
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "products": products
    })

@app.get("/cart", response_class=HTMLResponse)
async def cart(request: Request):
    return templates.TemplateResponse("cart.html", {
        "request": request
    })
