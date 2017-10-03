from stuff.mana_pool import ManaPool

class Player:
    def __init__(self):
        self.mana_pool = ManaPool()

    def cast(self, spell, *args, **kwargs):
        docstring = spell.__doc__
        cost = {}
        for mana_type in ['W', 'U', 'B', 'R', 'G']:
            cost[mana_type] = docstring.count(mana_type)
            docstring = docstring.replace(mana_type, '')
        generic_cost = int(docstring)
        spell(*args, **kwargs)

def func(thingy):
    """2BB"""
    print(thingy)

player = Player()
player.cast(func, 'boop')
