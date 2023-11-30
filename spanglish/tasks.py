import logging
from spanglish.serializers import LanguageSerializer, CategorySerializer, WordSerializer, SentenceSerializer, VerbSerializer, TranslationSerializer

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def create_language(request) -> bool:
    """process the saving of the language object through the worker in celery."""

    logger.debug(f"received request to create language {request}")
    # serialize and validate before saving
    serializer = LanguageSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"created language {serializer.data}")
        return True
    else:
        logger.error(f"failed to create language {request} with error {serializer.errors}")
    return False


@shared_task
def create_category(request) -> bool:
    """process the saving of the category object through the worker in celery."""

    logger.debug(f"received request to create category {request}")
    # serialize and validate before saving
    serializer = CategorySerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"created category {serializer.data}")
        return True
    else:
        logger.error(f"failed to create category {request} with error {serializer.errors}")
    return False


@shared_task
def create_word(request) -> bool:
    """process the saving of the word object through the worker in celery."""

    logger.debug(f"received request to create word {request}")
    # serialize and validate before saving
    serializer = WordSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"created word {serializer.data}")
        return True
    else:
        logger.error(f"failed to create word {request} with error {serializer.errors}")
    return False


@shared_task
def create_sentence(request) -> bool:
    """process the saving of the sentence object through the worker in celery."""

    logger.debug(f"received request to create sentence {request}")
    # serialize and validate before saving
    serializer = SentenceSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"created sentence {serializer.data}")
        return True
    else:
        logger.error(f"failed to create sentence {request} with error {serializer.errors}")
    return False


@shared_task
def create_translation(request) -> bool:
    """process the saving of the translation object through the worker in celery."""

    logger.debug(f"received request to create translation {request}")
    # serialize and validate before saving
    serializer = TranslationSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"created translation {serializer.data}")
        return True
    else:
        logger.error(f"failed to create translation {request} with error {serializer.errors}")
    return False


@shared_task
def create_verb(request) -> bool:
    """process the saving of the verb object through the worker in celery."""

    logger.debug(f"received request to create verb {request}")
    # serialize and validate before saving
    serializer = VerbSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"created verb {serializer.data}")
        return True
    else:
        logger.error(f"failed to create verb {request} with error {serializer.errors}")
    return False
