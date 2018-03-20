#!/usr/bin/env python3
"""Lists the scores that a pure chalk bracket would receive for a given year"""

import sys

from utils import sum_for_game, get_flattened_games

# these are the scores used by common bracket sites
_ROUNDS_SCORES = [
    (64, 10),
    (32, 20),
    (16, 40),
    (8, 80),
    (4, 160),
    (2, 320),
]

def chalk(game, c_range):
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

    t1 = game[0][0]
    t2 = game[0][1]

    winner = t1 if t1["score"] > t2["score"] else t2
    loser = t1 if t1["score"] < t2["score"] else t2

    return winner["seed"] in c_range

def get_score(game_years, year):
    score = 0
    for i, rnd_scr in enumerate(_ROUNDS_SCORES):
        rnd = rnd_scr[0]
        scr = rnd_scr[1]
        games = [g for g in game_years if 
                 g[0][0]["round_of"] == rnd and g[1] == year]
        # range of seeds allowed. See comment under chalk() for more info
        r = range(1, (16/(i+2))+1)
        for g in games:
            if chalk(g, r):
                score += scr
    return score


def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    scores = []
    for year in years:
        scores += [(year, get_score(game_years, year))]

    scores = sorted(scores, key=lambda x: x[1])
    print("year: score")
    print("===========")
    for s in reversed(scores):
        print("%d: %d" % (s[0], s[1]))

if __name__ == '__main__':
    main()
