from django.urls import path
from . import views

app_name = "spanglish"
urlpatterns = [
    path("language/", views.LanguageListView.as_view(), name="language-list"),
    path("language/<int:pk>/detail/", views.LanguageDetailView.as_view(), name="language-detail"),
    path("category/", views.CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/detail/", views.CategoryDetailView.as_view(), name="category-detail"),
    path("word/", views.WordListView.as_view(), name="word-list"),
    path("word/<int:pk>/detail/", views.WordDetailView.as_view(), name="word-detail"),
    path("sentence/", views.SentenceListView.as_view(), name="sentence-list"),
    path("sentence/<int:pk>/detail/", views.SentenceDetailView.as_view(), name="sentence-detail"),
    path("translation/", views.TranslationListView.as_view(), name="translation-list"),
    path("translation/<int:pk>/detail/", views.TranslationDetailView.as_view(), name="translation-detail"),
    path("verb/", views.VerbListView.as_view(), name="verb-list"),
    path("verb/<int:pk>/detail/", views.VerbDetailView.as_view(), name="verb-detail"),
    path("verbtense/", views.VerbTenseListView.as_view(), name="verbtense-list"),
    path("verbtense/<int:pk>/detail/", views.VerbTenseDetailView.as_view(), name="verbtense-detail"),
]
