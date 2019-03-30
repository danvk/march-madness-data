# March Madness Data

This repo contains JSON files for all the NCAA brackets from 1985–2017.

## Results

### Sums of Seeds

After #16 seed UMBC became the first to beat a #1 seed, I was curious what the highest sum of seeds in a game was. This was harder to find out than I expected, so I grabbed some data from Wikipedia and found the answer. It's 25!

```
(1989) 25:            Minnesota 11 vs 14 Siena
(1991) 25:     Eastern Michigan 12 vs 13 Penn State
(1991) 25:               Temple 10 vs 15 Richmond
(1991) 25:          Connecticut 11 vs 14 Xavier
(1992) 25:     New Mexico State 12 vs 13 Southwest Louisiana
(1993) 25:    George Washington 12 vs 13 Southern
(1997) 25:                Texas 10 vs 15 Coppin State
(1998) 25:           Washington 11 vs 14 Richmond
(1998) 25:        Florida State 12 vs 13 Valparaiso
(2001) 25:           Georgetown 10 vs 15 Hampton
(2001) 25:              Gonzaga 12 vs 13 Indiana State
(2008) 25:            Villanova 12 vs 13 Siena
(2008) 25:                  WKU 12 vs 13 San Diego
(2009) 25:              Arizona 12 vs 13 Cleveland State
(2011) 25:             Richmond 12 vs 13 Morehead State
(2012) 25:               Xavier 10 vs 15 Lehigh
(2012) 25:        South Florida 12 vs 13 Ohio
(2013) 25:          Mississippi 12 vs 13 La Salle
(2014) 25:            Tennessee 11 vs 14 Mercer
(2015) 25:                 UCLA 11 vs 14 UAB
(2016) 25:             Syracuse 10 vs 15 Middle Tennessee
(2018) 25:                 UMBC 16 vs  9 Kansas State
(1997) 24:          Chattanooga 14 vs 10 Providence
(1993) 22:               Temple  7 vs 15 Santa Clara
(2012) 22:              Florida  7 vs 15 Norfolk State
(2013) 22:        Wichita State  9 vs 13 La Salle
(2013) 22:      San Diego State  7 vs 15 Florida Gulf Coast
(1986) 21:      Cleveland State 14 vs  7 Navy
(1998) 21:         Rhode Island  8 vs 13 Valparaiso
(2011) 21:                  VCU 11 vs 10 Florida State
(2014) 21:               Dayton 11 vs 10 Stanford
```

All the 25s are in the Round of 32. This happens whenever there are two first-round upsets in the
same part of the bracket. You can't get a higher sum than 25 until the third round or later, and
this has yet to happen. The closest was 14 Chattanooga vs. 10 Providence in 1997.

**Sweet 16**:
```
(1997) 24:          Chattanooga 14 vs 10 Providence
(2013) 22:        Wichita State  9 vs 13 La Salle
(1986) 21:      Cleveland State 14 vs  7 Navy
(1998) 21:         Rhode Island  8 vs 13 Valparaiso
(2011) 21:                  VCU 11 vs 10 Florida State
(2014) 21:               Dayton 11 vs 10 Stanford
(2016) 21:              Gonzaga 11 vs 10 Syracuse
(2002) 20:                 UCLA  8 vs 12 Missouri
(1990) 18:     Loyola Marymount 11 vs  7 Alabama
(2001) 18:               Temple 11 vs  7 Penn State
```

**Elite Eight**
```
(2000) 15:       North Carolina  8 vs  7 Tulsa
(2002) 15:              Indiana  5 vs 10 Kent State
(1990) 14:             Arkansas  4 vs 10 Texas
(1997) 14:              Arizona  4 vs 10 Providence
(2000) 14:            Wisconsin  8 vs  6 Purdue
(2002) 14:             Missouri 12 vs  2 Oklahoma
(1986) 12:             Kentucky  1 vs 11 LSU
(1990) 12:                 UNLV  1 vs 11 Loyola Marymount
(1994) 12:       Boston College  9 vs  3 Florida
(2001) 12:       Michigan State  1 vs 11 Temple
```

