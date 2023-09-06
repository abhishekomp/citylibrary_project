from django.urls import path
from book_inventory_app import views

urlpatterns = [
    path("home", views.home, name="index"),
    path("books/", views.booksList, name="book-list"),
    path("book/<int:pk>", views.bookView, name="book-detail"),

    path("redirect-me/", views.redirect_me, name="redirect-me")
]

# urlpatterns = [
#     path("home", views.home),
#     path("books/", views.booksList),
#     path("book/<int:pk>", views.bookView)
# ]