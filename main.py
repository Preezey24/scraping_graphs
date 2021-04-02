from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: 
    content = html_file.read() 
    
    soup = BeautifulSoup(content, 'lxml')
    courses = soup.find_all('h5')
    