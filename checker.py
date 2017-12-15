from subprocess import PIPE, Popen

EXTENSIONS = ['com', 'net', 'io', 'ai']


def whois(domain, extension):
    ctr = 5
    while ctr >= 0:
        ctr -= 1
        try:
            out, err = Popen('whois {d}.{e} | grep -i "No match for domain"'.format(d=domain, e=extension), shell=True,
                             stdout=PIPE, stderr=PIPE).communicate()
        except Exception as e:
            print 'Exception:', e

        if err:
            print 'Error', err

        if out:
            return True
        else:
            return False


def write(domain, extension):
    f = open('availables', 'a+')
    f.write('{d}.{e}\n'.format(d=domain, e=extension))
    f.close()

    if 3 <= len(domain) <= 7:
        f = open('availables-3-7', 'a+')
        f.write('{d}.{e}\n'.format(d=domain, e=extension))
        f.close()


def check():
    domains = []
    with open('wordlist') as f:
        domains = f.read().strip().split('\n')
    for domain in domains:
        domain = domain.lower()
        print 'Trying ', domain
        for extension in EXTENSIONS:
            if whois(domain, extension):
                write(domain, extension)


def main():
    check()


if __name__ == '__main__':
    main()
