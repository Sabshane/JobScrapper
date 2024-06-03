import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
from tqdm import tqdm

DEFAULTURL = "https://www.jobup.ch/"
BASEURL = "https://www.jobup.ch/fr/emplois/"

defaultPage = requests.get(BASEURL)
defaultSoup = BeautifulSoup(defaultPage.content, "html.parser")

maxPage = defaultSoup.select('div[class*="PaginatedLink___"]')[-2]
maxPageInt = int("".join(filter(str.isdecimal, maxPage.text)))
print(f"Total pages to process: {maxPageInt}")
jobEntry=0
# Create a new session
session = requests.Session()
# Add headers to simulate incognito mode
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'

with open('results.csv', 'a', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Lien de l'annonce", "Lieu", "Taux d'occupation", "Type de contrat",])

    progress_bar = tqdm(total=maxPageInt, desc="Progress")

    for x in range(1, maxPageInt + 1):
        URL = f"https://www.jobup.ch/fr/emplois/?page={x}"
        progress_bar.set_description(f"Processing page {x}/{maxPageInt} , {jobEntry} job entries found")

        page = session.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        links = soup.select("a[data-cy='job-link']")

        for item in links:
            url = urljoin(DEFAULTURL, item["href"])
            text = item["title"]
            job_datas = {
                "location": "",
                "required_time": "",
                "contract_type": "",
                "entreprise": "",
            }
            try:
                job_datas_soup = item.select("[class='P-sc-hyu5hk-0 Text__p2-sc-1lu7urs-10 Span-sc-1ybanni-0 Text__span-sc-1lu7urs-12 Text-sc-1lu7urs-13 KlqjR']")
                for idx, job_data in enumerate(job_datas_soup):
                    if idx < len(job_datas):
                        jobEntry+=1
                        job_datas[list(job_datas.keys())[idx]] = job_data.get_text()
            except AttributeError:
                job_datas = 0
            hyperlink = f'=HYPERLINK("{url}"; "{text}")'
            writer.writerow([hyperlink, job_datas["location"], job_datas["required_time"], job_datas["contract_type"], job_datas["entreprise"]])

        progress_bar.update(1)

    progress_bar.close()  

print("Script completed successfully! \n We found "+ jobEntry+" job entries.")
