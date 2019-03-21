from django.urls import path
from . import views as inventory_views

urlpatterns = [
	path('', inventory_views.HomePageView.as_view(), name="home_page")
]

