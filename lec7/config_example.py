# coding: utf-8

import ConfigParser

def main():
    conf = ConfigParser.ConfigParser()
    conf.read('test.conf')

    if conf.has_section('main'):
        print conf.getint('main', 'log_size')

if __name__ == "__main__":
    main()
