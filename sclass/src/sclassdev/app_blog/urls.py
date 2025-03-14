from django.urls import path
from .views import view
#dalam file view ada function view

urlpatterns = {
    path('', view, name = 'app_blog')
}