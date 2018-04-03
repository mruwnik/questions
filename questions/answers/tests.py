from django.test import TestCase
from django.urls import reverse

from answers.models import Question, Category


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
            response = self.client.get(reverse('questions_filter', args=[search]))
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


class CategoryViewTests(TestCase):

    question = Question(content='question')
    other_question = Question(content='question 2')

    def test_no_categories(self):
        """Check that an empty list is returned when no categories are available."""
        self.question.save()

        response = self.client.get(reverse('categories', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'question': 1, 'parent': None, 'categories': [], 'title': self.question.content, 'answers': []
        })

        cat = Category(title='asd', question=self.question)
        cat.save()
        response = self.client.get(reverse('category', args=[self.question.id, cat.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {'question': 1, 'parent': cat.parent_id, 'categories': [], 'title': cat.title, 'answers': []}
        )

    def test_id_validation(self):
        """Check whether ids get correctly validated."""
        self.question.save()
        cat = Category(title='asd', question=self.question)
        cat.save()

        # check that an non existant parent category raises a 404
        response = self.client.get(reverse('category', args=[self.question.id, 123]))
        self.assertEqual(response.status_code, 404)

        # check that a non existant question raises a 404
        response = self.client.get(reverse('categories', args=[124]))
        self.assertEqual(response.status_code, 404)

        # check that a non existant question raises a 404 even when a valid parent is provided
        response = self.client.get(reverse('category', args=[124, cat.id]))
        self.assertEqual(response.status_code, 404)

    def test_get_cat_no_parent(self):
        """Check if getting categories without providing the parent works,"""
        self.question.save()
        self.other_question.save()

        for cat in ['cat 1', 'cat 2', 'cat 3']:
            cat = Category(question=self.question, title=cat)
            cat.save()

        # add a sub category - this should be ignored
        Category(question=self.question, title='sub cat', parent=cat).save()
        # add a category for a different question
        Category(question=self.other_question, title='sub cat').save()

        response = self.client.get(reverse('categories', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'question': 1,
            'parent': None,
            'title': self.question.content,
            'answers': [],
            'categories': [{'id': 1, 'title': 'cat 1'}, {'id': 2, 'title': 'cat 2'}, {'id': 3, 'title': 'cat 3'}]
        })

    def test_get_cat_parent(self):
        """Check if getting categories when providing the parent works,"""
        self.question.save()
        self.other_question.save()

        # add a sub category - this should be ignored
        parent = Category(question=self.question, title='parent cat')
        parent.save()

        for cat in ['cat 1', 'cat 2', 'cat 3']:
            cat = Category(question=self.question, title=cat, parent=parent)
            cat.save()

        # add a category for a different question
        Category(question=self.other_question, title='sub cat').save()

        response = self.client.get(reverse('category', args=[self.question.id, parent.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'question': 1,
            'parent': parent.parent_id,
            'title': 'parent cat',
            'answers': [],
            'categories': [{'id': 2, 'title': 'cat 1'}, {'id': 3, 'title': 'cat 2'}, {'id': 4, 'title': 'cat 3'}]
        })
