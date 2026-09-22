Computers can't generate _truly_ random numbers on demand, they use a deterministic algorithm that produces numbers which _look_ random, called a pseudo-random number generator (PRNG). The "seed" is the starting input to that algorithm. 



Same seed -&gt; same exact sequence of "random" numbers every time, even though the sequence looks random. 



This is huge for reproducibility - if you're testing your code, or writing a research pipeline, you want to be able to rerun something and get the exact same "random" result. Without setting the seed, you get a different array every run.



**Uniform Distribution**

A uniform distribution over [0, 1) means every value in that range is equally likely to come up - no value is more probable than any other, and it's flat across the whole interval.



**Normal Distribution - "mean zero, std one"**

This is a completely different shape of randomness, the classic bell curve. Instead of every value being equally likely, values cluster around the mean (0 here) and get rarer the further you go from it, with the standard deviation (1 here) controlling how spread out that clustering is. 

"Standard normal" specifically means mean=0, std=1, the canonical/default version of the normal distribution, often written N(0,1)



std = 1 - on average, values tend to sit about 1 unit away from the mean.



**Why it matters for ML**

I've heard of "weight initialization" before, this is exactly wwhat that is. Initializing a neural network's weights isn't just "any randomness will do" - uniform vs. normal initialization, and the specific spread/scale used, genuinely affects how well a network trains

Too large or oddly-distributed initial weights can cause vanishing/exploding gradients early in training.

So this problem, while simple-looking, is directly practicing the mechanism behind a real, consequential ML decision.



Since for this problem I need the output to be a **2D array** of a given shape (like (rows, cols)), not just a flat list of numbers, I need to accept a shape tuple and fill an array of that shape.