t2
==

The simple script "translate to" to translate words &amp; sentences in CLI (based on yandex API translate resource)<br>
TODO: update this description

Requirements
====
Current version should work on:
* python 2.7.3+

> porting to python 3 seems to do easily

PIP dependencies:
* [clint](https://github.com/kennethreitz/clint) (Python Command-line Application Tools)
* [requests](http://docs.python-requests.org/en/latest/) (Pretty HTTP library, written in Python, for human beings)

Usage
====
Arguments
---
```bash
  > t2.py en ru text to translate
  > t2.py ru en текст для перевода
```
first arg       - source lang<br>
second arg      - target lang<br>
third(+) arg(s) - string to translate(no quotes required)<br>

Aliases
---
* toru - t2.py en ru
* toen - t2.py ru en

Examples
---
```shell
  > toru Hello world! I am here
  Привет мир ! Я здесь / Hello world! I am here / Privet mir ! YA zdes'

  > toen Привет всем! Меня зовут Вася.
  Hi everyone! My name is Bob . / Привет всем! Меня зовут Вася. / Privet vsem!Menya zovut Vasya.
  
  > toen дом
  house / дом / dom
  noun
	  house
	  home
	  dwelling
	  door
	  premises
	  crib
	  hearth and home
	  establishment
	  base
  no interjection
```
