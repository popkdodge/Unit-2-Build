from urllib import request
from datetime import datetime
from bs4 import BeautifulSoup
import csv


# add the correct User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# the company page you're about to scrape
company_page = 'https://www.crunchbase.com/organization/o-1-labs#section-overview'

# open the page
page_request = request.Request(company_page, headers=headers)
page = request.urlopen(page_request)

# parse the html using beautiful soup
html_content = BeautifulSoup(page, 'html.parser')