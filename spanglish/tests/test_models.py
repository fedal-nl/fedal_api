from django.test import TestCase
from spanglish.models import Language, Category, Word, Sentence, Verb, Translation


class LanguageModelTest(TestCase):
    def setUp(self):
        self.language = Language.objects.create(name="English")

    def test_str(self):
        self.assertEqual(str(self.language), self.language.name)

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="General")

    def test_str(self):
        self.assertEqual(str(self.category), self.category.name)

class WordModelTest(TestCase):
    def setUp(self):
        self.language = Language.objects.create(name="English")
        self.category = Category.objects.create(name="General")
        self.word = Word.objects.create(text="Hello", language=self.language, category=self.category)

    def test_str(self):
        self.assertEqual(str(self.word), self.word.text)

class SentenceModelTest(TestCase):
    def setUp(self):
        self.language = Language.objects.create(name="English")
        self.category = Category.objects.create(name="General")
        self.sentence = Sentence.objects.create(text="Hello World", language=self.language, category=self.category)

    def test_str(self):
        self.assertEqual(str(self.sentence), self.sentence.text)

class TranslationModelTest(TestCase):
    def setUp(self):
        self.language = Language.objects.create(name="English")
        self.category = Category.objects.create(name="General")
        self.word = Word.objects.create(text="Hello", language=self.language, category=self.category)
        self.sentence = Sentence.objects.create(text="Hello World", language=self.language, category=self.category)
        self.translation = Translation.objects.create(word=self.word, language=self.language, translation=["Hola"])

    def test_str(self):
        expected_translation = f"{self.translation.translation}"
        self.assertEqual(str(self.translation), expected_translation)
