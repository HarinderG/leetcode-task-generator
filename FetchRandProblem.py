import requests
import random
import json
import sys


def getRandLeetCode(topic: str, paid: bool = False):
	data = {}

	# This header value is used in the request to fetch personal progress.
	from const import USER_COOKIE, difficulties
	# TODO Add instructions on how to obtain this

	response = requests.get('https://leetcode.com/api/problems/' + topic, cookies = USER_COOKIE).json()

	problem_list = response['stat_status_pairs']

	# Pick an unsolved problem
	problem = random.choice(problem_list)
	while problem['status'] == 'ac' or (problem['paid_only'] != paid and paid != None):
		problem = random.choice(problem_list)

	# Build json response
	data['user'] = response['user_name']
	data['url'] = (f'https://leetcode.com/problems/{problem["stat"]["question__title_slug"]}')
	data['difficulty'] = difficulties[problem['difficulty']['level']-1]
	data['paid'] = problem['paid_only']
	data['progress'] = {
		'easy': response['ac_easy'],
		'medium': response['ac_medium'],
		'hard': response['ac_hard']
	}

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
