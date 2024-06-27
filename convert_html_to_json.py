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

def parse_section_text(soup, section_id, container_tags, tag='li', tag_class=None):
    section = None
    for container_tag in container_tags:
        section = soup.find(container_tag, {'id': section_id})
        if section:
            break
        section = soup.find(container_tag, {'data-cy-section': section_id})
        if section:
            break

    if not section:
        return []

    items = section.find_all(tag, class_=tag_class) if tag_class else section.find_all(tag)
    return [item.get_text(strip=True) for item in items]

def parse_posting_header(soup):
    header_data = {}
    header_section = soup.find('common-posting-header')
    if header_section:
        header_data['Job Title'] = header_section.find('h1').get_text(strip=True) if header_section.find('h1') else None
        header_data['Company Name'] = header_section.find('a', {'id': 'postingCompanyUrl'}).get_text(strip=True) if header_section.find('a', {'id': 'postingCompanyUrl'}) else None
        header_data['Company Logo URL'] = header_section.find('img')['src'] if header_section.find('img') else None
    return header_data

def parse_posting_info(soup):
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
            info_data['Location'] = locations.get_text(strip=True)
    return info_data

def parse_description(soup, section_id):
    return " ".join(parse_section_text(soup, section_id, ['section', 'div'], tag='p'))

def parse_tasks(soup, section_id):
    return parse_section_text(soup, section_id, ['section', 'div'], tag='li')

def parse_salary_info(soup):
    salary_data = {}
    salary_info = soup.find('common-posting-salaries-list')
    if salary_info:
        salary_text = salary_info.find('h4').get_text(strip=True) if salary_info.find('h4') else None
        salary_details = salary_info.find('div', class_='paragraph').get_text(strip=True) if salary_info.find('div', class_='paragraph') else None
        salary_data['salary'] = {'amount': salary_text, 'details': salary_details}

    bonus_info = soup.find('common-postings-bonus', class_='d-flex flex-column')
    if bonus_info:
        bonus_text = bonus_info.find('a').get_text(strip=True) if bonus_info.find('a') else None
        bonus_details = bonus_info.find('div', class_='p-3').get_text(strip=True) if bonus_info.find('div', class_='p-3') else None
        salary_data['bonus'] = {'percentage': bonus_text, 'details': bonus_details}
    return salary_data

def parse_job_offer_requirements(soup):
    return parse_section_text(soup, 'JobOffer_Requirements', ['section'], tag='li')

def extract_job_posting_data(url):
    html_content = fetch_html_content(url)
    if not html_content:
        return None

    soup = BeautifulSoup(html_content, 'html.parser')

    data = {
        "Header": parse_posting_header(soup),
        "Info": parse_posting_info(soup),
        "Obowiązkowe": parse_section_text(soup, 'posting-requirements', ['section', 'div']),
        "Mile widziane": parse_section_text(soup, 'posting-nice-to-have', ['section', 'div']),
        "Opis wymagań": parse_job_offer_requirements(soup),
        "Opis oferty": parse_description(soup, 'posting-description'),
        "Zakres obowiązków": parse_tasks(soup, 'posting-tasks'),
        "Szczegóły oferty": parse_tasks(soup, 'posting-specs'),
        "Sprzęt": parse_tasks(soup, 'posting-equipment'),
        "Metodologia": parse_tasks(soup, 'posting-environment'),
        "Udogodnienia w biurze": parse_tasks(soup, 'posting-benefits'),
        "Wynagrodzenie": parse_salary_info(soup)
    }

    return json.dumps(data, ensure_ascii=False, indent=4)

url = 'https://nofluffjobs.com/pl/job/data-engineer-talent-hills-warszawa-1'
json_data = extract_job_posting_data(url)
if json_data:
    print(json_data)
