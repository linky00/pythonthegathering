DEFAULT_POOL = {
    'W': 0,
    'U': 0,
    'B': 0,
    'R': 0,
    'G': 0}

LANDS = {
    'plains': 'W',
    'island': 'U',
    'swamp': 'B',
    'mountain': 'R',
    'forest': 'G'
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
        for mana_type in ['W', 'U', 'B', 'R', 'G']:
            if self.pool[mana_type] - cost[mana_type] < 0:
                raise ManaError(mana_type)
            else:
                self.pool[mana_type] -= cost[mana_type]