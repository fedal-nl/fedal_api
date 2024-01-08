from jsonschema import validate, ValidationError
from spanglish import jsonschemas
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from spanglish.models import Language, Category, Word, Sentence, Translation, Verb
from spanglish.serializers import (
    LanguageSerializer,
    CategorySerializer,
    WordSerializer,
    SentenceSerializer,
    TranslationViewSerializer,
    TranslationSerializer,
    VerbSerializer,
    VerbViewSerializer,
)

from spanglish.tasks import create_language, create_category, create_word, create_sentence, create_translation, create_verb

logger = logging.getLogger(__name__)


class LanguageListView(APIView):
    """
    List all languages, or create a new language.
    """

    serializer_class = LanguageSerializer

    def get(self, request, format=None):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # make it an async task, return 400 if the validation doesn't past.
        # Validate post
        try:
            validate(request.data, jsonschemas.language_schema)
            create_language.delay(request.data)
            return Response(status=status.HTTP_202_ACCEPTED)

        except ValidationError as e:
            logger.warning(f"Validation error: {e.message}. Post data was {request.data}")
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class LanguageDetailView(APIView):
    """
    Retrieve, update or delete a language instance.
    """

    serializer_class = LanguageSerializer

    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        language = self.get_object(pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    """
    List all categories, or create a new category.
    """

    serializer_class = CategorySerializer

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # make it an async task, return 400 if the validation doesn't past.
        # Validate post
        try:
            validate(request.data, jsonschemas.category_schema)
            create_category.delay(request.data)
            return Response(status=status.HTTP_202_ACCEPTED)

        except ValidationError as e:
            logger.warning(f"Validation error: {e.message}. Post data was {request.data}")
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    """
    Retrieve, update or delete a category instance.
    """

    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WordListView(APIView):
    """
    List all words, or create a new word.
    """

    serializer_class = WordSerializer

    def get(self, request, format=None):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # make it an async task, return 400 if the validation doesn't past.
        # Validate post
        try:
            validate(request.data, jsonschemas.word_schema)
            create_word.delay(request.data)
            return Response(status=status.HTTP_202_ACCEPTED)

        except ValidationError as e:
            logger.warning(f"Validation error: {e.message}. Post data was {request.data}")
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class WordDetailView(APIView):
    """
    Retrieve, update or delete a word instance.
    """

    serializer_class = WordSerializer

    def get_object(self, pk):
        try:
            return Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        word = self.get_object(pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SentenceListView(APIView):
    """
    List all sentences, or create a new sentence.
    """

    serializer_class = SentenceSerializer

    def get(self, request, format=None):
        sentences = Sentence.objects.all()
        serializer = SentenceSerializer(sentences, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # make it an async task, return 400 if the validation doesn't past.
        # Validate post
        try:
            validate(request.data, jsonschemas.sentence_schema)
            create_sentence.delay(request.data)
            return Response(status=status.HTTP_202_ACCEPTED)

        except ValidationError as e:
            logger.warning(f"Validation error: {e.message}. Post data was {request.data}")
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class SentenceDetailView(APIView):
    """
    Retrieve, update or delete a sentence instance.
    """

    serializer_class = SentenceSerializer

    def get_object(self, pk):
        try:
            return Sentence.objects.get(pk=pk)
        except Sentence.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sentence = self.get_object(pk)
        serializer = SentenceSerializer(sentence)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sentence = self.get_object(pk)
        serializer = SentenceSerializer(sentence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sentence = self.get_object(pk)
        sentence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TranslationListView(APIView):
    """
    List all translations, or create a new translation.
    """

    serializer_class = TranslationSerializer

    def get(self, request, format=None):
        translations = Translation.objects.all()
        serializer = TranslationViewSerializer(translations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            validate(request.data, jsonschemas.translation_schema)
            create_translation.delay(request.data)
            return Response(status=status.HTTP_202_ACCEPTED)

        except ValidationError as e:
            logger.warning(f"Validation error: {e.message}. Post data was {request.data}")
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class TranslationDetailView(APIView):
    """
    Retrieve, update or delete a translation instance.
    """

    serializer_class = TranslationViewSerializer

    def get_object(self, pk):
        try:
            return Translation.objects.get(pk=pk)
        except Translation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        translation = self.get_object(pk)
        serializer = TranslationViewSerializer(translation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        translation = self.get_object(pk)
        serializer = TranslationSerializer(translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        translation = self.get_object(pk)
        translation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VerbListView(APIView):
    """
    List all verbs, or create a new verb.
    """

    serializer_class = VerbSerializer

    def get(self, request, format=None):
        verbs = Verb.objects.all()
        serializer = VerbViewSerializer(verbs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            validate(request.data, jsonschemas.verb_schema)
            create_verb.delay(request.data)
            return Response(status=status.HTTP_202_ACCEPTED)
        except ValidationError as e:
            logger.warning(f"Validation error: {e.message}. Post data was {request.data}")
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class VerbDetailView(APIView):
    """
    Retrieve, update or delete a verb instance.
    """

    serializer_class = VerbViewSerializer

    def get_object(self, pk):
        try:
            return Verb.objects.get(pk=pk)
        except Verb.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        verb = self.get_object(pk)
        serializer = VerbViewSerializer(verb)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        verb = self.get_object(pk)
        serializer = VerbSerializer(verb, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        verb = self.get_object(pk)
        verb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
