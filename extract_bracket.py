#!/usr/bin/env python3

from collections import defaultdict
import json
import re
import sys

import mwparserfromhell

NAME_RE = re.compile(r'\s*RD(\d)-(score|team|seed)(\d+)', re.I)


def dict_to_array(d):
    return [d[k] for k in sorted(d.keys())]


def extract_template(template):
    # round # --> game # --> 0 or 1 --> {team|score|seed} --> value
    rounds = defaultdict(lambda: defaultdict(lambda: [{}, {}]))
    for p in template.params:
        m = re.match(NAME_RE, str(p.name))
        if not m:
            continue
        round_num = int(m.group(1)) - 1
        field = m.group(2)
        slot = int(m.group(3)) - 1
        value = p.value.strip_code().strip()

        game_num = slot // 2
        game_slot = slot % 2
        rounds[round_num][game_num][game_slot][field] = value

    return [dict_to_array(v) for v in dict_to_array(rounds)]


def extract_bracket(source):
    wikicode = mwparserfromhell.parse(source)
    templates = wikicode.filter_templates()
    brackets = [t for t in templates if 'Bracket' in t.name]
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
