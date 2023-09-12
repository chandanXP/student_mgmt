from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="handle_records"),
    path('record/', views.record, name='record'),
]
