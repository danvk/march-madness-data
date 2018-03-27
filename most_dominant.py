#!/usr/bin/env python3
"""Given a winner, what was the closest game they played in the tournament?"""

import sys

from utils import sum_for_game, get_flattened_games

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

def get_dom_score(winner, year, game_years):
    """Returns score difference from the closest game the winner played."""
    diffs = []
    for rnd in (64, 32, 16, 8, 4, 2):
        games = [g for g in game_years if 
            g[0][0]["round_of"] == rnd and g[1] == year and 
            is_game_with_eventual_winner(g, winner["team"])]
        assert(len(games) == 1)
        game = games[0]
        diffs += [abs(game[0][0]["score"] - game[0][1]["score"])]
    #
    # CHANGE ME
    #
    # modifying this return to change the metrics. Other cool ideas:
    #   - return the avg score differential
    #   - return the sum of the score differentials
    return min(diffs)

def fmt_data(yr, winner, score):
    return '%4d - %14s (%1d): %2d' % (yr, winner['team'], winner['seed'], score)

def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    results = []
    for year in years:
        winner = get_winner(year, game_years)
        dom_score = get_dom_score(winner, year, game_years)
        results += [(year, winner, dom_score)]

    results = sorted(results, key=lambda x: x[2])
    for s in reversed(results):
        print(fmt_data(s[0], s[1], s[2]))

if __name__ == '__main__':
    main()
