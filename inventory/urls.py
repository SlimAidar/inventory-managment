from django.urls import path
from . import views as inventory_views

urlpatterns = [
	path('', inventory_views.HomePageView.as_view(), name="home_page"),
	path('create-item/', inventory_views.ItemCreateView.as_view(), name="create_item"),
	path('update-item/<int:pk>/', inventory_views.ItemUpdateView.as_view(), name="update_item"),
	path('create-category/', inventory_views.CategoryCreateView.as_view(), name="create_category"),
]

