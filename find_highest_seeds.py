#!/usr/bin/env python3
"""What's the highest sum of seeds ever in an NCAA game?"""

import json
import re
import sys


SEED_RE = re.compile(r'(\d+)')


def all_games(bracket):
    return [
        game
        for region in bracket
        for rnd in region
        for game in rnd
    ]


def extract_seed(seed):
    """Sometimes a seed is something like MW1. This extracts the 1."""
    m = SEED_RE.search(seed)
    assert m, seed
    return int(m.group(1))


def sum_for_game(game):
    print(game)
    return extract_seed(game[0]['seed']) + extract_seed(game[1]['seed'])


def main():
    games = []
    for path in sys.argv[1:]:
        bracket = json.load(open(path))
        games += [(game, path) for game in all_games(bracket)]
    ordered_games = sorted(games, key=lambda gp: -sum_for_game(gp[0]))
    print(ordered_games[:10])


if __name__ == '__main__':
    main()
