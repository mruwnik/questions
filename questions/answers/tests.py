from django.test import TestCase
from django.urls import reverse

from answers.models import Question


class QuestionViewTests(TestCase):

    def test_no_questions(self):
        """Check that an empty list is returned when no questions are available."""
        response = self.client.get(reverse('questions_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"questions": []})

    def test_questions(self):
        """Check that a correct list is returned when questions are available."""
        for q in ["question 1", "question 2", "question 3", "question 4"]:
            Question(content=q).save()

        response = self.client.get(reverse('questions_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"questions": [
            {'id': 1, 'content': "question 1"},
            {'id': 2, 'content': "question 2"},
            {'id': 3, 'content': "question 3"},
            {'id': 4, 'content': "question 4"},
        ]})

    def test_filter_questions(self):
        """Check that a correct list is returned when questions are filtered."""
        for q in ["question 1", "QuEsTiOn 2", "bla bla", "blaquest"]:
            Question(content=q).save()

        def check_query(search, expected):
            response = self.client.get(reverse('questions_list') + search + '/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"questions": expected})

        check_query('question', [
            {'id': 1, 'content': "question 1"},
            {'id': 2, 'content': "QuEsTiOn 2"},
        ])
        check_query('bla', [
            {'id': 3, 'content': "bla bla"},
            {'id': 4, 'content': "blaquest"},
        ])
        check_query('ques', [
            {'id': 1, 'content': "question 1"},
            {'id': 2, 'content': "QuEsTiOn 2"},
            {'id': 4, 'content': "blaquest"},
        ])
