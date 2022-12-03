"""
Advent of Code 2022
Day 02
"""
with open('input.txt', 'r') as file:
    game_strategy = file.read()

# part 1
shape_score = {'X': 1,
               'Y': 2,
               'Z': 3}

outcome_score = {'A Y': 6, 'B Z': 6, 'C X': 6,
                 'A X': 3, 'B Y': 3, 'C Z': 3,
                 'A Z': 0, 'B X': 0, 'C Y': 0}

game_score = 0
for game in game_strategy.strip().split('\n'):
    game_score += outcome_score[game] + shape_score[game[2]]


# part 2
result_lookup = {'X': 0,
                 'Y': 3,
                 'Z': 6}

real_game_score = 0
for game in game_strategy.strip().split('\n'):
    print(game)
    # get overall game outcome score
    game_result_score = result_lookup[game[2]]
    game_result = {score for score in outcome_score if (outcome_score[score] == game_result_score)}
    play_move = [move[2] for move in list(game_result) if move.startswith(game[0])]
    # get play move score
    play_move_score = shape_score[play_move[0]]
    real_game_score += (game_result_score + play_move_score)


