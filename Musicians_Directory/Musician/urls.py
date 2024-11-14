from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.CreateMusicianClassView.as_view(),name="AddMusician"),
    path('edit/<int:id>',views.EditMusicianClassView.as_view(),name="EditMusician"),
]