import unittest
import LeetCodeAPI as api
import json

settings = json.load(open('settings.json', 'r'))
username = settings['USER_NAME']
cookie = settings['SESSION_COOKIE']

class TestAPI(unittest.TestCase):

    def test_username(self):
        self.assertEqual(api.getUserName(cookie), username)


    def test_difficulty(self):
        self.assertEqual(api.getRandomProblem(cookie, 'algorithms', False, 'easy')[
                'difficulty'], 'easy')
        self.assertEqual(api.getRandomProblem(cookie, 'algorithms', False, 'medium')[
                'difficulty'], 'medium')
        self.assertEqual(api.getRandomProblem(cookie, 'algorithms', False, 'hard')[
                'difficulty'], 'hard')


    def test_category(self):
        self.assertEqual(api.getRandomProblem(cookie)['category'], 'algorithms')
        self.assertEqual(api.getRandomProblem(cookie, topic='algorithms')[
                'category'], 'algorithms')
        self.assertEqual(api.getRandomProblem(cookie, topic='database')['category'], 'database')
        self.assertEqual(api.getRandomProblem(cookie, topic='shell')['category'], 'shell')
        self.assertEqual(api.getRandomProblem(cookie, topic='concurrency')[
                'category'], 'concurrency')


    def test_paid(self):
        self.assertEqual(api.getRandomProblem(cookie)['paid'], False)
        self.assertEqual(api.getRandomProblem(cookie, paid=True)['paid'], True)
        self.assertEqual(api.getRandomProblem(cookie, paid=False)['paid'], False)


if __name__ == '__main__':
    unittest.main()