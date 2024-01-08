from unittest.mock import patch, Mock

from django.test import TestCase

from spanglish.models import Language, Category, Word, Sentence, Translation, Verb
from spanglish.tests.factories import (
    LanguageFactory,
    CategoryFactory,
    WordFactory,
    SentenceFactory,
    TranslationWordFactory,
    TranslationSentenceFactory,
    VerbFactory,
)
from spanglish import tasks


class LanguageTaskTests(TestCase):
    def setUp(self):
        """
        Set up common test data.
        """
        self.language = LanguageFactory(name="English")

    def test_create_language(self):
        """
        Test that a language is created.
        """
        data = {"name": "French"}
        response = tasks.create_language(data)

        total_languages = Language.objects.count()

        self.assertTrue(response)
        self.assertEqual(total_languages, 2)


class CategoryTaskTests(TestCase):
    def setUp(self):
        """
        Set up common test data.
        """
        self.category = CategoryFactory(name="Days")

    def test_create_category(self):
        """
        Test that a category is created.
        """
        data = {"name": "Months"}
        response = tasks.create_category(data)

        total_categories = Category.objects.count()

        self.assertTrue(response)
        self.assertEqual(total_categories, 2)


class WordTaskTests(TestCase):
    def setUp(self):
        """
        Set up common test data.
        """
        self.language = LanguageFactory(name="English")
        self.category = CategoryFactory(name="Days")
        self.word = WordFactory(text="Monday", language=self.language, category=self.category)

    def test_create_word(self):
        """
        Test that a word is created.
        """
        data = {"text": "Tuesday", "language": self.language.pk, "category": self.category.pk}
        response = tasks.create_word(data)

        total_words = Word.objects.count()

        self.assertTrue(response)
        self.assertEqual(total_words, 2)


class SentenceTaskTests(TestCase):
    def setUp(self):
        """
        Set up common test data.
        """
        self.language = LanguageFactory(name="English")
        self.category = CategoryFactory(name="Days")
        self.sentence = SentenceFactory(text="Today is Monday", language=self.language, category=self.category)

    def test_create_sentence(self):
        """
        Test that a sentence is created.
        """
        data = {"text": "Today is Tuesday", "language": self.language.pk, "category": self.category.pk}
        response = tasks.create_sentence(data)

        total_sentences = Sentence.objects.count()

        self.assertTrue(response)
        self.assertEqual(total_sentences, 2)


class TranslationTaskTests(TestCase):
    def setUp(self):
        """
        Set up common test data.
        """
        self.language = LanguageFactory(name="English")
        self.category = CategoryFactory(name="Days")
        self.word = WordFactory(text="Monday", language=self.language, category=self.category)
        self.sentence = SentenceFactory(text="Today is Monday", language=self.language, category=self.category)
        # self.translation = Translation.objects.create(word=self.word, language=self.language, translation=["Lunes"])

    def test_create_translation(self):
        """
        Test that a translation is created.
        """
        data_word = {"word": self.word.pk, "sentence": "", "language": self.language.pk, "translation": ["Martes"]}
        data_sentence = {"word": "", "sentence": self.sentence.pk, "language": self.language.pk, "translation": ["Hoy es Lunes"]}
        response_word = tasks.create_translation(data_word)
        response_sentence = tasks.create_translation(data_sentence)

        total_translations = Translation.objects.count()

        self.assertTrue(response_word)
        self.assertTrue(response_sentence)
        self.assertEqual(total_translations, 2)


class VerbTaskTests(TestCase):
    def setUp(self):
        """
        Set up common test data.
        """
        self.language = LanguageFactory(name="English")
        self.category = CategoryFactory(name="Verbs")
        self.category_greeting = CategoryFactory(name="Greetings")
        self.word = WordFactory(text="be", language=self.language, category=self.category)

    def test_create_verb(self):
        """
        Test that a verb is created.
        """
        data = {
            "tense": "SIMPLE_PRESENT",
            "word": self.word.pk,
            "yo": "soy",
            "tu": "eres",
            "usted": "es",
            "nosotros": "somos",
            "vosotros": "sois",
            "ustedes": "son",
        }
        response = tasks.create_verb(data)

        total_verbs = Verb.objects.count()

        self.assertTrue(response)
        self.assertEqual(total_verbs, 1)

    def test_do_not_create_verb_category_not_verb(self):
        # excpet a False response becausse the category is not Verbs

        word = WordFactory(text="Hola", language=self.language, category=self.category_greeting)
        data = (
            {
                "tense": "SIMPLE_PRESENT",
                "word": word.pk,
                "yo": "voy",
                "tu": "vas",
                "usted": "va",
                "nosotros": "vamos",
                "vosotros": "vais",
                "ustedes": "van",
            },
        )

        response = tasks.create_verb(data)
        total_verbs = Verb.objects.count()

        self.assertFalse(response)
        self.assertEqual(total_verbs, 0)
