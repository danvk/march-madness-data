#!/usr/bin/env python3
"""Traces the winners path through the tournament"""

import sys

from utils import sum_for_game, get_flattened_games

# Common names of each round
_ROUNDS_NAMES = [
    (64, "Round of 64"),
    (32, "Round of 32"),
    (16, "Sweet Sixteen"),
    (8,  "Elite Eight"),
    (4,  "Final Four"),
    (2,  "Championship"),
]

def get_winner(year, game_years):
    rnd = 2
    games = [g for g in game_years if 
                 g[0][0]["round_of"] == rnd and g[1] == year]
    assert(len(games) == 1)
    game = games[0]
    t1 = game[0][0]
    t2 = game[0][1]

    return t1 if t1["score"] > t2["score"] else t2

def is_game_with_eventual_winner(game, winner):
    return game[0][0]["team"] == winner or game[0][1]["team"] == winner

def print_winner(winner, year, game_years):
    """Returns score difference from the closest game the winner played."""
    for rnd, name in _ROUNDS_NAMES:
        games = [g for g in game_years if 
            g[0][0]["round_of"] == rnd and g[1] == year and 
            is_game_with_eventual_winner(g, winner["team"])]
        assert(len(games) == 1)
        game = games[0]
        t1 = game[0][0]
        t2 = game[0][1]
        loser = t1 if t1["score"] < t2["score"] else t2
        winner = t1 if t1["score"] > t2["score"] else t2
        print("\tIn the %13s, they beat %21s %3d - %3d  (+%2d)" % 
            (name, loser['team'], 
             winner['score'], loser['score'], 
             winner['score'] - loser['score']))
    print("\n")

def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    results = []
    for year in years:
        winner = get_winner(year, game_years)
        print("%d - Winner: %s:" % (year, winner['team']))
        print_winner(winner, year, game_years)

    results = sorted(results, key=lambda x: x[2])
    for s in reversed(results):
        print(fmt_data(s[0], s[1], s[2]))

if __name__ == '__main__':
    main()
