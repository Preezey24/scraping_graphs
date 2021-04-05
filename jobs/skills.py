from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.linkedin.com/jobs/search/?alertAction=viewjobs&f_JT=F%2CC%2CI&f_TPR=a1617317976-&keywords=software%20engineer&savedSearchId=1213016336&searchAlertRefId=1724ba75-f511-46fe-93cf-a0d5befb7a32').text
soup = BeautifulSoup(html_text, 'lxml')
print(soup)