import requests
from chp6.login import parse_form

REGISTER_URL = 'http://example.webscraping.com/places/default/user/register'

session = requests.Session()

html = session.get(REGISTER_URL)
form = parse_form(html.content)
print(form)
