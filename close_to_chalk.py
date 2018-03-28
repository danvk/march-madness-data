#!/usr/bin/env python3
"""Lists the scores that a pure chalk bracket would receive for a given year"""

import sys

from utils import get_flattened_games

# these are the scores used by common bracket sites
_ROUNDS_SCORES = {
    64: 10,
    32: 20,
    16: 40,
    8: 80,
    4: 160,
    2: 320,
}


def score(game):
    return _ROUNDS_SCORES[game[0]['round_of']]


def chalk(game):
    global strs
    """Was this game a chalk win?

    This is actually a little tricky. If a 1 beats a 16, its obviously chalk.
    However, if a 7 seed beats an 11 seed, it cannot be counted in a pure chalk
    bracket, because that bracket would have had the 7 losing to the 2 seed in
    the round of 32.

    The trick is the relationship between round and the seeds of teams that
    should be left if all games were decided by seed. For example, in the sweet
    sixteen, there are 4 teams per region, so a win is only chalk if the higher
    seed wins AND if that winner is a 1, 2, 3, or 4 seed.
    """

    _, winner = sorted(game, key=lambda t: t['score'])
    return winner['seed'] <= max(1, winner['round_of'] / 8)


def get_score(game_years, year):
    total_score = 0
    games = [g[0] for g in game_years if g[1] == year]
    for game in games:
        if (chalk(game)):
            total_score += score(game)
    return total_score


def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    scores = []
    for year in years:
        scores += [(year, get_score(game_years, year))]

    scores = sorted(scores, key=lambda x: x[1])
    print('year: score')
    print('===========')
    for year, score in reversed(scores):
        print('%d: %d' % (year, score))


if __name__ == '__main__':
    main()
