import requests
from bs4 import BeautifulSoup
from time import clock, sleep

cities = ['Porto Alegre', 'Florianopolis', 'Curitiba', 'Sao Paulo', 'Rio de Janeiro', 'Vitoria-ES', 'Belo Horizonte',
          'Campo Grande', 'Cuiaba', 'Goiania']


def get_temperature(cities):
    dict = {}
    base_url = 'https://www.google.com/search?q='

    for city in cities:
        search_string = '{}+tempo'.format(city)
        page = requests.get(base_url+search_string)

        soup = BeautifulSoup(page.text, 'html.parser')
        weather_data = soup.find("div", class_='BNeawe').text
        dict[city] = weather_data
        sleep(0.01)

    return dict

print(get_temperature(cities))
