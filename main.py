import uvicorn
from fastapi import FastAPI
from fastapi import request
from fastapi.templating import Jinja2Templates  # Templating
from fastapi.responses import HTMLResponse  # Response
from fastapi.staticfiles import StaticFiles
from fastapi import BackgroundTasks  # Run background tasks
from fastapi.middleware.cors import CORSMiddleware # CORS

class Settings(BaseSettings):
    message: str
    
settings = Settings()

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(firectory="static"), name="static")

# Asynchronous 
# @app.get("/")
# async def home():
#     result = await some_async_task()
#     return result

# Run background tasks after returning a response
# def process_file(filename: str):
#     # process file :: takes minimum 3 secs (just an example)
#     pass

# @app.post("/upload/{filename}")
# async def upload_and_process(filename: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(process_file, filename)
#     return {"message": "processing file"}

# Dependency Injections
# from databases import Database
# from fastapi import Depends
# from starlette.requests import Request

# from db_helpers import get_all_data
# def get_db(request: Request):
#     return request.app.state._db

# @app.get("/data")
# def get_data(db: Database = Depends(get_db)):
#     return get_all_data(db)

# Data Validation

# from pydantic import BaseModel

# app = FastAPI()

# class Request(BaseModel):
#     username: str
#     password: str

# @app.post("/login")
# async def login(req: Request):
#     if req.username == "testdriven.io" and req.password == "testdriven.io":
#         return {"message": "success"}
#     return {"message": "Authentication Failed"}

# correct payload format
# curl -X POST 'localhost:8000/login' \
#     --header 'Content-Type: application/json' \
#     --data-raw '{\"username\": \"testdriven.io\",\"password\":\"testdriven.io\"}'


# Middleware
# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     print(f"request processed in {process_time} s")
#     return response

# CORS

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins)

# End of CORS
                   
@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/settings")
def get_settings():
    return {"message": settings.message}

# URL parameters
@app.get("/employee/{id}")
def home(id: int):
    return {"id": id}

# Query Parameters
@app.get("/employee")
def home(department: str):
    return {"department" : department}

# Templating

templates = Jinja2Templates(directory="templates")

@app.get("/about", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.post("/")
def root_post():
    return {"Hello": "POST"}

# Also available
# @app.delete("/")
# @app.patch("/")

# This code below is use when you run python main.py instead of unicorn main:app
# on command line

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    # Reload is optional, mostly for development only
    
    