from django.urls import path
from .views import product_list_create

# Routes for the products app. Add path(...) entries here as you build views.
urlpatterns = [
    path('', product_list_create, name='product_list_create'),
]
