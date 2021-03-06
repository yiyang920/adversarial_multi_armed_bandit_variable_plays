import random

# draw: [float] -> int
# pick an index from the given list of floats proportionally
# to the size of the entry (i.e. normalize to a probability
# distribution and draw according to the probabilities).
def draw(weights):
    choice = random.uniform(0, sum(weights))
    choiceIndex = 0

    for weight in weights:
        choice -= weight
        if choice <= 0:
            return choiceIndex

        choiceIndex += 1


# distr: [float] -> (float)
# Normalize a list of floats to a probability distribution.  Gamma is an
# egalitarianism factor, which tempers the distribtuion toward being uniform as
# it grows from zero to one.
def distr(weights, gamma=0.0):
    theSum = float(sum(weights))
    return [(1.0 - gamma) * (w / theSum) + (gamma / len(weights)) for w in weights]


# distr_multiPlays: [float] -> (float)
# Normalize a list of floats to a probability distribution.  Gamma is an
# egalitarianism factor, which tempers the distribtuion toward being uniform as
# it grows from zero to one.
def distr_multiPlays(weights, numPlays, gamma=0.0):
    theSum = float(sum(weights))
    return [
        numPlays * ((1.0 - gamma) * (w / theSum) + (gamma / len(weights)))
        for w in weights
    ]


def mean(aList):
    theSum = 0
    count = 0

    for x in aList:
        theSum += x
        count += 1

    return 0 if count == 0 else theSum / count
