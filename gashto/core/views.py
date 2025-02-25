from django.views.generic import ListView, DetailView
from .models import Profile, Category, SubCategory, Place, Item, Rate, Review, Owner


class ProfileListView(ListView):
    model = Profile
    template_name = 'core/profile_list.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'core/profile_detail.html'
    context_object_name = 'profile'


class CategoryListView(ListView):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'core/category_detail.html'
    context_object_name = 'category'


class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'core/subcategory_list.html'
    context_object_name = 'subcategories'


class SubCategoryDetailView(DetailView):
    model = SubCategory
    template_name = 'core/subcategory_detail.html'
    context_object_name = 'subcategory'


class PlaceListView(ListView):
    model = Place
    template_name = 'core/place_list.html'
    context_object_name = 'places'


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'core/place_detail.html'
    context_object_name = 'place'


class ItemListView(ListView):
    model = Item
    template_name = 'core/item_list.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/item_detail.html'
    context_object_name = 'item'


class RateListView(ListView):
    model = Rate
    template_name = 'core/rate_list.html'
    context_object_name = 'rates'


class RateDetailView(DetailView):
    model = Rate
    template_name = 'core/rate_detail.html'
    context_object_name = 'rate'


class ReviewListView(ListView):
    model = Review
    template_name = 'core/review_list.html'
    context_object_name = 'reviews'


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'core/review_detail.html'
    context_object_name = 'review'


class OwnerListView(ListView):
    model = Owner
    template_name = 'core/owner_list.html'
    context_object_name = 'owners'


class OwnerDetailView(DetailView):
    model = Owner
    template_name = 'core/owner_detail.html'
    context_object_name = 'owner'
