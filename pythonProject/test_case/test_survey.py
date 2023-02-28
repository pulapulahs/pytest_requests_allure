import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_single_response(self):
        question = "你的母语是啥"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        question = "你的母语是啥"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Chinese']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()