#!/usr/bin/env python


def calculateScore(rolls):
    """Produces the total score for a single line of American Ten-Pin Bowling.

    rolls is a string, assumed to be a valid sequence for the game, where:
        'X' indicates a strike
        '/' indicates a spare
        '-' indicates a miss
        [1-9] otherwise, indicate the number of knocked pins on a given roll
    """
    return -1


if __name__ == '__main__':
    import fileinput

    for line in fileinput.input():
        line = line.strip()
        score = calculateScore(line)

        print("Input: %s" % line)
        print("Score: %d" % score)
