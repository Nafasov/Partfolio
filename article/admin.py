from django.contrib import admin

from .models import (
                    Category,
                    Tag,
                    Author,
                    Article,
                    SubArticle,
                    Comment,
                    Paragraph,
                            )


@admin.register(Category)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class SubArticleTabularInlineAdmin(admin.TabularInline):
    model = SubArticle
    extra = 1


class ParagraphTabularInlineAdmin(admin.TabularInline):
    model = Paragraph
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (SubArticleTabularInlineAdmin, ParagraphTabularInlineAdmin)
    list_display = ('id', 'title', 'author', 'category', 'created_date')
    search_fields = ('title', )
    readonly_fields = ('created_date', 'modified_date', 'slug')
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')

