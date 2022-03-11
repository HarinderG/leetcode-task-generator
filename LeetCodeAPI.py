import requests
import random
import json
import sys

# TODO Make sure session cookie matches username in case session expires

def getUserName(SESSION_COOKIE):
	return requests.get(
		'https://leetcode.com/api/problems/algorithms', cookies=SESSION_COOKIE).json()['user_name']


def getProgress(SESSION_COOKIE):
	difficulties = ['easy', 'medium', 'hard']
	response = requests.get(
		'https://leetcode.com/api/problems/algorithms', cookies=SESSION_COOKIE).json()
	return {'easy': response['ac_easy'], 'medium': response['ac_medium'], 'hard': response['ac_hard']}

