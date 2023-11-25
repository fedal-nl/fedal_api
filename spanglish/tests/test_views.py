from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from api.tests.factories import UserFactory
from spanglish.tests.factories import (
    LanguageFactory,
    CategoryFactory,
    WordFactory,
    SentenceFactory,
    VerbFactory,
    TranslationWordFactory,
    TranslationSentenceFactory
 )


class LanguageViewsTest(TestCase):
    def setUp(cls):
        cls.user = UserFactory()
        cls.client = APIClient()
        cls.token = str(RefreshToken.for_user(cls.user).access_token)  # Generate token
        LanguageFactory(name='English')
        LanguageFactory(name='Spanish')

    def test_get_languages(self):
        """Test that the languages are returned correctly"""

        response = self.client.get('/spanglish/language/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        response_languages = {language['name'] for language in response.json()}
        expected_languages = {'English', 'Spanish'}
        self.assertEqual(response_languages, expected_languages)

    def test_post_language_success(self):
        # excpet a 201 response because the user is authenticated and the language is created
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/language/', {"name": "French"})
        self.assertEqual(response.status_code, 201)

    def test_post_language_401(self):
        # excpet a 401 response because the user is not authenticated

        response = self.client.post('/spanglish/language/', {"name": "French"})
        self.assertEqual(response.status_code, 401)

    def test_post_language_400(self):
        # excpet a 400 response because the user is authenticated but the language is not created
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/language/', {"name": ""})
        self.assertEqual(response.status_code, 400)

    def test_category_list_view(self):
        # excpet a 200 response because the user is authenticated and the language is created
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get('/spanglish/category/')
        self.assertEqual(response.status_code, 200)

class CategoryViewsTest(TestCase):
    def setUp(cls):
        cls.user = UserFactory()
        cls.client = APIClient()
        cls.token = str(RefreshToken.for_user(cls.user).access_token)  # Generate token
        CategoryFactory(name='Food')
        CategoryFactory(name='Animals')

    def test_get_categories(self):
        """Test that the categories are returned correctly"""

        response = self.client.get('/spanglish/category/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        response_categories = {category['name'] for category in response.json()}
        expected_categories = {'Food', 'Animals'}
        self.assertEqual(response_categories, expected_categories)

    def test_post_category_success(self):
        # excpet a 201 response because the user is authenticated and the category is created
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/category/', {"name": "Colors"})
        self.assertEqual(response.status_code, 201)

    def test_post_category_401(self):
        # excpet a 401 response because the user is not authenticated

        response = self.client.post('/spanglish/category/', {"name": "Colors"})
        self.assertEqual(response.status_code, 401)

    def test_post_category_400(self):
        # excpet a 400 response because the user is authenticated but the category is not created
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/category/', {"name": ""})
        self.assertEqual(response.status_code, 400)
    
class WordViewsTest(TestCase):
    def setUp(cls):
        cls.user = UserFactory()
        cls.client = APIClient()
        cls.token = str(RefreshToken.for_user(cls.user).access_token)  # Generate token
        LanguageFactory(name='English')
        cls.language = LanguageFactory(name='Spanish')
        cls.category_food = CategoryFactory(name='Food')
        category_days = CategoryFactory(name='Days')
        WordFactory(text='manzana', language=cls.language, category=cls.category_food)
        WordFactory(text='lunes', language=cls.language, category=category_days)

    def test_get_words(self):
        """Test that the words are returned correctly"""

        response = self.client.get('/spanglish/word/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        response_words = {word['text'] for word in response.json()}
        expected_words = {'manzana', 'lunes'}
        self.assertEqual(response_words, expected_words)

    def test_post_word_no_category_400(self):
        # excpet a 400 response because there is no category

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/word/', {"text": "orange"})
        expected_response = {'category': ['This field is required.']}
        self.assertEqual(response.json(), expected_response)
        self.assertEqual(response.status_code, 400)

    def test_post_word_success_201(self):
        # excpet a 201 response because the language and category are provided

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(
            '/spanglish/word/', {
                "text": "naranja", 
                "category": self.category_food.pk, 
                "language": self.language.pk
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_post_word_401(self):
        # excpet a 401 response because the user is not authenticated

        response = self.client.post('/spanglish/word/', {"text": "orange"})
        self.assertEqual(response.status_code, 401)

    def test_post_word_400(self):
        # excpet a 400 response because the user is authenticated but the word is not created
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/word/', {"text": ""})
        self.assertEqual(response.status_code, 400)

class SentenceViewsTest(TestCase):
    def setUp(cls):
        cls.user = UserFactory()
        cls.client = APIClient()
        cls.token = str(RefreshToken.for_user(cls.user).access_token)  # Generate token
        cls.language = LanguageFactory(name='Spanish')
        cls.category_greeting = CategoryFactory(name='Greeting')
        CategoryFactory(name='Days')
        SentenceFactory(text='Como estas ?', language=cls.language, category=cls.category_greeting)
        SentenceFactory(text='Buenos dias', language=cls.language, category=cls.category_greeting)

    def test_get_sentence(self):
        """Test that the sentences are returned correctly"""

        response = self.client.get('/spanglish/sentence/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        response_sentence = {sentence['text'] for sentence in response.json()}
        expected_sentence = {'Como estas ?', 'Buenos dias'}
        self.assertEqual(response_sentence, expected_sentence)

    def test_post_sentence_no_category_400(self):
        # excpet a 400 response because there is no category

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/sentence/', {"text": "Por que no?"})
        expected_response = {'category': ['This field is required.']}
        self.assertEqual(response.json(), expected_response)
        self.assertEqual(response.status_code, 400)
    
    def test_post_sentence_success_201(self):
        # excpet a 201 response because the language and category are provided

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(
            '/spanglish/sentence/', {
                "text": "Por que no?", 
                "category": self.category_greeting.pk, 
                "language": self.language.pk
            }
        )
        self.assertEqual(response.status_code, 201)

class VerbViewsTest(TestCase):
    def setUp(cls):
        cls.user = UserFactory()
        cls.client = APIClient()
        cls.token = str(RefreshToken.for_user(cls.user).access_token)  # Generate token
        cls.language = LanguageFactory(name='Spanish')
        cls.category_verb = CategoryFactory(name='Verbs')
        cls.category_greeting = CategoryFactory(name='Greetings')
        VerbFactory(tense='SIMPLE_PRESENT', word=WordFactory(text='hablar', language=cls.language, category=cls.category_verb))
        VerbFactory(tense='SIMPLE_PRESENT', word=WordFactory(text='comer', language=cls.language, category=cls.category_verb))
        VerbFactory(tense='SIMPLE_PRESENT', word=WordFactory(text='vivir', language=cls.language, category=cls.category_verb))

    def test_get_verb(self):
        """Test that the verbs are returned correctly"""

        response = self.client.get('/spanglish/verb/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        response_verb = {verb['word'] for verb in response.json()}
        expected_verb = {'hablar', 'comer', 'vivir'}
        self.assertEqual(response_verb, expected_verb)

    def test_post_verb_success_201(self):
        # excpet a 201 response

        word = WordFactory(text='ser', language=self.language, category=self.category_verb)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/verb/', {
            "tense": "SIMPLE_PRESENT",
            "word": word.pk,
            "yo": "voy",
            "tu": "vas",
            "usted": "va",
            "nosotros": "vamos",
            "vosotros": "vais",
            "ustedes": "van"
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_post_verb_category_word_greeting(self):
        # excpet a 400 response becausse the category is not Verbs

        word = WordFactory(text='Hola', language=self.language, category=self.category_greeting)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/verb/', {
            "tense": "SIMPLE_PRESENT",
            "word": word.pk,
            "yo": "voy",
            "tu": "vas",
            "usted": "va",
            "nosotros": "vamos",
            "vosotros": "vais",
            "ustedes": "van"
            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'non_field_errors': ['Word category must be Verbs']})

class TransationViewsTest(TestCase):
    def setUp(cls):
        cls.user = UserFactory()
        cls.client = APIClient()
        cls.token = str(RefreshToken.for_user(cls.user).access_token)  # Generate token
        cls.language_es = LanguageFactory(name='Spanish')
        cls.language_en = LanguageFactory(name='English')
        cls.category_food = CategoryFactory(name='Food')
        cls.category_greeting = CategoryFactory(name='Greeting')
        word = WordFactory(text='manzana', language=cls.language_es, category=cls.category_food)
        sentence = SentenceFactory(text='Como estas ?', language=cls.language_es, category=cls.category_greeting)
        TranslationWordFactory(word=word, language=cls.language_en, translation=['apple'])
        TranslationSentenceFactory(sentence=sentence, language=cls.language_en, translation=['How are you ?'])

    def test_get_translation(self):
        """Test that the translations are returned correctly"""

        response = self.client.get('/spanglish/translation/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        # self.assertEqual(response.json()[0], {})
        response_translation_word = [translation['word'] for translation in response.json()]
        response_translation_sentence = [translation['sentence'] for translation in response.json()]
        response_translation = [translation['translation'] for translation in response.json()]
        expected_translation = [['apple'], ['How are you ?']]
        expected_translation_word = ['manzana', None]
        expected_translation_sentence = [None, 'Como estas ?']
        
        self.assertEqual(response_translation, expected_translation)
        self.assertEqual(response_translation_word, expected_translation_word)
        self.assertEqual(response_translation_sentence, expected_translation_sentence)

    def test_post_translation_word_success_201(self):
        # excpet a 201 response

        word = WordFactory(text='naranja', language=self.language_es, category=self.category_food)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/translation/', {
            "word": word.pk,
            "language": self.language_en.pk,
            "sentence": "",
            "translation": ['orange']
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_post_translation_sentence_success_201(self):
        # excpet a 201 response

        sentence = SentenceFactory(text='por que amigo por que', language=self.language_es, category=self.category_food)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post('/spanglish/translation/', {
            "word": "",
            "language": self.language_en.pk,
            "sentence": sentence.pk,
            "translation": ['Why my firend why']
            }
        )
        self.assertEqual(response.status_code, 201)
