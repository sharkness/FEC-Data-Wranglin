import os
import uvicorn
import json
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from src.data.data_fetcher import DataFetcher


# Instantiate fastAPI with appropriate descriptors
app = FastAPI(
    title='FEC Data Visualization',
    description="For displaying data gathered from FEC's API",
    version="1.0",
    docs_url='/docs'
)

# Instantiate templates path
templates = Jinja2Templates(directory="src/viz/templates/")

# Mount static files
app.mount(
    '/assets', StaticFiles(directory='src/viz/templates/assets/'), name='assets')
app.mount(
    '/images', StaticFiles(directory='src/viz/templates/images/'), name='images')


# Define routes


@app.get('/', response_class=HTMLResponse)
async def display_index(request: Request):
    """
    Displays the index page
    """
    return templates.TemplateResponse('index.html', {"request": request})


@app.get('/landing', response_class=HTMLResponse)
async def display_landing(request: Request):
    """
    Displays the landing page
    """
    return templates.TemplateResponse('landing.html', {"request": request})


@app.get('/generic', response_class=HTMLResponse)
async def display_generic(request: Request):
    """
    Displays the generic page
    """
    return templates.TemplateResponse('generic.html', {"request": request})


@app.get('/elements', response_class=HTMLResponse)
async def display_elements(request: Request):
    """
    Displays the elements page
    """
    return templates.TemplateResponse('elements.html', {"request": request})


@app.get('/map', response_class=HTMLResponse)
async def display_elements(request: Request):
    """
    Displays the map page
    """
    return templates.TemplateResponse('map.html', {"request": request, "MAPS_API_KEY": os.environ.get("MAPS_API_KEY")})


@app.post('/generic', response_class=HTMLResponse)
async def display_map_results(request: Request,
                            election_year: str = Form(...),
                            election_type: str = Form(...),
                            ship_address: str = Form(...),
                            locality: str = Form(...),
                            state: str = Form(...),
                            postcode: str = Form(...),
                            country: str = Form(...)):
    """
    Displays the generic page with map results
    """
    fetcher = DataFetcher(election_year, election_type, None, state, None)
    fetcher.api_starting_url_container
    fetcher.gimmie_data(record_limit=100)
    fetcher.save_df_data() 
    return templates.TemplateResponse('generic.html',
                                        {"request": request,
                                        "election_year": election_year,
                                        "election_type": election_type,
                                        "ship_address": ship_address,
                                        "locality": locality,
                                        "state": state,
                                        "postcode": postcode,
                                        "country": country})


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
