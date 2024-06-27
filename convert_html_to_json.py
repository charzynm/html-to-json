from bs4 import BeautifulSoup
import json
import requests

def fetch_html(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.content  # Return the HTML content
        else:
            print(f"Failed to retrieve HTML: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML: {e}")

def extract_requirements(section_id):
    section = soup.find('section', {'id': section_id})
    requirements = []
    if section:
        items = section.find_all('li')
        for item in items:
            span = item.find('span')
            if span:
                requirements.append(span.get_text(strip=True))
            else:
                requirements.append(item.get_text(strip=True))
    return requirements

def extract_posting_header():
    header_data = {}
    header_section = soup.find('common-posting-header')
    if header_section:
        job_title = header_section.find('h1')
        company_name = header_section.find('a', {'id': 'postingCompanyUrl'})
        company_logo = header_section.find('img')
        
        header_data['Job Title'] = job_title.get_text(strip=True) if job_title else None
        header_data['Company Name'] = company_name.get_text(strip=True) if company_name else None
        header_data['Company Logo URL'] = company_logo['src'] if company_logo else None

    return header_data

def extract_posting_info():
    info_data = {}
    info_section = soup.find('section', {'class': ''})
    if info_section:
        category = info_section.find('li', {'commonpostingcattech': ''})
        seniority = info_section.find('li', {'id': 'posting-seniority'})
        locations = info_section.find('common-posting-locations')

        if category:
            category_text = category.get_text(strip=True).replace("Kategoria:", "").strip()
            info_data['Category'] = [cat.strip() for cat in category_text.split(',')]
        
        if seniority:
            seniority_text = seniority.find('span', {'class': 'mr-10 font-weight-medium'})
            info_data['Seniority'] = seniority_text.get_text(strip=True) if seniority_text else None

        if locations:
            location_text = locations.get_text(strip=True)
            info_data['Location'] = location_text

    return info_data

def extract_description(section_id):
    description_data = ""
    section = soup.find('section', {'id': section_id})
    if section:
        paragraphs = section.find_all('p')
        for paragraph in paragraphs:
            description_data += paragraph.get_text(strip=True) + " "
    return description_data.strip()

def extract_tasks(section_id):
    tasks = []
    section = soup.find('section', {'id': section_id})
    if section:
        items = section.find_all('li')
        for item in items:
            tasks.append(item.get_text(strip=True))
    return tasks

def extract_salary(section_id):
    salary_data = {}
    posting_salary_bonus_section = soup.find('section', {'id': section_id})
    if posting_salary_bonus_section:
        salary_info = posting_salary_bonus_section.find('common-posting-salaries-list', class_='salary')
        if salary_info:
            salary_text = salary_info.find('h4').get_text(strip=True)
            salary_details = salary_info.find('div', class_='paragraph').get_text(strip=True)
            salary_data['salary'] = {
                'amount': salary_text,
                'details': salary_details
            }
        
        bonus_info = posting_salary_bonus_section.find('common-postings-bonus', class_='d-flex flex-column')
        if bonus_info:
            bonus_text = bonus_info.find('a').get_text(strip=True)
            bonus_details = bonus_info.find('div', class_='p-3').get_text(strip=True)
            salary_data['bonus'] = {
                'percentage': bonus_text,
                'details': bonus_details
            }
    return salary_data

url = 'https://nofluffjobs.com/pl/job/data-engineer-talent-hills-warszawa-1'
soup = BeautifulSoup(fetch_html(url), 'html.parser')

data = {
    "Header": extract_posting_header(),
    "Info": extract_posting_info(),
    "Obowiązkowe": extract_requirements('posting-requirements'),
    "Mile widziane": extract_requirements('posting-nice-to-have'),
    "Opis wymagań": [],
    "Opis oferty": extract_description('posting-description'),
    "Zakres obowiązków": extract_tasks('posting-tasks'),
    "Szczegóły oferty": extract_tasks('posting-specs'),
    "Sprzęt": extract_tasks('posting-equipment'),
    "Uwagi": extract_tasks('posting-notes'),
    "Wynagrodzenie": extract_salary('posting-salary-bonus')
}

# Extracting job description
description_section = soup.find('section', {'data-cy-section': 'JobOffer_Requirements'})
if description_section:
    ul = description_section.find('ul')
    if ul:
        description_items = ul.find_all('li')
        for item in description_items:
            data["Opis wymagań"].append(item.get_text(strip=True))

json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data)
