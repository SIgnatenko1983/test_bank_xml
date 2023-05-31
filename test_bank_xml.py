import requests
from lxml import etree

URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'


def test_valid_xml():
    response = requests.get(URL)
    assert etree.fromstring(response.content), "Ошибка в XML"


def test_check_xml():
    schema_url = 'http://www.cbr.ru/StaticHtml/File/92172/ValCurs.xsd'
    response = requests.get(schema_url)
    schema_root = etree.XML(response.content)
    schema = etree.XMLSchema(schema_root)
    xmlparser = etree.XMLParser(schema=schema)
    response = requests.get(URL)
    assert etree.fromstring(response.content, xmlparser)
