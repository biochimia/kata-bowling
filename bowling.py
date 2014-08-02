#!/usr/bin/env python


def calculateScore(rolls):
    """Produces the total score for a single line of American Ten-Pin Bowling.

    rolls is a string, assumed to be a valid sequence for the game, where:
        'X' indicates a strike
        '/' indicates a spare
        '-' indicates a miss
        [1-9] otherwise, indicate the number of knocked pins on a given roll
    """

    runningScore = 0

    # Incremented by 2 for strikes, one for other rolls; divide by 2 for actual
    # frame count
    frameCount = 0

    # Keep count of knocked pins for scoring spares
    previousKnockedPins = 0
    knockedPins = 0

    # Spares and strikes influence multiplier for subsequent rolls (current,
    # next and after)
    rollMultipliers = [1, 1, 1]

    for roll in rolls:
        frameCount += 1
        if roll == 'X':
            frameCount += 1
            knockedPins = 10
            if frameCount < 20:
                rollMultipliers[1] += 1
                rollMultipliers[2] += 1
        elif roll == '/':
            knockedPins = 10 - previousKnockedPins
            if frameCount < 20:
                rollMultipliers[1] += 1
        elif roll == '-':
            knockedPins = 0
        else:
            knockedPins = int(roll)

        multiplier = rollMultipliers.pop(0)
        rollMultipliers.append(1)
        previousKnockedPins = knockedPins

        runningScore += multiplier * knockedPins

    return runningScore


if __name__ == '__main__':
    import fileinput

    for line in fileinput.input():
        line = line.strip()
        score = calculateScore(line)

        print("Input: %s" % line)
        print("Score: %d" % score)
