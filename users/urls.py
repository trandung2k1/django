from django.urls import path

# from . import views
from users.views import main

urlpatterns = [
    # path("", views.index, name="index"),
    path("<str:name>/", main),
]
