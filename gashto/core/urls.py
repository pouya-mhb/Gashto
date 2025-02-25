from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(),
         name='profile_detail'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(),
         name='category_detail'),
    path('subcategories/', views.SubCategoryListView.as_view(),
         name='subcategory_list'),
    path('subcategories/<int:pk>/', views.SubCategoryDetailView.as_view(),
         name='subcategory_detail'),
    path('places/', views.PlaceListView.as_view(), name='place_list'),
    path('places/<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    # path('rates/', views.RateListView.as_view(), name='rate_list'),
    # path('rates/<int:pk>/', views.RateDetailView.as_view(), name='rate_detail'),
    # path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    # path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('owners/', views.OwnerListView.as_view(), name='owner_list'),
    path('owners/<int:pk>/', views.OwnerDetailView.as_view(), name='owner_detail'),
]
