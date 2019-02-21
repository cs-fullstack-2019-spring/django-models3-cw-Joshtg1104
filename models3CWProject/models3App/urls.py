from django.urls import path
from . import views
# url paths
urlpatterns = [
    path("", views.index, name="index"),
    path("bookTitle/", views.bookTitle, name="index"),
    path("pub2018OrByond/", views.pub2018OrByond, name="index"),
    path("updateGenre/", views.updateGenre, name="index"),
]