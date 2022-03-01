import requests
import random
import json
import sys


def getRandLeetCode(topic: str):
	data = {}

	# This header value is used in the request to fetch personal progress.
	from const import USER_COOKIE
	# TODO Add instructions on how to obtain this

	response = requests.get('https://leetcode.com/api/problems/' + topic, cookies = USER_COOKIE).json()
		
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
	topics = ['algorithms', 'database', 'shell', 'concurrency']

	# TODO Add option to give custom set
	if len(sys.argv) > 1 and sys.argv[1] in topics:
		print(getRandLeetCode(sys.argv[1]))
	elif len(sys.argv) > 1 and sys.argv[1] == 'any':
		print(getRandLeetCode(random.choice(topics)))
	else:
		print(getRandLeetCode('algorithms'))


if __name__ == "__main__":
	main()
