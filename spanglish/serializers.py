import logging
from rest_framework import serializers
from spanglish.models import Language, Category, Word, Sentence, Translation, Verb

logger = logging.getLogger(__name__)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'text', 'language', 'category', 'added_at']

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['id', 'text', 'language', 'category', 'added_at']


class TranslationViewSerializer(serializers.ModelSerializer):
    
    word = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='text'
    )
    sentence = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='text'
    )

    class Meta:
        model = Translation
        fields = ['id', 'word', 'sentence', 'language', 'translation', 'added_at']


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['id', 'word', 'sentence', 'language', 'translation', 'added_at']


class VerbViewSerializer(serializers.ModelSerializer):
    word = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='text'
    )

    class Meta:
        model = Verb
        fields = ['id', 'tense', 'word', 'yo', 'tu', 'usted', 'nosotros', 'vosotros', 'ustedes', 'added_at']


class VerbSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """add a check to ensure that the word category is Verbs"""
        logger.debug(f"VerbSerializer.validate() data: {data}")
        if data['word'].category.name != 'Verbs':
            raise serializers.ValidationError("Word category must be Verbs")
        return data


    class Meta:
        model = Verb
        fields = ['id', 'tense', 'word', 'yo', 'tu', 'usted', 'nosotros', 'vosotros', 'ustedes', 'added_at']
