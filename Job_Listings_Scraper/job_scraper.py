import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://realpython.github.io/fake-jobs/'

response = requests.get(BASE_URL)

soup = BeautifulSoup(response.text, 'html.parser')

jobs = soup.find_all('div', class_='card-content')

job = jobs[0]



job_list = []

for job in jobs:
    title = job.find('h2', class_='title is-5').text.strip()
    company = job.find('h3', class_='subtitle is-6 company').text.strip()
    location = job.find('p', class_='location').text.strip()
    time = job.find('time').text.strip()
    link = job.find('a')['href']

    job_list.append([title, company, location, time, link])

with open("jobs.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([title, company, location, time, link])
    writer.writerows(job_list)
print("Jobs saved to jobs.csv")

# print(job_list[2])