# -*- coding: utf-8 -*-
# tools, 8 juin 2017

import requests
from urlparse import urlparse

MY_USER_AGENT = u"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
HEADERS = {u'User-Agent': MY_USER_AGENT}

STATUS_TOO_MANY_REDIRECTS = 3100
STATUS_BAD_REQUEST = 400
STATUS_TOO_MANY_REQUESTS = 429
STATUS_SSL_ERROR = 495

def check_http(url, verify_ssl=True):
    url = url.strip()
    try:
        r = requests.get(url, headers=HEADERS, verify=verify_ssl)
        
        # check root domain
        if r.status_code == 404:
            parsed_uri = urlparse(r.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            r = requests.get(domain, headers=HEADERS, verify=verify_ssl)
        
        # check original status_code for redirects
        if r.history:
            return (r.url, r.history[0].status_code)
        
        return (r.url, r.status_code)
    except requests.exceptions.MissingSchema:
        return (url, STATUS_BAD_REQUEST)
    except requests.exceptions.SSLError:
        return (url, STATUS_SSL_ERROR)
    except requests.exceptions.ConnectionError:
        return (url, STATUS_TOO_MANY_REQUESTS)
    except requests.exceptions.TooManyRedirects:
        return (url, STATUS_TOO_MANY_REDIRECTS)

def check_http_list(url_list):
    result = []
    for url in url_list:
        result.append(check_http(url))
    return result
