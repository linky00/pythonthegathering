from .mana_pool import MANA_TYPES

class PayError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

def spell(mana_cost):
    """
    Decorator function to create spells!
    """
    def decorator(func):
        def wrap(*args, **kwargs):
            mana_pool = kwargs['mana_pool']
            pay = kwargs['mana_pay']
            kwargs.pop('mana_pool')
            kwargs.pop('mana_pay')

            cost = {}
            temp_mana_cost = mana_cost
            for mana_type in MANA_TYPES:
                cost[mana_type] = temp_mana_cost.count(mana_type)
                temp_mana_cost = temp_mana_cost.replace(mana_type, '')
            if temp_mana_cost != '':
                cost['generic'] = int(temp_mana_cost)
            else:
                cost['generic'] = 0

            generic_paid = 0
            temp_pay = dict(pay)
            for mana_type in MANA_TYPES:
                if mana_type in temp_pay:
                    temp_pay[mana_type] -= cost[mana_type]
                    if temp_pay[mana_type] < 0:
                        raise PayError("Not paying enough " + mana_type + "!")
                    generic_paid += temp_pay[mana_type]
            if generic_paid == cost['generic']:
                mana_pool.spend(pay)
            elif generic_paid > cost['generic']:
                raise PayError("Paying too much generic mana!")
            else:
                raise PayError("Not paying enough for generic mana!")

            func(*args, **kwargs)
        return wrap
    return decorator
