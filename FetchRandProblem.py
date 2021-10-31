import requests
import random
import json


def getRandLeetCode():
	data = {}

	# This header value is used in the request to fetch personal progress.
	from const import USER_COOKIE
	# TODO Add instructions on how to obtain this

	response = requests.get('https://leetcode.com/api/problems/algorithms/', headers={'cookie': USER_COOKIE}).json()
	# TODO: Add option to switch between topics: [algorithms, database, concurrency, etc..]

	# For debugging
	data['user'] = response['user_name']
	# TODO Display current progress

	problem_list = response['stat_status_pairs']

	# Pick an unsolved problem
	# TODO Add option to filter out paid only probs
	# TODO Display difficulty level
	problem = random.choice(problem_list)
	while problem['status'] == 'ac':
		print(f'You have alread completed: {problem["stat"]["question__title_slug"]}')
		problem = random.choice(problem_list)

	data['url'] = (f'https://leetcode.com/problems/{problem["stat"]["question__title_slug"]}')

	return json.dumps(data)


def main():
	print(getRandLeetCode())


if __name__ == "__main__":
	main()
