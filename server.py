from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from scraper import get_job_links
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/get_jobs")
def get_jobs(job_title: str = Query(...), location: str = Query(...)):
    try:
        
        links = get_job_links(job_title, location)
        # Use jsonable_encoder to handle pandas Timestamps
        return jsonable_encoder({"count": len(links), "job_details": links})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})