from bs4 import BeautifulSoup
import json

# Placeholder for your HTML
html = '''
<html><head><meta/><link/><link/><title>Oferta pracy Analityk Biznesowy, LUX MED Sp. z o.o., Warszawa</title><meta/><meta/><meta/><meta/><meta/><meta/><link/><meta/><meta/><meta/><meta/><meta/><meta/><meta/><meta/><meta/><meta/><link/><link/><link/><link/><link/><link/><link/><link/><meta/><meta/><link/><link/><link/><link/><link/><link/><noscript></noscript><style>@font-face{font-family:"Open Sans";font-style:normal;font-stretch:100%;font-weight:400;font-display:fallback;src:url(https://offerpage.gpcdn.pl/public/fonts/OpenSans/OpenSans-Regular.woff2)format("woff2")}@font-face{font-family:"Open Sans";font-style:normal;font-stretch:100%;font-weight:600;font-display:fallback;src:url(https://offerpage.gpcdn.pl/public/fonts/OpenSans/OpenSans-SemiBold.woff2)format("woff2")}@font-face{font-family:"Open Sans";font-style:normal;font-stretch:100%;font-weight:700;font-display:fallback;src:url(https://offerpage.gpcdn.pl/public/fonts/OpenSans/OpenSans-Bold.woff2)format("woff2")}@font-face{font-family:"Open Sans-fallback";size-adjust:105.44%;src:local("Arial")}@font-face{font-family:"Work Sans";font-style:normal;font-stretch:100%;font-weight:400;font-display:fallback;src:url(https://offerpage.gpcdn.pl/public/fonts/WorkSans/WorkSans-Regular.woff2)format("woff2")}@font-face{font-family:"Work Sans";font-style:normal;font-stretch:100%;font-weight:600;font-display:fallback;src:url(https://offerpage.gpcdn.pl/public/fonts/WorkSans/WorkSans-SemiBold.woff2)format("woff2")}@font-face{font-family:"Work Sans";font-style:normal;font-stretch:100%;font-weight:700;font-display:fallback;src:url(https://offerpage.gpcdn.pl/public/fonts/WorkSans/WorkSans-Bold.woff2)format("woff2")}@font-face{font-family:"Work Sans-fallback";size-adjust:111.81%;src:local("Arial")}</style></head><body><noscript><iframe></iframe></noscript><div><div><div></div><div><picture><source/><source/><source/><source/><source/><img/></picture></div><div><a>Przejdź do treści ogłoszenia</a><a>Przejdź do panelu aplikowania</a><a>Przejdź do panelu bocznego</a><a>Przejdź do stopki</a></div><div><div><div><span><svg><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path><path></path></svg></span></div><div><p>Niestety, nie wspieramy Twojej przeglądarki</p><p>Niestety nie wpieramy Twojej przeglądarki co może znacznie wpłynąć na poprawne ładowanie skryptów strony.</p></div></div></div><header><div><div><div><a><img/></a></div><nav><div><div><div><nav><span>nowość</span><span>Oferty pracy</span> <span><svg><path></path></svg></span></nav></div></div></div><a><span><img/>Pобота</span></a><a><span>Profile pracodawców</span></a><div><div><nav><span>Moja kariera</span> <span><svg><path></path></svg></span></nav></div></div></nav><div><div><div><div><div><img/><span><svg><path></path></svg></span></div></div></div></div><div><div><div><div><button><span>Moje konto</span><span><svg><path></path></svg></span></button></div></div></div></div><div><a><span>Dla firm</span><span>Dodaj ogłoszenie</span></a></div></div></div></div><div><div><button><span><svg><path></path></svg></span></button><div>Oferta pracy<!-- --> </div><div></div><nav><a><span><svg><path></path></svg></span><p>Start</p></a><a><span><svg><path></path></svg></span><p>Szukaj</p></a><a><span><svg><path></path></svg></span><p>Strefa ofert</p></a><a><span><svg><path></path><path></path></svg></span><p>Konto</p></a><a><span><svg><path></path></svg></span><p>Menu</p></a></nav></div></div></header><div><div></div><picture><source/><source/><source/><source/><source/><img/></picture></div><div><div><div><div><div><div><div><div><picture><source/><source/><img/></picture></div><div><h1>Analityk Biznesowy</h1><h2>LUX MED Sp. z o.o.<a>O firmie</a></h2></div></div></div><div></div><ul><li><div><span><svg><path></path><path></path></svg></span></div><div><div><a>Szturmowa 2, Mokotów, Warszawa</a></div><div>Warszawa, mazowieckie</div></div></li><li><div><span><svg><path></path><path></path></svg></span></div><div><div>ważna jeszcze 9 dni</div><div>do 07 sierpnia 2024</div></div></li><li><div><span><svg><path></path></svg></span></div><div><div>umowa o pracę</div></div></li><li><div><span><svg><path></path><path></path></svg></span></div><div><div>pełny etat</div></div></li><li><div><span><svg><path></path></svg></span></div><div><div>specjalista (Mid / Regular)</div></div></li><li><div><span><svg><path></path><path></path></svg></span></div><div><div>praca hybrydowa</div></div></li></ul></div><div><div><div><p>LUX MED Sp. z o.o.</p><p>Szturmowa 2</p><p>Mokotów</p><p>Warszawa</p><a>Sprawdź jak dojechać<span><svg><path></path></svg></span></a></div></div><iframe></iframe></div><section><div><h2>Twój zakres obowiązków</h2></div><div><ul><li><span><svg><path></path><path></path></svg></span>Przygotowywanie raportów i analiz cyklicznych oraz ad – hoc;</li><li><span><svg><path></path><path></path></svg></span>Analiza danych, z wykorzystaniem głównie metod ilościowych (wiedza z zakresu modelowania ekonometrycznego mile widziana);</li><li><span><svg><path></path><path></path></svg></span>Analiza danych, trendów, identyfikacja powiązań i korelacji między wskaźnikami;</li><li><span><svg><path></path><path></path></svg></span>Pozyskiwanie danych z różnych źródeł i ich analiza;</li><li><span><svg><path></path><path></path></svg></span>Wsparcie analityczne projektów prowadzonych przez Departament;</li><li><span><svg><path></path><path></path></svg></span>Interpretacja i prezentowanie wyników dotyczących przeprowadzanych analiz;</li><li><span><svg><path></path><path></path></svg></span>Optymalizacja istniejących rozwiązań;</li><li><span><svg><path></path><path></path></svg></span>Odpowiedzialność za jakość danych publikowanych przez Departament.</li></ul></div></section><section><div><h2>Nasze wymagania</h2></div><div><div><div><ul><li><span><svg><path></path><path></path></svg></span>Wykształcenie wyższe;</li><li><span><svg><path></path><path></path></svg></span>Znajomość SQL na bardzo dobrym poziomie- wymóg konieczny;</li><li><span><svg><path></path><path></path></svg></span>Znajomość pakietu MS Office z bardzo dobrą obsługą MS Excel;</li><li><span><svg><path></path><path></path></svg></span>Wysoko rozwinięte umiejętności analityczne;</li><li><span><svg><path></path><path></path></svg></span>Umiejętność pracy zespołowej oraz organizacji pracy własnej;</li><li><span><svg><path></path><path></path></svg></span>Dokładność i precyzja, odpowiedzialność, spostrzegawczość, komunikatywność, myślenie przyczynowo – skutkowe, dążenie do celu.</li></ul></div></div><div><h3>Mile widziane</h3><div><ul><li><span><svg><path></path><path></path></svg></span>Doświadczenie zawodowe na podobnym stanowisku;</li><li><span><svg><path></path><path></path></svg></span>Znajomość Power BI oraz Tableau.</li></ul></div></div></div></section><section><div><h2>Benefity</h2></div><div><ul><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>dofinansowanie zajęć sportowych</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>prywatna opieka medyczna</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>dofinansowanie nauki języków</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>dofinansowanie szkoleń i kursów</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>ubezpieczenie na życie</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>owoce</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>program rekomendacji pracowników</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>ubezpieczenie szpitalne</div></div></li><li><div><div><svg><defs><mask><image/></mask></defs><rect></rect></svg></div><div>program wellbeingowy</div></div></li></ul><img/></div></section><div><section><div><h3>Tak się u nas pracuje</h3><span><svg><path></path></svg></span></div><div><img/><div><span><svg><path></path></svg></span></div></div><div><span><svg><path></path></svg></span></div></section></div><div><div><div><div><a><span><picture><svg><g><path></path></g></svg></picture>Aplikuj szybko</span></a><div></div></div></div><div><div><a><span><picture><svg><g><path></path></g></svg></picture>Aplikuj szybko</span></a><div></div></div><div><div><button><span><svg><path></path></svg></span><span>Zapisz</span></button><button><span><svg><path></path><path></path><path></path><path></path></svg></span><span>Drukuj</span></button><button><span><svg><path></path><path></path><path></path><path></path><path></path></svg></span><span>Udostępnij</span></button></div></div><div><div><picture><svg><g><path></path></g></svg></picture>Oferta z szybkim aplikowaniem</div><div><button><span>co to?</span></button></div></div><div><div><p>Wszystkie informacje o przetwarzaniu danych osobowych w tej rekrutacji znajdziesz w formularzu aplikacyjnym, po kliknięciu w przycisk "Aplikuj Teraz".</p></div></div></div></div></div><div><div><div><a>Praca</a></div><span><svg><path></path></svg></span><div><a>Warszawa</a><div><div><div><span><svg><path></path></svg></span></div></div></div></div><span><svg><path></path></svg></span><div><a>Finanse / Ekonomia</a></div><span><svg><path></path></svg></span><div><a>Doradztwo / Konsulting</a><div><div><div><span><svg><path></path></svg></span></div></div></div></div></div></div></div><div><div><div><div><div><a><span><picture><svg><g><path></path></g></svg></picture><span>Aplikuj szybko</span></span></a><div></div></div><div><div><button><span><svg><path></path></svg></span><span>Zapisz</span></button><button><span><svg><path></path><path></path><path></path><path></path></svg></span><span>Drukuj</span></button><button><span><svg><path></path><path></path><path></path><path></path><path></path></svg></span><span>Udostępnij</span></button></div></div><div><div><picture><svg><g><path></path></g></svg></picture>Oferta z szybkim aplikowaniem</div><div><button><span>co to?</span></button></div></div></div></div></div><div><div><strong>Powiadamiaj mnie o podobnych ofertach</strong><p>Analityk Biznesowy, Szturmowa 2, Mokotów, Warszawa</p></div><div><label><input/><span></span></label></div></div><div></div></div></div></div><div></div></div><footer><div><div><div><div><div>Dla kandydatów<span><svg><path></path></svg></span></div><div><div><a>Pomoc</a><a>Pracuj w Grupie Pracuj</a><a>Festiwal Pracy JOBICON</a><a>Kalkulator godzinowy</a></div></div></div></div><div><div><div>Dla firm<span><svg><path></path></svg></span></div><div><div><a>Dodaj ogłoszenie</a><a>Konto pracodawcy</a><a>Pomoc dla firm</a><a>Porady dla firm</a><a>Porady rekrutacyjne</a></div></div></div></div><div><div><div>Grupa Pracuj<span><svg><path></path></svg></span></div><div><div><a><img/></a><a>O nas</a><a>Centrum Prasowe</a><a>Reklama</a><a>Partnerzy</a><a>Archiwum ofert</a></div></div></div></div><div><div><div>Narzędzia<span><svg><path></path></svg></span></div><div><div><a>Kreator CV</a><a>Porady zawodowe</a><a>Kalkulator zarobków</a><a>Zarobki</a><a>The:blog</a></div></div></div></div><div><div><div>Nasze produkty<span><svg><path></path></svg></span></div><div><div><a><img/></a><a><img/></a><a><img/></a><a><img/></a><a><img/></a></div></div></div></div><div><div>Pobierz aplikację</div><div><a><img/></a><a><img/></a><a><img/></a></div></div></div><div><div><a>© Grupa Pracuj S.A.</a><a><img/></a></div><div><a>Regulamin</a><a>Polityka Prywatności</a><a>Polityka plików cookies</a><button>Ustawienia plików cookies</button><a>Akt o usługach cyfrowych</a></div><div><a><img/></a><a><img/></a><a><img/></a></div></div></div></footer></div></div></body></html>
'''

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Extract job offer details
job_offer = {}

