# urls.py
from django.urls import path
from django.contrib import admin

from tables.views import PersonListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("people/", PersonListView.as_view())
]