**Final Four**
```
(2011) 19:                  VCU 11 vs  8 Butler
(2006) 14:              Florida  3 vs 11 George Mason
(1986) 13:                  LSU 11 vs  2 Louisville
(2000) 13:              Florida  5 vs  8 North Carolina
(2016) 11:       North Carolina  1 vs 10 Syracuse
(1985) 10:            Villanova  8 vs  2 Memphis State
(1992) 10:            Michigan#  6 vs  4 Cincinnati
(2010) 10:       Michigan State  5 vs  5 Butler
(2013) 10:           Louisville  1 vs  9 Wichita State
(2014) 10:            Wisconsin  2 vs  8 Kentucky
```

**Finals**
```
(2014) 15:          Connecticut  7 vs  8 Kentucky
(2011) 11:          Connecticut  3 vs  8 Butler
(1985)  9:           Georgetown  1 vs  8 Villanova
(1988)  7:               Kansas  6 vs  1 Oklahoma
(1992)  7:                 Duke  1 vs  6 Michigan#
(1989)  6:           Seton Hall  3 vs  3 Michigan
(2000)  6:              Florida  5 vs  1 Michigan State
(2002)  6:             Maryland  1 vs  5 Indiana
(2010)  6:               Butler  5 vs  1 Duke
(1991)  5:               Kansas  3 vs  2 Duke
```

### Craziest Final Four

