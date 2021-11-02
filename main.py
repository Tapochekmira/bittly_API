import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('url', nargs='?')
 
    return parser


def shorten_link(token, url):
    base_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}'
        }
    payload = {
        'long_url': url
        }
    response = requests.post(base_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, clear_link):
    base_url = f'https://api-ssl.bitly.com/v4/bitlinks/{clear_link}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
        }
    clicks_count = requests.get(base_url, headers=headers)
    clicks_count.raise_for_status()
    return clicks_count.json()['total_clicks']


def is_bitlink(clear_link, token):
    base_url = f'https://api-ssl.bitly.com/v4/bitlinks/{clear_link}'
    headers = {
        'Authorization': f'Bearer {token}'
        }
    response = requests.get(base_url, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    
    parser = createParser()
    url = parser.parse_args().url

    url_parse = urlparse(url)
    netloc = url_parse.netloc
    path = url_parse.path
    clear_link = f'{netloc}{path}'
    if is_bitlink(clear_link, token):
        try:
            print('Клики', count_clicks(token, clear_link))
        except requests.exceptions.HTTPError:
            print('Invalid bitlink')
    else:
        try:
            bitlink = shorten_link(token, url)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError:
            print('Invalid site address')
