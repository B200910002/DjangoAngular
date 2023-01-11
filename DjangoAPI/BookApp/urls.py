from django.urls import re_path
from BookApp import views

urlpatterns=[
    re_path(r'^books/categories/$',views.CategorieApi),
    re_path(r'^books/categories/([0-9]+)$',views.CategorieApi),

    re_path(r'^books/book$',views.BookApi),
    re_path(r'^books/book/([0-9]+)$',views.BookApi)
]