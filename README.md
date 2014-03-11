t2
==

The simple script "translate to" to translate words &amp; sentences in CLI (based on Google translate resource)<br>
Initial version taken from http://habrahabr.ru/post/113243/

Requirements
====
Current version testsed on python 2.7.3, Ubuntu 12.04<br>
PIP dependencies:
* clint
* requests

Usage
====
```bash
> t2.py en ru text to translate
> t2.py ru en текст для перевода
```
first arg       - source lang<br>
second arg      - target lang<br>
third(+) arg(s) - string to translate(no quotes required)<br>
