# from requests import get

# websites = (
#     "https://google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "https://facebook.com",
#     "tiktok.com",
# )
# results = {}
# for website in websites:
#   if not website.startswith("https://"):
#       website = f"https://{website}"
#   response = get(website)
#   if response.status_code == 200:
#     results[website] = 'OK'
#   else:
#     results[website] = 'FAILED'
# print(results)



from requests import get

from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"
results = []
response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't Request Website")

else:

  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="jobs")
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts: 
      anchors = post.find_all('a')
      anchor = anchors[1]
      link = anchor['href']
      company, kind, region = anchor.find_all('span', class_="company")
      title = anchor.find('span', class_='title')
      job_data = {
      'company' : company.string, 
      'region' : region.string, 
      'position' : title.string
      }
      results.append(job_data)
    # print(results)
    # print("/////////////////////")
for result in results:
  print(result)

# git config --global user.name "Chan"
# git config --global user.email "chanhyung.kim1130@gmail.com"






