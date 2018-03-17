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
    return extract_seed(game[0]['seed']) + extract_seed(game[1]['seed'])


def extract_year(path):
    m = re.search(r'(\d\d\d\d)', path)
    assert m, path
    return int(m.group(1))


def format_result(game_path):
    game, path = game_path
    return '(%s) %2d: %20s %2d vs %2d %-20s' % (
        extract_year(path),
        sum_for_game(game),
        game[0]['team'],
        extract_seed(game[0]['seed']),
        extract_seed(game[1]['seed']),
        game[1]['team'],
    )


def main():
    game_paths = []
    for path in sys.argv[1:]:
        bracket = json.load(open(path))
        for game in all_games(bracket):
            sum_for_game(game)
        game_paths += [(game, path) for game in all_games(bracket)]
    ordered_games = sorted(game_paths, key=lambda gp: -sum_for_game(gp[0]))
    for game_path in ordered_games[:30]:
        print(format_result(game_path))


if __name__ == '__main__':
    main()
