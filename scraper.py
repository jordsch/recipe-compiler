import requests
from bs4 import BeautifulSoup

def joshua_scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())

    title = soup.select_one('h2').text
    print(title)


if __name__ == '__main__':
    joshua_scrape('https://www.joshuaweissman.com/post/joshua-weissman-s-instant-ramen-recipe')