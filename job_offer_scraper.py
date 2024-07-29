import requests
from bs4 import BeautifulSoup
import json

class JobOffer:
    '''
    Holds job offer details.
    Converts details to dictionary and JSON formats.
    '''
    def __init__(self, title, company, location, details):
        self.title = title
        self.company = company
        self.location = location
        self.details = details

    def to_dict(self):
        return {
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'details': self.details
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

class JobOfferParser:
    '''
    Parses HTML to extract job details.
    Uses BeautifulSoup to traverse and extract information.
    '''
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.soup = self.soup.find('div', id = 'offer-details')
        # Remove all <script> tags
        for svg in self.soup.find_all('svg'):
            svg.decompose()

    def parse(self):
        print(self.soup.prettify())
        # Parse job offer details from HTML
        title = self.soup.find('h1').text.strip() if self.soup.find('h1') else 'No title'
        company = self.soup.find('h2').text.strip().split('<a')[0].strip() if self.soup.find('h2') else 'No company'
        location = self._parse_location()
        details = self._parse_details()

        return JobOffer(title, company, location, details)

    def _parse_location(self):
        # Implement location parsing logic
        location_div = self.soup.find('ul').find_all('div')[1] if self.soup.find('ul') else None
        return location_div.text.strip() if location_div else 'No location'

    def _parse_details(self):
        # Implement job details parsing logic
        details_section = self.soup.find('section', string='Twój zakres obowiązków')
        if details_section:
            details = [li.text.strip() for li in details_section.find_next('ul').find_all('li')]
        else:
            details = []

        return details

class JobOfferScraper:
    '''
    Fetches HTML from provided URLs.
    Uses JobOfferParser to parse each HTML document and gather job offers.
    '''
    def __init__(self, urls):
        self.urls = urls

    def get_html(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def scrape(self):
        job_offers = []
        for url in self.urls:
            html = self.get_html(url)
            if html:
                parser = JobOfferParser(html)
                job_offer = parser.parse()
                job_offers.append(job_offer.to_dict())

        return job_offers

if __name__ == '__main__':
    urls = [
        'https://www.pracuj.pl/praca/analityk-biznesowy-warszawa-szturmowa-2,oferta,1003457480',
    ]
    scraper = JobOfferScraper(urls)
    offers = scraper.scrape()

    for offer in offers:
        print(json.dumps(offer, indent=4))
