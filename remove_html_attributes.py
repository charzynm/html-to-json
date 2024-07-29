"""import requests
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
"""

import requests
from bs4 import BeautifulSoup

def remove_attributes_from_html(html, div_id):
    """
    Extracts a section from HTML with the given div_id and removes all attributes from all HTML tags.
    
    Parameters:
    - html (str): The HTML content as a string.
    - div_id (str): The id of the div element to extract and process.
    
    Returns:
    - str: The HTML content with all attributes removed from the specified div section.
    """
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the div with the given id
    div = soup.find('div', id=div_id)
    
    if div is None:
        raise ValueError(f"No div found with id '{div_id}'")
    
    # Remove attributes from all tags within the div
    for tag in div.find_all(True):  # `True` finds all tags
        tag.attrs = {}
    
    # Return the modified HTML as a string
    return str(div)

url = 'https://www.pracuj.pl/praca/analityk-biznesowy-warszawa-szturmowa-2,oferta,1003457480?s=1f7c2c91m'
# Fetch the HTML content from the URL
response = requests.get(url)
response.raise_for_status()  # Ensure we notice bad responses

div_id = 'offer-details'
result = remove_attributes_from_html(response.text, div_id)
print(result)
