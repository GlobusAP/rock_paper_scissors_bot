import random

from lexicon.lexicon_ru import rock_paper_scissors


def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


def get_winner(user_choice: str, bot_choice: str):
    user_choice = rock_paper_scissors[user_choice]
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    if rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'
