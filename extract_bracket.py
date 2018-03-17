#!/usr/bin/env python3

from collections import defaultdict
import json
import re
import sys

import mwparserfromhell

NAME_RE = re.compile(r'\s*RD(\d)-(score|team|seed)(\d+)', re.I)


def dict_to_array(d):
    return [d[k] for k in sorted(d.keys())]


DEFAULTS16 = [
    ('RD1-seed01', '1'),
    ('RD1-seed02', '16'),
    ('RD1-seed03', '8'),
    ('RD1-seed04', '9'),
    ('RD1-seed05', '5'),
    ('RD1-seed06', '12'),
    ('RD1-seed07', '4'),
    ('RD1-seed08', '13'),
    ('RD1-seed09', '6'),
    ('RD1-seed10', '11'),
    ('RD1-seed11', '3'),
    ('RD1-seed12', '14'),
    ('RD1-seed13', '7'),
    ('RD1-seed14', '10'),
    ('RD1-seed15', '2'),
    ('RD1-seed16', '15')
]


def extract_template(template):
    # round # --> game # --> 0 or 1 --> {team|score|seed} --> value
    rounds = defaultdict(lambda: defaultdict(lambda: [{}, {}]))
    pairs = [
        (str(p.name), p.value.strip_code().strip())
        for p in template.params
    ]
    if template.name.matches('16TeamBracket'):
        pairs += DEFAULTS16
    for name, value in pairs:
        m = re.match(NAME_RE, name)
        if not m:
            continue
        round_num = int(m.group(1)) - 1
        field = m.group(2)
        slot = int(m.group(3)) - 1

        game_num = slot // 2
        game_slot = slot % 2
        rounds[round_num][game_num][game_slot][field] = value

    return [dict_to_array(v) for v in dict_to_array(rounds)]


def extract_bracket(source):
    wikicode = mwparserfromhell.parse(source)
    templates = wikicode.filter_templates()
    brackets = [
        t
        for t in templates
        if 'Bracket' in t.name and not t.name.matches('2TeamBracket')
    ]
    return [
        extract_template(b)
        for b in brackets
    ]


def main():
    for path in sys.argv[1:]:
        assert '.wiki' in path
        source = open(path).read()
        bracket = extract_bracket(source)
        json.dump(bracket, open(path.replace('.wiki', '.json'), 'w'))


if __name__ == '__main__':
    main()
