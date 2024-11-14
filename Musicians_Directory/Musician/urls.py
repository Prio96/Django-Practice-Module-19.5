from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.CreateMusicianClassView.as_view(),name="AddMusician"),
    path('edit/',views.EditMusicianClassView.as_view(),name="EditMusician"),
]