from stuff.mana_pool import ManaPool

def spell(mana_cost):
    def decorator(func):
        def wrap(*args, **kwargs):
            mana_pool = kwargs['mana_pool']
            kwargs.pop('mana_pool')
            cost = {}
            temp_mana_cost = mana_cost
            for mana_type in ['W', 'U', 'B', 'R', 'G']:
                cost[mana_type] = temp_mana_cost.count(mana_type)
                temp_mana_cost = temp_mana_cost.replace(mana_type, '')
            cost['generic'] = int(temp_mana_cost)
            print(cost)
            func(*args, **kwargs)
        return wrap
    return decorator

my_pool = ManaPool()

@spell("2BB")
def func(thingy):
    print(thingy)

func('boop')