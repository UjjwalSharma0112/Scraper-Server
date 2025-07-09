from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from cookie_loader import load_cookies_from_txt  # if you're using cookie injection



 
def get_job_links_from_linkedin(job_title,location)->list:
        
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}&f_AL=true"

    # Setup browser
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Inject cookies
    driver.get("https://www.linkedin.com")
    time.sleep(2)

    for cookie in load_cookies_from_txt("./linkedin_cookies.txt"):
        try:
            driver.add_cookie(cookie)
        except Exception:
            pass

    # Go to search results
    driver.get(search_url)
    time.sleep(4)

    # Scroll to load more jobs
    for _ in range(3):  # adjust for more results
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Extract job posting links
    job_links = set()

    job_cards = driver.find_elements(By.CSS_SELECTOR, "a[href*='/jobs/view/']")

    for card in job_cards:
        href = card.get_attribute("href")
        if href:
            job_links.add(href)

    print(f"🔗 Found {len(job_links)} unique job links:\n")
    

    driver.quit()
    return list(job_links)

    