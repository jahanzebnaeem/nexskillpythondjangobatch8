from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formindex/', views.form_index, name='form_index'),
    path('formpage/', views.form_name_view, name='form_page'),
]
