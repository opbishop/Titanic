import custom_exception
from config import user_agent

import tldextract
import requests


def get_url(url):
    """
    Check URL's robots.txt for permission to access. If allowed, return HTTP of page.

    :param url:
    :return:
    """

    ext = tldextract.extract(url)

    try:
        response = requests.get('http://{}.{}/robots.txt'.format(ext.domain, ext.suffix), headers={
            'User-Agent': 'python-requests/4.8.2 (Compatible;{};{})'.format(user_agent['name'], user_agent['email'])
        }, timeout=10)
        # Only scrape URL if allowed by robots.txt
        if response.status_code != 200:
            if response.status_code == 404:
                # TODO 404 exception
                print('Robots.txt not found')
            else:
                raise custom_exception.DisallowedException(response.status_code)
    except custom_exception.DisallowedException as e:
        print('Connection to {} not permitted with HTTP code {}. Does its robots.txt allow access?'.format(url, e.status))

    return requests.get(url)
