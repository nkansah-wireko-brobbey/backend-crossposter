from django.urls import path
from core.api.views.post_view import simple_test

urlpatterns = [
    path("test/", simple_test, name="simple_test"),
]