from django.test import TestCase, Client
from spanglish.tests.factories import LanguageFactory #, CategoryFactory #, WordFactory, SentenceFactory, TranslationFactory, VerbFactory

class LanguageListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_languages(self):
        LanguageFactory(name='English')
        LanguageFactory(name='Spanish')

        response = self.client.get('/spanglish/language/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        expected_response = [
            {
                "id": 1,
                "name": "English"
            },
            {
                "id": 2,
                "name": "Spanish"
            }
        ]
        self.assertEqual(response.json(), expected_response)

    def test_post_language(self):
        response = self.client.post('/spanglish/language/', {"name": "French"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'id': 3, 'name': 'French'})
