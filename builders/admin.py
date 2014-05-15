from django.contrib import admin
from .models import Builder, Website, Review, Photo, Rating

class BuilderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Builder, BuilderAdmin)

class WebpageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Website, WebpageAdmin)

class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)

class RatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rating, RatingAdmin)

