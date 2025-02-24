from django.contrib import admin
from .models import Profile, Category, SubCategory, Place, Item, Rate, Review, Owner
from blog.models import Post


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'age')
    search_fields = ('user__username', 'first_name', 'last_name')
    list_filter = ('gender', 'age')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory',
                    'address', 'phone', 'location')
    search_fields = ('title', 'category__name', 'subcategory__name', 'address')
    list_filter = ('category', 'subcategory')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'place', 'amount', 'item_type')
    search_fields = ('title', 'place__title')
    list_filter = ('item_type', 'place')


class RateAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    search_fields = ('user__username', 'place__title')
    list_filter = ('rating',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_date')
    search_fields = ('user__username', 'place__title', 'content')
    list_filter = ('created_date',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('profile', 'place')
    search_fields = ('profile__user__username', 'place__title')
    list_filter = ('profile', 'place')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Owner, OwnerAdmin)
