DEFAULT_POOL = {
    'w': 0,
    'u': 0,
    'b': 0,
    'r': 0,
    'g': 0}

LANDS = {
    'plains': 'w',
    'island': 'u',
    'swamp': 'b',
    'mountain': 'r',
    'forest': 'g'
}

class ManaError(Exception):
    def __init__(self, mana_type):
        Exception.__init__(self, "Not enough mana of type {" + mana_type + "}!")

class ManaPool:
    def __init__(self):
        self.pool = DEFAULT_POOL

    def tap(self, land):
        self.pool[LANDS[land]] += 1

    def spend(self, cost):
        for mana_type in ['w', 'u', 'b', 'r', 'g']:
            if self.pool[mana_type] - cost[mana_type] < 0:
                raise ManaError(mana_type)
            else:
                self.pool[mana_type] -= cost[mana_type]
