import factory
from factory.django import DjangoModelFactory
from spanglish.models import Language, Category, Word, Sentence, Translation, Verb

class LanguageFactory(DjangoModelFactory):
    """Creates a LanguagFactory object with all possible fields populated."""

    name = factory.Faker("word")

    class Meta:
        model = Language

class CategoryFactory(DjangoModelFactory):
    """Creates a CategoryFactory object with all possible fields populated."""

    name = factory.Faker("word")

    class Meta:
        model = Category

class WordFactory(DjangoModelFactory):
    """Creates a WordFactory object with all possible fields populated."""

    text = factory.Faker("word")
    language = factory.SubFactory(LanguageFactory)
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Word

class SentenceFactory(DjangoModelFactory):
    """Creates a SentenceFactory object with all possible fields populated."""

    text = factory.Faker("sentence")
    language = factory.SubFactory(LanguageFactory)
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Sentence

class TranslationFactory(DjangoModelFactory):
    """Creates a TranslationFactory object with all possible fields populated."""

    word = factory.SubFactory(WordFactory)
    sentence = factory.SubFactory(SentenceFactory)
    language = factory.SubFactory(LanguageFactory)
    translation = factory.Faker("sentence")

    class Meta:
        model = Translation

class VerbFactory(DjangoModelFactory):
    """Creates a VerbFactory object with all possible fields populated."""

    tense = factory.Faker("word")
    word = factory.SubFactory(WordFactory)
    yo = factory.Faker("word")
    tu = factory.Faker("word")
    usted = factory.Faker("word")
    nosotros = factory.Faker("word")
    vosotros = factory.Faker("word")
    ustedes = factory.Faker("word")

    class Meta:
        model = Verb
