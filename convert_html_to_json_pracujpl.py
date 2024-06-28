from bs4 import BeautifulSoup
import json
import requests

def fetch_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None

url = 'https://www.pracuj.pl/praca/data-engineer-data-science-hub-warszawa-zelazna-51-53,oferta,1003427675?s=d4b7c35b'

# Parse the HTML content
soup = BeautifulSoup(fetch_html_content(url), 'html.parser')

# Extracting the necessary data
offer_header = soup.find('div', id='offer-header')

# Company logo
logo = offer_header.find('div', {'data-test': 'section-company-logo'}).img['src']

# Job details
job_details = offer_header.find('div', {'data-test': 'section-offer-job-details'})
position_name = job_details.find('h1', {'data-test': 'text-positionName'}).text
employer_name = job_details.find('h2', {'data-test': 'text-employerName'}).contents[0].strip()

# Salary
salary_section = offer_header.find('div', {'data-test': 'section-salary'})
salary = salary_section.find('div', {'data-test': 'text-earningAmount'}).text.replace('\xa0', ' ')

# Benefits and work conditions
benefit_list = []
benefits = soup.find_all('li', {'data-test': 'sections-benefit-list'})
for benefit in benefits:
    title = benefit.find('div', {'data-test': 'offer-badge-title'}).text
    description = benefit.find('div', {'data-test': 'offer-badge-description'}).text
    benefit_list.append({'title': title, 'description': description})

# Specializations
specializations = soup.find('ul', {'data-test': 'work-conditions'}).find('li', {'data-test': 'it-specializations'}).div.next_sibling.text

# Technologies
technologies_section = soup.find('section', {'data-test': 'section-technologies'})
expected_technologies = [tech.text for tech in technologies_section.find_all('li', {'data-test': 'item-technologies-expected'})]

# Responsibilities
responsibilities_section = soup.find('section', {'data-test': 'section-responsibilities'})
responsibilities = [resp.text for resp in responsibilities_section.find_all('li', {'class': 'tkzmjn3'})]

# Construct the JSON object
job_data = {
    'company_logo': logo,
    'position_name': position_name,
    'employer_name': employer_name,
    'salary': salary,
    'benefits': benefit_list,
    'specializations': specializations,
    'technologies': {
        'expected': expected_technologies
    },
    'responsibilities': responsibilities
}

# Convert to JSON string
job_data_json = json.dumps(job_data, indent=4)

print(job_data_json)
