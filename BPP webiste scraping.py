from bs4 import BeautifulSoup as bs

import requests



url= 'https://activities.osu.edu/involvement/student_organizations/find_a_student_org?v=card&c=Columbus&m=Undergraduate'
r=requests.get(url)

def save_html(html,path):
    with open(path, 'wb') as f:
        f.write(html)

save_html(r.content,url)
soup = bs(r.content, 'html.parser')


def open_html(path): 
    with open(path, 'rb') as f:
        return f.read()
html=open_html(url)

print (r.content[:100])





