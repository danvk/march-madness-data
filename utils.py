import re

SEED_RE = re.compile(r'(\d+)')


def all_games(bracket):
    return [
        game
        for region in bracket
        for rnd in region
        for game in rnd
    ]


def final_four(bracket):
    assert len(bracket) == 5, len(bracket)
    return bracket[4]


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
    return extract_seed(game[0]['seed']) + extract_seed(game[1]['seed'])
