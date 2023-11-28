from typing import Any
from django.contrib import messages
from django.contrib import admin
from spanglish.models import Language, Category, Word, Sentence, Translation, Verb


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name",)
    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name",)
    ordering = ("name",)


class WordAdmin(admin.ModelAdmin):
    list_display = ("text", "language", "category", "added_at", "id")
    search_fields = ("text",)
    ordering = ("text",)


class VerbAdmin(admin.ModelAdmin):
    list_display = ("tense", "word", "yo", "tu", "usted", "nosotros", "vosotros", "ustedes", "added_at", "id")
    search_fields = ("tense", "word")
    ordering = ("tense", "word")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "word":
            kwargs["queryset"] = Word.objects.filter(category=1, verb__isnull=True)
        return super(VerbAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class SentenceAdmin(admin.ModelAdmin):
    list_display = ("text", "language", "category", "added_at", "id")
    search_fields = ("text",)
    ordering = ("text",)


class TranslationAdmin(admin.ModelAdmin):
    list_display = ("word", "sentence", "language", "translation", "added_at", "id")

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        """
        Override the save method to add a custom message and set the message level
        before calling the super.
        """
        if obj.word is None and obj.sentence is None:
            self.message_user(request, "Either word or sentence must be set", level="ERROR")
            messages.set_level(request, level=messages.ERROR)
        elif obj.word is not None and obj.sentence is not None:
            messages.set_level(request, level=messages.ERROR)
            self.message_user(request, "Either word or sentence must be null", level="ERROR")
        else:
            messages.set_level(request, level=messages.SUCCESS)
            return super().save_model(request, obj, form, change)


admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Translation, TranslationAdmin)
admin.site.register(Verb, VerbAdmin)
