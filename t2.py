#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This script allow users to translate a string
from one language to another with Google translate"""

import sys
import re
import json
import requests
from clint.textui import colored

def print_params(data):
    """print parameters from list"""
    for val in data:
        if isinstance(val, basestring):
            print colored.blue("\t " + val)

url = 'http://translate.google.com/translate_a/t'


def main():
    """
    Usage:
        first arg   - source lang
        second arg  - target lang
        third arg + - string to translate(no quotes required)
    Example:
        t2.py en ru text to translate
        t2.py ru en текст для перевода
    """

    if len(sys.argv) <= 3:
        print colored.cyan(main.__doc__)
        sys.exit(1)

    params = {
            'client' : 't',
            'hl' : 'en',
            'multires' : '1',
            'text' : ' '.join(sys.argv[3:]),
            'sl' : sys.argv[1],
            'tl' : sys.argv[2]
            }
    headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept-Charset': 'utf-8'
            }

    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code != 200:
        print colored.red("Server returned code {}".format(resp.status_code))
        sys.exit(1)

    fixed_json = re.sub(r',{2,}', ',', resp.text).replace(',]', ']').replace('[,', '[')
    try:
        data = json.loads(fixed_json)
    except ValueError, ex:
        print colored.red(u"{}: bad json: {}\n{}\n{}".format(resp.status_code, ex, resp.text, fixed_json))
        sys.exit(1)

    #import pprint
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(data)

    #simple translation
    translated, origin, pronounce = u'', u'', u''
    for item in data[0]:
        translated += item[0]
        origin += item[1] + u' '
        pronounce += item[2] or item[3]

    print colored.green(translated),  u'/ {}/ {}'.format(origin, pronounce)
    #abbreviation
    if not isinstance(data[1], basestring):
        print data[1][0][0]
        print_params(data[1][0][1])
    #interjection
    try:
        if not isinstance(data[1][1], basestring):
            print data[1][1][0]
            print_params(data[1][1][1])
    except Exception:
        print colored.cyan("no interjection")


if __name__ == '__main__':
    main()
