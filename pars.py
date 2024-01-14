import requests
from bs4 import BeautifulSoup
import fake_useragent
from urllib.parse import urljoin
import zipfile

user_agent = fake_useragent.UserAgent().random
headers = {
    'User-agent' : user_agent
}
responce = None
link = 'https://chat.openai.com/'

def pars(link):
    responce = requests.get(link, headers=headers)
    with open('index.html', 'w') as file:
        file.write(responce.text)

    soup = BeautifulSoup(responce.content, 'html.parser')

    js_files = []
    for script in soup.find_all('script'):
        if script.attrs.get('src'):
            script_url = urljoin(link, script.attrs.get('src'))
            js_files.append(script_url)

    with open('js.txt', 'w') as js_file:
        js_file.write('\n'.join(js_files))

    css_files = []
    for css in soup.find_all('link'):
        if css.attrs.get('href'):
            css_url = urljoin(link, css.attrs.get('href'))
            css_files.append(css_url)
    with open('css.txt', 'w') as css_file:
        css_file.writelines('\n'.join(css_files))

    with zipfile.ZipFile('Site.zip', 'w') as site:
        site.write('index.html')
        site.write('js.txt')
        site.write('css.txt')

pars(link)