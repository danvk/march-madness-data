#!/usr/bin/env python3
"""What's the highest sum of seeds ever in an NCAA game?"""

import json
import sys

from utils import all_games, sum_for_game


def format_result(game_year):
    game, year = game_year
    return '(%s) %2d: %20s %2d vs %2d %-20s' % (
        year,
        sum_for_game(game),
        game[0]['team'],
        game[0]['seed'],
        game[1]['seed'],
        game[1]['team'],
    )


def main():
    game_years = []
    for path in sys.argv[1:]:
        bracket = json.load(open(path))
        year = bracket['year']
        game_years += [(game, year) for game in all_games(bracket)]
    ordered_games = list(sorted(game_years, key=lambda gp: -sum_for_game(gp[0])))

    print('All rounds')
    for game_path in ordered_games[:30]:
        print(format_result(game_path))

    for rnd in (32, 16, 8, 4, 2):
        print('\nRound of %d' % rnd)
        results = [gp for gp in ordered_games if gp[0][0]['round_of'] == rnd]
        for game_path in results[:10]:
            print(format_result(game_path))


if __name__ == '__main__':
    main()
