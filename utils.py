import re
import json

SEED_RE = re.compile(r'(\d+)')


def all_games(bracket):
    return [
        game
        for region in bracket['regions']
        for rnd in region
        for game in rnd
    ] + [
        game
        for rnd in bracket['finalfour']
        for game in rnd
    ]


def get_flattened_games(filenames):
    """Return a list of (game, year) tuples for all games in the JSON files."""
    game_years = []
    for path in filenames:
        bracket = json.load(open(path))
        year = bracket['year']
        game_years += [(game, year) for game in all_games(bracket)]
    return game_years


def extract_seed(seed):
    """Sometimes a seed is something like MW1. This extracts the 1."""
    m = SEED_RE.search(seed)
    assert m, seed
    return int(m.group(1))


def extract_year(path):
    m = re.search(r'(\d\d\d\d)', path)
    assert m, path
    return int(m.group(1))


def sum_for_game(game):
    return game[0]['seed'] + game[1]['seed']
