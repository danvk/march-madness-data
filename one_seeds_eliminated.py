#!/usr/bin/env python3
"""What's the earliest round in which all 1 seeds were eliminated"""

import sys

from utils import get_flattened_games


def count_one_seeds(games):
    count = 0
    for g in games:
        if g[0]['seed'] == 1 or g[1]['seed'] == 1:
            count += 1
    return count


def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    for year in years:
        for rnd in (64, 32, 16, 8, 4, 2):
            games = [game for game, y in game_years if
                     game[0]['round_of'] == rnd and y == year]
            num_one_seeds = count_one_seeds(games)
            if num_one_seeds == 0:
                print('In %d, no one seeds remained in the round of %d' % (year, rnd))
                break


if __name__ == '__main__':
    main()
