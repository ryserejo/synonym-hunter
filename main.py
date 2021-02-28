from bs4 import BeautifulSoup as Bsoup
from unidecode import unidecode
import requests


def sanitizing(dirty):
    return unidecode(dirty)


def get_target(url, word, html_tag, class_name):
    document = requests.get(url + word).content
    soup = Bsoup(document, 'html.parser')
    result = soup.find_all(html_tag, class_=class_name)
    return result


def get_synonym(argument):
    url = "https://www.sinonimos.com.br/"
    html_tag = "div"
    class_name = "s-wrapper"
    parse_string = [x.text for x in get_target(url, argument, html_tag, class_name)]
    show(parse_string)


def show(arr):
    for section in arr:
        print(section)
        print("------------------------")


synonym = sanitizing(input("Digite uma palava > "))
get_synonym(synonym)
