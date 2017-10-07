from pythonthegathering import ManaPool, spell

pool = ManaPool()

@spell('WBB')
def boop(x):
    print(x)

pool.tap('plains').tap('swamp').tap('swamp')
boop('boop', mana_pool=pool, mana_pay={'W': 1, 'B': 2})
