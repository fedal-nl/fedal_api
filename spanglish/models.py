from django.db import models
from django.contrib.postgres.fields import ArrayField
from django_statsd.clients import statsd


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Word(models.Model):
    text = models.CharField(max_length=50, unique=True)
    language = models.ForeignKey(Language, default=2, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        indexes = [
            models.Index(fields=['language', 'category']),
        ]
    

class Sentence(models.Model):
    text = models.CharField(max_length=200, unique=True)
    language = models.ForeignKey(Language, default=2, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        indexes = [
            models.Index(fields=['language', 'category']),
        ]

class VerbTenseChoices(models.TextChoices):
    SIMPLE_PRESENT = "SIMPLE_PRESENT", "EL PRESENTE SIMPLE"
    SIMPLE_PAST = "SIMPLE_PAST", "EL PASADO SIMPLE"
    SIMPLE_FUTURE = "SIMPLE_FUTURE", "EL FUTURO SIMPLE"
    PRESENT_CONTINUOUS = "PRESENT_CONTINUOUS", "EL PRESENTE CONTINUO"
    PAST_CONTINUOUS = "PAST_CONTINUOUS", "EL PASADO CONTINUO"
    FUTURE_CONTINUOUS = "FUTURE_CONTINUOUS", "EL FUTURO CONTINUO"
    PRESENT_PERFECT = "PRESENT_PERFECT", "EL PRESENTE PERFECTO"
    PAST_PERFECT = "PAST_PERFECT", "EL PASADO PERFECTO"
    FUTURE_PERFECT = "FUTURE_PERFECT", "EL FUTURO PERFECTO"
    PRESENT_PERFECT_CONTINUOUS = "PRESENT_PERFECT_CONTINUOUS", "EL PRESENTE PERFECTO CONTINUO"
    PAST_PERFECT_CONTINUOUS = "PAST_PERFECT_CONTINUOUS", "EL PASADO PERFECTO CONTINUO"
    FUTURE_PERFECT_CONTINUOUS = "FUTURE_PERFECT_CONTINUOUS", "EL FUTURO PERFECTO CONTINUO"


class Verb(models.Model):

    tense = models.CharField(max_length=50, choices=VerbTenseChoices.choices)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='verb')
    yo = models.CharField(max_length=25, blank=True, null=True)
    tu = models.CharField(max_length=25, blank=True, null=True)
    usted = models.CharField(max_length=25, blank=True, null=True)
    nosotros = models.CharField(max_length=25, blank=True, null=True)
    vosotros = models.CharField(max_length=25, blank=True, null=True)
    ustedes = models.CharField(max_length=25, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('tense', 'word'),)


    def __str__(self):
        return f"{self.word}"


class Translation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name='word')
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, null=True, blank=True, related_name='sentence')
    language = models.ForeignKey(Language, default=1, on_delete=models.CASCADE, related_name='language')
    translation = ArrayField(models.CharField(max_length=200))
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.translation}"
    
    class Meta:
        indexes = [
            models.Index(fields=['word', 'sentence']),
        ]
        unique_together = [
            ['word', 'language'],
            ['sentence', 'language'],
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    word__isnull=True,
                    sentence__isnull=False
                ) | models.Q(
                    word__isnull=False,
                    sentence__isnull=True
                ), name='word or sentence can not both be null or both be not null'
            ),
        ]
