import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
def display_index(request: Request):
    """
    Displays the index page
    """
    return templates.TemplateResponse('index.html', {"request": request})

@app.get('/landing', response_class=HTMLResponse)
def display_landing(request: Request):
    """
    Displays the landing page
    """
    return templates.TemplateResponse('landing.html', {"request": request})

@app.get('/generic', response_class=HTMLResponse)
def display_generic(request: Request):
    """
    Displays the index page
    """
    return templates.TemplateResponse('generic.html', {"request": request})

@app.get('/elements', response_class=HTMLResponse)
def display_elements(request: Request):
    """
    Displays the index page
    """
    return templates.TemplateResponse('elements.html', {"request": request})



if __name__ == '__main__':
    uvicorn.run(app)