# Job Title
job_offer['title'] = soup.find('h1').get_text(strip=True)

# Company Name
company_element = soup.find('h2')
if company_element:
    job_offer['company'] = company_element.get_text(strip=True).split('O firmie')[0].strip()

# Location
location_info = soup.find_all('li')[0].find_all('div')[1].get_text(strip=True)
job_offer['location'] = location_info

# Validity
validity_info = soup.find_all('li')[1].find_all('div')[1].get_text(strip=True)
job_offer['validity'] = validity_info

# Employment Type
employment_type = soup.find_all('li')[2].find_all('div')[1].get_text(strip=True)
job_offer['employment_type'] = employment_type

# Working Hours
working_hours = soup.find_all('li')[3].find_all('div')[1].get_text(strip=True)
job_offer['working_hours'] = working_hours

# Experience Level
experience_level = soup.find_all('li')[4].find_all('div')[1].get_text(strip=True)
job_offer['experience_level'] = experience_level

# Work Mode
work_mode = soup.find_all('li')[5].find_all('div')[1].get_text(strip=True)
job_offer['work_mode'] = work_mode

# Responsibilities
responsibilities_section = soup.find(string='Twój zakres obowiązków')
if responsibilities_section:
    responsibilities_parent = responsibilities_section.find_parent('section')
    if responsibilities_parent:
        responsibilities_div = responsibilities_parent.find_next_sibling('div')
        if responsibilities_div:
            responsibilities_list = responsibilities_div.find_all('li')
            job_offer['responsibilities'] = [li.get_text(strip=True) for li in responsibilities_list]
        else:
            print("Failed to find the responsibilities div.")
    else:
        print("Failed to find the responsibilities parent section.")
