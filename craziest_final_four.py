#!/usr/bin/env python3
"""What's the craziest (highest sum of seeds) final four ever?"""

import json
import sys

from utils import sum_for_game


def final_four_sum(bracket):
    round_of_4 = bracket['finalfour'][0]
    return sum(sum_for_game(g) for g in round_of_4)


def formatted_final4(bracket):
    round_of_4 = bracket['finalfour'][0]
    a = round_of_4[0][0]
    b = round_of_4[0][1]
    c = round_of_4[1][0]
    d = round_of_4[1][1]

    def fmt_team(x):
        return '%20s (%2d)' % (x['team'], x['seed'])

    return ' '.join(fmt_team(x) for x in (a, b, c, d))


def main():
    results = []
    for path in sys.argv[1:]:
        bracket = json.load(open(path))
        score = final_four_sum(bracket)
        results.append((score, bracket['year'], bracket))
    ordered_years = reversed(sorted(results))
    for score, year, bracket in ordered_years:
        fmt = formatted_final4(bracket)
        print("{score:2} {year} {fmt}".format(score=score,year=year,fmt=fmt))


if __name__ == '__main__':
    main()
