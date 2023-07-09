from django.contrib import admin
from .models import *

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

def delete_all_chosen(modeladmin, request, queryset):
    queryset.delete()
    delete_all_chosen.short_description = 'Удалить все выбранные позиции'

class NewsPortalAdmin(admin.ModelAdmin):
    model = PostCategory
    inlines = (PostCategoryInline,)
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с новостями
    # list_display = [field.article_title for field in NewsPortal._meta.get_fields()]  # генерируем список имён всех
    # полей для более красивого отображения
    list_display = ('post_title', 'post_author', 'post_date')    # Отображение определенных
    # характеристик
    list_filter = ('post_title', 'post_author', 'post_date')  # Фильтры
    search_fields = ('post_title', 'category__post_title')  # Поиск
    actions = [delete_all_chosen]  # добавляем действия в список

# Приложение с новостями
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Post, NewsPortalAdmin)