else:
    print("Failed to find the responsibilities section.")

# Requirements
requirements_section = soup.find(string='Nasze wymagania')
if requirements_section:
    requirements_parent = requirements_section.find_parent('section')
    if requirements_parent:
        requirements_div = requirements_parent.find_next_sibling('div')
        if requirements_div:
            requirements_list = requirements_div.find_all('li')
            job_offer['requirements'] = [li.get_text(strip=True) for li in requirements_list]
        else:
            print("Failed to find the requirements div.")
    else:
        print("Failed to find the requirements parent section.")
else:
    print("Failed to find the requirements section.")

# Preferred Qualifications
preferred_qualifications_section = soup.find(string='Mile widziane')
if preferred_qualifications_section:
    preferred_qualifications_parent = preferred_qualifications_section.find_parent('h3')
    if preferred_qualifications_parent:
        preferred_qualifications_ul = preferred_qualifications_parent.find_next_sibling('ul')
        if preferred_qualifications_ul:
            preferred_qualifications_list = preferred_qualifications_ul.find_all('li')
            job_offer['preferred_qualifications'] = [li.get_text(strip=True) for li in preferred_qualifications_list]
        else:
            print("Failed to find the preferred qualifications ul.")
    else:
        print("Failed to find the preferred qualifications parent h3.")
else:
    print("Failed to find the preferred qualifications section.")

# Benefits
benefits_section = soup.find(string='Benefity')
if benefits_section:
    benefits_parent = benefits_section.find_parent('section')
    if benefits_parent:
        benefits_div = benefits_parent.find_next_sibling('div')
        if benefits_div:
            benefits_list = benefits_div.find_all('li')
            job_offer['benefits'] = [li.get_text(strip=True) for li in benefits_list]
        else:
            print("Failed to find the benefits div.")
    else:
        print("Failed to find the benefits parent section.")
else:
    print("Failed to find the benefits section.")

# Print the job offer as JSON
print(json.dumps(job_offer, ensure_ascii=False, indent=2))
