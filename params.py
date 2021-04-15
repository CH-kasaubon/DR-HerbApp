from fractions import Fraction

LEVELS = ['None', 'Weak (1)', 'Basic (2)',
          'Mediocre (3)', 'Fair (4)', 'Good (5)',
          'Great (6)', 'Superb (7)',
          'Legendary (8)', 'Legendary 2 (9)',
          'Legendary 3 (10)', 'Legendary 4 (11)',
          'Legendary 5 (12)', 'Legendary 6 (13)',
          'Legendary 7 (14)', 'Legendary 8 (15)', ]

MAX_HERBS = {'None': 0,
             'Weak (1)': 1,
             'Basic (2)': 2,
             'Mediocre (3)': 2,
             'Fair (4)': 3,
             'Good (5)': 3,
             'Great (6)': 4,
             'Superb (7)': 4,
             'Legendary (8)': 5,
             'Legendary 2 (9)': 5,
             'Legendary 3 (10)': 5,
             'Legendary 4 (11)': 5,
             'Legendary 5 (12)': 5,
             'Legendary 6 (13)': 5,
             'Legendary 7 (14)': 5,
             'Legendary 8 (15)': 5,
             }

REMEDY_DIFFS = {'Poultice': 0,
                'Potion': 1,
                'Oil': 2
                }

REMEDY_COSTS = {
    'Poultice': {},
    'Potion': {},
    'Oil': {}
}

LEVELS_DICT = {LEVELS[k]: k for k in range(16)}

FUDGE_PROBS = {
    4: Fraction(1, 81),  # rolling +4
    3: Fraction(5, 81),  # rolling +3 or better
    2: Fraction(15, 81),  # rolling +2 or better
    1: Fraction(31, 81),  # rolling +1 or better
    0: Fraction(50, 81),  # etc.. etc...
    -1: Fraction(66, 81),
    -2: Fraction(76, 81),
    -3: Fraction(80, 81),
}

SAVE_POUCH_FILE = 'pouch_save.csv'
REMEDY_COST_FILE = 'herb_remedies_costs.csv'
