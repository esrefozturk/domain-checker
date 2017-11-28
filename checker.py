from subprocess import PIPE, Popen

EXTENSIONS = ['com', 'net', 'io', 'ai']


def whois(domain, extension):
    out, err = Popen('whois {d}.{e} | grep -i "No match for domain"'.format(d=domain, e=extension), shell=True,
                     stdout=PIPE, stderr=PIPE).communicate()

    if err:
        print err

    if out:
        return True


def write(domain, extension):
    f = open('availables', 'a+')
    f.write('{d}.{e}\n'.format(d=domain, e=extension))
    f.close()


def check():
    domains = []
    with open('wordlist') as f:
        domains = f.read().strip().split('\n')
    for domain in domains:
        print 'Trying ', domain
        for extension in EXTENSIONS:
            if whois(domain, extension):
                write(domain, extension)


def main():
    check()


if __name__ == '__main__':
    main()
