import requests
from bs4 import BeautifulSoup

def get_html_without_attributes(url):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove all attributes from each tag
    for tag in soup.find_all(True):
        tag.attrs = {}

    # Remove all <script> tags
    for script in soup(["script"]):
        script.decompose()

    # Return the modified HTML as a string
    return str(soup)

# Example usage
url = 'https://www.pracuj.pl/praca/analityk-biznesowy-warszawa-szturmowa-2,oferta,1003457480?s=1f7c2c91m'
plain_html = get_html_without_attributes(url)
print(plain_html)
