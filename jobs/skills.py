from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://ca.indeed.com/jobs?q=software+developer&l=Vancouver%2C+BC&radius=25&ts=1615295423449&rq=1&rsIdx=1&fromage=last&newcount=720').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('h2', class_="title")
for job in jobs: 
    print(job.a.text) 
    print("")