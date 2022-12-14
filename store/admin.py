from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe
from .models import Tag, Product, Category
from django import forms


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title', 'category', 'price', 'is_onsale',
                    'get_preview_photo')
    list_editable = ('is_onsale', 'category', 'price')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'get_photo', 'photo', 'category', 
              'views_counter', 'price', 'tags', 'is_onsale')
    readonly_fields = ('get_photo', 'views_counter')
    

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="200px">')
        else:
            return 'Фото отсуствует'

    
    def get_preview_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50px">')
        else:
            return 'Фото отсуствует'


    get_preview_photo.short_description = 'Миниатюра'
    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.site_title = 'Админка chlenomylo'
admin.site.site_header = 'Chlenomylo'