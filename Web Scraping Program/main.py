import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub User: ')
url = 'https://github.com/' + github_user

r = requests.get(url) # Sending the request to the paticular URL
soup = bs(r.content, 'html.parser')

profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)
