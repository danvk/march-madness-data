#!/usr/bin/env python3
"""Extract wikisource from an "Edit" page."""

import sys

from bs4 import BeautifulSoup


def extract_source(html):
    soup = BeautifulSoup(html, 'html.parser')
    textareas = soup.select('textarea')
    assert len(textareas) == 1
    return textareas[0].text


def main():
    for path in sys.argv[1:]:
        assert '.html' in path
        html = open(path).read()
        source = extract_source(html)
        open(path.replace('.html', '.wiki'), 'w').write(source)


if __name__ == '__main__':
    main()
