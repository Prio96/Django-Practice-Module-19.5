from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.CreateAlbum.as_view(),name="AddAlbum"),
    path('edit/<int:id>',views.EditAlbum.as_view(),name="EditAlbum"),
    path('delete/<int:id>',views.DeleteAlbum.as_view(),name="DeleteAlbum"),
]