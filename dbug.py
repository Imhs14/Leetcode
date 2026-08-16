"""
We are building the back-end for an online gaming platform. The system tracks
players and their match history. Each match result records the outcome from
that player's perspective.

Definitions:
* A "player" has: player_id, username.
* A "match result" has: player_id, opponent_id, outcome, score, timestamp.
* Outcome is one of: WIN, LOSS, DRAW.
* "GameManager" manages players and match results and provides player statistics.

To begin with, we present you with two tasks:
1-1) Read through and understand the code below. Feel free to run it.
1-2) The test for GameManager is not passing due to a bug in the code.
     Make the necessary changes to GameManager to fix the bug.
"""
"""
We are extending the platform to support recording match results
and computing per-player score statistics.

Each MatchResult represents one player's experience of a single match:
- player_id      : the player this record belongs to
- opponent_id    : the opponent in that match
- outcome        : one of WIN, LOSS, DRAW
- score          : the player's score in that match
- timestamp      : when the match was played

To implement these changes, we need to add two functions to the GameManager class:

2.1) The add_match_result function should be used to store a match result.
     Only the player_id is validated: if it does not refer to a known player in GameManager, the match result should be ignored. A match
     result with a known player_id must still be stored even when the opponent_id does not refer to a known player.

2.2) The get_average_score_by_outcome function should return a dictionary
     mapping each outcome (WIN, LOSS, DRAW) to the player's average score
     for that outcome. Only outcomes the player has at least one result
     for should appear in the dictionary. If the player has no match
     results at all, return an empty dictionary.

To assist you in testing these new functions, we have provided the
test_add_match_result and test_get_average_score_by_outcome tests.
"""

import unittest
from enum import Enum
from collections import defaultdict

class Outcome(Enum):
    WIN = "WIN"
    LOSS = "LOSS"
    DRAW = "DRAW"


class Player:
    def __init__(self, player_id, username):
        self.player_id = player_id
        self.username = username


class MatchResult:
    def __init__(self, player_id, opponent_id, outcome, score, timestamp):
        self.player_id = player_id
        self.opponent_id = opponent_id
        self.outcome = outcome
        self.score = score
        self.timestamp = timestamp


class PlayerStats:
    def __init__(self, total_matches, wins, win_rate):
        self.total_matches = total_matches
        self.wins = wins
        self.win_rate = win_rate


class GameManager:
    def __init__(self):
        self.players = {}        # player_id -> Player
        self.match_results = []  # list of MatchResult

    def add_player(self, player):
        self.players[player.player_id] = player

    def get_player_statistics(self, player_id):
        player_matches = [m for m in self.match_results
                         if m.player_id == player_id]

        total_matches = sum(1 for m in player_matches
                           if m.outcome in [Outcome.WIN, Outcome.LOSS])
        wins = sum(1 for m in player_matches
                  if m.outcome == Outcome.WIN)
        win_rate = wins / total_matches if total_matches > 0 else 0.0

        return PlayerStats(total_matches, wins, win_rate)
        

class TestSuite(unittest.TestCase):
    def test_get_player_statistics(self):
        print("Running test_get_player_statistics")
        gm = GameManager()
        gm.add_player(Player(1, "player1"))
        gm.add_player(Player(2, "player2"))

        gm.match_results.append(MatchResult(1, 2, Outcome.WIN,  80, 1000))
        gm.match_results.append(MatchResult(1, 2, Outcome.LOSS, 50, 2000))
        gm.match_results.append(MatchResult(1, 2, Outcome.DRAW, 60, 3000))
        gm.match_results.append(MatchResult(1, 2, Outcome.WIN,  90, 4000))

        stats = gm.get_player_statistics(1)
        print(stats.total_matches)
        self.assertEqual(4, stats.total_matches)
        self.assertEqual(2, stats.wins)
        self.assertAlmostEqual(0.5, stats.win_rate, places=4)

        gm.match_results.append(MatchResult(2, 1, Outcome.DRAW, 60, 1000))
        gm.match_results.append(MatchResult(2, 1, Outcome.DRAW, 60, 2000))

        stats2 = gm.get_player_statistics(2)
        self.assertEqual(2, stats2.total_matches)
        self.assertEqual(0, stats2.wins)
        self.assertAlmostEqual(0.0, stats2.win_rate, places=4)
        
    def test_add_match_result(self):
        print("Running test_add_match_result")
        gm = GameManager()
        gm.add_player(Player(1, "player1"))
        gm.add_player(Player(2, "player2"))
        
        gm.add_match_result(MatchResult(1, 2, Outcome.WIN, 80, 1000))
        gm.add_match_result(MatchResult(2, 1, Outcome.LOSS, 50, 1000))

        # unknown player ignored
        gm.add_match_result(MatchResult(99, 1, Outcome.WIN, 100, 2000))

        # known player, unregistered opponent -> still stored
        gm.add_match_result(MatchResult(1, 99, Outcome.WIN, 70, 3000))

        self.assertEqual(3, len(gm.match_results))


    def test_get_average_score_by_outcome(self):
        print("Running test_get_average_score_by_outcome")
        gm = GameManager()
        gm.add_player(Player(1, "player1"))
        gm.add_player(Player(2, "player2"))

        # match 1 - player1 wins
        gm.add_match_result(MatchResult(1, 2, Outcome.WIN,  80, 1000))
        gm.add_match_result(MatchResult(2, 1, Outcome.LOSS, 50, 1000))

        # match 2 - player1 wins again
        gm.add_match_result(MatchResult(1, 2, Outcome.WIN,  91, 2000))
        gm.add_match_result(MatchResult(2, 1, Outcome.LOSS, 60, 2000))

        # match 3 - draw
        gm.add_match_result(MatchResult(1, 2, Outcome.DRAW, 70, 3000))
        gm.add_match_result(MatchResult(2, 1, Outcome.DRAW, 70, 3000))

        avg1 = gm.get_average_score_by_outcome(1)
        self.assertAlmostEqual(85.5, avg1[Outcome.WIN],  places=4)  # (80+91)/2
        self.assertAlmostEqual(70.0, avg1[Outcome.DRAW], places=4)
        self.assertNotIn(Outcome.LOSS, avg1)                         # player1 has no losses

        avg2 = gm.get_average_score_by_outcome(2)
        self.assertAlmostEqual(55.0, avg2[Outcome.LOSS], places=4)  # (50+60)/2
        self.assertAlmostEqual(70.0, avg2[Outcome.DRAW], places=4)
        self.assertNotIn(Outcome.WIN, avg2)                          # player2 has no wins

        # player with no match results
        gm.add_player(Player(3, "player3"))
        self.assertEqual({}, gm.get_average_score_by_outcome(3))


if __name__ == "__main__":
    unittest.main()