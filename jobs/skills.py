from bs4 import BeautifulSoup
import requests

for count in range(0,110,10): 
    if not count: 
        html_text = requests.get('https://ca.indeed.com/jobs?q=software+developer&l=Vancouver%2C+BC&fromage=last&radius=25').text
    else: 
        html_text = requests.get(f'https://ca.indeed.com/jobs?q=software+developer&l=Vancouver%2C+BC&fromage=last&radius=25&start={count}')
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_="jobSearch-SerpJobCard")
    for job in jobs: 
        print(job.h2.a.text) 
        print("")