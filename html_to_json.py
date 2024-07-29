from bs4 import BeautifulSoup
import json

def extract_job_offer(html):
    """
    Extracts job offer details from the provided HTML and converts them to JSON format.
    
    Parameters:
    - html (str): The HTML content as a string.
    
    Returns:
    - str: The JSON representation of the job offer.
    """
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the job offer section
    offer_section = soup.find('div', id='offer-details')
    
    if offer_section is None:
        raise ValueError("No section found with id 'offer-details'")
    
    # Extract job title and company
    title = offer_section.find('h1').text.strip() if offer_section.find('h1') else 'N/A'
    company_info = offer_section.find('h2').text.strip() if offer_section.find('h2') else 'N/A'
    company = company_info.split('\n')[0].strip()
    
    # Extract job details (address, location, etc.)
    details = {}
    details_list = offer_section.find('ul').find_all('li') if offer_section.find('ul') else []
    
    for item in details_list:
        divs = item.find_all('div')
        if len(divs) >= 2:
            key = divs[0].text.strip()
            value = divs[-1].text.strip()
            details[key] = value
    
    # Extract job responsibilities
    responsibilities = []
    responsibility_section = offer_section.find_all('section')[0].find_all('li') if len(offer_section.find_all('section')) > 0 else []
    
    for item in responsibility_section:
        text = item.text.strip()
        if text:
            responsibility = text.split(' ', 1)[1] if ' ' in text else text
            responsibilities.append(responsibility)
    
    # Extract job requirements
    requirements = []
    requirements_section = offer_section.find_all('section')[1].find_all('li') if len(offer_section.find_all('section')) > 1 else []
    
    for item in requirements_section:
        text = item.text.strip()
        if text:
            requirement = text.split(' ', 1)[1] if ' ' in text else text
            requirements.append(requirement)
    
    # Extract additional qualifications
    additional_qualifications = []
    additional_section = offer_section.find_all('section')[2].find_all('li') if len(offer_section.find_all('section')) > 2 else []
    
    for item in additional_section:
        text = item.text.strip()
        if text:
            qualification = text.split(' ', 1)[1] if ' ' in text else text
            additional_qualifications.append(qualification)
    
    # Extract benefits
    benefits = []
    benefits_section = offer_section.find_all('section')[3].find_all('li') if len(offer_section.find_all('section')) > 3 else []
    
    for item in benefits_section:
        divs = item.find_all('div')
        if len(divs) >= 2:
            benefit = divs[1].text.strip()
            benefits.append(benefit)
    
    # Assemble all data into a dictionary
    job_offer = {
        'title': title,
        'company': company,
        'details': details,
        'responsibilities': responsibilities,
        'requirements': requirements,
        'additional_qualifications': additional_qualifications,
        'benefits': benefits
    }
    
    # Convert dictionary to JSON
    return json.dumps(job_offer, ensure_ascii=False, indent=4)

