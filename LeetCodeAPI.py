import requests
import random
import json
import sys

# TODO Make sure session cookie matches username in case session expires

def getUserName(SESSION_COOKIE):
	return requests.get('https://leetcode.com/api/problems/algorithms', cookies=SESSION_COOKIE).json()['user_name']
		

def getProgress(SESSION_COOKIE):
	response = requests.get('https://leetcode.com/api/problems/algorithms', cookies=SESSION_COOKIE).json()
	return {'easy': response['ac_easy'], 'medium': response['ac_medium'], 'hard': response['ac_hard']}

def getRandomProblem(SESSION_COOKIE, topic = 'algorithms', paid = False, difficulty = 'any'):
	data = {}
	difficulties = ['easy', 'medium', 'hard']

	response = requests.get('https://leetcode.com/api/problems/' + topic, cookies=SESSION_COOKIE).json()

	problem_list = response['stat_status_pairs']

	# Pick an unsolved problem
	problem = random.choice(problem_list)
	while problem['status'] == 'ac' or (problem['paid_only'] != paid and paid != None) or (difficulty != 'any' and difficulties[problem['difficulty']['level']-1] != difficulty):
		problem = random.choice(problem_list)

	# Build json response
	data['title'] = problem['stat']['question__title']
	data['url'] = (f'https://leetcode.com/problems/{problem["stat"]["question__title_slug"]}')
	data['difficulty'] = difficulties[problem['difficulty']['level']-1]
	data['category'] = response['category_slug']
	data['paid'] = problem['paid_only']

	return data
