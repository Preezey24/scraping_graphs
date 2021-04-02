from bs4 import BeautifulSoup
import requests

print('Put a skill that you are not familiar with')
unfamiliar_skill = input('>')
unfamiliar_skills = unfamiliar_skill.split()
print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml') 
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for idx, job in enumerate(jobs): 
    published = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published: 
        skills = job.find('span', class_ = "srp-skills").text.replace(' ','')
        for unfamiliar in unfamiliar_skills: 
            if unfamiliar not in skills: 
                company = job.find('h3', class_="joblist-comp-name").text.replace(' ','')
                more_info = job.header.h2.a["href"]
                with open(f'posts/{str(idx) + company.strip()}.txt', 'w') as f:
                    f.write(f'Company Name: {company.strip()} \n')
                    f.write(f'Skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info} \n')
                print(f'File saved: {idx}')