# Example usage
html_content = '''
<div class="o2ns6n9" data-test="section-offerview" id="offer-details"><div><div><div><div><div><picture><source/><source/><img/></picture></div><div><h1>Analityk Biznesowy</h1><h2>LUX MED Sp. z o.o.<a>O firmie</a></h2></div></div></div><div></div><ul><li><div><span><svg><path></path><path></path></svg></span></div><div><div><a>Szturmowa 2, Mokotów, Warszawa</a></div><div>Warszawa, mazowieckie</div></div></li><li><div><span><svg><path></path><path></path></svg></span></div><div><div>ważna jeszcze 9 dni</div><div>do 07 sierpnia 2024</div></div></li><li><div><span><svg><path></path></svg></span></div><div><div>umowa o pracę</div></div></li><li><div><span><svg><path></path><path></path></svg></span></div><div><div>pełny etat</div></div></li><li><div><span><svg><path></path></svg></span></div><div><div>specjalista (Mid / Regular)</div></div></li><li><div><span><svg><path></path><path></path></svg></span></div><div><div>praca hybrydowa</div></div></li></ul></div><div><div><div><p>LUX MED Sp. z o.o.</p><p>Szturmowa 2</p><p>Mokotów</p><p>Warszawa</p><a>Sprawdź jak dojechać<span><svg><path></path></svg></span></a></div></div><iframe></iframe></div><section><div><h2>Twój zakres obowiązków</h2></div><div><ul><li><span><svg><path></path><path></path></svg></span>Przygotowywanie raportów i analiz cyklicznych oraz ad – hoc;</li><li><span><svg><path></path><path></path></svg></span>Analiza danych, z wykorzystaniem głównie metod ilościowych (wiedza z zakresu modelowania ekonometrycznego mile widziana);</li><li><span><svg><path></path><path></path></svg></span>Analiza danych, trendów, identyfikacja powiązań i korelacji między wskaźnikami;</li><li><span><svg><path></path><path></path></svg></span>Pozyskiwanie danych z różnych źródeł i ich analiza;</li><li><span><svg><path></path><path></path></svg></span>Wsparcie analityczne projektów prowadzonych przez Departament;</li><li><span><svg><path></path><path></path></svg></span>Interpretacja i prezentowanie wyników dotyczących przeprowadzanych analiz;</li><li><span><svg><path></path><path></path></svg></span>Optymalizacja istniejących rozwiązań;</li><li><span><svg><path></path><path></path></svg></span>Odpowiedzialność za jakość danych publikowanych przez Departament.</li></ul></div></section><section><div><h2>Nasze wymagania</h2></div><div><div><div><ul><li><span><svg><path></path><path></path></svg></span>Wykształcenie wyższe;</li><li><span><svg><path></path><path></path></svg></span>Znajomość SQL na bardzo dobrym poziomie- wymóg konieczny;</li><li><span><svg><path></path><path></path></svg></span>Znajomość pakietu MS Office z bardzo dobrą obsługą MS Excel;</li><li><span><svg><path></path><path></path></svg></span>Wysoko rozwinięte umiejętności analityczne;</li><li><span><svg><path></path><path></path></svg></span>Umiejętność pracy zespołowej oraz organizacji pracy własnej;</li><li><span><svg><path></path><path></path></svg></span>Dokładność i precyzja, odpowiedzialność, spostrzegawczość, komunikatywność, myślenie przyczynowo – skutkowe, dążenie do celu.</li></ul></div></div><div><h3>Mile widziane</h3><div><ul><li><span><svg><path></path><path></path></svg></span>Doświadczenie zawodowe na podobnym stanowisku;</li><li><span><svg><path></path><path></path></svg></span>Znajomość Power BI oraz Tableau.</li></ul></div></div></div></section><section><div><h2>Benefity</h2></div><div><ul><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>dofinansowanie zajęć sportowych</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>prywatna opieka medyczna</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>dofinansowanie nauki języków</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>dofinansowanie szkoleń i kursów</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>ubezpieczenie na życie</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>owoce</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>program rekomendacji pracowników</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>ubezpieczenie szpitalne</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>program wellbeingowy</div></div></li></ul><img/></div></section><div><section><div><h3>Tak się u nas pracuje</h3><span><svg><path></path></svg></span></div><div><img/><div><span><svg><path></path></svg></span></div></div><div><span><svg><path></path></svg></span></div></section></div><div><div><div><div><a><span><picture><svg><g><path></path></g></svg></picture>Aplikuj szybko</span></a><div></div></div></div><div><div><a><span><picture><svg><g><path></path></g></svg></picture>Aplikuj szybko</span></a><div></div></div><div><div><button><span><svg><path></path></svg></span><span>Zapisz</span></button><button><span><svg><path></path><path></path><path></path><path></path></svg></span><span>Drukuj</span></button><button><span><svg><path></path><path></path><path></path><path></path><path></path></svg></span><span>Udostępnij</span></button></div></div><div><div><picture><svg><g><path></path></g></svg></picture>Oferta z szybkim aplikowaniem</div><div><button><span>co to?</span></button></div></div><div><div><p>Wszystkie informacje o przetwarzaniu danych osobowych w tej rekrutacji znajdziesz w formularzu aplikacyjnym, po kliknięciu w przycisk "Aplikuj Teraz".</p></div></div></div></div></div><div><div><div><a>Praca</a></div><span><svg><path></path></svg></span><div><a>Warszawa</a><div><div><div><span><svg><path></path></svg></span></div></div></div></div><span><svg><path></path></svg></span><div><a>Finanse / Ekonomia</a></div><span><svg><path></path></svg></span><div><a>Doradztwo / Konsulting</a><div><div><div><span><svg><path></path></svg></span></div></div></div></div></div></div></div><div><div><div><div><div><a><span><picture><svg><g><path></path></g></svg></picture><span>Aplikuj szybko</span></span></a><div></div></div><div><div><button><span><svg><path></path></svg></span><span>Zapisz</span></button><button><span><svg><path></path><path></path><path></path><path></path></svg></span><span>Drukuj</span></button><button><span><svg><path></path><path></path><path></path><path></path><path></path></svg></span><span>Udostępnij</span></button></div></div><div><div><picture><svg><g><path></path></g></svg></picture>Oferta z szybkim aplikowaniem</div><div><button><span>co to?</span></button></div></div></div></div></div><div><div><strong>Powiadamiaj mnie o podobnych ofertach</strong><p>Analityk Biznesowy, Szturmowa 2, Mokotów, Warszawa</p></div><div><label><input/><span></span></label></div></div><div></div></div></div>
'''

json_output = extract_job_offer(html_content)
print(json_output)
