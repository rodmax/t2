#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This script allow users to translate a string
from one language to another with Yandex translate/dictionary API"""

import sys
import os
import json
import requests
from clint.textui import colored


DICT_API_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'  # words translate
TRANSL_API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'  # text translate
CONFIG_FILE = os.path.expanduser('~')+'/.t2conf'


def display_dict_response(data):
    for item in data['def']:
        for tr in item['tr']:
            print u'{} / {} / {}'.format(colored.green(tr['text']), tr['pos'], item.get('ts', '[no transcription]'))
            for mean in tr.get('mean', []):
                print(u'\t\t{}'.format(colored.blue(mean['text'])))


def display_transl_response(data):
    print colored.green(data['text'][0])


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

    if len(sys.argv) < 4:
        print colored.cyan(main.__doc__)
        sys.exit(1)
    try:
        config = json.loads(file(CONFIG_FILE).read())
    except IOError as exc:
        print colored.red('Config file {} not found.'.format(CONFIG_FILE))
        sys.exit(1)
    except ValueError as exc:
        print colored.red('{}: bad json format: {}'.format(CONFIG_FILE, exc))
        sys.exit(1)

    use_dict = len(sys.argv) == 4  # if only one word specified

    params = {
        'key': config.get('dict_key') if use_dict else config.get('transl_key'),
        'text': ' '.join(sys.argv[3:]),
        'lang': '-'.join(sys.argv[1:3]),
    }
    url = DICT_API_URL if use_dict else TRANSL_API_URL
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print colored.red("Server returned code {}".format(resp.status_code))
        sys.exit(1)

    data = resp.json()

    # Uncomment to debug response data
    # print json.dumps(data, indent=4)

    (display_dict_response if use_dict else display_transl_response)(data)


if __name__ == '__main__':
    main()
