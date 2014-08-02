import bowling
from nose.tools import eq_

testCases = {
    "XXXXXXXXXXXX": 300,
    "9-9-9-9-9-9-9-9-9-9-": 90,
    "5/5/5/5/5/5/5/5/5/5/5": 150,
    "--------------------": 0,
    "------X------------": 10,
    "11111111111111111111": 20,
    "12121212121212121212": 30,
    "9/9/9/9/9/9/9/9/9/9/9": 190,
    "1/------------------": 10,
    "1/X----------------": 30,
    "1/X5---------------": 40,
    "X------------------": 10,
    "X1-----------------": 12,
    "X1/5---------------": 40,
    "X111111111111111111": 30,
}


def check_score(rolls, expectedScore):
    actualScore = bowling.calculateScore(rolls)
    eq_(actualScore, expectedScore)


def test_score():
    for rolls, expectedScore in testCases.items():
        yield check_score, rolls, expectedScore
