# Production Server

Since FastAPI doesn't have a development server, you'll use Uvicorn (or Daphne) for both development and production.

Install Uvicorn:

pip install uvicorn
Start server:

# main.py
# app = FastAPI()

uvicorn main:app
You may want to use Gunicorn to manage Uvicorn in order to take advantage of both concurrency (via Uvicorn) and parallelism (via Gunicorn workers):

# main.py
# app = FastAPI()

gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app