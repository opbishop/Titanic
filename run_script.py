# local module imports
from config import urls
import data_processor as dp
import scraper as scrape

# external module imports
from bs4 import BeautifulSoup

page = scrape.get_url(urls['titanic_data']).text
soup = BeautifulSoup(page, 'html.parser')

titanic = dp.populate(soup)
dp.analyse(titanic.passengers)