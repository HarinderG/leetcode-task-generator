import requests as req
import random

# This header value is used in the request to fetch personal progress.
from const import USER_COOKIE
# TODO Add instructions on how to obtain this

res = req.get('https://leetcode.com/api/problems/algorithms/', headers={'cookie': USER_COOKIE}).json()
# TODO: Add option to switch between topics: [algorithms, database, concurrency, etc..]

# For debugging
print(res['user_name'])
# TODO Display current progress

problem_list = res['stat_status_pairs']

# Pick an unsolved problem
# TODO Add option to filter out paid only probs
# TODO Display difficulty level
problem = random.choice(problem_list)
while problem['status'] == 'ac':
    print(f'You have alread completed: {problem["stat"]["question__title_slug"]}')
    problem = random.choice(problem_list)

print(f'Link: https://leetcode.com/problems/{problem["stat"]["question__title_slug"]}')
