from django.urls import path
from .views import *



urlpatterns = [
    path('', getRoutes,  name="routes"),
    path('notes/', getNotes, name="notes"),
    path('notes/<str:pk>', getNote, name="note"),
]
