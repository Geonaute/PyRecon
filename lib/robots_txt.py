import urllib
import io


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    result = ''
    try:
        req = urllib.urlopen(path + 'robots.txt', data=None)
        # data = io.TextIOWrapper(req, encoding='utf-8')
        result = req.read()
    except:
        result = 'robots.txt not found.'
    return result
