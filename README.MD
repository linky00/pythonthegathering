# Python the Gathering

Hey you! Is Python too easy to use? Are functions just a bit too convenient? Do you feel the need to inject some Magic the Gathering into your coding experience? Well, here's your 'solution'! (an actual solution would probably involve therapy and hugs)

Oh yeah, if you don't actually play Magic, this is gonna get way too complicated way too fast. So... go learn it :grin:

First, lets import our module! Until this is on pip, you'll just have to throw this folder into your project; it should work out fine.
```python
from pythonthegathering import ManaPool, spell
```
Now, lets make ourselves a ManaPool. This stores our mana, which we need to cast 'spells'.
```python
pool = ManaPool()
```
Nice! Next, let's get make a spell. This is just a function with a decorator, but I'm calling it a spell from now on because if I don't, who will?
```python
@spell('3UB')
def square(x):
	return x**2 
```
See that '3UB'? That means 'a blue (U), a black (B), and 3 generic mana'. In case you didn't know, 'U' in magic stands for 'blue', because 'B' is taken by 'black' and 'L' is taken by 'land'.

Anway, this is all great. But how do we cast this spell? Well, first, we'll have to generate the mana. Let's generate the extra 3 mana using the other three colours, so I can show you all the lands you can tap!
```python
pool.tap('plains')
pool.tap('island')
pool.tap('swamp')
pool.tap('mountain')
pool.tap('forest')
```
Since tap() returns itself, we can also do:
```python
pool.tap('plains').tap('island').tap('swamp').tap('mountain').tap('forest')
```
But that's beside the point.

Let's finally get round to casting this spell! Just call the spell like any other function, but remember to add mana_pool and mana_pay as keyword arguements.
```python
square(4, mana_pool=pool, mana_pay={'W': 1, 'U': 1, 'B': 1, 'R': 1, 'G': 1})
```
mana_pool is pretty simple, but what's going on with mana_pay? Basically, mana_pay is the way in which we would like to spend our mana. Say I wanted to pay for the generic mana using 3 more black mana, I would do it in this way:
```python
square(4, mana_pool=pool, mana_pay={'U': 1, 'B': 4})
```
Of course, you'd need an additional 3 swamps tapped to do this, but I'm sure you figured that out. The important question is, what does this function return?
```python
16
```
Yay! It worked! Anway, feel free to shove this into your projects if you're that insane or whatever. Have a good day, and enjoy!

Oh, P.S., I had the idea for this in a dream after a long night of coding whilst shuffling my awesome standard deck which you should absolutely check out [here](http://tappedout.net/mtg-decks/black-blue-scarab-dude-control-feat-zombies/).