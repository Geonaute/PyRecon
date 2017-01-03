from tld import get_tld


# get top level of domain name from http(s)://(www/ftp/etc).name.com to name.com
def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

# get_domain_name('http://arslansoftware.com')