Or what was the craziest final four (i.e. highest sum of seeds)? It was 26, in [2011][].
The least crazy was [2008's final four][2008], the only with four 1 seeds.

```
26 2011         Kentucky (4)     Connecticut (3)              VCU (11)          Butler ( 8)
22 2000          Florida (5)  North Carolina (8)   Michigan State ( 1)       Wisconsin ( 8)
20 2006              LSU (4)            UCLA (2)          Florida ( 3)    George Mason (11)
18 2014          Florida (1)     Connecticut (7)        Wisconsin ( 2)        Kentucky ( 8)
18 2013       Louisville (1)   Wichita State (9)         Michigan ( 4)        Syracuse ( 4)
15 2016        Villanova (2)        Oklahoma (2)   North Carolina ( 1)        Syracuse (10)
16 2018  Loyola–Chicago (11)       Michigan ( 3)        Villanova ( 1)          Kansas ( 1)
15 1986             Duke (1)          Kansas (1)              LSU (11)      Louisville ( 2)
13 2010   Michigan State (5)          Butler (5)    West Virginia ( 2)            Duke ( 1)
13 1992             Duke (1)         Indiana (2)        Michigan# ( 6)      Cincinnati ( 4)
12 2017   South Carolina (7)         Gonzaga (1)           Oregon ( 3)  North Carolina ( 1)
12 1990             Duke (3)        Arkansas (4)     Georgia Tech ( 4)            UNLV ( 1)
12 1985       Georgetown (1)       St John's (1)        Villanova ( 8)   Memphis State ( 2)
11 2005         Illinois (1)      Louisville (4)   North Carolina ( 1)  Michigan State ( 5)
11 1996    Massachusetts (1)        Kentucky (1)      Miss. State ( 5)        Syracuse ( 4)
10 2015         Kentucky (1)       Wisconsin (1)   Michigan State ( 7)            Duke ( 1)
10 1988             Duke (2)          Kansas (6)         Oklahoma ( 1)         Arizona ( 1)
10 1987         Syracuse (2)      Providence (6)          Indiana ( 1)            UNLV ( 1)
 9 2012         Kentucky (1)      Louisville (4)       Ohio State ( 2)          Kansas ( 2)
 9 2003         Syracuse (3)           Texas (1)        Marquette ( 3)          Kansas ( 2)
 9 2002         Maryland (1)          Kansas (1)          Indiana ( 5)        Oklahoma ( 2)
 9 1998   North Carolina (1)            Utah (3)         Kentucky ( 2)        Stanford ( 3)
 9 1995   Oklahoma State (4)            UCLA (1)   North Carolina ( 2)        Arkansas ( 2)
 9 1989             Duke (2)      Seton Hall (3)         Michigan ( 3)        Illinois ( 1)
 8 2004   Oklahoma State (2)    Georgia Tech (3)             Duke ( 1)     Connecticut ( 2)
 8 1994          Florida (3)            Duke (2)         Arkansas ( 1)         Arizona ( 2)
 7 2009     Michigan St. (2)     Connecticut (1)        Villanova ( 3)  North Carolina ( 1)
 7 2001             Duke (1)        Maryland (3)   Michigan State ( 1)         Arizona ( 2)
 7 1999             Duke (1)  Michigan State (1)       Ohio State ( 4)     Connecticut ( 1)
 7 1997   North Carolina (1)         Arizona (4)       Minnesota* ( 1)        Kentucky ( 1)
 7 1991   North Carolina (1)          Kansas (3)             Duke ( 2)            UNLV ( 1)
 6 2007          Florida (1)            UCLA (2)       Georgetown ( 2)      Ohio State ( 1)
 5 1993   North Carolina (1)          Kansas (2)         Kentucky ( 1)      Michigan * ( 1)
 4 2008   North Carolina (1)          Kansas (1)          Memphis ( 1)            UCLA ( 1)
```

## Using the data

The data comes from [Wikipedia articles][2011]. It's all in `data/YYYY.json`. For example:

```json
{
  "year": 1997,
  "regions": [
    [
      [
        [
          {
            "round_of": 64, "seed": 1,
            "team": "North Carolina", "score": 82,
          },
          {
            "round_of": 64, "seed": 16,
            "team": "Fairfield", "score": 74
          }
        ],
        ...
      ],
      ...
    ],
    ...
  ],
  "finalfour": [
    [
      [
        {
          "round_of": 4, "seed": 1,
          "team": "North Carolina", "score": 58
        },
        {
          "round_of": 4, "seed": 4,
          "team": "Arizona", "score": 66
        }
      ],
      [
        {
          "round_of": 4, "seed": 1,
          "team": "Minnesota*", "score": 69
        },
        {
          "round_of": 4, "seed": 1,
          "team": "Kentucky", "score": 78
        }
      ]
    ],
    [
      [
        {
          "round_of": 2, "seed": 4,
          "team": "Arizona", "score": 84
        },
        {
          "round_of": 2, "seed": 1,
          "team": "Kentucky", "score": 79
        }
      ]
    ]
  ]
}
```

- There are four regions.
- Each contains an array of four rounds.
- Each round contains an array of games.
- Each game is an array of two teams.
- Each team is an object with `round_of`, `seed`, `team` and `score` keys.

If you're working in Python, you can find some helper functions in `utils.py` and some
example code in `find_highest_seeds.py` and `craziest_final_four.py`:

    $ ./craziest_final_four.py data/*.json
    26 2011         Kentucky ( 4)       Connecticut ( 3)              VCU (11)           Butler ( 8)
    22 2000          Florida ( 5)    North Carolina ( 8)   Michigan State ( 1)        Wisconsin ( 8)
    20 2006              LSU ( 4)              UCLA ( 2)          Florida ( 3)     George Mason (11)
    18 2014          Florida ( 1)       Connecticut ( 7)        Wisconsin ( 2)         Kentucky ( 8)
    18 2013       Louisville ( 1)     Wichita State ( 9)         Michigan ( 4)         Syracuse ( 4)
    ...

## Updating the data

To regenerate (or update) the data, you'll need Python 3.6 or later.
Set up your virtual environment and run:

    pip install -r requirements.txt
    ./extract_wiki_source.py pages/*.html
    ./extract_bracket.py pages/*.wiki
    mv pages/*.json data/

To add a new year, use `curl` to put a new HTML file in `pages/YYYY.html`. You can
use the URLs in `urls.txt` as a template.

[2008]: https://en.wikipedia.org/wiki/2008_NCAA_Division_I_Men%27s_Basketball_Tournament
[2011]: https://en.wikipedia.org/wiki/2011_NCAA_Division_I_Men%27s_Basketball_Tournament
