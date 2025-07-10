import pandas as pd
from jobspy import scrape_jobs

def get_job_links(job_title: str, location: str):
    jobs = scrape_jobs(
        site_name=["linkedin"],
        search_term=job_title,
        google_search_term=f"{job_title} jobs near {location} since yesterday",
        location=location,
        results_wanted=20,
        hours_old=72,
        country_indeed='USA',
        easy_apply=True,
        linkedin_fetch_description=True,
    )

    # Select only required columns
    jobs = jobs[["job_url", "title", "company", "location", "date_posted"]]

    # Clean and convert
    jobs = jobs.where(pd.notnull(jobs), None)
    jobs["date_posted"] = jobs["date_posted"].astype(str)

    # Filter out entries with no date_posted or location (optional)
    jobs = jobs[jobs["date_posted"] != "None"]
    jobs = jobs[jobs["location"] != ""]

    # Sort by date_posted descending
    jobs["date_posted"] = pd.to_datetime(jobs["date_posted"])
    jobs = jobs.sort_values(by="date_posted", ascending=False)

    return jobs.to_dict(orient="records")

