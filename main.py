#5.10
# from requests import get
# from bs4 import BeautifulSoup
# from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("python")
# print(jobs)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")

# soup = BeautifulSoup(browser.page_source, "html.parser")

# print("test : " ,soup)
print(browser.page_source)