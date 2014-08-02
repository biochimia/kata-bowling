import bowling
from nose.tools import eq_

testCases = {
    "XXXXXXXXXXXX": 300,
    "9-9-9-9-9-9-9-9-9-9-": 90,
    "5/5/5/5/5/5/5/5/5/5/5": 150,
}


def check_score(rolls, expectedScore):
    actualScore = bowling.calculateScore(rolls)
    eq_(actualScore, expectedScore)


def test_score():
    for rolls, expectedScore in testCases.items():
        yield check_score, rolls, expectedScore
