from django.urls import path
from book_inventory_app import views
from django.contrib import admin

admin.site.site_header = "Göthenburg Stad Bibliotek"
admin.site.site_title = "Gothenburg Stad Bibliotek Title"
admin.site.index_title = "Gothenburg Stad Bibliotek index title"

urlpatterns = [
    path("", views.redirect_to_home, name="redirect_to_home"),
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