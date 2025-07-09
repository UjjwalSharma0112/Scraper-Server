from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from scraper import get_job_links_from_linkedin  # assuming your function is in scraper.py

app = FastAPI()

@app.get("/get_jobs")
def get_jobs(job_title: str = Query(...), location: str = Query(...)):
    try:
        links = get_job_links_from_linkedin(job_title, location)
        return {"count": len(links), "job_links": links}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
