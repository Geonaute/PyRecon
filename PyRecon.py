import getopt
import sys

from lib.domain_name import *
from lib.general import *
from lib.ip_address import *
from lib.robots_txt import *
from lib.whois import *
from lib.nmap import *

ROOT_DIR = 'results'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)


def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)


def main(argv):
    name = ''
    url = ''
    try:
        opts, args = getopt.getopt(argv, "hn:u:", ["name=", "url="])
    except getopt.GetoptError:
        print('PyRecon.py -n <name> -h <url>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('PyRecon.py -n <name> -h <url>')
            sys.exit(2)
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-u", "--url"):
            url = arg
    gather_info(name, url)

if __name__ == "__main__":
    main(sys.argv[1:])
