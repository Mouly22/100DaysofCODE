we can use random module for these following tasks:
To play a game of chance where the computer needs to throw some dice, pick a number, or flip a coin,
To shuffle a deck of playing cards randomly,
To randomly allow a new enemy spaceship to appear and shoot at you,
To simulate possible rainfall when we make a computerized model for estimating the environmental impact of building a dam,
For encrypting your banking session on the Internet.

```
import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)
```

The randrange function generates an integer between its lower and upper argument where the lower bound is included, but the upper bound is excluded. So, randrange(1,7) will include numbers from 1-6. If you omit the first parameter it is assumed to be 0 so randrange(10) will give you numbers from 0-9. All the values have an equal probability of occurring (i.e. the results are uniformly distributed).

The random() function returns a floating point number in the range [0.0, 1.0) — the square bracket means “closed interval on the left” and the round parenthesis means “open interval on the right”. In other words, 0.0 is possible, but all returned numbers will be strictly less than 1.0. It is usual to scale the results after calling this method, to get them into a range suitable for your application.

```
import random

prob = random.random()
result = prob * 5
print(result)
```
In the case, we’ve converted the result of the method call to a number in the range [0.0, 5.0). Once more, these are uniformly distributed numbers — numbers close to 0 are just as likely to occur as numbers close to 3, or numbers close to 5. If you continue to press the run button you will see random values between 0.0 and up to but not including 5.0.

It is important to note that random number generators are based on a deterministic algorithm — repeatable and predictable. So they’re called pseudo-random generators — they are not genuinely random. They start with a seed value. Each time you ask for another random number, you’ll get one based on the current seed attribute, and the state of the seed (which is one of the attributes of the generator) will be updated. The good news is that each time you run your program, the seed value is likely to be different meaning that even though the random numbers are being created algorithmically, you will likely get random behavior each time you execute.
