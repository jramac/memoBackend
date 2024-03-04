from django.urls import path, include
from . import views

urlpatterns = [
    path('scores/',views.scoreList, name="score-list"),
    path('scores/<int:num>/',views.scoreListCut, name="score-list-cut"),
    path('names/',views.nameList, name="name-list"),
    path('score-create/',views.scoreCreate, name="score-create"),
    path('score-update/<str:pk>/',views.scoreUpdate, name="score-update"),
    path('score-delete/<str:pk>/',views.scoreDelete, name="score-delete"),
    path('name-create/',views.nameCreate, name="name-create"),
    path('name-update/<str:pk>/',views.nameUpdate, name="name-update"),
    path('name-delete/<str:pk>/',views.nameDelete, name="name-delete"),
]