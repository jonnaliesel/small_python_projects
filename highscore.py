highscores = {1: {}}

def save_highscore(game, highscore):
    user_name = str(list(highscore.keys())[0])
    score = int(list(highscore.values())[0])
    highscores[game][user_name] = score
    print(highscores[game])