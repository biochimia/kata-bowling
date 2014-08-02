#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG)


def frameDescription(frameCount):
    """Returns a user-friendly description for a given frame count, as used in
    calculateScore().
    """
    if frameCount > 20:
        return "Extra ball"

    frameCount -= 1
    frame = frameCount / 2 + 1
    roll = frameCount % 2 + 1

    return "Frame %i, roll %i" % (frame, roll)


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

    # Spares and strikes influence multiplier for subsequent rolls
    rollMultipliers = [1] * 22

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
        previousKnockedPins = knockedPins

        runningScore += multiplier * knockedPins
        logging.debug(
            "%s: knocked %i pins, running score %i",
            frameDescription(frameCount), knockedPins, runningScore)

    return runningScore


if __name__ == '__main__':
    import fileinput

    for line in fileinput.input():
        line = line.strip()
        score = calculateScore(line)

        print("Input: %s" % line)
        print("Score: %d" % score)
