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

url = 'https://www.pracuj.pl/praca/analityk-biznesowy-warszawa-szturmowa-2,oferta,1003457480?s=1f7c2c91'

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

# Parse "Our requirements"
requirements_section = soup.find('section', {'data-scroll-id': 'requirements-1'})
requirements = []
if requirements_section:
    for li in requirements_section.find_all('li', {'class': 'tkzmjn3'}):
        requirements.append(li.get_text(strip=True))

# Parse "This is how we organize our work"
work_organization_section = soup.find('section', {'data-scroll-id': 'work-organization-1'})
if work_organization_section:
    work_style = work_organization_section.find('li', {'data-test': 'item-work-organization-work-style'})
    work_style = work_style.get_text(strip=True) if work_style else ''

# Parse "Development opportunities we offer"
development_opportunities_section = soup.find('section', {'data-scroll-id': 'training-space-1'})
development_opportunities = []
if development_opportunities_section:
    for li in development_opportunities_section.find_all('li', {'class': 't174u8f7'}):
        development_opportunities.append(li.get_text(strip=True))

# Parse "What we offer"
what_we_offer_section = soup.find('section', {'data-scroll-id': 'offered-1'})
offers = []
if what_we_offer_section:
    for li in what_we_offer_section.find_all('li', {'class': 'tkzmjn3'}):
        offers.append(li.get_text(strip=True))

# Extract and parse the benefits
benefits_section = soup.find('section', {'data-test': 'section-benefits'})
benefits = []
if benefits_section:
    benefits_list = benefits_section.find_all('li', {'data-test': 'list-item-benefit'})
    for benefit in benefits_list:
        title = benefit.find('div', {'data-test': 'text-benefit-title'}).text.strip()
        icon = benefit.find('image')['href']
        benefits.append({'title': title, 'icon': icon})

# Extract and parse the "Why is it worth working with us" section
worth_working_section = soup.find('section', {'data-test': 'section-additional-module'})
worth_working_points = []
if worth_working_section:
    worth_working_list = worth_working_section.find_all('li')
    for point in worth_working_list:
        text = point.get_text(strip=True)
        worth_working_points.append(text)

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
    'responsibilities': responsibilities,
    'requirements': requirements,
    'work_style': work_style,
    'development_opportunities': development_opportunities,
    'offers': offers,
    'benefits': benefits,
    'worth_working_points': worth_working_points
}

# Convert to JSON string
job_data_json = json.dumps(job_data, indent=4)

print(job_data_json)
