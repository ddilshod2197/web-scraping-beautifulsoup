import requests
from bs4 import BeautifulSoup

def scrap_sarlavhalar(url):
    # Veb-sahifani olib kelish
    response = requests.get(url)
    
    # Veb-sahifani o'rganish
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Sarlavhalarni olib kelish
    sarlavhalar = soup.find_all('h1') + soup.find_all('h2') + soup.find_all('h3')
    
    # Sarlavhalarni ro'yxatga qo'shish
    sarlavhalar = [sarlavha.text.strip() for sarlavha in sarlavhalar]
    
    return sarlavhalar

url = 'https://www.example.com'  # Veb-sahifaning URL-masini kiritish
sarlavhalar = scrap_sarlavhalar(url)
print(sarlavhalar)
